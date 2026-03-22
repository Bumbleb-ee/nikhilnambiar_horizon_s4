# Level 3 - ROS2 Nodes

## Setup
```
cd ros2_ws
colcon build
source install/setup.bash
```

## Run Publisher
```
ros2 run my_robot_controller distance_publisher
```

## Run Subscriber
```
ros2 run my_robot_controller distance_subscriber
```

## Run Decision Node (Bonus)
```
ros2 run my_robot_controller decision_node
```

- **publisher.py** - Publishes random distance values to /distance every second
- **subscriber.py** - Subscribes to /distance and prints received values
- **decision_node.py** - Subscribes to /distance, publishes STOP/MOVE_FORWARD to /rover_command
