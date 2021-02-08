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
    timeHelper.sleep(2.5)
    for i in range(TRIALS):
        # for cf in allcfs.crazyflies:
        #     cf.uploadTrajectory(0, 0, traj1)

        allcfs.takeoff(targetHeight=0.4, duration=2.0)
        timeHelper.sleep(2.5)
        for cf in allcfs.crazyflies:
            pos = np.array(cf.initialPosition) + np.array([0, 0, 0.4])
            cf.goTo(pos, np.pi, 2.0)
        timeHelper.sleep(2.5)

        for j in range(25):
            for cf in allcfs.crazyflies:
                pos = np.array(cf.initialPosition) + np.array([0, 0.3, 0.4])
                cf.goTo(pos, np.pi/2, 2.0)
            timeHelper.sleep(2.5)

            for cf in allcfs.crazyflies:
                pos = np.array(cf.initialPosition) + np.array([0.3, 0.3, 0.4])
                cf.goTo(pos, np.pi, 2.0)
            timeHelper.sleep(2.5)
            
            for cf in allcfs.crazyflies:
                pos = np.array(cf.initialPosition) + np.array([0.3, 0.0, 0.4])
                cf.goTo(pos, np.pi*3/2, 2.0)
            timeHelper.sleep(2.5)
            
            for cf in allcfs.crazyflies:
                pos = np.array(cf.initialPosition) + np.array([0.0, 0.0, 0.4])
                cf.goTo(pos, 0, 2.0)
            timeHelper.sleep(2.5)
        # allcfs.startTrajectory(0, timescale=TIMESCALE)
        # timeHelper.sleep(traj1.duration * TIMESCALE + 2.0)
        # allcfs.startTrajectory(0, timescale=TIMESCALE, reverse=True)
        # timeHelper.sleep(traj1.duration * TIMESCALE + 2.0)

        allcfs.land(targetHeight=0.04, duration=2.0)
        timeHelper.sleep(3.0)

