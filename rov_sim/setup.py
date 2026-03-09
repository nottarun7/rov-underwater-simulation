from setuptools import find_packages, setup

package_name = 'rov_sim'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
    ('share/ament_index/resource_index/packages',
        ['resource/' + package_name]),
    ('share/' + package_name, ['package.xml']),
    ('share/' + package_name + '/launch', ['launch/sim.launch.py']),
    ('share/' + package_name + '/models/babyrov', [
        'models/babyrov/model.sdf',
        'models/babyrov/model.config']),
    ('share/' + package_name + '/launch', [
        'launch/sim.launch.py',
        'launch/rov_demo.launch.py'
    ]),
    ('share/' + package_name + '/worlds', ['worlds/ocean.world']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='root',
    maintainer_email='root@todo.todo',
    description='TODO: Package description',
    license='TODO: License declaration',
    extras_require={
        'test': [
            'pytest',
        ],
    },
    entry_points={
        'console_scripts': [
        ],
    },
    
)
