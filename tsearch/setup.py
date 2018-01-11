from setuptools import setup

setup(
    name='tsearch',
    packages=['tsearch'],
    include_package_data=True,
    install_requires=[
        'flask', 'twitter',
    ],
)
