"""epuck_avoid_collision controller."""

# You may need to import some classes of the controller module. Ex:
#  from controller import Robot, Motor, DistanceSensor
from controller import Robot, Motor, DistanceSensor

MAX_SPEED = 6.28

# create the Robot instance.
robot = Robot()

# get the time step of the current world.
timestep = int(robot.getBasicTimeStep())

# Initialize sensors
ps=[]
psNames = ['ps' + str(x) for x in range(8)]
for i in psNames:
    x = robot.getDevice(i)
    ps.append(x)
    x.enable(timestep)

# Initialize sensors
leftMotor = robot.getDevice('left wheel motor')
rightMotor = robot.getDevice('right wheel motor')
leftMotor.setPosition(float('inf'))
rightMotor.setPosition(float('inf'))
leftMotor.setVelocity(0)
rightMotor.setVelocity(0)

# Main loop:
while robot.step(timestep) != -1:
    # read sensors
    psValues = []
    for i in ps:
        psValues.append(i.getValue())
    # analyze obstacles
    right_obstacle = psValues[0] > 80.0 or psValues[1] > 80.0 or psValues[2] > 80.0
    left_obstacle = psValues[5] > 80.0 or psValues[6] > 80.0 or psValues[7] > 80.0
    if left_obstacle:
        # Turn left
        leftMotor.setVelocity(0.5 * MAX_SPEED)
        rightMotor.setVelocity(-0.5 * MAX_SPEED)
    elif right_obstacle:
        # Turn right
        leftMotor.setVelocity(-0.5 * MAX_SPEED)
        rightMotor.setVelocity(0.5 * MAX_SPEED)
    else:
        # Go straight
        leftMotor.setVelocity(0.5 * MAX_SPEED)
        rightMotor.setVelocity(0.5 * MAX_SPEED)




# Enter here exit cleanup code.
