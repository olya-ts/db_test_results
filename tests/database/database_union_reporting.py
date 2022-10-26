from framework.utils.database.general_db import GeneralDataBase
from framework.utils.filter_util import FilterUtils
from framework.utils.random_util import RandomUtils
from framework.utils.convert_util import ConvertUtils
from framework.utils.logger import Logger

from tests.config.db import DataBase


class DataBaseUnionReporting(GeneralDataBase):
    def create_record_in_table(self, table_data: dict):
        Logger.info("Creating a record in the table " + table_data[DataBase.TABLE_NAME_FIELD])
        self.create_new_record(data=table_data)

        self.commit_to_db()
        count = self.count_affected_rows()

        return count

    def get_column_value_from_table(self, column: str, table_name: str, name: str,
                                    condition_column: str = DataBase.NAME_COLUMN):
        Logger.info("Getting a value from the column " + column + " from the table " + table_name)
        condition = f"{condition_column} = {name}"
        column_value = self.retrieve_records_from_table(field_names=column,
                                                        table_name=table_name,
                                                        condition=condition)
        for value in column_value:
            return value[0]

    def get_all_column_values_from_table(self, column: str, table_name: str):
        Logger.info("Getting all values from the column " + column + " from the table " + table_name)
        column_values = self.retrieve_records_from_table(field_names=column,
                                                         table_name=table_name)

        column_values_list = []
        for row in column_values:
            column_values_list.append(row[0])

        return sorted(column_values_list)

    def choose_ten_test_table_ids_with_repeating_digits(self):
        Logger.info("Selecting 10 ids from Test table that have repeating digits")
        all_ids = self.get_all_column_values_from_table(column=DataBase.ID_COLUMN,
                                                        table_name=DataBase.TEST[DataBase.TABLE_NAME_FIELD])
        filtered_ids = FilterUtils.filter_list_of_ints_with_repeating_digits(all_ids)

        selected_list_of_ids = RandomUtils.\
            select_random_items_from_list_without_repetition(filtered_ids, DataBase.NUM_OF_RECORDS_TO_COPY)
        return ConvertUtils.convert_list_of_ints_to_str(selected_list_of_ids)

    def get_ten_records_with_repeating_digits_in_id_from_test_table(self):
        Logger.info("Getting 10 records from Test table")
        ten_ids = self.choose_ten_test_table_ids_with_repeating_digits()

        records = self.retrieve_records_from_table(field_names=DataBase.TEST[DataBase.COLUMNS_FIELD],
                                                   table_name=DataBase.TEST[DataBase.TABLE_NAME_FIELD],
                                                   condition=f"{DataBase.ID_COLUMN} in ({ten_ids})")

        return records

    def insert_records_to_table(self, table_name: str, columns: str, values: str):
        Logger.info("Inserting records to the table " + table_name)
        self.create_several_new_records(table_name=table_name,
                                        columns=columns,
                                        values=values)

        self.commit_to_db()

    def get_num_of_records_in_table(self, table_name):
        Logger.info("Getting the number of records in the table " + table_name)
        self.get_count_of_records(table_name)

        for row in self.get_cursor():
            return row[0]

    def get_last_ten_ids_of_copied_records(self):
        Logger.info("Getting last 10 ids of the copied records")
        ids = self.retrieve_limited_records_num(field_names=DataBase.ID_COLUMN,
                                                table_name=DataBase.TEST[DataBase.TABLE_NAME_FIELD],
                                                order_by=DataBase.ID_COLUMN,
                                                limit=str(DataBase.NUM_OF_RECORDS_TO_COPY),
                                                ordered=DataBase.DESC_ORDER)

        Logger.info("Converting ids - a list of tuples to a list of strings")
        ids_list = ConvertUtils.convert_list_of_tuples_to_list_of_strs(ids)

        return ids_list

    @staticmethod
    def check_if_tests_completed(tests_results: list):
        Logger.info("Checking if the simulated tests have completed")
        flag = True
        for elem in tests_results:
            if not int(elem[DataBase.TEST_COLUMNS_LIST[1]]) <= DataBase.MAX_VALUE_STAT_ID:
                flag = False
                break
        return flag

    def update_copied_record_in_test_table(self, selected_id: str, simulated_test_result: str):
        Logger.info("Updating one copied record with id " + selected_id + " in Test table")
        test_columns = DataBase.TEST_COLUMNS_LIST
        values = simulated_test_result

        data = f"{test_columns[0]} = {values[test_columns[0]]}, " \
               f"{test_columns[1]} = {values[test_columns[1]]}, " \
               f"{test_columns[2]} = {values[test_columns[2]]}, " \
               f"{test_columns[3]} = {values[test_columns[3]]}, " \
               f"{test_columns[4]} = {values[test_columns[4]]}, " \
               f"{test_columns[5]} = {values[test_columns[5]]}, " \
               f"{test_columns[6]} = {values[test_columns[6]]}, " \
               f"{test_columns[7]} = {values[test_columns[7]]}, " \
               f"{test_columns[8]} = {values[test_columns[8]]}, " \
               f"{test_columns[9]} = {values[test_columns[9]]} "

        condition = f"{DataBase.ID_COLUMN} = {selected_id}"

        self.update_table(table_name=DataBase.TEST[DataBase.TABLE_NAME_FIELD],
                          data=data,
                          condition=condition)

        self.commit_to_db()
        count = self.count_affected_rows()

        return count

    def update_copied_records_in_test_table(self, tests_results: list):
        Logger.info("Updating all the copied records in the test table")
        all_ids = self.get_last_ten_ids_of_copied_records()

        updated_nums_of_records = []

        for test_result in tests_results:
            selected_id = self.return_and_remove_id_from_id_list(all_ids)
            updated_records_num = self.update_copied_record_in_test_table(selected_id=selected_id,
                                                                          simulated_test_result=test_result)
            updated_nums_of_records.append(updated_records_num)

        return updated_nums_of_records

    @staticmethod
    def return_and_remove_id_from_id_list(ids: list):
        Logger.info("Returning and removing ID from the list of ids")
        current_id = ids[0]
        ids.remove(ids[0])
        return current_id

    @staticmethod
    def check_if_records_have_been_updated(result: list):
        Logger.info("Checking if the records have been updated")
        check = all(map(lambda x: True if x < DataBase.MAX_VALUE_STAT_ID else False, result))
        return check

    def delete_ten_copied_records(self):
        Logger.info("Deleting the 10 copied records from Test table")
        ids = self.get_last_ten_ids_of_copied_records()

        for i in range(DataBase.NUM_OF_RECORDS_TO_COPY):
            current_id = self.return_and_remove_id_from_id_list(ids)
            condition = f"{DataBase.ID_COLUMN} = {current_id}"

            self.delete_record(table_name=DataBase.TEST[DataBase.TABLE_NAME_FIELD],
                               condition=condition)

            self.commit_to_db()
