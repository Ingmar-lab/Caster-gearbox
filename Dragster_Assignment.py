import copy #line:1
import matplotlib .pyplot as plt #line:2
from Car import Car #line:3
import math #line:4
import numpy as np #line:5
from student_AutomaticGearbox import student_AutomaticGearbox #line:6
def caster_GearShift (OO0OO0O0O0OO000O0 ,O0OO00O00O00O0000 ,O000OO000OOO00O0O ,OOOOOO0O00O00OOOO ):#line:8
    OOOO00O0O0OOO0O00 =1.3 #line:9
    if O0OO00O00O00O0000 ==0 and OOOOOO0O00O00OOOO :#line:11
        print ("GearShift version ",OOOO00O0O0OOO0O00 )#line:12
    O0O0OOO00O00OO00O =O000OO000OOO00O0O .gearbox .shiftingtime #line:14
    OO0OO0O0O0OO000O0 =min (OO0OO0O0O0OO000O0 ,O000OO000OOO00O0O .gearbox .gears )#line:17
    OO0OO0O0O0OO000O0 =max (-1 ,OO0OO0O0O0OO000O0 )#line:18
    if O000OO000OOO00O0O .dyn .time -O0OO00O00O00O0000 >=O0O0OOO00O00OO00O :#line:21
        if OO0OO0O0O0OO000O0 !=O000OO000OOO00O0O .dyn .gear :#line:23
            if O000OO000OOO00O0O .dyn .gear !=-1 :#line:25
                O000OO000OOO00O0O .dyn .gear =-1 #line:26
                O0OO00O00O00O0000 =O000OO000OOO00O0O .dyn .time #line:27
                O000OO000OOO00O0O .dyn .gotogear =OO0OO0O0O0OO000O0 #line:28
            else :#line:29
                O000OO000OOO00O0O .dyn .gear =O000OO000OOO00O0O .dyn .gotogear #line:30
                O0OO00O00O00O0000 =O000OO000OOO00O0O .dyn .time #line:31
    return O0OO00O00O00O0000 #line:33
def caster_GetTelemetry (O00O0000OOOOO0OOO ,O0O0OOOO0O00OOO0O ):#line:35
    class OO0OOO0OOO0O000O0 (object ):#line:37
        def __init__ (OO0O0O000O00000OO ,O0O0O00OO0O00OOOO ):#line:38
            OO0O0O000O00000OO .Gear =O0O0O00OO0O00OOOO .dyn .gear #line:39
            OO0O0O000O00000OO .Throttle =O0O0O00OO0O00OOOO .dyn .throttle #line:40
            caster_dragsterCar (O0O0O00OO0O00OOOO )#line:41
            OO0O0O000O00000OO .RPM =O0O0O00OO0O00OOOO .dyn .rpm #line:42
            OO0O0O000O00000OO .LongAcc =O0O0O00OO0O00OOOO .dyn .acc #line:43
            OO0O0O000O00000OO .Velocity =O0O0O00OO0O00OOOO .dyn .speed #line:44
            OO0O0O000O00000OO .Distance =O0O0O00OO0O00OOOO .dyn .dist #line:45
            OO0O0O000O00000OO .TimeLap =O0O0O00OO0O00OOOO .dyn .time #line:46
            OO0O0O000O00000OO .TimeTotal =O0O0O00OO0O00OOOO .dyn .time #line:47
    O00OOOO00O000000O =1.4 #line:49
    if O00O0000OOOOO0OOO .dyn .time ==0 and O0O0OOOO0O00OOO0O :#line:51
        print ("GetTelemetry version ",O00OOOO00O000000O )#line:52
    O0O0OOOO00O0000O0 =OO0OOO0OOO0O000O0 (O00O0000OOOOO0OOO )#line:56
    return O0O0OOOO00O0000O0 #line:57
