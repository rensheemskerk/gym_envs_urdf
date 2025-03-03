import numpy as np

from urdfenvs.boxer_robot.resources.boxer_robot import BoxerRobot
from urdfenvs.urdfCommon.urdf_env import UrdfEnv


class BoxerRobotEnv(UrdfEnv):
    def __init__(self, render=False, dt=0.01):
        super().__init__(BoxerRobot(), render=render, dt=dt)
        self.set_spaces()

    def check_initial_state(self, pos, vel):
        if (
            not isinstance(pos, np.ndarray)
            or not pos.size == self._robot.n() + 1
        ):
            pos = np.zeros(self._robot.n() + 1)
        if not isinstance(vel, np.ndarray) or not vel.size == self._robot.n():
            vel = np.zeros(self._robot.n())
        return pos, vel
