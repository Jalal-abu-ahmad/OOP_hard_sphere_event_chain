import matplotlib.pyplot as plt


def testing():
    unpaired_up_down = [[415.98662569012504, 15.694666809786845, 415.9866256901251, 17.351013459786692],
                        [269.53092880820367, 71.92472866571053, 269.53092880820367, 73.5810753157104],
                        [477.7097167292764, 231.56202803375393, 477.70971672927635, 233.21837468375378],
                        [380.5827136596927, 118.10736250133851, 380.5827136596927, 119.76370915133836],
                        [90.30332569835575, 446.94325219286793, 90.30332569835575, 448.59959884286775],
                        [13.11927096528446, 405.77455545054255, 13.119270965284459, 407.4309021005424],
                        [493.3368920867657, 409.56056961197544, 493.3368920867658, 407.90422296197556],
                        [152.92268513259555, 28.260323175600938, 152.9226851325956, 26.60397652560109],
                        [397.8573910028393, 29.5272116295496, 397.8573910028393, 27.870864979549758],
                        [65.67752954873555, 63.479017765073834, 65.67752954873555, 61.82267111507399],
                        [339.7716444432442, 54.040216133244854, 339.77164444324416, 52.38386948324501],
                        [443.1083300933478, 165.3854446166331, 443.10833009334783, 163.72909796663325]]

    unpaired_right_left = [[380.5827136596927, 118.10736250133851, 382.2390603096925, 118.10736250133851],
                           [398.98820489250676, 28.0244428793119, 400.6445515425066, 28.024442879311895],
                           [340.7160178235847, 53.59673650967849, 342.3723644735845, 53.59673650967849],
                           [68.05440252601632, 61.444190253674805, 69.71074917601617, 61.444190253674805],
                           [473.9807452250817, 232.58591419357725, 475.63709187508147, 232.58591419357725],
                           [267.7071235700269, 73.62808306597579, 266.05077692002703, 73.62808306597579],
                           [159.93300531582304, 30.52547561119387, 158.27665866582316, 30.525475611193865],
                           [89.925854023958, 447.9094553034587, 88.26950737395813, 447.9094553034586],
                           [418.06941795620816, 16.038947268296393, 416.41307130620834, 16.038947268296393],
                           [441.8152134538558, 162.51396145353226, 440.158866803856, 162.51396145353226]]

    full = unpaired_right_left + unpaired_up_down

    for [p1_x, p1_y, p2_x, p2_y] in full:
        dx = p2_x - p1_x
        dy = p2_y - p1_y
        plt.arrow(p1_x, p1_y, dx, dy, head_width=0.4,
                  head_length=0.7,
                  length_includes_head=True,
                  color='black')

    plt.gca().set_aspect('equal')




