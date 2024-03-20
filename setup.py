from distutils.core import setup

setup(
    name="ubcaerodesign",
    packages=["ubcaerodesign"],
    version="0.6",
    license="GNU Affero General Public License v3.0",
    description="PyPi package for networking.py and loggingconfig",
    author="Midora",
    author_email="midorashiu@gmail.com",
    url="https://github.com/ubcaerodesign/ubcaerodesign",
    download_url="https://github.com/ubcaerodesign/ubcaerodesign/archive/refs/tags/v0.6.tar.gz",
    keywords=["aerodesign"],
    install_requires=["zmq"],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Build Tools",
        "License :: OSI Approved :: GNU Affero General Public License v3.0",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.9",
    ],
)
