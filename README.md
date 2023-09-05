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
