from launch import LaunchDescription
from launch.actions import ExecuteProcess
from launch_ros.actions import Node


def generate_launch_description():

    gazebo = ExecuteProcess(
        cmd=[
            'gazebo',
            '/root/rov_ws/src/rov_sim/worlds/ocean.world',
            '--verbose',
            '-s', 'libgazebo_ros_factory.so'
        ],
        output='screen'
    )

    spawn_robot = Node(
        package='gazebo_ros',
        executable='spawn_entity.py',
        arguments=[
            '-file',
            '/root/rov_ws/src/rov_sim/models/babyrov/model.sdf',
            '-entity',
            'babyrov'
        ],
        output='screen'
    )

    camera_view = Node(
        package='rqt_image_view',
        executable='rqt_image_view',
        output='screen'
    )

    return LaunchDescription([
        gazebo,
        spawn_robot,
        camera_view
    ])