def caster_dragsterCar (O00O00O0O0O00OO00 ):#line:59
    O00OO0O0O0000O00O =0.01 #line:61
    O0O00000000OOO0O0 =O00O00O0O0O00OO00 .dyn .rpm #line:64
    O0O000O0OOOOOOOO0 =O00O00O0O0O00OO00 .dyn .acc #line:65
    OO00OOO0OOO000O00 =O00O00O0O0O00OO00 .dyn .speed #line:66
    OOOOOOOOO00OOO0OO =O00O00O0O0O00OO00 .dyn .dist #line:67
    O0OOOOOO000OO0OOO =O00O00O0O0O00OO00 .dyn .time #line:68
    O00O0O0000O00O000 =O00O00O0O0O00OO00 .dyn .throttle #line:69
    O0O0OOO0OOO0O0O00 =O00O00O0O0O00OO00 .dyn .gear #line:70
    O0OO0O00000OOOO0O =O00O00O0O0O00OO00 .dyn .w_wheel #line:71
    O0O0OOO0OOO0O0O00 =max (min (O0O0OOO0OOO0O0O00 ,O00O00O0O0O00OO00 .gearbox .gears ),-1 )#line:75
    O00O0O0000O00O000 =max (min (O00O0O0000O00O000 ,1 ),0 )#line:76
    if O0O0OOO0OOO0O0O00 ==-1 :#line:79
        OO000OOOOOOO0OO00 =0 #line:80
    else :#line:81
        OO000OOOOOOO0OO00 =O00O00O0O0O00OO00 .gearbox .ratio [O0O0OOO0OOO0O0O00 ]#line:82
    O0O0000000000OOO0 =np .interp (O0O00000000OOO0O0 ,O00O00O0O0O00OO00 .engine .rpm ,O00O00O0O0O00OO00 .engine .torque )*O00O0O0000O00O000 #line:84
    O000O0OO0OOOO0OO0 =O0O0000000000OOO0 *OO000OOOOOOO0OO00 *O00O00O0O0O00OO00 .gearbox .final /2 #line:85
    OOO0O00OO0OOOO0OO =O000O0OO0OOOO0OO0 /O00O00O0O0O00OO00 .wheel .radius #line:86
    if OO000OOOOOOO0OO00 !=0 :#line:89
        O0OO0O00000OOOO0O =(O0O00000000OOO0O0 /OO000OOOOOOO0OO00 /O00O00O0O0O00OO00 .gearbox .final )*(2 *math .pi )/60 #line:90
    OOO000O0O00OOOO00 =O0OO0O00000OOOO0O *O00O00O0O0O00OO00 .wheel .radius #line:92
    O0O000OOOO00O00OO =(OOO000O0O00OOOO00 /max (OO00OOO0OOO000O00 ,0.01 )-1 )*100 #line:95
    O000OO00OOOOO0O00 =O00O00O0O0O00OO00 .aero .drag_coefficient *O00O00O0O0O00OO00 .aero .frontal_area *O00O00O0O0O00OO00 .aero .air_density *OO00OOO0OOO000O00 **2 /2 #line:99
    OO000OO00OOO00O0O =O00O00O0O0O00OO00 .aero .down_coefficient *O00O00O0O0O00OO00 .aero .frontal_area *O00O00O0O0O00OO00 .aero .air_density *OO00OOO0OOO000O00 **2 /2 #line:102
    O0O00000OOOOO0OO0 =O00O00O0O0O00OO00 .chassis .mass *O0O000O0OOOOOOOO0 #line:105
    O0OOOOOO000OO000O =O00O00O0O0O00OO00 .chassis .mass *9.81 #line:108
    O00OO0OO00OO00O00 =(O00O00O0O0O00OO00 .chassis .cog_height /O00O00O0O0O00OO00 .chassis .wheel_base )*(O0O00000OOOOO0OO0 +O000OO00OOOOO0O00 )/2 +(OO000OO00OOO00O0O /4 )+(O0OOOOOO000OO000O /4 )#line:111
    O0OO000OOOO0O0OO0 =caster_Pacejka96 (O00O00O0O0O00OO00 .pacejka ,O00OO0OO00OO00O00 ,O0O000OOOO00O00OO )#line:114
    O00OOOO0000O0O000 =O0OO000OOOO0O0OO0 *O00OO0OO00OO00O00 #line:115
    O0O0O00O0OO0O0OO0 =min (O00OOOO0000O0O000 ,OOO0O00OO0OOOO0OO )#line:116
    O0O000O0OOOOOOOO0 =((O0O0O00O0OO0O0OO0 *2 )-O000OO00OOOOO0O00 -(O0OOOOOO000OO000O +OO000OO00OOO00O0O )*O00O00O0O0O00OO00 .wheel .rollcoeff )/O00O00O0O0O00OO00 .chassis .mass #line:119
    OO00OOO0OOO000O00 =OO00OOO0OOO000O00 +O0O000O0OOOOOOOO0 *O00OO0O0O0000O00O #line:120
    OOOO00OO000O0OO0O =OOO0O00OO0OOOO0OO -O00OOOO0000O0O000 #line:123
    OOO00O0000OOOOOOO =(OOOO00OO000O0OO0O *O00O00O0O0O00OO00 .wheel .radius )/O00O00O0O0O00OO00 .wheel .inertia #line:126
    O0OO0O00000OOOO0O =O0OO0O00000OOOO0O +OOO00O0000OOOOOOO *O00OO0O0O0000O00O #line:127
    O000O00OOO000OOO0 =O0OO0O00000OOOO0O /(2 *math .pi )*60 *O00O00O0O0O00OO00 .gearbox .final *OO000OOOOOOO0OO00 #line:129
    O0O00000000OOO0O0 =max (O000O00OOO000OOO0 ,O00O00O0O0O00OO00 .engine .idle_rpm )#line:131
    OOOOOOOOO00OOO0OO =OOOOOOOOO00OOO0OO +OO00OOO0OOO000O00 *O00OO0O0O0000O00O #line:134
    O0OOOOOO000OO0OOO =O0OOOOOO000OO0OOO +O00OO0O0O0000O00O #line:135
    O00O00O0O0O00OO00 .dyn .rpm =O0O00000000OOO0O0 #line:137
    O00O00O0O0O00OO00 .dyn .acc =O0O000O0OOOOOOOO0 #line:138
    O00O00O0O0O00OO00 .dyn .speed =OO00OOO0OOO000O00 #line:139
    O00O00O0O0O00OO00 .dyn .dist =OOOOOOOOO00OOO0OO #line:140
    O00O00O0O0O00OO00 .dyn .time =O0OOOOOO000OO0OOO #line:141
    O00O00O0O0O00OO00 .dyn .throttle =O00O0O0000O00O000 #line:142
    O00O00O0O0O00OO00 .dyn .gear =O0O0OOO0OOO0O0O00 #line:143
    O00O00O0O0O00OO00 .dyn .w_wheel =O0OO0O00000OOOO0O #line:144
