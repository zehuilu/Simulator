#!/usr/bin/env python3
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import time
from matplotlib.pyplot import plot, draw, show


class Simulator(object):
    # specify the data type of each property if possibles
    # NOTE: tab as 4 spaces

    mapSize_x: int
    mapSize_y: int
    mapSize_z: int
    resolution: int
    value_non_obs: int
    frequency: int

    def __init__(self,
                 dimensionStr: str,
                 resolution: int,
                 mapSize_x_meter: float,
                 mapSize_y_meter: float,
                 mapSize_z_meter: float):
        """
        This is the constructor. Fill in usage and example later.
        Intialize a Simulator.
        """

        self.frequency = 10
        self.dimensionStr = dimensionStr
        # map resolution, how many cells per meter
        self.resolution = resolution
        # how many cells for x,y,z direction
        mapSize_x = mapSize_x_meter * resolution
        mapSize_y = mapSize_y_meter * resolution
        mapSize_z = mapSize_z_meter * resolution

        # check if cell numbers are integers
        assert (mapSize_x.is_integer() == True)
        assert (mapSize_y.is_integer() == True)
        assert (mapSize_z.is_integer() == True)

        self.mapSize_x = int(mapSize_x)
        self.mapSize_y = int(mapSize_y)
        self.mapSize_z = int(mapSize_z)

        self.value_non_obs = 1

        self.position = []

    def plotOnce(self):
        """
        Plot a figure once.
        """

        if self.dimensionStr == "2d":
            # plot a 2d figure
            self.map_array = self.value_non_obs * np.ones((self.mapSize_x, self.mapSize_y)).astype(int)
#            fig_map, ax_map = plt.subplots(1, 1)
#            cmap = matplotlib.colors.ListedColormap(['white', 'black'])
#            ax_map.pcolor(self.map_array, cmap=cmap, edgecolors='k')

#            #            ax_map.legend(bbox_to_anchor=(1.05, 1), loc='upper left')
#            ax_map.set_xlabel("x")
#            ax_map.set_ylabel("y")
#            ax_map.set_aspect('equal')
#            ax_map.set_xlim([0, self.mapSize_x])
#            ax_map.set_ylim([0, self.mapSize_y])
            # line, = ax_map.plot(self.position[0][0], self.position[0][1])
            plt.ylim(1, self.mapSize_x)
            plt.xlim(1, self.mapSize_y)
            show(block=False)
            
            for idx in range(len(self.position)):
                plt.plot(self.position[idx][0], self.position[idx][1], color='black', linestyle='solid', linewidth = 2, marker='o', markersize=2)
                print(self.position[idx])
#                time.sleep(0.1)
                plt.show(block=False)
                plt.pause(0.01)

                
                

#            self.line, = ax_map.plot(self.position[0][0], self.position[0][1])

            # for idx in range(len(self.position)):
            #     line.set_xdata(self.position[idx][0])
            #     line.set_ydata(self.position[idx][1])

#            animation = FuncAnimation(fig_map, self.update_frame, frames=self.position)
            pass
        elif self.dimensionStr == "3d":
            # plot a 3d figure
            pass
        else:
            print("dimensionStr only supports 2d or 3d!")
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

#    def update_frame(self, idx):
#        if self.dimensionStr == "2d":
#            self.line.set_x(self.position[idx][0])
#            self.line.set_y(self.position[idx][1])

#        return self.line,

    def compute_path(self):
        acceleration = np.ones((100, 2)) / 10.0
        velocity = np.zeros((len(acceleration) + 1, 2))
        self.position = np.zeros((len(acceleration) + 1, 2))
        for idx in range(len(acceleration)):
            velocity[idx + 1] = velocity[idx] + acceleration[idx] / self.frequency
            self.position[idx + 1] = self.position[idx] + velocity[idx] / self.frequency
