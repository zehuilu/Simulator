#!/usr/bin/env python3
import os
import sys
sys.path.append(os.getcwd()+'/lib')
import matplotlib.pyplot as plt
from Simulator import Simulator


if __name__ == "__main__":
    # define map
    map_dimensionStr = "2d"
    map_resolution = 1
    mapSize_x_meter = 10.0
    mapSize_y_meter = 10.0
    # set mapSize_z_meter to 0 if select 2d
    mapSize_z_meter = 0.0


    MySimulator = Simulator(map_dimensionStr, map_resolution, mapSize_x_meter, mapSize_y_meter, mapSize_z_meter)
    MySimulator.compute_path()
    MySimulator.plotOnce()


    print("Program end...")