def caster_Pacejka96 (OO000O00O00OOO0O0 ,OO0O00OOOOO0000O0 ,OOOO00OO0O000OO0O ):#line:146
    OO0O00OOOOO0000O0 =OO0O00OOOOO0000O0 /1000 #line:148
    O0O0000O0OO0O0000 =OO000O00O00OOO0O0 .b0 #line:149
    O00000OO00OOO00O0 =(OO000O00O00OOO0O0 .b1 *OO0O00OOOOO0000O0 +OO000O00O00OOO0O0 .b2 )*OO0O00OOOOO0000O0 #line:150
    O0000OOOOO0OOOOO0 =(OO000O00O00OOO0O0 .b3 *OO0O00OOOOO0000O0 **2 +OO000O00O00OOO0O0 .b4 *OO0O00OOOOO0000O0 )*math .exp (-OO000O00O00OOO0O0 .b5 *OO0O00OOOOO0000O0 )#line:151
    OOOO0OO0OO0000O0O =O0000OOOOO0OOOOO0 /(O0O0000O0OO0O0000 *O00000OO00OOO00O0 )#line:152
    O0O00OOO00O0O0OO0 =OO000O00O00OOO0O0 .b9 *OO0O00OOOOO0000O0 +OO000O00O00OOO0O0 .b10 #line:153
    O0OOOOOO0O00OOOOO =0 #line:154
    O0O000O0O0O000OO0 =(OO000O00O00OOO0O0 .b6 *OO0O00OOOOO0000O0 **2 +OO000O00O00OOO0O0 .b7 *OO0O00OOOOO0000O0 +OO000O00O00OOO0O0 .b8 )#line:155
    O00OOO00OOO000OO0 =O00000OO00OOO00O0 *math .sin (O0O0000O0OO0O0000 *math .atan (OOOO0OO0OO0000O0O *(1 -O0O000O0O0O000OO0 )*(OOOO00OO0O000OO0O +O0O00OOO00O0O0OO0 )+O0O000O0O0O000OO0 *math .atan (OOOO0OO0OO0000O0O *(OOOO00OO0O000OO0O +O0O00OOO00O0O0OO0 ))))+O0OOOOOO0O00OOOOO #line:156
    O00O0OOOO000O0O0O =O00OOO00OOO000OO0 /(OO0O00OOOOO0000O0 *1000 )#line:157
    return O00O0OOOO000O0O0O #line:159
