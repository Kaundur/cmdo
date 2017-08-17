from setuptools import setup

setup(name='cmdo',
      version='0.1',
      description='Cmdo the command line todo list',
      url='http://github.com/kaundur/cmdo',
      author='Kaundur',
      author_email='cmdo@kaundur.com',
      license='MIT',
      packages=['cmdo'],
      entry_points={
            "console_scripts": [
                  'cmdo = cmdo.cmdo:run_cmdo'
            ]
      },
      zip_safe=False)
