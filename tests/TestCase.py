import unittest
import pyodbc
import HtmlTestRunner
import logging.config


class DatabaseTestCase(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        # Adding logger
        logging.config.fileConfig('..\\Config\\config.ini', disable_existing_loggers=False)
        cls.logger = logging.getLogger('customLogger')

        # Initialize database connection and cursor
        cls.conn = pyodbc.connect(
            'Driver={SQL SERVER};'
            'Server=EPINHYDW03E2\\SQLEXPRESS;'
            'Database=AdventureWorks2012;'
            'Trusted_Connection=yes;')
        cls.ad_cursor = cls.conn.cursor()

    @classmethod
    def tearDownClass(cls):
        # Close cursor and connection
        cls.ad_cursor.close()
        cls.conn.close()


# Test suite for UnitMeasure table
class TestUnitMeasure(DatabaseTestCase):

    # Test: Count validation on UnitMeasure table
    def test_unitmeasure_count_rows(self):
        self.ad_cursor.execute('select count(*) from AdventureWorks2012.Production.UnitMeasure')
        record_count = self.ad_cursor.fetchval()
        self.logger.info(f'Record count is {record_count}')
        self.assertEqual(record_count, 38)

    # Test: Primary key column UnitMeasureCode should not contain nulls
    def test_not_null(self):
        self.ad_cursor.execute('select count(*) from AdventureWorks2012.Production.UnitMeasure '
                               'where UnitMeasureCode is null')
        unit_measure_code = self.ad_cursor.fetchval()
        self.logger.info(f'UnitMeasureCode is having {unit_measure_code} nulls')
        self.assertEqual(unit_measure_code, 0, "Sum UnitMeasureCode values are null")


# Test suite for Address Table
class TestAddress(DatabaseTestCase):

    # Test: min max validation on AddressId column
    def test_min_max(self):
        self.ad_cursor.execute('select min(AddressID), max(AddressID) from AdventureWorks2012.Person.Address')
        min_max_values = self.ad_cursor.fetchall()
        self.logger.info(f'Min and Max values are {min_max_values}')
        self.assertEqual(list(min_max_values[0]), [1, 32521], "Min and Max values does not match")

    # Test: Duplicate check on Address table
    def test_duplicates(self):
        self.ad_cursor.execute('select AddressID, count(*) from AdventureWorks2012.Person.Address '
                               'group by AddressID having count(*)>1')
        duplicate_records = self.ad_cursor.fetchall()
        self.logger.info(f'Duplicate records are {duplicate_records}')
        self.assertEqual(len(duplicate_records), 0, "Address table contains duplicate records")


if __name__ == '__main__':
    # Create test suite for each table
    suite_unitmeasure = unittest.TestLoader().loadTestsFromTestCase(TestUnitMeasure)
    suite_address = unittest.TestLoader().loadTestsFromTestCase(TestAddress)

    # Combine the test suites
    all_tests = unittest.TestSuite([suite_unitmeasure, suite_address])

    # Run the tests and generate the HTML report
    report_file = 'test_report.html'
    with open(report_file, 'w') as output_stream:
        runner = HtmlTestRunner.HTMLTestRunner(
            stream=output_stream,
            report_title='Database Test Report',
            descriptions='Test results for database queries'
        )
        runner.run(all_tests)