def caster_InitCommunication (O00OO0OO000O0OOOO ):#line:161
    OO0OO0O00OOO00OOO =1.5 #line:162
    if O00OO0OO000O0OOOO :#line:164
        print ("InitCommunication Version ",OO0OO0O00OOO00OOO )#line:165
    OO0O0O0000O0O000O =Car ()#line:167
    if not hasattr (OO0O0O0000O0O000O ,"version"):#line:168
        print ("It's fun to modify the car, but for this task it is considered cheating and not allowed.")#line:169
        return #line:170
    else :#line:171
        if OO0O0O0000O0O000O .version ==240913 :#line:172
            return OO0O0O0000O0O000O #line:173
        else :#line:174
            print ("It's fun to modify the car, but for this task it is considered cheating and not allowed.")#line:175
            return #line:176
def main (O00OO0OOO0000O0OO ):#line:178
    print ("Main program Version 2.0")#line:191
    OOOOO0000O0000O0O =caster_InitCommunication (O00OO0OOO0000O0OO )#line:195
    OO00O0OOO0000OOOO =40 #line:197
    O0000OOO00000O00O =0 #line:198
    O00OOOO0O0OO00OO0 =list ()#line:199
    O0OOO00O000O0OO00 =1 #line:200
    O000O00OOOO0OO0O0 =True #line:201
    while (O0000OOO00000O00O <=OO00O0OOO0000OOOO ):#line:203
        if O000O00OOOO0OO0O0 :#line:204
            (O0O0000O0O0OO00O0 ,OOOO0O0000OO00OOO )=student_AutomaticGearbox (OOOOO0000O0000O0O .dyn .gear +1 ,OOOOO0000O0000O0O .dyn .rpm ,OOOOO0000O0000O0O .dyn .acc ,OOOOO0000O0000O0O .dyn .speed ,OOOOO0000O0000O0O .dyn .throttle ,OOOOO0000O0000O0O .dyn .dist ,OOOOO0000O0000O0O .dyn .time )#line:205
            O000O00OOOO0OO0O0 =False #line:206
        else :#line:207
            OOOOO00000O0O00O0 =caster_GetTelemetry (OOOOO0000O0000O0O ,O00OO0OOO0000O0OO )#line:209
            O00OOOO0O0OO00OO0 .append (copy .deepcopy (OOOOO00000O0O00O0 ))#line:210
            (O0O0000O0O0OO00O0 ,OOOO0O0000OO00OOO )=student_AutomaticGearbox (OOOOO00000O0O00O0 .Gear +1 ,OOOOO00000O0O00O0 .RPM ,OOOOO00000O0O00O0 .LongAcc ,OOOOO00000O0O00O0 .Velocity ,OOOOO00000O0O00O0 .Throttle ,OOOOO00000O0O00O0 .Distance ,OOOOO00000O0O00O0 .TimeLap )#line:211
            O0000OOO00000O00O =OOOOO00000O0O00O0 .Distance #line:212
        if O00OO0OOO0000O0OO :#line:213
            if O0O0000O0O0OO00O0 <=0 :#line:214
                print ("You have tried to put in reverse or neutral (",O0O0000O0O0OO00O0 ,"). While this works physically, the simulation will probably get stuck in an infinite loop since the car won't reach the finish line")#line:215
            if O0O0000O0O0OO00O0 >OOOOO0000O0000O0O .gearbox .gears +1 :#line:216
                print ("You have tried to put in the gear ",O0O0000O0O0OO00O0 ,". This car only has ",OOOOO0000O0000O0O .gearbox .gears +1 ,"gears. Did you think you could cheat? Picking gear ",OOOOO0000O0000O0O .gearbox .gears +1 ," instead.")#line:217
            if OOOO0O0000OO00OOO >1 :#line:218
                print ("You have tried to give a throttle higher than 1 (",OOOO0O0000OO00OOO ,"), which would be equal to pressing the pedal through the floor. Since I don't want holes in the floor, i will change the throttle to 1")#line:219
            if OOOO0O0000OO00OOO <0 :#line:220
                print ("You have tried to give a throttle lower than 0, which would be equal to ripping the pedal loose. Since I want to keep the pedal I will change the throttle to 0")#line:221
            if OOOO0O0000OO00OOO ==0 :#line:222
                print ("No throttle is being given. This won't move the car and will probably leave the simulation stuck in a loop.")#line:223
            if round (O0O0000O0O0OO00O0 )!=O0O0000O0O0OO00O0 :#line:224
                print ("Gear input must be an integer within the range [1, 4]. The input was ",O0O0000O0O0OO00O0 +1 ,".")#line:225
        if O0O0000O0O0OO00O0 <0 :#line:226
            O0O0000O0O0OO00O0 =0 #line:227
        O0O0000O0O0OO00O0 =round (O0O0000O0O0OO00O0 -1 )#line:228
        OOOOO0000O0000O0O .dyn .throttle =OOOO0O0000OO00OOO #line:229
        O0OOO00O000O0OO00 =caster_GearShift (O0O0000O0O0OO00O0 ,O0OOO00O000O0OO00 ,OOOOO0000O0000O0O ,O00OO0OOO0000O0OO )#line:230
    if O00OO0OOO0000O0OO :#line:232
        OO0000OO0OO00O0O0 ,O0O0000OO00O0OOO0 =plt .subplots (2 ,2 )#line:233
        O0OOOOO0OO0OO0OO0 =[OOOO0O0OO00OO0O0O .Distance for OOOO0O0OO00OO0O0O in O00OOOO0O0OO00OO0 ]#line:234
        OOO0O0OOOOO0O0000 =[OOOO0O00OOO00000O .Velocity for OOOO0O00OOO00000O in O00OOOO0O0OO00OO0 ]#line:236
        O0O000O0OOOOO0OOO =[O0OO0OO00000O00OO .RPM for O0OO0OO00000O00OO in O00OOOO0O0OO00OO0 ]#line:237
        OO0O0OO0OOO00O0OO =[OOO0OO0OO0000O000 .Gear for OOO0OO0OO0000O000 in O00OOOO0O0OO00OO0 ]#line:238
        OO00000O00O00O0O0 =[OO0OOO00OO00OOO00 .LongAcc for OO0OOO00OO00OOO00 in O00OOOO0O0OO00OO0 ]#line:239
        O0O0000OO00O0OOO0 [0 ,0 ].scatter (O0OOOOO0OO0OO0OO0 ,np .multiply (OOO0O0OOOOO0O0000 ,3.6 ),s =1 )#line:241
        O0O0000OO00O0OOO0 [0 ,0 ].set (xlabel ="Distance [m]",ylabel ="Velocity [km/h]")#line:242
        O0O0000OO00O0OOO0 [0 ,1 ].scatter (O0OOOOO0OO0OO0OO0 ,O0O000O0OOOOO0OOO ,s =1 )#line:244
        O0O0000OO00O0OOO0 [0 ,1 ].set (xlabel ="Distance [m]",ylabel ="Engine RPM")#line:245
        O0O0000OO00O0OOO0 [1 ,0 ].scatter (O0OOOOO0OO0OO0OO0 ,np .add (OO0O0OO0OOO00O0OO ,1 ),s =1 )#line:247
        O0O0000OO00O0OOO0 [1 ,0 ].set_title ("")#line:248
        O0O0000OO00O0OOO0 [1 ,0 ].set (xlabel ="Distance [m]",ylabel ="Current Gear")#line:249
        O0O0000OO00O0OOO0 [1 ,1 ].scatter (O0OOOOO0OO0OO0OO0 ,OO00000O00O00O0O0 ,s =1 )#line:251
        O0O0000OO00O0OOO0 [1 ,1 ].set_title ("")#line:252
        O0O0000OO00O0OOO0 [1 ,1 ].set (xlabel ="Distance [m]",ylabel ="Longitudinal Acceleration [m/s^2]")#line:253
        O0O0OO00O0O0O00OO =[OOO0000O0O0000OO0 .TimeLap for OOO0000O0O0000OO0 in O00OOOO0O0OO00OO0 ]#line:255
        O0OO0O00000O0O0OO =np .interp (OO00O0OOO0000OOOO ,O0OOOOO0OO0OO0OO0 ,O0O0OO00O0O0O00OO )#line:256
        print ("Finish time: ","{:.2f}".format (O0OO0O00000O0O0OO )," seconds.")#line:257
        plt .show ()#line:259
if __name__ =="__main__":#line:261
    main (True )#line:262
print ()