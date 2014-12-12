#!/usr/bin/python
import roslib; roslib.load_manifest('fast_simulator')
import rospy

from fast_simulator import client

if __name__ == "__main__":
    rospy.init_node('fast_simulator_object_spawner')

    W = client.SimWorld()

    W.add_object("coke-1", "coke",  0.856, 3.671, 0.8)
    W.add_object("coke-2", "coke",  0.476, 3.659, 0.8)
    W.add_object("coke-3", "coke", -0.003, 3.663, 0.8)
    W.add_object("coke-4", "coke",  0.676, 1.906, 0.9)

    W.add_object("coke-5", "coke", -1.708,  3.767, 0.9)
    W.add_object("coke-6", "coke", -1.836, -1.318, 0.8)
    W.add_object("coke-7", "coke",  2.202,  0.508, 0.5)

