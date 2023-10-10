# SeleniumTrainings
SET Series - Test Automation with Python Mentoring Program #4

# Logging Functionality
This project uses a `config.ini` file to manage configuration settings. Below is an example of the `config.ini` content:

```ini
[loggers]
keys=root,customLogger

[handlers]
keys=consoleHandler,fileHandler

[formatters]
keys=fileFormatter,consoleFormatter

[logger_root]
level=DEBUG
handlers=consoleHandler

[logger_customLogger]
level=DEBUG
handlers=consoleHandler,fileHandler
qualname=customLogger
propagate=0

[handler_consoleHandler]
class=StreamHandler
level=WARNING
formatter=consoleFormatter
args=(sys.stdout,)

[handler_fileHandler]
class=FileHandler
level=DEBUG
formatter=fileFormatter
args=('..\\Logs\\logfile.log','a')

[formatter_fileFormatter]
format=%(asctime)s - %(name)s - %(levelname)s - %(message)s
datefmt='%m:%d:%Y

[formatter_consoleFormatter]
format=%(levelname)s - %(message)s
datefmt='%m:%d:%Y

# CustomLogger for unit testing 
The `CustomLogger` class provides an example of how to set up logging and perform unit tests using the `unittest` framework. It demonstrates testing two functions: `add` and `multiply`.

# TestCase.py for Unit test framework
This project demonstrates how to perform database testing using Python's `unittest` framework along with `HTMLTestRunner`. It includes test cases for validating a SQL Server database.

## Prerequisites
- Python (>= 3.x)
- SQL Server (or another compatible database)
- Required Python libraries (PyODBC, HTMLTestRunner)

Usage:
This project contains test cases for validating SQL Server Database. The tests are organized into test suites for different database tables (eg: `UnitMeasure`, `Address`).

Test Suites:
. `TestUnitMeasure`: Test Cases for the `UnitMeasure` table.
. `TestAddress`: Test cases for the `Address` table.

