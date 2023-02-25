from setuptools import setup, find_packages, Extension

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
)
