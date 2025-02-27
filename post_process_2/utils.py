import math
import matplotlib.pyplot as plt
import numpy as np
from scipy.spatial import Delaunay
from sklearn.neighbors import kneighbors_graph

epsilon = 0.00001


def less_first(a, b):
    return [a, b] if a < b else [b, a]


def two_points_2_vector(p1, p2):
    return [p2[0] - p1[0], p2[1] - p1[1]]


def two_points_sum(p1, p2):
    return [p2[0] + p1[0], p2[1] + p1[1]]


def get_closest_vector_in_length(original_vec, list_of_vecs) -> float:
    minimum_dist = float('inf')
    for v in list_of_vecs:
        diff = np.linalg.norm(v - original_vec)
        minimum_dist = min(minimum_dist, diff)
    return minimum_dist


def vector_length(v):
    return np.sqrt(dot_product(v, v))


def vec_length_from_2_points(p1, p2):
    return math.dist(p1, p2)


def dot_product(v1, v2):
    product = sum((a * b) for a, b in zip(v1, v2))  # general n-dimesnsions vector
    return product


def rotation_matrix(theta):
    return np.array([[np.cos(theta), -np.sin(theta)], [np.sin(theta), np.cos(theta)]])


def rotate_points_by_angle(points, angle):
    rotated_points = points
    if len(points) > 0:
        rotated_points = points @ rotation_matrix(angle)
    return rotated_points


def rotate_Burger_vecs(Burger_field, theta):
    temp1 = rotate_points_by_angle(np.array([[vec[0], vec[1]] for vec in Burger_field]), theta)
    temp2 = rotate_points_by_angle(np.array([[vec[2], vec[3]] for vec in Burger_field]), theta)
    rotated_Burger_vec = np.hstack((temp1, temp2))

    return rotated_Burger_vec


def is_horizontal(edge, points):
    x = np.array([[1, 0], [-1, 0]])
    y = np.array([[0, 1], [0, -1]])
    vec = points[edge[1]] - points[edge[0]]
    x_diff = get_closest_vector_in_length(vec, x)
    y_diff = get_closest_vector_in_length(vec, y)
    if x_diff < y_diff:
        return True
    return False


def where_2_lines_intersect(p1, p2, p3, p4):  # p1->p2 , p3->p4
    x1, y1 = p1
    x2, y2 = p2
    x3, y3 = p3
    x4, y4 = p4
    denom = (y4 - y3) * (x2 - x1) - (x4 - x3) * (y2 - y1)
    if denom == 0:  # parallel
        return False
    ua = ((x4 - x3) * (y1 - y3) - (y4 - y3) * (x1 - x3)) / denom
    if ua < 0 or ua > 1:  # out of range
        return False
    ub = ((x2 - x1) * (y1 - y3) - (y2 - y1) * (x1 - x3)) / denom
    if ub < 0 or ub > 1:  # out of range
        return False
    x = x1 + ua * (x2 - x1)
    y = y1 + ua * (y2 - y1)
    return [x, y]


def is_diagonal(edge, perfect_lattice_vectors_only_diags, perfect_lattice_vectors_only_no_diags, points) -> bool:
    vec = points[edge[1]] - points[edge[0]]
    x = get_closest_vector_in_length(vec, perfect_lattice_vectors_only_diags)
    y = get_closest_vector_in_length(vec, perfect_lattice_vectors_only_no_diags)

    if x > y:
        return False
    else:
        return True


def nearest_neighbors_graph(points, l_x, l_y, n_neighbors):
    cyc = lambda p1, p2: cyc_dist(p1, p2, [l_x, l_y])
    NNgraph = kneighbors_graph(points, n_neighbors=n_neighbors, metric=cyc)
    return NNgraph


def cyc_dist(p1, p2, boundaries):
    dx = np.array(p1) - p2  # direct vector
    dsq = 0
    for i in range(2):
        L = boundaries[i]
        dsq += min(dx[i] ** 2, (dx[i] + L) ** 2, (dx[i] - L) ** 2)  # find shorter path through B.D.
    return np.sqrt(dsq)


def paired_through_boundary(p1, p2, boundaries, theta):
    p1, p2 = rotate_points_by_angle([p1, p2], -theta)
    which_boundary = [0, 0]

    dx = np.array(p1) - p2  # direct vector
    for i in range(2):
        L = boundaries[i]
        if (dx[i] + L) ** 2 < dx[i] ** 2:
            which_boundary[i] = L
        if (dx[i] - L) ** 2 < dx[i] ** 2:
            which_boundary[i] = -L

    if which_boundary == [0, 0]:
        return False
    return True


