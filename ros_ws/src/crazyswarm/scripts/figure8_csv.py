#!/usr/bin/env python

import numpy as np

from pycrazyswarm import *
import uav_trajectory

if __name__ == "__main__":
    swarm = Crazyswarm()
    timeHelper = swarm.timeHelper
    allcfs = swarm.allcfs

    traj1 = uav_trajectory.Trajectory()
    traj1.loadcsv("figure8.csv")

    TRIALS = 1
    TIMESCALE = 1.0
    for i in range(TRIALS):
        # for cf in allcfs.crazyflies:
        #     cf.uploadTrajectory(0, 0, traj1)

        allcfs.takeoff(targetHeight=0.5, duration=3.0)
        timeHelper.sleep(3.5)
        # for cf in allcfs.crazyflies:
        #     pos = np.array(cf.initialPosition) + np.array([0, 0, 0.5])
        #     cf.goTo(pos, 0, 3.0)
        if 1:
            for j in range(10):
                for cf in allcfs.crazyflies:
                    theta = 2 * np.pi / 10 * j
                    pos = np.array(cf.initialPosition) + np.array([0, 0, 0.5])
                    from math import cos, sin
                    pos = np.array([cos(theta) * pos[0] - sin(theta) * pos[1], 
                                cos(theta) * pos[1] + sin(theta) * pos[0], pos[2]])
                    cf.goTo(pos, 0, 1)
                timeHelper.sleep(1.1)
        timeHelper.sleep(3.5)

        # allcfs.startTrajectory(0, timescale=TIMESCALE)
        # timeHelper.sleep(traj1.duration * TIMESCALE + 2.0)
        # allcfs.startTrajectory(0, timescale=TIMESCALE, reverse=True)
        # timeHelper.sleep(traj1.duration * TIMESCALE + 2.0)

        allcfs.land(targetHeight=0.06, duration=2.0)
        timeHelper.sleep(3.0)

