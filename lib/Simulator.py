#!/usr/bin/env python3
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import time
from matplotlib.pyplot import plot, draw, show


class Simulator:
    # specify the data type of each property if possibles
    # NOTE: tab as 4 spaces

    frequency: int
    dimensionStr: str

    def __init__(self, frequency: int, dimensionStr: str):
        """
        This is the constructor. Fill in usage and example later.
        Intialize a Simulator.
        """
        self.frequency = frequency
        self.dimensionStr = dimensionStr

    def createFigure(self):
        """
        Create an empty figure.
        """
        realtimeFlag = False
        _, self.ax = plt.subplots(1, 1)
        if realtimeFlag:
            plt.ion()
            plt.show()
        # figure settings
        self.ax.set_xlabel("x")
        self.ax.set_ylabel("y")
        self.ax.set_aspect("equal")
        return self.ax

    def plotOnce(self, position2d: list):
        """
        Plot a figure once.

        Input:
            position2d: [[px0,py0], [px1,py1], ...]
        """
        if self.dimensionStr == "2d":
            # do something here
            for idx_agent in range(len(position2d)):
                self.ax.plot(position2d[idx_agent][0], position2d[idx_agent][1], marker="x")

        elif self.dimensionStr == "3d":
            # plot a 3d figure
            pass
        else:
            print("dimensionStr only supports 2d or 3d!")
            Exception("dimensionStr only supports 2d or 3d!")
        plt.show(block=False)

    def loadDynamics(self, dynamicsFunctionDict: dict):
        """
        This function loads the dynamics of an agent.
        In the future, we could load a list of dynamics for multiple agents
        """
        # dynamicsFunctionDict should be a dictionary which contains a lambda function as the dynamics,
        # and a string to indicate where discret-time or continuous-time
        # For discrete-time, the dynamics is a difference equation. For continuous-time, the dynamics is a differential equation

        # Finish this function, and create a test:
        # input a simple differential equation as the dynamics, give an open-loop input with a certain amount of time, let it simulate
        # and plotOnce()
        self.dynamicsFunction = dynamicsFunctionDict["dynamicsFunction"]
        self.modelType = dynamicsFunctionDict["modelType"]
