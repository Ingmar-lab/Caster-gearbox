from caster_AutomaticGearbox import caster_AutomaticGearbox
from Car import Car
import math
car = Car()
def student_AutomaticGearbox(gear, RPM, longAcc, velocity, throttle, distance, timeLap):

    #Convert m/s to km/h
    final_drive_ratio = car.gearbox.final
    gear_ratios = car.gearbox.ratio
    rpm_vector = car.engine.rpm
    torque_vector = car.engine.torque
    wheel_radius = car.wheel.radius
    optimal_slip = car.optimal_slip
    wheelCircumference = 2 * wheel_radius * math.pi
    speed = velocity * 3.6
    gear_demand = gear
    
    currentGearRatio = gear_ratios[gear_demand - 1]
    currentWheelSpeed = RPM /60 * 1/currentGearRatio * 1/final_drive_ratio * wheelCircumference * 3.6
    optimalSlip_ = optimal_slip / 100 
    wheelSlip = 1
    beginningThrottleByGear = [0.5,0.8,1,1]

    if speed != 0:
        wheelSlip = (currentWheelSpeed / speed) - 1
        if wheelSlip < 0:
            wheelSlip = 0
    else:
        wheelSlip = optimalSlip_
        throttle = beginningThrottleByGear[0]

    if gear_demand == 0:
        gear_demand = 1
    if RPM > 9000 and gear != 4 and wheelSlip <= 1.3:
       gear_demand = gear_demand + 1
       throttle = beginningThrottleByGear[gear_demand - 1]

    if wheelSlip == optimalSlip_:
        throttle = throttle
    elif wheelSlip < optimalSlip_:
        throttle += 0.01 * gear_demand
        
    if throttle > 1:
        throttle = 1 
    
    
    # if gear == 1:
    #     throttle = 0.3
    # elif gear == 2:
    #     throttle = 0.5
    # elif gear == 3:
    #     throttle = 0.8
    # else:
    #     throttle = 1
    print(optimalSlip_, throttle, wheelSlip, RPM, gear, distance)
    #print(wheelCircumference)
    # For comparison, uncomment the line below to see how Caster gearbox performs
    #gear_demand = caster_AutomaticGearbox(gear, RPM, longAcc, velocity, throttle, distance, timeLap)
    #Return the selected gear
    return (gear_demand, throttle)
