from setuptools import setup
from glob import glob
import os

package_name = 'drone_offboard_py'

setup(
    name=package_name,
    version='0.0.1',
    packages=[package_name],
    data_files=[
        (
            'share/ament_index/resource_index/packages',
            ['resource/' + package_name]
        ),
        (
            'share/' + package_name,
            ['package.xml']
        ),
        (
            os.path.join('share', package_name, 'launch'),
            glob('launch/*.py')
        ),
        (
            os.path.join('share', package_name, 'config'),
            glob('config/*.yaml')
        ),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='Saeed Jafari Kang',
    maintainer_email='sjafarik@mtu.edu',
    description='PX4 ROS2 Python offboard control node',
    license='MIT',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'offboard_control = drone_offboard_py.offboard_control:main',
            'mission_planner = drone_offboard_py.mission_planner:main',
        ],
    },
)