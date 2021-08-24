#!/usr/bin/env python3
import os
import sys
sys.path.append(os.getcwd()+'/lib')
import time
import matplotlib.pyplot as plt
from Simulator import Simulator


if __name__ == "__main__":
    frequency = 10
    dimensionStr = "2d"

    # created by user
    dynamicsFunction = lambda x: [x[0]+5, x[1]+5]
    # dynamicsFunction = lambda x,u: [x[0]+u, x[1]-u]

    dynamicsFunctionDict = {"modelType": "discrete", "dynamicsFunction": dynamicsFunction}

    # initialize a Simulator
    MySimulator = Simulator(frequency, dimensionStr)
    # load a dynamics
    MySimulator.loadDynamics(dynamicsFunctionDict)
    # create an empty figure
    MySimulator.createFigure()

    # this is a single agent
    xNow = [1, 2]

    for k in range(20):
        # convert xNow to position2d
        ####

        MySimulator.plotOnce(position2d)

        # move your agent one step forward
        ####

        plt.pause(1/frequency)

    plt.show()
