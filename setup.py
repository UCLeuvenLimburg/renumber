from setuptools import setup


setup(name='renumber',
      version='0.1.0',
      description='Renumbers directories',
      url='http://github.com/UCLeuvenLimburg/renumber',
      author='Frederic Vogels',
      author_email='frederic.vogels@ucll.be',
      license='MIT',
      packages=['renumber'],
      entry_points = {
            'console_scripts': [ 'renumber=renumber.command_line:shell_entry_point']
      },
      zip_safe=False)