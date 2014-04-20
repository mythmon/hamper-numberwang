from distutils.core import setup

with open('requirements.txt') as f:
    requirements = [l.strip() for l in f]

setup(
    name='numberwang',
    version='0.1',
    packages=['numberwang'],
    author='Mike Cooper',
    author_email='mythmon@gmail.com',
    url='https://github.com/mythmon/hamper-numberwang',
    install_requires=requirements,
    package_data={'cah': ['requirements.txt', 'README.md', 'LICENSE']}
)
