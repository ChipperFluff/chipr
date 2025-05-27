from setuptools import setup

setup(
    name="chipr",
    version="0.0.1",
    packages=["chipr"],
    entry_points={
        'console_scripts': [
            'chipr = chipr.__main__:main',
        ],
    },
)
