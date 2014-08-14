from distutils.core import setup
from setuptools import find_packages


setup(
    name="PsProfile",
    version='0.1.1',
    description="Collects resource usage of an executed script",
    url="http://github.com/egafni/PsProfile",
    author="Erik Gafni",
    author_email="egafni@gmail.com",
    maintainer="Erik Gafni",
    maintainer_email="egafni@gmail.com",
    license="GPL",
    install_requires=[
        "psutil",],
    packages=find_packages(),
    include_package_data=True,
    scripts=["bin/psprofile"],
)


