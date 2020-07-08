from setuptools import setup, find_packages

VERSION = 0.1

setup(
  name="ykxtools",
  version=VERSION,
  packages=find_packages(exclude=["*.tests", "*.tests.*", "tests.*", "tests"]),
  install_requires=[
    "ipaddress",
    "psutil",
  ],
  entry_points={

    "tools_scripts": [
      "split_str = mytools.mytools:split_str",
      "read_json_file = mytools.mytools.read_json_file",

    ],
  },

)
