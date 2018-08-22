try:
    from setuptools import setup, find_packages
except ImportError:
    import ez_setup

    ez_setup.use_setuptools()
    from setuptools import setup, find_packages

setup(
    name="atomic",
    version="0.0.1",
    url='https://github.com/mattpaletta/atomic',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[],
    author="Matthew Paletta",
    author_email="mattpaletta@gmail.com",
    description="Atomic operations in python.",
    license="BSD",
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Communications',
    ]
)