def nearest_neighbors(N, NNgraph):
    return [[j for j in NNgraph.getrow(i).indices] for i in range(N)]


def wrap_boundaries(points_with_z, boundaries, w):
    for p in points_with_z:
        if p[0] < w:
            points_with_z = np.append(points_with_z, [[p[0] + boundaries[0], p[1], p[2]]], axis=0)
        if p[1] < w:
            points_with_z = np.append(points_with_z, [[p[0], p[1] + boundaries[1], p[2]]], axis=0)
        if p[0] + w > boundaries[0]:
            points_with_z = np.append(points_with_z, [[p[0] - boundaries[0], p[1], p[2]]], axis=0)
        if p[1] + w > boundaries[1]:
            points_with_z = np.append(points_with_z, [[p[0], p[1] - boundaries[1], p[2]]], axis=0)
        if p[0] < w and p[1] < w:
            points_with_z = np.append(points_with_z, [[p[0] + boundaries[0], p[1] + boundaries[1], p[2]]], axis=0)
        if p[0] < w and p[1] + w > boundaries[1]:
            points_with_z = np.append(points_with_z, [[p[0] + boundaries[0], p[1] - boundaries[1], p[2]]], axis=0)
        if p[0] + w > boundaries[0] and p[1] < w:
            points_with_z = np.append(points_with_z, [[p[0] - boundaries[0], p[1] + boundaries[1], p[2]]], axis=0)
        if p[0] + w > boundaries[0] and p[1] + w > boundaries[1]:
            points_with_z = np.append(points_with_z, [[p[0] - boundaries[0], p[1] - boundaries[1], p[2]]], axis=0)

    return points_with_z


def cyclic_vec(boundaries, sphere1, sphere2):
    dx = np.array(sphere1) - sphere2  # direct vector
    vec = np.zeros(len(dx))
    for i in range(2):
        l = boundaries[i]
        dxs = np.array([dx[i], dx[i] + l, dx[i] - l])
        vec[i] = dxs[np.argmin(dxs ** 2)]  # find shorter path through B.D.
    return vec


def no_cyclic_vec(boundaries, sphere1, sphere2):
    dx = np.array(sphere1) - sphere2  # direct vector
    vec = np.zeros(len(dx))
    for i in range(2):
        l = boundaries[i]
        dxs = np.array([dx[i], dx[i] + l, dx[i] - l])
        vec[i] = dxs[np.argmin(dxs ** 2)]  # find shorter path through B.D.
    if vector_length(vec) < vector_length(dx):
        return None
    return vec


def filter_none(l: list) -> list:
    return list(filter(lambda item: item is not None, l))


def remove_points_outside_boundaries(points, boundaries):
    points_in_boundary = []

    for p in points:
        if not out_of_boundaries([p[0], p[1]], boundaries[0]):
            points_in_boundary.append(p)

    return points_in_boundary


def out_of_boundaries(point, L):
    x, y = point[0], point[1]
    if x > L or x < 0:
        return True
    if y > L or y < 0:
        return True
    return False


def plot(points, edges_with_colors, no_diagonal, line_style):
    print("plotting edges")
    for (p1, p2), color, in_circuit in edges_with_colors:
        x1, y1 = points[p1]
        x2, y2 = points[p2]
        if not (color == 'salmon' and no_diagonal):
            if not in_circuit:
                plt.plot([x1, x2], [y1, y2], lw=0.4, linestyle= line_style  ,color='grey', alpha=1)


def plot_burger_field(burger_vecs, pairs_connecting_lines, boundaries, plot_pairing=False):
    print("plotting Burger field")
    if burger_vecs is not None:
        for [p1_x, p1_y, p2_x, p2_y], neighbor in burger_vecs:
            dx = p2_x - p1_x
            dy = p2_y - p1_y
            plt.arrow(p1_x-dx/2, p1_y-dy/2, dx, dy, head_width=0.3,
                      head_length=0.4,
                      length_includes_head=True,
                      lw=2,
                      color='#008080')

    if plot_pairing:
        for pair_line in pairs_connecting_lines:
            p1_x = pair_line.coords[0][0]
            p1_y = pair_line.coords[0][1]
            r_x = pair_line.coords[1][0]
            r_y = pair_line.coords[1][1]

            plt.plot([p1_x, r_x], [p1_y, r_y], lw=1.5, linestyle = 'dotted', color="orange")


