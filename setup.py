from setuptools import setup

setup(
    name='ClickExampleApp',
    version='0.1',
    py_modules=['main'],
    install_requires=[
        'click',
    ],
    entry_points={
        'console_scripts': [
            'app_name=main:entrypoint_fn',
        ],
    },
)
