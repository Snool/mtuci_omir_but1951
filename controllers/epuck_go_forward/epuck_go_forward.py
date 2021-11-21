"""epuck_go_forward controller."""
from controller import Motor, Robot

MAX_SPEED = 6.28

# create the Robot instance.
robot = Robot()
# get motors
leftMotor = robot.getDevice('left wheel motor')
rightMotor = robot.getDevice('right wheel motor')

# get the time step of the current world.
timestep = int(robot.getBasicTimeStep())

# set "infinity" position
leftMotor.setPosition(float('inf'))
rightMotor.setPosition(float('inf'))

# set velocity for motors
leftMotor.setVelocity(0.5 * MAX_SPEED)
rightMotor.setVelocity(0.5 * MAX_SPEED)

# Main loop:
while robot.step(timestep) != -1:
    pass
