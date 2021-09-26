from setuptools import find_packages, setup
from waafipay import package_version

long_description = "Python sdk "

PYTHON_SDK_VERSION = package_version
setup(
    name='waafipay',
    package_data={'waafipay': ['VERSION.ini']},
    version=PYTHON_SDK_VERSION,
    author='Abdulkareem/Nadeem',
    description="Waafipay payment gateway sdk",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=find_packages(),
    install_requires=["requests", "pycryptodome"],
    include_package_data=True,
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
)