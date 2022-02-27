from setuptools import setup

setup(name='myst2rst',
      version='0.1',
      description='MyST to RST convertser',
      url='http://github.com/mgielda/myst2rst',
      author='Antmicro',
      author_email='mgielda@antmicro.com',
      install_requires=[
          'docutils', 'myst-docutils'
      ],
      license='MIT',
      scripts=['bin/myst2rst'],
      packages=['myst2rst'])
