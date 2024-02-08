from setuptools import setup, find_packages

setup(
    name="simple-visualizer",
    author="Nataša Džudžar",
    version="0.2",
    packages=find_packages(),
    namespace_packages=["plugin", "plugin.visualizer"],
    entry_points={
        'plugin.visualizer':
        ['simple-visualizer=plugin.visualizer.simple_visualizer:SimpleVisualizer']
    },
    install_requires=["sok-core>=0.1"],

    zip_safe=True
)