# [ 14.34041874 404.05478199   2.514062  ]
# [ 12.67934097 404.65608941   1.45196833]
# [ 13.64921939 402.80130568   1.0072386 ]
# [ 12.18974779 402.16286174   2.40756694]
# [ 13.90513966 400.98744977   2.59332719]
# [ 12.4260337  400.54971407   1.02029196]
# [ 13.8726741  399.10674102   1.00627038]
# [ 12.41625297 399.08037512   2.51014022]
# [ 14.59066093 397.1067067    2.56571944]
# [ 12.68095403 396.80425413   1.11266625]
# [ 14.38350731 395.59716724   1.19696038]
# [ 12.62431084 395.39801184   2.56121611]
# [ 13.86572152 393.58645153   2.59750359]
# [ 12.67144753 394.04775478   1.05534705]
# [ 13.61592179 392.26285467   1.02225877]
# [ 12.26097497 392.11963585   2.59049026]
# [ 14.13631859 390.98600814   2.49607918]
# [ 12.13345092 390.71345887   1.13072043]
# [ 14.15633183 389.57915576   1.0093047 ]
# [ 12.75851882 389.21299995   2.50618343]
# [ 14.23494843 387.8017231    2.52779572]
# [ 12.70960258 387.68284355   1.17320742]
# [ 14.08177565 386.17629492   1.25916809]
# [ 12.5531784  386.18074591   2.58180168]
# [ 14.00552998 384.56290482   2.4751202 ]
# [ 12.45911423 384.52785459   1.13423335]
# [ 13.97010903 382.79978475   1.12716831]
# [ 12.46373987 382.96822431   2.45506075]
# [ 14.16641145 381.37865655   2.55609294]
# [ 11.77151339 381.27051271   1.03430498]
# [ 13.6088359 380.050965    1.0028896]
# [ 12.16337302 379.74161736   2.59747484]
# [ 13.95092322 378.52722236   2.34142654]
# [ 12.17206789 378.15688952   1.05395035]
# [ 13.75005778 373.8070861    2.53455619]
# [ 12.29508173 373.8920336    1.02355221]
# [ 13.78358183 372.43408597   1.01563667]
# [ 11.98446998 372.42318428   2.59496795]
# [ 13.77189129 370.99968989   2.59345916]
# [ 12.35411927 371.01512058   1.05563488]
# [ 14.09041367 369.43182105   1.05555477]
# [ 12.53200332 369.23716143   2.39911867]
# [ 14.121903   367.80230012   2.32629382]
# [ 12.32851832 367.57452147   1.07321312]
# [ 13.978576   366.13233318   1.07905865]
# [ 12.13211054 365.99319019   2.53080552]
# [ 13.81848095 364.70628012   2.59604499]
# [ 12.26811897 364.46173893   1.10230905]
# [ 13.98025938 363.35201168   1.05192714]
# [ 12.05774756 362.75773493   2.58237934]
# [ 13.79122238 361.63738959   2.38257742]
# [ 12.29614252 361.19541585   1.06471143]
# [ 13.89748447 359.9419429    1.13694124]
# [ 12.40557181 359.78420651   2.53938655]
# [ 13.67220756 358.07070386   2.55118527]
# [ 12.12114228 357.9168653    1.09484489]
# [ 13.72805573 356.52864734   1.27566785]
# [ 12.02845505 356.37336319   2.57753109]
# [ 13.51443081 354.75008333   2.58966876]
# [ 12.09488402 354.69426106   1.0850123 ]
# [ 14.10188454 353.32075304   1.01827147]
# [ 12.2080671  353.18789269   2.47402794]
# [ 13.95138522 351.76544953   2.43398797]
# [ 12.19335276 351.74377487   1.07183028]
# [ 14.06795338 350.31238476   1.02654609]
# [ 12.46263416 349.94205828   2.5583912 ]
# [ 14.5498     348.86232903   2.51917154]
# [ 12.44716071 348.32807106   1.18221974]
# [ 13.87262568 346.88223342   1.14302569]
# [ 12.41257228 346.58210268   2.57554663]
# [ 14.39788573 345.05505387   2.41121942]
# [ 12.36830898 345.0883515    1.16572823]
# [ 14.72943549 343.2065755    1.03441021]
# [ 12.52764928 342.97033945   2.54459176]
# [ 14.13795499 341.70213498   2.47302563]
# [ 12.64484914 341.54879357   1.11544729]
# [ 14.43951966 339.87289917   1.04205574]
# [ 12.85577745 339.77373745   2.29717924]
# [ 14.29860523 338.29689566   2.53591039]
# [ 12.64540242 338.20170774   1.02479125]
# [ 14.69827978 336.51973863   1.02920424]
# [ 12.66817936 336.87894474   2.554097  ]
# [ 15.03019292 334.94294303   2.58283204]
# [ 13.07755478 335.29113481   1.28843656]
# [ 14.92324239 333.54645039   1.10859996]
# [ 13.03917875 333.69802346   2.51020813]
# [ 14.42487581 331.67376631   2.55008193]
# [ 13.1574486  332.20968271   1.00706064]
# [ 14.27441262 330.18845328   1.02201838]
# [ 12.78279846 330.07333998   2.59179547]
# [ 14.46737716 328.29468413   2.54249123]
# [ 12.98435673 328.48091327   1.00115302]
# [ 14.23209144 326.79561171   1.08919205]
# [ 12.60432112 327.04646271   2.58863226]
# [ 14.53432929 325.33201834   2.4384709 ]
# [ 12.61003854 325.47016569   1.07009688]
# [ 13.94814118 323.59166264   1.05816074]
# [ 12.64810834 323.89068168   2.58448278]
# [ 14.28854542 321.888041     2.46218589]
# [ 12.54382891 321.90934736   1.31132467]
# [ 14.0262962  320.31110195   1.04545309]
# [ 12.42383609 320.06800472   2.553045  ]
# [ 14.2941678  318.80448976   2.58470545]
# [ 12.43455109 318.76867223   1.00219245]
# [ 13.91012112 317.08279231   1.02239985]
# [ 12.28239658 317.04294144   2.59591938]
# [ 14.00982767 312.21474843   2.5841926 ]
# [ 14.00982767 312.21474843   2.5841926 ]
# [ 13.73562736 313.64745059   1.00548659]
# [ 12.44589648 312.04046503   1.11154959]
# [ 14.0928071  310.57269436   1.22452296]
# [ 12.48552927 310.54393702   2.53702167]
# [ 14.21680448 309.05518193   2.52764283]
# [ 12.36365943 309.16894375   1.08800963]
# [ 14.55854087 307.49733904   1.05618049]
# [ 12.87272038 306.85562172   2.57129698]
# [ 14.42021577 303.88492171   1.27669113]
# [ 12.80329747 303.65000173   2.47311997]
# [ 14.77675095 302.31964024   2.58634398]
# [ 12.71770419 301.74937666   1.09647662]
# [ 14.63320865 300.91068951   1.00421489]
# [ 12.68790076 300.321948     2.55299185]
# [ 14.65966111 299.37023192   2.32972431]
# [ 12.8753725  298.9732157    1.00675186]
# [ 11.99307361 297.38996853   2.54845675]
# [ 10.55186998 297.64856668   1.13920572]
# [ 12.26942886 295.9767437    1.07418538]
# [ 10.56247534 295.97277115   2.32134793]
# [ 12.15823954 294.20705154   2.51222561]
# [ 10.56969027 293.70962094   1.10968205]
# [ 12.41781518 292.87789631   1.02775928]
# [ 11.12031097 292.25399449   2.59479505]
# [ 12.33947622 290.59947556   2.51476575]
# [ 10.77034151 290.85355054   1.00290234]
# [ 12.34282295 289.10678658   1.14049502]
# [ 10.49763185 289.50727006   2.51691899]
# [ 12.18907258 287.7082687    2.58807714]
# [ 10.6629891  287.81328385   1.02602529]
# [ 12.48388274 285.78779605   1.52080974]
# [ 10.54463789 286.53769483   2.56790955]
# [ 12.53725711 284.02903769   2.52852048]
# [ 10.76654366 284.3961478    1.3009594 ]
# [ 12.25423606 282.72711822   1.02319664]
# [ 10.93012718 282.71627695   2.52861523]
# [ 12.49479844 281.27580845   2.53444684]
# [ 10.94711917 281.15104588   1.00161702]
# [ 12.49943031 279.66265767   1.16087802]
# [ 10.8229865  279.52698664   2.45029543]
# [ 12.57160484 278.22855226   2.58860822]
# [ 11.29281337 277.91241088   1.06430602]
# [ 12.79488924 275.78195598   1.09426742]
# [ 10.78423674 275.79595786   2.59985251]
# [ 12.36972998 274.38436538   2.49064116]
# [ 10.94645351 274.33916543   1.08072932]
# [ 12.66035496 272.97632398   1.05122776]
# [ 11.07882216 272.8476941    2.49770178]
# [ 12.33873834 270.96606405   2.56792552]
# [ 10.89609778 270.77335966   1.03918063]
# [ 12.4190369  269.30199805   1.05491466]
# [ 11.07005003 269.0898663    2.56244654]
# [ 12.85684174 267.66341672   2.597144  ]
# [ 10.89341934 267.59444619   1.16832612]
# [ 12.50728393 266.30253685   1.07722731]
# [ 11.03628414 266.04214219   2.46302229]
# [ 12.76529513 264.10233487   2.5520776 ]
# [ 11.21570596 264.48135932   1.04856372]
# [ 12.44281955 262.84653114   1.0264361 ]
# [ 10.62788231 262.84375503   2.53008342]
# [ 12.71051967 261.35903747   2.51003448]
# [ 10.77919759 261.21948702   1.11090172]
# [ 12.66673592 259.47974693   1.05381156]
# [ 10.8678528  259.49750329   2.47711918]
# [ 12.72231779 258.03436011   2.55975571]
# [ 10.92147544 257.96667487   1.07286714]
# [ 12.59324563 256.30009098   1.16979336]
# [ 11.05632283 255.98942924   2.54966192]
# [ 12.78788955 254.74547801   2.50005759]
# [ 10.77779196 254.66574747   1.04187824]
# [ 12.72544788 253.02258345   1.17138848]
# [ 10.99103287 253.04775628   2.56372531]
# [ 12.57434565 251.49348655   2.48881957]
# [ 10.84715574 251.61002694   1.08350682]
# [ 12.5546404  249.92872796   1.02230457]
# [ 10.91158375 249.93618901   2.31776514]
# [ 12.69105995 248.21888207   2.48301342]
# [ 11.26359697 248.25806201   1.08263371]
# [ 12.72616904 246.28804159   1.06960375]
# [ 11.38300236 246.49528835   2.54875841]
# [ 12.73736574 244.90958234   2.52080976]
# [ 11.02804411 244.91093025   1.00545568]
# [ 13.01313528 243.37224701   1.03184372]
# [ 11.33113313 243.16583808   2.57345892]
# [ 12.56059467 241.57932354   2.54204201]
# [ 11.07735079 241.42854058   1.18089213]
# [ 12.68141716 239.96752261   1.19407427]
# [ 11.02560634 239.96206682   2.59767643]
# [ 12.65435835 238.07917548   2.47219224]
# [ 11.03492715 238.45138091   1.00093623]
# [ 12.79688637 236.68981706   1.01929227]
# [ 11.63444402 236.04993267   2.59731614]
# [ 12.58675699 234.05918415   2.51775396]
# [ 11.15438469 234.14219939   1.08669885]
# [ 12.65642566 232.62469828   1.10116626]
# [ 10.89968574 232.80525998   2.59665535]
# [ 12.35145182 230.78972239   2.56991334]
# [ 10.98834828 231.47610289   1.07950151]
# [ 12.57340201 229.41527922   1.03706288]
# [ 10.56308931 229.79123139   2.50961703]
# [ 12.46151694 228.06370388   2.5787228 ]
# [ 10.54049295 228.06226473   1.27805075]
# [ 12.55026385 226.35793775   1.1308474 ]
# [ 10.55777788 226.52200596   2.56794286]
# [ 12.30854294 224.69129923   2.58991848]
# [ 10.60707782 225.00512829   1.09096917]
# [ 12.68750357 223.26039317   1.03790414]
# [ 10.59351246 223.1094567    2.4927815 ]
# [ 12.56988387 221.73965999   2.59899987]
# [ 11.07931156 221.72396231   1.07597012]
# [ 12.67404324 220.09013471   1.00039252]
# [ 11.17253517 219.84821302   2.4391051 ]
# [ 12.53904827 218.32163032   2.52329112]
# [ 10.96833068 218.35167012   1.03128123]
# [ 12.66154167 216.9539838    1.02441325]
# [ 10.90196621 216.91309782   2.52108892]
# [ 12.50931561 215.4387762    2.59536591]
# [ 11.11814865 214.76125387   1.20728751]
# [ 12.41443515 212.99557227   1.14297954]
# [ 10.73242225 213.18544      2.57771177]
# [ 12.56705355 211.49479829   2.50859114]
# [ 10.75930689 211.86396905   1.05224338]
# [ 12.69042069 209.88322235   1.11843153]
# [ 10.97551049 209.83361485   2.57271709]
# [ 12.84171138 208.25896359   2.47666956]
# [ 11.18658025 208.15623506   1.18134127]
# [ 12.75072206 206.56491516   1.11147461]
# [ 11.29350721 206.68772707   2.54989756]
# [ 13.09273654 204.96042949   2.59998189]
# [ 10.81486101 204.78018473   1.12055688]
# [ 12.85366068 203.51827009   1.0365249 ]
# [ 11.0639185  203.04364053   2.49200105]
# [ 12.75911725 201.8549439    2.52263896]
# [ 11.45081277 201.71402673   1.01044239]
# [ 13.14892912 200.34449856   1.05122524]
# [ 11.15123146 200.1430976    2.52029516]
# [ 12.83996572 198.6031819    2.43106218]
# [ 10.69982113 198.83468151   1.02218904]
# [ 12.59197986 197.14453698   1.00100673]
# [ 10.9701775  197.08912676   2.50362478]
# [ 12.51552411 195.62163981   2.59541501]
# [ 10.96267241 195.46692615   1.07617024]
# [ 12.52630466 193.57560885   1.0020794 ]
# [ 10.97966204 193.84429555   2.54055045]
# [ 12.72286843 192.30666348   2.59542444]
# [ 10.85884494 192.4530552    1.02424686]
# [ 12.03018325 190.56873201   1.06685074]
# [ 10.62689323 190.40084658   2.56476065]
# [ 13.06033662 188.70837068   2.59926944]
# [ 10.96242243 188.8747441    1.17541615]
# [ 12.98208583 187.29288823   1.08081439]
# [ 11.18173537 187.33811227   2.54301083]
# [ 12.57805338 185.79842841   2.50515949]
# [ 10.98998807 185.6331001    1.11639506]
# [ 12.7500489  184.13613687   1.08889746]
# [ 11.31289613 183.96601956   2.58846722]
# [ 12.74238031 182.30808748   2.55538666]
# [ 11.15148452 182.29812295   1.10602331]
# [ 12.30891562 180.65236682   1.03391637]
# [ 11.00217434 180.66609589   2.58426523]
# [ 12.67656548 179.04301197   2.58613737]
# [ 10.94976344 179.18358229   1.13159263]
# [ 13.0783476  177.75222116   1.04813347]
# [ 11.31242942 177.47114048   2.50834377]
# [ 13.19029532 175.89144542   2.58692984]
# [ 11.22854932 175.73230549   1.03872942]
# [ 12.98951032 174.21737188   1.13960321]
# [ 11.32283967 174.21756983   2.46350653]
# [ 12.96039327 172.44127393   2.54830817]
# [ 11.34692493 172.39154085   1.06409334]
# [ 12.91971224 170.94784518   1.18861823]
# [ 11.35791643 170.98610778   2.50594107]
# [ 13.06789417 169.13838868   2.54848767]
# [ 11.64345541 169.21102338   1.11901584]
# [ 12.90463265 167.47460245   1.05186634]
# [ 11.38334156 167.52541237   2.54479461]
# [ 12.76245542 165.91310665   2.43792777]
# [ 11.27268487 166.08209185   1.06928657]
# [ 12.77793325 164.48736864   1.00615922]
# [ 11.027829   164.2966106    2.45523394]
# [ 12.76350995 162.58250247   2.58752599]
# [ 11.0828692  162.67877789   1.17289527]
# [ 12.83773496 161.25866744   1.03538815]
# [ 11.24474608 160.96610342   2.45803124]
# [ 12.84955434 158.94609577   2.57032522]
# [ 11.53169431 159.53832066   1.00575724]
# [ 12.70603476 157.5568773    1.05994802]
# [ 10.86474558 157.85462582   2.54039177]
# [ 12.52451406 156.05551842   2.59829471]
# [ 11.13652683 156.05886985   1.04204   ]
# [ 12.79649645 154.36761185   1.09467357]
# [ 11.09039984 154.61944663   2.54926745]
# [ 12.2325834  152.79418293   2.58347399]
# [ 10.96171205 152.74618601   1.02170936]
# [ 12.49982676 151.38337851   1.11527646]
# [ 10.61231668 151.28280683   2.58333368]
# [ 13.05439946 149.13749084   2.47847144]
# [ 11.43599901 149.53266993   1.30997392]
# [ 12.71127984 147.64987252   1.14552645]
# [ 10.92499422 147.52010161   2.59652263]
# [ 12.51817759 146.06079085   2.54615097]
# [ 10.87246424 146.00055641   1.05036483]
# [ 12.5698284  144.68078667   1.04673572]
# [ 11.29439753 144.18374516   2.57030368]
# [ 12.75443996 142.62476421   2.57416364]
# [ 11.10136762 142.65291492   1.28820219]
# [ 12.55813996 141.12849366   1.04433179]
# [ 10.97451104 141.08061641   2.55498928]
# [ 12.5439421  139.64778554   2.38954133]
# [ 10.91729189 139.40557682   1.119268  ]
# [ 12.31702978 137.94412502   1.04147872]
# [ 10.96659696 137.55210398   2.5957234 ]
# [ 12.26465958 135.95365184   2.52750173]
# [ 10.77978559 136.01412396   1.02630763]
# [ 12.26932325 134.50509875   1.06059596]
# [ 10.85233093 134.18311962   2.48494188]
# [ 12.42128447 132.74178565   2.42562451]
# [ 10.53312718 132.53554732   1.02322147]
# [ 12.48969886 131.23884017   1.01708401]
# [ 10.68804351 131.20989417   2.54181103]
# [ 12.01678282 129.54667325   2.596926  ]
# [ 10.41279521 129.72056476   1.02720549]
# [ 12.3589599  128.19821441   1.08523291]
# [ 10.57509312 128.0839627    2.39696176]
# [ 12.33486416 126.03917983   2.58829001]
# [ 10.82039544 126.51902815   1.15830105]
# [ 12.32560319 124.54572371   1.08255143]
# [ 10.5774394  124.77344702   2.54584921]
# [ 12.46272527 122.75630054   2.56478745]
# [ 11.04553678 122.97414585   1.12443772]
# [ 12.53321856 121.22161224   1.11479776]
# [ 10.77199298 121.49983429   2.58563639]
# [ 12.32378721 119.68698956   2.55431621]
# [ 10.70829347 119.67100691   1.09419737]
# [ 12.68692865 117.72898341   1.0177964 ]
# [ 11.0395822  118.09648121   2.55057989]
# [ 11.95388123 114.69440271   1.00788349]
# [ 10.63231054 115.12326614   2.53590163]
# [ 12.11126661 113.1982583    2.57583139]
# [ 10.73617135 113.04775685   1.02957595]
# [ 12.32134305 111.38713439   1.69163725]
# [ 10.48944418 111.43368422   2.5124862 ]
# [ 12.4248702  109.42461244   2.59321771]
# [ 11.0378361  109.62952231   1.07775581]
# [ 12.47133253 108.0298805    1.09885359]
# [ 10.75919032 108.16136964   2.55521415]
# [ 12.16213376 106.21256307   2.58126532]
# [ 10.91089037 106.56192955   1.029397  ]
# [ 12.64316815 104.52379081   1.13138901]
# [ 11.10674447 104.36524126   2.59794347]
# [ 12.74291783 102.5603702    2.59907455]
# [ 11.07369823 102.97371632   1.11364824]
# [ 12.26636652 100.73695264   1.06528473]
# [ 11.03951321 101.155922     2.59956115]
# [12.58095502 99.37611229  2.59415312]
# [10.30273397 99.65102314  1.01705431]
# [12.43895586 97.8200571   1.22937285]
# [10.5178466  98.06174272  2.48031247]
# [12.41397736 96.23920747  2.55290281]
# [10.78899429 96.56939782  1.15402777]
# [12.28923521 94.87874536  1.07910313]
# [10.5743657  94.56289414  2.45497143]
# [12.12783752 93.26798184  2.41738276]
# [10.41177002 92.92843643  1.13879875]
# [12.01437755 91.55347467  1.22446793]
# [10.51885793 91.08689999  2.57521163]
# [12.29853869 89.73497963  2.59890668]
# [10.82076465 89.71130487  1.12311986]
# [12.51466754 88.07283572  1.07883642]
# [10.53751868 88.33615968  2.58506174]
# [12.71686081 86.35846533  2.57750001]
# [10.72724928 86.77259984  1.00605186]
# [12.32527859 84.67026467  1.1177352 ]
# [10.78590499 84.95726294  2.41631787]
# [12.13348867 83.16466758  2.54280168]
# [10.59378793 83.24063941  1.12130141]
# [12.23569087 81.72231904  1.02348355]
# [10.48108537 81.76086731  2.59052224]
# [12.05344122 80.29313959  2.56920434]
# [10.40115174 80.37171649  1.06373629]
# [11.83739901 78.7482983   1.0656071 ]
# [10.26541522 78.62164068  2.58535818]
# [12.32603504 77.31115614  2.40298799]
# [10.41494342 77.05483421  1.21724753]
# [11.91511207 75.70649867  1.13615849]
# [10.46447644 75.35803176  2.56442094]
# [12.42031569 74.32242046  2.5930068 ]
# [11.06027846 73.70353785  1.06548288]
# [12.72763476 72.3791448   1.20521483]
# [11.08620544 72.17291024  2.51494781]
# [12.85124204 70.80450223  2.58151553]
# [10.99860972 70.27876003  1.14485344]
# [12.83351513 69.4687199   1.03730636]
# [10.92260937 68.73486742  2.46986009]
# [12.64723319 67.71782312  2.24702857]
# [10.84213252 67.09974067  1.0342735 ]
# [12.22558459 65.35432671  1.04738143]
# [10.94354861 65.73928603  2.54432827]
# [12.49398728 63.85982989  2.41495071]
# [10.78517187 63.59526235  1.06405028]
# [12.39172014 62.37087167  1.00706244]
# [10.90287512 62.04729307  2.5087406 ]
# [12.37403689 60.61834301  2.43686488]
# [10.71386898 60.72223021  1.00864988]
# [12.31502712 58.74830472  1.04004408]
# [10.65863083 58.83642247  2.41231171]
# [11.95110495 57.21816061  2.53700905]
# [10.57925257 57.2693153   1.00787267]
# [12.26138167 55.8658933   1.03515228]
# [10.58735943 55.59956268  2.29345829]
# [12.14377635 54.14019533  2.57567063]
# [10.8436098  53.90194479  1.0511753 ]
# [12.26869284 52.4546947   1.17479027]
# [10.71045793 52.51450517  2.51170074]
# [12.35887093 50.63140972  2.46170186]
# [10.68715131 50.8553472   1.10265249]
# [12.17775741 49.13144579  1.15096669]
# [10.69134723 48.98951956  2.53993986]
# [12.27747793 47.44041608  2.58427012]
# [10.91411025 47.0905392   1.13943607]
# [12.58956637 45.91214839  1.0078943 ]
# [10.85020522 45.52887401  2.55775958]
# [12.91012013 44.34751763  2.5226466 ]
# [11.09784701 44.08347761  1.15005082]
# [12.46945187 42.50943973  1.06914171]
# [11.08249693 42.55081796  2.59338366]
# [12.56966518 40.79260532  2.37109551]
# [10.79767226 41.07612025  1.07167248]
# [12.52667254 39.1909261   1.09426037]
# [11.07149918 39.26880104  2.54440405]
# [12.49165149 37.52004911  2.56541024]
# [11.04667232 37.67462759  1.00299442]
# [12.18643742 35.75845268  1.05207331]
# [10.88174712 35.46106406  2.57141187]
# [12.35548889 33.98806713  2.58681683]
# [10.14886723 33.80402746  1.03176304]
# [12.12846603 32.62912788  1.01595924]
# [10.53695154 32.22920695  2.46992006]
# [12.61402434 30.40292696  2.59188503]
# [10.36044863 30.69092659  1.12902825]
# [11.94133804 29.27282011  1.03885857]
# [10.45815494 29.17595732  2.5402129 ]
# [12.21177035 27.71544891  2.37435464]
# [10.70074281 27.63011838  1.02044461]
# [11.99769085 25.81057204  1.08831804]
# [10.59395198 25.60944679  2.56267392]
# [12.38300471 24.5075427   2.57631676]
# [10.81904968 22.72941079  2.53068669]
# [10.73212374 24.22724865  1.11372047]
# [10.73212374 24.22724865  1.11372047]
# [ 9.47801363 22.58118488  1.04368082]
# [ 9.16190854 24.14543558  2.51269298]
# [ 7.84486084 22.53758467  2.35931217]
# [ 7.68635002 24.20075647  1.13909848]
# [ 6.09957    22.38336586  1.1012371 ]
# [ 6.30988295 24.13292597  2.59111859]
# [ 4.68130563 22.62829115  2.54655191]
# [ 4.81170751 24.20033184  1.24696162]
# [ 3.03625727 22.78296566  1.2321413 ]
# [ 2.89872743 24.64648486  2.41681512]
# [ 1.40343149 22.57259059  2.52070377]
# [ 1.32252305 24.22360289  1.20304063]
