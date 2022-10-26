from framework.utils.logger import Logger
from framework.utils.convert_util import ConvertUtils


class FilterUtils:
    @staticmethod
    def check_if_digits_in_int_equal(num: int):
        Logger.info("Checking if a number consists of identical digits")
        num = str(num)
        for i in range(len(num) - 1):
            if num[i] != num[i + 1]:
                return False
        return True

    @staticmethod
    def filter_list_of_ints_with_more_than_two_digits(ints_list: list):
        Logger.info("Filtering a list of integers, keeping only those integers that have more than 2 digits")
        str_list = ConvertUtils.convert_list_of_ints_to_list_of_strs(ints_list)
        result = list(filter(lambda x: len(x) > 1, str_list))
        return ConvertUtils.convert_list_of_strs_to_list_of_ints(result)

    @staticmethod
    def filter_list_of_ints_with_repeating_digits(int_list: list):
        Logger.info("Filtering a list of integers, keeping only those integers that have repeating digits")
        int_list_with_more_digits = FilterUtils.filter_list_of_ints_with_more_than_two_digits(int_list)
        return list(filter(lambda x: FilterUtils.check_if_digits_in_int_equal(x), int_list_with_more_digits))
