from setuptools import setup, find_packages


setup(
    name="aioredis",
    version="2.0.1",
    description="asyncio (PEP 3156) Redis support",
    platforms=["POSIX"],
    url="https://github.com/anton-dovnar/aioredis",
    license="MIT",
    packages=find_packages(exclude=["tests"]),
    install_requires=[
        "async-timeout",
        "typing-extensions",
    ],
    extras_require={
        "hiredis": 'hiredis>=1.0; implementation_name=="cpython"',
    },
    package_data={"aioredis": ["py.typed"]},
    python_requires=">=3.6",
    include_package_data=True,
)
