import pytest

from framework.utils.logger import Logger
from tests.config.db import DataBase
from tests.result import TestResult
from tests.database.database_union_reporting import DataBaseUnionReporting
from tests.utils.generate_data_util import GenerateDataUtil


class TestDataBase:
    def test_insert_operation_in_db(self, create_db_connection_and_cursor):
        Logger.step("Step 1. Running the test in the module 'test_api.py'")
        pytest.main([DataBase.TEST_NAME])
        result = TestResult.result_of_test
        assert result.outcome in DataBase.VALID_TEST_RESULT, "The test hasn't been completed"

        Logger.step("Post-condition. Adding a result of the completed test to the database")
        database_union = DataBaseUnionReporting()
        inserted_num_of_rows_in_author = database_union.create_record_in_table(DataBase.AUTHOR)
        assert inserted_num_of_rows_in_author > 0, "The record in the Author table hasn't been inserted"
        inserted_num_of_rows_in_project = database_union.create_record_in_table(DataBase.PROJECT)
        assert inserted_num_of_rows_in_project > 0, "The record in the Project table hasn't been inserted"
        inserted_num_of_rows_in_dev_info = database_union.create_record_in_table(DataBase.DEV_INFO)
        assert inserted_num_of_rows_in_dev_info > 0, "The record in the Dev_Info table hasn't been inserted"
        inserted_num_of_rows_in_session = database_union.create_record_in_table(DataBase.SESSION)
        assert inserted_num_of_rows_in_session > 0, "The record in the Session table hasn't been inserted"
        DataBase.TEST["values"] = GenerateDataUtil.generate_data_for_test_table()
        inserted_num_of_rows_in_test = database_union.create_record_in_table(DataBase.TEST)
        assert inserted_num_of_rows_in_test > 0, "The record in the Test table hasn't been inserted"

    def test_existing_records_in_db(self, create_db_connection_and_cursor):
        Logger.step("Precondition. Selecting tests from the the test table "
                    "where ID contains two random repeating digits")
        database_union = DataBaseUnionReporting()
        records = database_union.get_ten_records_with_repeating_digits_in_id_from_test_table()

        Logger.step("Precondition. Copying selected tests with an indication of the current project "
                    "and the author to the test table")
        values = GenerateDataUtil.generate_values_for_selected_records_to_copy_them_in_test_table(records)
        database_union.insert_records_to_table(table_name=DataBase.TEST["table_name"],
                                               columns=DataBase.TEST["columns"],
                                               values=values)

        Logger.step("Step 1. Stimulating the launch of each test. Updating information about them in the database")
        db_union = DataBaseUnionReporting()
        simulated_tests_results = GenerateDataUtil.generate_results_for_tests_simulations()
        assert db_union.check_if_tests_completed(simulated_tests_results), "Tests haven't been completed"
        num_of_updated_records = db_union.update_copied_records_in_test_table(simulated_tests_results)
        assert db_union.check_if_records_have_been_updated(num_of_updated_records), "The records haven't been updated"

        Logger.step("Post-condition. Deleting the records created in Preconditions from the database")
        records_num_in_test_before = database_union.get_num_of_records_in_table(DataBase.TEST["table_name"])
        database_union.delete_ten_copied_records()
        records_num_in_test_after = database_union.get_num_of_records_in_table(DataBase.TEST["table_name"])
        assert records_num_in_test_before > records_num_in_test_after, \
               "The record in the Test table hasn't been inserted"
