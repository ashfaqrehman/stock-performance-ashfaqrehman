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
- What was the original (or average) purchase price?

When symbols are added through the program, the CSV portfolio containing the
data should be updated.

- The ticker symbol must be listed on the IEX. These are mostly NASDAQ
  stock symbols. Unrecognized symbols should be rejected / ignored


#### Implementation
- Fetch the list of symbols from IEX on load using the API
  (https://api.iextrading.com/1.0/ref-data/symbols)
- Read data found in `portfolio.csv` (provided)
- Using the portfolio data, obtain the latest market price for each holding.
  This can be achieved using the batch IEX API (e.g.
  https://api.iextrading.com/1.0/stock/market/batch?symbols=aapl,fb&types=quote)
- Write a method that calculates the current value and change percentage of
  each holding
- Write a method that gets the current value of


### Examples
#### Starting View
```
** Welcome to your stock portfolio! **

You currently own the following stocks:

Symbol     Cost         Latest Price   Units   Current Value     Change %
--------------------------------------------------------------------------
AAPL       $123.56      $156.23        1000    $15,623.00        +26.4%
AMZN       $2,001.10    $1,478.19      20      $29,563.80        -26.1%


Your total portfolio value is:
$45,186.80 (-15.9%)

Choose one from the following options:
(b) Buy / add to portfolio
(s) Save the report
(q) Quit

>
```
#### Save the report
Entering the `s` option should do the following:
```
Saving the report to "portfolio-2019-01-01-17-23-23.csv".

Goodbye!
```

#### Quit
Entering `q` should simply exit

#### Buy
Entering `b` should prompt with the following:

```
Buy stock:

Enter symbol: banana
"banana" is not a valid symbol

Enter symbol: AAPL
(AAPL) Apple Inc.

Enter purchase price: 165.23

Thank you. Returning to main screen.
```
Following a successful buy, the `portfolio.csv` should be updated with the new
holdings information.
