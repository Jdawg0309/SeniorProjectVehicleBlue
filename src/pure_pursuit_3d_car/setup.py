from setuptools import find_packages, setup

package_name = 'pure_pursuit_3d_car'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='junaet-mahbub',
    maintainer_email='52060704+Jdawg0309@users.noreply.github.com',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
    'console_scripts': [
        'pure_pursuit_node = pure_pursuit_3d_car.pure_pursuit_node:main',
    ],
},

)
