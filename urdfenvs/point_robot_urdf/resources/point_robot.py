import os
import numpy as np

from urdfenvs.urdfCommon.holonomic_robot import HolonomicRobot


class PointRobot(HolonomicRobot):
    def __init__(self):
        urdf_file = os.path.join(os.path.dirname(__file__), "pointRobot.urdf")
        n = 3
        super().__init__(n, urdf_file)

    def set_joint_indices(self):
        self._robot_joints = [0, 1, 2]
        self._urdf_joints = [0, 1, 2]

    def set_acceleration_limits(self):
        acc_limit = np.ones(self._n)
        self._limit_acc_j[0, :] = -acc_limit
        self._limit_acc_j[1, :] = acc_limit
