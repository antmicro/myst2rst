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
      entry_points={
          'console_scripts': ['myst2rst=myst2rst:main'],
      },
      packages=['myst2rst'])
