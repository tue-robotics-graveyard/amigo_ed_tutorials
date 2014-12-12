ED Tutorials using the AMIGO robot
======

## Introduction

This package contains some configuration files that will help you to simulate an environment and TU/e's AMIGO robot, and map the world using the ED world model.

## Installation

*Note: Currently only ROS Hydro is supported*

We assume you have successfully installed ROS and set-up a Catkin workspace. Check out the following packages in your workspace:

    cd <your_catkin_workspace>/src

    git clone https://github.com/tue-robotics/amigo_ed_tutorials.git
    git clone https://github.com/tue-robotics/fast_simulator_data
    git clone https://github.com/tue-robotics/ed.git
    git clone https://github.com/tue-robotics/tue_filesystem
    git clone https://github.com/tue-robotics/geolib2
    git clone https://github.com/tue-robotics/code_profiler
    git clone https://github.com/tue-robotics/tue_config.git
    git clone https://github.com/tue-robotics/tue_serialization
    git clone https://github.com/tue-robotics/rgbd
    git clone https://github.com/tue-robotics/fast_simulator.git
    git clone https://github.com/tue-robotics/virtual_cam
    git clone https://github.com/tue-robotics/ed_object_models.git
    git clone https://github.com/tue-robotics/tue_msgs
    git clone https://github.com/tue-robotics/amigo_description

    
You will also need the following system dependencies:

    sudo apt-get install ros-hydro-xacro ros-hydro-tf-conversions ros-hydro-image-transport ros-hydro-common-msgs ros-hydro-ros-comm ros-hydro-stereo-msgs ros-hydro-opencv2 ros-hydro-std-msgs ros-hydro-sensor-msgs ros-hydro-visualization-msgs ros-hydro-geometry-msgs ros-hydro-pcl-ros ros-hydro-message-filters ros-hydro-image-geometry ros-hydro-kdl-parser ros-hydro-roslib ros-hydro-std-srvs ros-hydro-navigation yaml-cpp ros-hydro-cv-bridge ros-hydro-tf libassimp-dev ros-hydro-message-generation ros-hydro-roscpp ros-hydro-message-runtime ros-hydro-class-loader ros-hydro-pcl-conversions
    
This should be sufficient to successfully compile the simulator and ED:

    cd <your_catkin_workspace>
    catkin_make
    
## Quick Start

We created a setup file that sets up ED and defines some Bash aliases that will make it easier to control AMIGO in simulation:

    source `rospack find amigo_ed_tutorials`/setup/setup.bash

*Note:* this setup-file should be sourced in every new terminal or Bash session. To make life a bit easier, you can add it to your ~/.bashrc file.

Then you can launch the simulator and ED using:

    roslaunch amigo_ed_tutorials amigo_ed.launch

To visualize both the robot and the ED world, run:

    rviz-amigo

This command is defined in *./setup/setup.bash*. The rviz configuration can be found in *./config/rviz/amigo_ed.rviz*. The colored blocks / objects represent the world as it is currently stored in ED. You can display the Kinect point cloud by ticking the box behind *Cam - Head Point Cloud*.

You can navigate the robot with the keyboard by running:

    amigo-teleop

Use the numpad to drive around amigo. Use '/' and '*' to rotate.

Drive around AMIGO while paying attention to RViz. The simulated world and the prior world loaded in ED are nearly identical, so the robot won't discover many *new* things. There are however some small items in the simulated world that ED does not yet know about. Try driving around until you find them. They should be displayed in RViz as colored 3D polygons.


