# Assignment 5 - Stock Portfolio

This assignment will test the following skills:

- Reading and writing to the file system
- Making HTTP requests
- Testing read & write operations to the disk
- Testing HTTP requests using a mock library


## Description
We will write a program which will help us manage our stock portfolio, and
generate a CSV file of our current holdings using real-time data. We will use
the [IEX Trading API](https://iextrading.com/developer/docs/), as the data
source data source.


### Requirements
The program will ask us about our portfolio. What stocks do you currently own?
The user is given the opportunity to add stocks to their portfolio.

- What is the ticker symbol? (e.g. APPL is Apple)
- How many units do you own?
- What was your original purchase price?

When symbols are added through the program, the CSV portfolio containing the
data should be updated.


- The ticker symbol must be listed on the IEX. These are mostly NASDAQ and NYSE
  stock symbols. Unrecognized symbols should be rejected
