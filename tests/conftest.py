import pytest

from framework.utils.database.general_db import GeneralDataBase
from tests.config.db import DataBase
from tests.result import TestResult


@pytest.fixture
def create_db_connection_and_cursor():
    GeneralDataBase.establish_db_connection(user=DataBase.USER,
                                            password=DataBase.PASSWORD,
                                            host=DataBase.HOST,
                                            database=DataBase.DATABASE)
    GeneralDataBase.create_cursor()

    yield
    GeneralDataBase.close_cursor()
    GeneralDataBase.close_db_connection()


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    test_report = outcome.get_result()
    test_report.start = call.start
    test_report.stop = call.stop
    if test_report.when == 'call':
        TestResult.result_of_test = test_report
