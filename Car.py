import numpy as np #line:2
class Car (object ):#line:4
    def __init__ (O0000000O0OO0O0O0 ):#line:5
        class O0OO00OO0OO0O0O0O (object ):#line:6
            def __init__ (OO0000OO0OOO000O0 ,O00OO000OOOO0O000 ):#line:8
                OO0000OO0OOO000O0 .rpm =O00OO000OOOO0O000 .engine .idle_rpm #line:9
                OO0000OO0OOO000O0 .speed =0 #line:10
                OO0000OO0OOO000O0 .acc =0 #line:11
                OO0000OO0OOO000O0 .dist =0 #line:12
                OO0000OO0OOO000O0 .time =0 #line:13
                OO0000OO0OOO000O0 .w_wheel =0 #line:14
                OO0000OO0OOO000O0 .prevshifttime =-1 #line:15
                OO0000OO0OOO000O0 .gotogear =1 #line:16
                OO0000OO0OOO000O0 .gear =0 #line:17
                OO0000OO0OOO000O0 .throttle =0 #line:18
        class OO0O00O00000OO000 ():#line:20
            def __init__ (O0O0O0OOOOO000OOO ):#line:22
                O0O0O0OOOOO000OOO .b0 =1.6 #line:23
                O0O0O0OOOOO000OOO .b1 =-58 #line:24
                O0O0O0OOOOO000OOO .b2 =1750 #line:25
                O0O0O0OOOOO000OOO .b3 =6.8 #line:26
                O0O0O0OOOOO000OOO .b4 =200 #line:27
                O0O0O0OOOOO000OOO .b5 =0 #line:28
                O0O0O0OOOOO000OOO .b6 =0.0034 #line:29
                O0O0O0OOOOO000OOO .b7 =-0.008 #line:30
                O0O0O0OOOOO000OOO .b8 =-0.76 #line:31
                O0O0O0OOOOO000OOO .b9 =0 #line:32
                O0O0O0OOOOO000OOO .b10 =0 #line:33
                O0O0O0OOOOO000OOO .b11 =0 #line:34
                O0O0O0OOOOO000OOO .b12 =0 #line:35
        class O0O0O0O000O0OOOO0 ():#line:37
            def __init__ (O00OOOOOO0OO0O00O ):#line:38
                O00OOOOOO0OO0O00O .rpm =np .array ([0 ,511.11 ,1211.11 ,2044.45 ,4166.66 ,5200 ,5533.34 ,5922.22 ,6322.22 ,6500 ,6955.56 ,7488.89 ,7500 ,7922.22 ,8000 ,8300 ,8500 ,10000 ,10500 ])#line:44
                O00OOOOOO0OO0O00O .torque =np .array ([0.1894 ,0.2030 ,0.2421 ,0.2740 ,0.3784 ,0.8142 ,0.8702 ,0.9501 ,0.9994 ,0.9994 ,0.9450 ,0.9025 ,0.9242 ,0.8668 ,0.9027 ,0.7887 ,0.8597 ,0 ,0 ])#line:50
                O00OOOOOO0OO0O00O .torque =np .multiply (O00OOOOOO0OO0O00O .torque ,864 )#line:52
                O00OOOOOO0OO0O00O .max_rpm =8500 #line:53
                O00OOOOOO0OO0O00O .idle_rpm =1850 #line:54
        class O00OO0O000OOOOOO0 ():#line:56
            def __init__ (O00O0O0000OO00OO0 ):#line:57
                O00O0O0000OO00OO0 .gears =4 -1 #line:59
                O00O0O0000OO00OO0 .ratio =np .array ([3.8 ,2.3 ,1.4 ,0.95 ])#line:61
                O00O0O0000OO00OO0 .final =4.03 #line:63
                O00O0O0000OO00OO0 .shiftingtime =0.1 #line:64
        class OO0O00O0OOOOOOOOO ():#line:66
            def __init__ (O0OOO00OO0OOOO00O ):#line:67
                O0OOO00OO0OOOO00O .inertia =2.04 +2.05 /2 +0.1 /2 +0.05 #line:68
                O0OOO00OO0OOOO00O .radius =0.32 #line:69
                O0OOO00OO0OOOO00O .rollcoeff =0.015 #line:70
        class OOOOO00OOO00000O0 ():#line:72
            def __init__ (O00O0OOOOO0OO00O0 ):#line:73
                O00O0OOOOO0OO00O0 .mass =1030 +46 +36 +30 #line:74
                O00O0OOOOO0OO00O0 .cog_height =0.4 #line:75
                O00O0OOOOO0OO00O0 .wheel_base =2.273 #line:76
        class O0OO0000OO000000O ():#line:78
            def __init__ (O000O00O0OOO0O0O0 ):#line:79
                O000O00O0OOO0O0O0 .frontal_area =1.9 #line:80
                O000O00O0OOO0O0O0 .down_coefficient =0.1 #line:81
                O000O00O0OOO0O0O0 .drag_coefficient =0.3 #line:82
                O000O00O0OOO0O0O0 .air_density =1.225 #line:83
        O0000000O0OO0O0O0 .pacejka =OO0O00O00000OO000 ()#line:86
        O0000000O0OO0O0O0 .engine =O0O0O0O000O0OOOO0 ()#line:89
        O0000000O0OO0O0O0 .gearbox =O00OO0O000OOOOOO0 ()#line:92
        O0000000O0OO0O0O0 .wheel =OO0O00O0OOOOOOOOO ()#line:95
        O0000000O0OO0O0O0 .chassis =OOOOO00OOO00000O0 ()#line:98
        O0000000O0OO0O0O0 .aero =O0OO0000OO000000O ()#line:101
        O0000000O0OO0O0O0 .dyn =O0OO00OO0OO0O0O0O (O0000000O0OO0O0O0 )#line:104
        O0000000O0OO0O0O0 .optimal_slip =15.5 #line:106
        O0000000O0OO0O0O0 .version =240913 