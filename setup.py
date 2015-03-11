from setuptools import setup
# from setuptools import find_packages
from setuptools.command.test import test as testcommand
import sys
import re
import os
import codecs

here = os.path.abspath(os.path.dirname(__file__))


def read(*parts):
    # intentionally *not* adding an encoding option to open
    return codecs.open(os.path.join(here, *parts), 'r').read()


def find_version(*file_paths):
    version_file = read(*file_paths)
    version_match = re.search(r"^__version__ = ['\"]([^'\"]*)['\"]",
                              version_file, re.M)
    if version_match:
        print('VERSION: ', version_match.group(1))
        return version_match.group(1)
    raise RuntimeError("Unable to find version string.")


class Tox(testcommand):
    def finalize_options(self):
        testcommand.finalize_options(self)
        self.test_args = []
        self.test_suite = True

    def run_tests(self):
        # import here, cause outside the eggs aren't loaded
        import tox
        errcode = tox.cmdline(self.test_args)
        sys.exit(errcode)

setup(
    name='project-euler',
    version=find_version('euler', '__init__.py'),
    url='https://github.com/nir0s/project_euler',
    author='nir0s',
    author_email='nir36g@gmail.com',
    license='LICENSE',
    platforms='All',
    description='Project Euler wrapper and solutions',
    long_description=read('README.rst'),
    packages=['euler'],
    install_requires=[
    ],
    tests_require=['nose', 'tox'],
    cmdclass={'test': Tox},
)
