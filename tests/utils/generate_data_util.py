from framework.utils.logger import Logger
from framework.utils.datetime_util import DatetimeUtil
from framework.utils.platform_util import PlatformUtil
from framework.utils.convert_util import ConvertUtils
from framework.utils.random_util import RandomUtils
from framework.constants.date_time_constants import YEAR_MONTH_DATE_TIME_FORMAT

from tests.database.database_union_reporting import DataBaseUnionReporting
from tests.config.db import DataBase
from tests.result import TestResult


class GenerateDataUtil:
    @staticmethod
    def generate_data_for_test_table():
        Logger.info("Generating data for Test table")
        db_reunion = DataBaseUnionReporting()
        test_result = TestResult.result_of_test.__dict__
        status_id = db_reunion.get_column_value_from_table(column=DataBase.ID_COLUMN,
                                                           table_name=DataBase.STATUS[DataBase.TABLE_NAME_FIELD],
                                                           name=f'"{test_result[DataBase.TEST_RESULT_OUTCOME]}"')
        project_id = db_reunion.get_column_value_from_table(column=DataBase.ID_COLUMN,
                                                            table_name=DataBase.PROJECT[DataBase.TABLE_NAME_FIELD],
                                                            name=DataBase.PROJECT[DataBase.VALUES_FIELD])
        author_id = db_reunion.get_column_value_from_table(column=DataBase.ID_COLUMN,
                                                           table_name=DataBase.AUTHOR[DataBase.TABLE_NAME_FIELD],
                                                           name=DataBase.AUTHOR["author_name"])
        session_id = db_reunion.get_column_value_from_table(column=DataBase.ID_COLUMN,
                                                            table_name=DataBase.SESSION[DataBase.TABLE_NAME_FIELD],
                                                            name=f'"{DataBase.SESSION["session_key"]}"',
                                                            condition_column=DataBase.SESSION_KEY_COLUMN)
        start_time = DatetimeUtil.convert_unix_time_to_date_time(test_result["start"])
        stop_time = DatetimeUtil.convert_unix_time_to_date_time(test_result["stop"])

        str_data = "'" + test_result[DataBase.TEST_RESULT_NODEID] + "'" + ", " + str(status_id) + ", " + "'" \
                   + test_result[DataBase.TEST_RESULT_LOCATION][2] + "'" + ", " + str(project_id) + ", " + str(session_id) + ", "\
                   + "'" + str(start_time) + "'" + ", " + "'" + str(stop_time) + "'" + ", " \
                   + "'" + PlatformUtil.get_system_name() + "'" + ", " + DataBase.NOT_GIVEN + ", " + str(author_id)

        return str_data

    @staticmethod
    def generate_values_for_selected_records_to_copy_them_in_test_table(records: list):
        Logger.info("Generating values for selected records to copy them to Test table")

        Logger.info("Replacing project_id and author_id in 10 retrieved records from Test table")
        db_reunion = DataBaseUnionReporting()
        author_id = db_reunion.get_column_value_from_table(column=DataBase.ID_COLUMN,
                                                           table_name=DataBase.AUTHOR[DataBase.TABLE_NAME_FIELD],
                                                           name=DataBase.AUTHOR["author_name"])
        project_id = db_reunion.get_column_value_from_table(column=DataBase.ID_COLUMN,
                                                            table_name=DataBase.PROJECT[DataBase.TABLE_NAME_FIELD],
                                                            name=DataBase.PROJECT[DataBase.VALUES_FIELD])
        records_with_replaced_ids = ConvertUtils.convert_list_of_tuples_to_list_of_lists(records)

        for record in records_with_replaced_ids:
            record[-1] = author_id
            record[4] = project_id

        Logger.info("Adding inverted commas to strings in retrieved records")
        for i in range(len(records_with_replaced_ids)):
            records_with_replaced_ids[i] = list(map(lambda x: "'" + str(x) + "'" if not isinstance(x, int)
                                                    and x is not None else x, records_with_replaced_ids[i]))

        Logger.info("Replacing the None with NULL value in retrieved records data")
        for i in range(len(records_with_replaced_ids)):
            records_with_replaced_ids[i] = list(map(lambda x: "NULL" if x is None else x, records_with_replaced_ids[i]))

        Logger.info("Converting all elements of retrieved records to strings")
        str_records = list(map(lambda x: ConvertUtils.convert_list_of_dif_types_to_list_of_str(x),
                               records_with_replaced_ids))

        Logger.info("Converting retrieved records from a list of lists to a list of strings")
        for i in range(len(str_records)):
            str_records[i] = ", ".join(str_records[i])

        Logger.info("Adding brackets to retrieved records")
        for i in range(len(str_records)):
            str_records[i] = "(" + str_records[i] + ")"

        Logger.info("Converting retrieved records from a list of strings to a string")
        values = ConvertUtils.convert_list_of_str_to_str(str_records)

        return values

    @staticmethod
    def generate_result_data_for_test_simulation():
        Logger.info("Generating random data for a test simulation")
        db_reunion = DataBaseUnionReporting()
        name = RandomUtils.generate_random_letters_and_digits_str(DataBase.RANDOM_STR_LENGTH)
        status_id = RandomUtils.generate_random_int(min_value=DataBase.MIN_VALUE_INT,
                                                    max_value=DataBase.MAX_VALUE_STAT_ID)
        method_name = RandomUtils.generate_random_letters_and_digits_str(DataBase.RANDOM_STR_LENGTH)
        project_id = db_reunion.get_column_value_from_table(column=DataBase.ID_COLUMN,
                                                            table_name=DataBase.PROJECT[DataBase.TABLE_NAME_FIELD],
                                                            name=DataBase.PROJECT[DataBase.VALUES_FIELD])
        session_id = RandomUtils.generate_random_int(min_value=DataBase.MIN_VALUE_INT,
                                                     max_value=DataBase.MAX_VALUE)
        start_time = RandomUtils.generate_random_datetime(DataBase.START_DATE_TIME, DataBase.END_DATE_TIME,
                                                          YEAR_MONTH_DATE_TIME_FORMAT)
        end_time = RandomUtils.generate_random_datetime(DataBase.START_DATE_TIME, DataBase.END_DATE_TIME,
                                                        YEAR_MONTH_DATE_TIME_FORMAT)
        env = RandomUtils.generate_random_letters_and_digits_str(DataBase.RANDOM_STR_LENGTH)
        browser = RandomUtils.generate_random_letters_and_digits_str(DataBase.RANDOM_STR_LENGTH)
        author_id = db_reunion.get_column_value_from_table(column=DataBase.ID_COLUMN,
                                                           table_name=DataBase.AUTHOR[DataBase.TABLE_NAME_FIELD],
                                                           name=DataBase.AUTHOR["author_name"])

        test_columns = DataBase.TEST_COLUMNS_LIST

        data = {f"{test_columns[0]}": f"'{name}'",
                f"{test_columns[1]}": f"{status_id}",
                f"{test_columns[2]}": f"'{method_name}'",
                f"{test_columns[3]}": f"{project_id}",
                f"{test_columns[4]}": f"{session_id}",
                f"{test_columns[5]}": f"'{start_time}'",
                f"{test_columns[6]}": f"'{end_time}'",
                f"{test_columns[7]}": f"'{env}'",
                f"{test_columns[8]}": f"'{browser}'",
                f"{test_columns[9]}": f"{author_id}"}
        return data

    @staticmethod
    def generate_results_for_tests_simulations():
        Logger.info("Generating results for tests simulations")
        new_list = []
        for i in range(DataBase.NUM_OF_RECORDS_TO_COPY):
            new_list.append(GenerateDataUtil.generate_result_data_for_test_simulation())
        return new_list
