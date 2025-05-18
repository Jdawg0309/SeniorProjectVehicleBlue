from glob import glob
from setuptools import setup

package_name = 'gazebo_environment'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        # ('share/' + package_name + '/launch', glob('launch/*.py')),
        # ('share/' + package_name + '/urdf', glob('urdf/*.urdf')),
        ('share/' + package_name + '/worlds', glob('worlds/*.world')),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='junaet-mahbub',
    maintainer_email='your@email.com',
    description='Gazebo setup for Sonoma car model',
    license='MIT',
    entry_points={
        'console_scripts': [],
    },
)
