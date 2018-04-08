from setuptools import setup

setup(name='cmdo-App',
      version='0.3',
      description='Cmdo: the command line todo list app',
      long_description='Cmdo: the command line todo list app',
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
      download_url='https://github.com/kaundur/cmdo/archive/0.3.tar.gz',
      keywords=['todo', 'todolist', 'todoapp', 'command-line-tool', 'command-line', 'python', 'productivity'],
      zip_safe=False)
