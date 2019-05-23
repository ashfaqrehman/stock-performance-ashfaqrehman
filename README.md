# Assignment 5 - Stock Portfolio Performance


pip install git+git://github.com:sheridan-python/stock-performance-ashfaqrehman#egg=portfolio

This assignment will test the following skills:

- Reading and writing to the file system
- Making HTTP requests
- Testing read & write operations to the disk
- Testing HTTP requests using a mock library


## Description
Write a program which will generate up-to-date performance reports for a given
stock portfolio. The program will accept two arguments: an input CSV file which
contains the holdings information, and, a path to output the CSV report.

We will use the [IEX Trading API](https://iextrading.com/developer/docs/), as
the market data source – it is a public (free) API.


### Requirements
The program will read a CSV file containing our portfolio data. Based on this
data, a new CSV report will be generated using live market value to indicate
our current holding performance using the IEX API.

The program will be installable using `pip`, and requires a `setup.py`
file. When installed, a binary should be added to the Python path which can be
invoked from anywhere on the filesystem.

An example interaction with the script looks like this:

```
$ portfolio_report --source portfolio.csv --target report1.csv
```

#### Input file
The input CSV will have 3 columns (example provided).

- `symbol`: the ticker symbol (e.g. AAPL is Apple)
- `units`: the quantity of shares held
- `cost`: the original / average purchase price of the holding


Example:

symbol | units | cost
-------| ------|------
AAPL   | 1000  | 123.56
AMZN   |  20   | 2001.1


The script will iterate over the data provided, and **validate** that the
symbol is listed on the IEX. An unrecognized symbol should be skipped, but,
warn the user that they have an unrecognized input.


Using the list of symbols from the input CSV, get quotes from IEX to fetch the
latest price. This can be done in a batch request – meaning, multiple quotes
can be requested in a single HTTP request. See:

    Docs: https://iextrading.com/developer/docs/#batch-requests

    Example: https://api.iextrading.com/1.0/stock/market/batch?symbols=aapl,fb&types=quote

Once the latest price is obtained, a series of calculations are made to
establish the current performance of the portfolio: what the current market
value is, the gain and loss for each holding and a percentage of change.


#### Output file

The expected CSV report will have the following columns

* `symbol`: The stock ticker symbol (i.e. AAPL)
* `company_name`: The name of the company (i.e. Apple Inc.)
* `units`: The amount of shares held
* `cost`: The original cost per share
* `latest_price`: The latest market price per share
* `book_value`: The value of the shares at time of purchase
* `market_value`: The value of the shares based on the latest market value
* `gain_loss`: The dollar amount either gained or lost
* `change`: A percentage (decimal) of the gain/loss

The final row will contain the total portfolio standing.

##### Sample output CSV
symbol  |  company_name  | units | cost     |   latest_price | book_value  |   market_value | gain_loss |   change
------- | ---------------|-------|----------|----------------|-------------|----------------| ----------|----------
AAPL    |  Apple Inc.    | 1000  | 123.56   |   156.23       | 12356       |   15623        | 3267      |   0.264
AMZN    |  Amazon Inc.   | 20    | 2001.1   |   1478.19      | 40022       |   29563        | -10459    |   -0.261


## Getting started

Take a modular approach to completing this assignment and build each functional
component in isolation, accompanied by appropriate tests.

Here is a breakdown of isolated functional units:

- Given a filename/path, read a CSV and convert it to a Python data structure
- Fetch the symbol list from the IEX API and into a Python data structure
- Validate that the symbols listed in the input CSV are listed on IEX.
- Build a method which returns the latest market price for holdings
- Build methods which calculate the book value, market value
- Build a method to convert the holding into CSV
- Build a method that writes to the output filename.

You are free to use any data types you wish to store this data.


## Testing

Testing against third-party services can be challenging as they are out of our
control. As developers, we must build our application with the expectation of
specific behaviours from these services. Mocks (faking) are a handy way to
isolate the dependency and replace it with a constant to which we can build
tests. For this, we will use the `requests-mock` library to stub out
HTTP requests.

    https://requests-mock.readthedocs.io/en/latest/pytest.html

Install using `pip install requests-mock`.

As for writing files, use the `tmp_path` fixture that ships with pytest to
write to temporary locations on the disk.


## Evaluation rubric

| Metric | 4 | 3 | 2 | 1 | 0
| - | - | - | - | - | -
| Meets requirements | All requirements are met | Almost all requirements are met |  Most requirements met, some bugs | Incorrect results, several bugs | Program does not work
| Testing | Unit tests are present and cover all functionality | Most of the script is covered by testing | Partial test coverage, some false assertions present | Minimal testing, false assertions present, missing main functional coverage. | No meaningful tests exist
| Packaging & delivery | The project is properly packaged, documented and can be installed using pip. | The project is packaged, but is missing certain metadata |  The project is installable, but with some issues. Documentation is incomplete.| Documentation is partial, the package does not install | No packaging present, little or no documentation
| Reusability | The code could be reused as a whole and each routine could be reused | Most of the code could be reused in other programs | Some parts of the code could be reused in other programs | A few parts of the code could be reused in other programs | The code is not organized for reusability
| Readability | The code is well organized and very easy to understand | The code is pretty well organized and fairly easy to read | The code has some organization, is a challenge to read | The code is readable only by someone who knows what it is supposed to do | The code is poorly organized and very difficult to read


## Installation

### Quick install

```
$ pip install git+ssh://git@github.com/sheridan-python/stock-performance-ashfaqrehman#egg=portfolio
```

### For development
1. Clone the repo
2. Install using pip like:

```
$ pip install -e .
```


## Usage

```
$ portfolio_report --source portfolio.csv --target report1.csv
```
