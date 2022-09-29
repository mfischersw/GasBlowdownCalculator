from setuptools import setup, find_packages


setup(
    name='gasblowdowncalculator',
    version='0.0.0',
    description='GasBlowdownCalculator',
    long_description='GasBlowdownCalculator',
    author='Michael Fischer',
    author_email='mfischer.sw@gmail.com',
    package_dir={'': 'src'},
    packages=find_packages(where='src'),
    python_requires='>=3.8, <4',
    project_urls={
        'Source': 'https://github.com/mfischersw/GasBlowdownCalculator/',
    }
)
