from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    ld = LaunchDescription()

    # Spawn a sample camera listener node that does whatever with the image using OpenCV
    camera_listener = Node(
        package='racecarx_control',
        executable='camera_listener',
        output='screen'
    )

    # Spawn a sample twist publishing node that sends a command to turn right, then stop
    twist_publisher = Node(
        package='racecarx_control',
        executable='twist_publisher',
        output='screen'
    )

    ld.add_action(camera_listener)
    ld.add_action(twist_publisher)

    return ld