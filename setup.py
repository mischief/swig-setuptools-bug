from setuptools import setup, find_packages, Extension
from setuptools.command.build_py import build_py

# Build extensions before python modules,
# or the generated SWIG python files will be missing.
class BuildPy(build_py):
    def run(self):
        self.run_command('build_ext')
        super(build_py, self).run()

ext = Extension('foo.bar._baz', ['foo/bar/baz.i', 'foo/bar/baz.c'])
setup(
    name="foo",
    version="0.0.1",
    description="Foo!",
    author="The Foo Authors",
    license="MIT",
    packages=find_packages(exclude=["tests*"]),
    entry_points={
        "console_scripts": [
            "foo = foo:main",
        ],
    },
    ext_modules=[ext],
    cmdclass={
        'build_py': BuildPy,
    },
)