def plot_boundaries(boundaries, global_theta):
    boundary_pairs = [[[0, 0], [0, boundaries[1]]],
                      [[0, 0], [boundaries[0], 0]],
                      [[0, boundaries[1]], [boundaries[0], boundaries[1]]],
                      [[boundaries[0], 0], [boundaries[0], boundaries[1]]]]

    for pair in boundary_pairs:
        pair = np.array(rotate_points_by_angle(np.array(pair), global_theta))
        plt.plot(pair[:, 0], pair[:, 1], color="purple")


def plot_colored_points(points, l_z):
    print("coloring the graph")
    for i in range(len(points)):
        p = points[i]
        if p[2] > l_z / 2:
            plt.plot(p[0], p[1], 'ro', markersize=4)
        else:
            plt.plot(p[0], p[1], 'bo', markersize=4)

    #plt.axis([185, 220, 434, 460])
    #plt.axis([185, 230, 430, 460])
    plt.axis([220, 264, 346, 376])
    #plt.axis([227, 264, 346, 368])
    plt.gca().set_aspect('equal')
    plt.axis('off')
    plt.tight_layout()
    plt.savefig('snapshot.pdf', format='pdf')


def plot_points(points):
    print("coloring the graph")
    for i in range(len(points)):
        p = points[i]
        plt.plot(p[0], p[1], 'blue', marker='o', markersize=5)
    plt.axis([130, 200, 360, 410])
    plt.gca().set_aspect('equal')


def plot_frustrations(array_of_edges, points_with_z, points, l_z, L):
    print("coloring frustrations green")
    no_of_frustrations = 0
    for (p1, p2), color, in_circuit in array_of_edges:
        if not (color == 'salmon' or in_circuit):
            if (points_with_z[p1][2] > l_z / 2 and points_with_z[p2][2] > l_z / 2) or \
                    (points_with_z[p1][2] < l_z / 2 and points_with_z[p2][2] < l_z / 2):

                x1, y1 = points[p1]
                x2, y2 = points[p2]
                if not (out_of_boundaries([x1, y1], L) or out_of_boundaries([x2, y2], L)):
                    no_of_frustrations += 1
                plt.plot([x1, x2], [y1, y2], color='purple', lw=1.5)
    print("no of frustrations outside dislocations:", no_of_frustrations)


def plot_nn_graph(N, NNgraph, points):
    nn = nearest_neighbors(N, NNgraph)
    for n in range(len(points)):
        x1, y1 = points[n]
        for j in nn[n]:
            x2, y2 = points[j]
            if math.dist([x1,y1], [x2,y2]) < 100:
                plt.plot([x1, x2], [y1, y2], color='blue')
    plt.scatter(points[:, 0], points[:, 1])
    plt.axis([130, 200, 360, 410])
    plt.gca().set_aspect('equal')
    plt.show()


def get_params(N, h, rho_H):
    # n_row = int(np.sqrt(N))
    # n_col = n_row  # Square initial condition for n_row!=n_col is not implemented...
    r, sig = 1.0, 2.0
    A = N * sig ** 2 / (rho_H * (1 + h))
    a = np.sqrt(A / N)
    n_row_cells, n_col_cells = int(np.sqrt(A) / (a * np.sqrt(2))), int(np.sqrt(A) / (a * np.sqrt(2)))
    edge = np.sqrt(A / (n_row_cells * n_col_cells))
    l_x = edge * n_col_cells
    l_y = edge * n_row_cells
    assert abs(l_x - l_y) < 0.000000001
    l_z = (h + 1) * sig
    return l_x, a, l_z


def perfect_lattice_vectors(a, order):
    # a = L / (np.sqrt(N) - 1)

    a1, a2 = np.array([a, 0]), np.array([0, a])

    # get lattice vectors
    perfect_lattice_vectors_only_diags = filter_none(
        [(n * a1 + m * a2 if n != 0 and m != 0 else None) for n in range(-order, order + 1) for m in
         range(-order, order + 1)]
    )
    perfect_lattice_vectors_only_no_diags = filter_none(
        [(n * a1 + m * a2 if (n == 0 or m == 0) and not (n == 0 and m == 0) else None) for n in range(-order, order + 1)
         for m in
         range(-order, order + 1)]
    )

    return perfect_lattice_vectors_only_diags, perfect_lattice_vectors_only_no_diags


def read_points_from_file(file_path: str) -> np.ndarray:
    # load points from file
    points = np.loadtxt(file_path)

    return points


"""

__________________________________________________________________________________________________________________
------------------------------------------------------------------------------------------------------------------

"cemetery of functions that fell out of use, to be deleted"

____________________________________________________________________________________________________________________
--------------------------------------------------------------------------------------------------------------------

"""


