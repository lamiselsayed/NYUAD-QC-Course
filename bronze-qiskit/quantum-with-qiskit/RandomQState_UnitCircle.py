
# your function is here
from math import cos, sin, pi
from random import randrange
def random_qstate_by_angle():
    #
    # your codes are here
    #
    quantum_state = [0, 0]                # quantum state 
    randomAngle = randrange(0, 361)
    angleInRadians = 2 * pi *(randomAngle / 360)
    
    quantum_state[0] = cos(angleInRadians)
    quantum_state[1] = sin(angleInRadians)
    
    return quantum_state
