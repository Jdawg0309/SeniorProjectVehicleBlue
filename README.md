source /opt/ros/jazzy/setup.bash
source ~/pp3d_car_ws/install/setup.bash
export GZ_SIM_RESOURCE_PATH=~/pp3d_car_ws/src/gazebo_environment
gz sim ~/pp3d_car_ws/src/gazebo_environment/worlds/car_world.sdf
