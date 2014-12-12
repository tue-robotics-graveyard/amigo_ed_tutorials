alias rviz-amigo='rosrun rviz rviz -d `rospack find amigo_ed_tutorials`/config/rviz/amigo_ed.rviz'
alias amigo-teleop='rosrun amigo_ed_tutorials teleop.py /cmd_vel:=/amigo/base/references'

export ED_PLUGIN_PATH=`rospack find ed`/../../devel/lib
