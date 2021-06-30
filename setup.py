from setuptools import setup

setup(
    setup_requires=['wheel'],
    name='date_time_literal',
    packages=['date_time_literal'],
    version='1.0.2',
    description='date-time-literal is '
                'a python module that helps convert date-time or'
                ' date to literal days, hours, seconds, or even minutes. Compare two DateTime or Date objects, by'
                ' converting the objects to literal days, hours, minutes, or even seconds if you want to be precise. ',
    author='Kelvin Sajere',
    author_email='kells4real@gmail.com',
    url='https://github.com/kells4real/date_literal',
    download_url='https://github.com/kells4real/date_literal/archive/refs/tags/1.0.0.tar.gz',
    keywords=['date-time', 'date', 'literal', 'date converter', 'literal date', 'date-time converter',
              'django', 'python', 'module', 'python package', 'date-time literal', 'convert time', 'convert date-time'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.5',
)
