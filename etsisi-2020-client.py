#!/usr/bin/python3

print('### Script:', __file__)

import math
import sys
import time

import sim

# --------------------------------------------------------------------------

def getRobotHandles(clientID):
    # Robot handle
    _,rbh = sim.simxGetObjectHandle(clientID, 'Pioneer_p3dx',
                                     sim.simx_opmode_blocking)

    # Motor handles
    _,lmh = sim.simxGetObjectHandle(clientID, 'Pioneer_p3dx_leftMotor',
                                     sim.simx_opmode_blocking)
    _,rmh = sim.simxGetObjectHandle(clientID, 'Pioneer_p3dx_rightMotor',
                                     sim.simx_opmode_blocking)

    # Sonar handles
    str = 'Pioneer_p3dx_ultrasonicSensor%d'
    sonar = [0] * 16
    for i in range(16):
        _,h = sim.simxGetObjectHandle(clientID, str % (i+1),
                                       sim.simx_opmode_blocking)
        sonar[i] = h
        sim.simxReadProximitySensor(clientID, h, sim.simx_opmode_streaming)

    return [lmh, rmh], sonar, rbh

# --------------------------------------------------------------------------

def setSpeed(clientID, hRobot, lspeed, rspeed):
    sim.simxSetJointTargetVelocity(clientID, hRobot[0][0], lspeed,
                                    sim.simx_opmode_oneshot)
    sim.simxSetJointTargetVelocity(clientID, hRobot[0][1], rspeed,
                                    sim.simx_opmode_oneshot)

# --------------------------------------------------------------------------



def getSonar(clientID, hRobot):
    r = [1.0] * 16
    for i in range(16):
        handle = hRobot[1][i]
        e,s,p,_,_ = sim.simxReadProximitySensor(clientID, handle,
                                                 sim.simx_opmode_buffer)
        if e == sim.simx_return_ok and s:
            r[i] = math.sqrt(p[0]*p[0]+p[1]*p[1]+p[2]*p[2])

    return r

# --------------------------------------------------------------------------
# --------------------------------------------------------------------------

def avoid(sonar):
    if (sonar[1] < 0.4) and (sonar[8] > 0.4):
        lspeed, rspeed = +0.9, +0.05
    ##elif (sonar[9] < 0.1) and (sonar[16] > 0.4):
        ##lspeed, rspeed = +0.9, +0.0
    elif (sonar[5] < 0.4) and (sonar[13] > 0.3):
        lspeed, rspeed = +0.05, +1.0
    elif (sonar[4] < 0.4) and (sonar[12] > 0.3):
        lspeed, rspeed = +1.0, +0.05
    elif (sonar[6] < 0.37) and (sonar[11] > 0.3):
        lspeed, rspeed = +0.05, +1.0
    elif (sonar[7] < 0.37) and (sonar[15] > 0.3):
        lspeed, rspeed = +0.05, +1.0
    elif (sonar[2] < 0.37) and (sonar[10] > 0.3):
        lspeed, rspeed = +1.0, +0.05
    elif (sonar[3] < 0.37) and (sonar[11] > 0.3):
        lspeed, rspeed = +1.0, +0.05
    else:
        lspeed, rspeed = +1.5, +1.5

    return lspeed, rspeed

# --------------------------------------------------------------------------

def main():
    print('### Program started')

    print('### Number of arguments:', len(sys.argv), 'arguments.')
    print('### Argument List:', str(sys.argv))

    sim.simxFinish(-1) # just in case, close all opened connections

    port = int(sys.argv[1])
    clientID = sim.simxStart('127.0.0.1', port, True, True, 2000, 5)

    if clientID == -1:
        print('### Failed connecting to remote API server')

    else:
        print('### Connected to remote API server')
        hRobot = getRobotHandles(clientID)

        while sim.simxGetConnectionId(clientID) != -1:
            # Perception
            sonar = getSonar(clientID, hRobot)

            # print '### s', sonar

            # Planning
            lspeed, rspeed = avoid(sonar)

            # Action
            setSpeed(clientID, hRobot, lspeed, rspeed)
            time.sleep(0.1)

        print('### Finishing...')
        sim.simxFinish(clientID)

    print('### Program ended')

# --------------------------------------------------------------------------

if __name__ == '__main__':
    main()
