"""
setup.py for package build
"""
import setuptools

setuptools.setup(
    name='portfolio_report',
    version='0.0.1',
    author='Ash',
    description='The program will read a CSV file containing portfolio data and generate a new CSV report using using live market price on IEX API.',
    packages=['portfolio'],
    entry_points={
        'console_scripts':['portfolio_report=portfolio.portfolio_report:main']
    },
    install_requires=[
        "requests"
    ]

)
