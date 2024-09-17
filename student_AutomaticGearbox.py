from caster_AutomaticGearbox import caster_AutomaticGearbox
from Car import Car

def student_AutomaticGearbox(gear, RPM, longAcc, velocity, throttle, distance, timeLap):

    #Convert m/s to km/h
    speed = velocity * 3.6
    throttle = 1
    gear_demand = gear
    if gear_demand == 0:
        gear_demand = 1
    if RPM > 8000 and gear != 4:
        gear_demand = gear_demand + 1
        
    #Wheel slip 
        

    # For comparison, uncomment the line below to see how Caster gearbox performs
    #gear_demand = caster_AutomaticGearbox(gear, RPM, longAcc, velocity, throttle, distance, timeLap)

    #Return the selected gear
    return (gear_demand, throttle)
