from caster_AutomaticGearbox import caster_AutomaticGearbox
from Car import Car
import math
car = Car()
def student_AutomaticGearbox(gear, RPM, longAcc, velocity, throttle, distance, timeLap):

    #Getting data from car object
    final_drive_ratio = car.gearbox.final
    gear_ratios = car.gearbox.ratio
    rpm_vector = car.engine.rpm
    torque_vector = car.engine.torque
    wheel_radius = car.wheel.radius
    optimal_slip = car.optimal_slip

    optimalSlip_ = optimal_slip / 100 

    gear_demand = gear

    # Converting speed to km/h
    speed = velocity * 3.6

    # calculating the wheel circumferance 
    wheelCircumference = 2 * wheel_radius * math.pi
    
    #Getting the current gear ratio from the transmission
    currentGearRatio = gear_ratios[gear_demand - 1]

    # Deffining the initial throttle in each gear
    beginningThrottleByGear = [0.5,0.8,1,1]

    # Calculating the current wheel slip and wheel speed
    wheelSlip = 1
    currentWheelSpeed = RPM /60 * 1/currentGearRatio * 1/final_drive_ratio * wheelCircumference * 3.6
    if speed != 0:
        wheelSlip = (currentWheelSpeed / speed) - 1

        #Making shure the wheel speed is positive
        if wheelSlip < 0:
            wheelSlip = 0
    else:
        wheelSlip = optimalSlip_
        throttle = beginningThrottleByGear[0]

    # Making shure that the car does not start in neutral
    if gear_demand == 0:
        gear_demand = 1

    # Shifting if rpm if over 9000 and the wheels are not slipping to much
    if RPM > 9000 and gear != 4 and wheelSlip <= 1.3:
        gear_demand = gear_demand + 1

        #Setting the initial throtle in each gear
        throttle = beginningThrottleByGear[gear_demand - 1]

    #Adding throttle if car is not slipping enough
    if wheelSlip == optimalSlip_:
        throttle = throttle
    elif wheelSlip < optimalSlip_:
        throttle += 0.01 * gear_demand
        
    #Making shure that throttle does not surpas 100% = 1
    if throttle > 1:
        throttle = 1 
    
    return (gear_demand, throttle)
