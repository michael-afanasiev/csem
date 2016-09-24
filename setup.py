from setuptools import setup

setup(
        name='csem',
        version='0.0.1',
        py_modules=['csem'],
        url='https://github.com/michael-afanasiev/csem',
        license='MIT',
        author='michaelafanasiev',
        author_email='michael.afanasiev@erdw.ethz.ch',
        description='',
        entry_points='''
        [console_scripts]
        csem=csem.csem:cli
        '''
)
