from setuptools import setup
import os
from glob import glob

package_name = 'racecarx_control'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        (os.path.join('share', package_name, 'launch'), glob('launch/*.launch.py')),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='danny',
    maintainer_email='metheorita@gmail.com',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'sample_publisher = racecarx_control.sample_publisher:main',
            'twist_publisher = racecarx_control.twist_publisher:main',
            'sample_listener = racecarx_control.sample_listener:main',
            'camera_listener = racecarx_control.camera_listener:main'
        ],
    },
)