def plot_points_with_delaunay_edges_where_diagonals_are_removed(points_with_z, alignment_angel, burger_vecs, a, l_z):
    # a = L / (np.sqrt(N) - 1)

    points = np.delete(points_with_z, 2, axis=1)

    # Perform Delaunay triangulation and get edges
    tri = Delaunay(points)
    edges = delaunay2edges(tri)

    # remove edges that are diagonal
    array_of_edges = filter_diagonal_edges(array_of_edges=edges, a=a, points=points, rotation_angel=alignment_angel,
                                           order=1)

    # edges
    edges_with_colors = []
    for e in array_of_edges:
        if is_horizontal(e, points):
            edges_with_colors.append((e, "y"))
        else:
            edges_with_colors.append((e, "blue"))

    plot(points=points, edges_with_colors=edges_with_colors, burger_vecs=burger_vecs)
    plot_frustrations(array_of_edges, points_with_z, l_z)


def plot_points_with_no_edges(points):
    plot(points=points, edges_with_colors=[])


def filter_diagonal_edges(array_of_edges, a, points, rotation_angel, order):
    # calculate a vectors
    a1, a2 = np.array([a, 0]), np.array([0, a])

    # get lattice vectors
    perfect_lattice_vectors_only_diags = filter_none(
        [(n * a1 + m * a2 if n != 0 and m != 0 else None) for n in range(-order, order + 1) for m in
         range(-order, order + 1)]
    )
    perfect_lattice_vectors_only_no_diags = filter_none(
        [(n * a1 + m * a2 if (n == 0 or m == 0) and not (n == 0 and m == 0) else None) for n in range(-order, order + 1)
         for m in
         range(-order, order + 1)]
    )

    perfect_lattice_vectors_only_no_diags_aligned = rotate_points_by_angle(perfect_lattice_vectors_only_no_diags,
                                                                           rotation_angel)
    perfect_lattice_vectors_only_diags_aligned = rotate_points_by_angle(perfect_lattice_vectors_only_diags,
                                                                        rotation_angel)

    list_of_edges = []
    iterations = len(array_of_edges)
    for i, edge in enumerate(array_of_edges):
        if (i % 1000) == 0:
            print("filter_edges progress = ", int((i / iterations) * 100), "%")
        if not is_diagonal(edge, perfect_lattice_vectors_only_diags_aligned,
                           perfect_lattice_vectors_only_no_diags_aligned, points):
            list_of_edges.append(edge)
    array_of_edges = np.unique(list_of_edges, axis=0)  # remove duplicates
    return array_of_edges


def delaunay2edges(tri):
    list_of_edges = []
    iterations = len(tri.simplices)
    for i, triangle in enumerate(tri.simplices):
        if (i % 1000) == 0:
            print("delaunay2edges progress = ", int((i / iterations) * 100), "%")
        for e1, e2 in [[0, 1], [1, 2], [2, 0]]:  # for all edges of triangle
            edge = less_first(triangle[e1], triangle[e2])  # always lesser index first
            list_of_edges.append(edge)
    array_of_edges = np.unique(list_of_edges, axis=0)  # remove duplicates
    return array_of_edges


def get_lengths_of_edges(tri, array_of_edges):
    list_of_lengths = []
    for p1, p2 in array_of_edges:
        x1, y1 = tri.points[p1]
        x2, y2 = tri.points[p2]
        list_of_lengths.append((x1 - x2) ** 2 + (y1 - y2) ** 2)
    array_of_lengths = np.sqrt(np.array(list_of_lengths))
    return array_of_lengths


def NN2edges(points, nearest_neighbours, L):
    list_of_edges = []
    for p in range(len(nearest_neighbours)):
        nn_edges = []
        for n in range(len(nearest_neighbours[p])):
            edge = (points[p], points[nearest_neighbours[p][n]])
            if vec_length_from_2_points(edge[0], edge[1]) < L / 2:
                nn_edges.append(edge)
        list_of_edges.append(nn_edges)
    return list_of_edges


def calculate_angle_between_two_vectors(v1, v2):
    return np.arccos(dot_product(v1, v2) / (vector_length(v1) * vector_length(v2)))


def cyc_position_alignment(points, boundaries):
    for p in points:
        if p[0] > boundaries[0]:
            p[0] = p[0] - boundaries[0]

        if p[0] < 0:
            p[0] = p[0] + boundaries[0]

        if p[1] > boundaries[1]:
            p[1] = p[1] - boundaries[1]

        if p[1] < 0:
            p[1] = p[1] + boundaries[1]
