import setuptools

setuptools.setup(
    name='public',
    install_requires=open('requirements.txt').read().splitlines(),
    packages=setuptools.find_packages()
)
