#!/usr/bin/env python3


class Simulator(object):
    # specify the data type of each property if possibles
    # NOTE: tab as 4 spaces

    dimensionStr: str

    def __init__(self, dimensionStr):
        """
        This is the constructor. Fill in usage and example later.
        Intialize a Simulator.
        """
        self.dimensionStr = dimensionStr

    def plotOnce(self):
        """
        Plot a figure once.
        """
        if self.dimensionStr == "2d":
            # plot a 2d figure
            pass
        elif self.dimensionStr == "3d":
            # plot a 3d figure
            pass
        else:
            Exception("dimensionStr only supports 2d or 3d!")

    def loadDynamics(self, DynamicsFunction):
        """
        This function loads the dynamics of an agent.
        In the future, we could load a list of dynamics for multiple agents
        """
        # DynamicsFunction should be a struct/dataclass which contains a lambda function as the dynamics,
        # and a string to indicate where discret-time or continuous-time
        # For discrete-time, the dynamics is a difference equation. For continuous-time, the dynamics is a differential equation

        # Finish this function, and create a test:
        # input a simple differential equation as the dynamics, give an open-loop input with a certain amount of time, let it simulate
        # and plotOnce()