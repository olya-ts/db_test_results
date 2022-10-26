from framework.utils.logger import Logger


class ConvertUtils:
    @staticmethod
    def convert_list_of_ints_to_list_of_strs(ints_list: list):
        Logger.info("Converting a list of integers to a list of strings")
        return list(map(lambda x: str(x), ints_list))

    @staticmethod
    def convert_list_of_strs_to_list_of_ints(strs_list: list):
        Logger.info("Converting a list of strings to a list of integers")
        return list(map(lambda x: int(x), strs_list))

    @staticmethod
    def convert_list_of_ints_to_str(ints_list: list):
        Logger.info("Converting a list of integers to a string")
        str_list = ConvertUtils.convert_list_of_ints_to_list_of_strs(ints_list)
        return ", ".join(str_list)

    @staticmethod
    def convert_list_of_str_to_str(strs_list: list):
        Logger.info("Converting a list of strings to a string")
        return ", ".join(strs_list)

    @staticmethod
    def convert_list_of_tuples_to_list_of_lists(tuples_list: list):
        Logger.info("Converting a list of tuples to a list of lists")
        return list(map(lambda x: list(x), tuples_list))

    @staticmethod
    def convert_list_of_tuples_to_list_of_strs(tuples_list: list):
        Logger.info("Converting a list of tuples to a list of strings")
        new_list = []
        for elem in tuples_list:
            new_list.append(str(elem[0]))
        return new_list

    @staticmethod
    def convert_list_of_dif_types_to_list_of_str(given_list: list):
        Logger.info("Converting a list of different data types to a string")
        new_list = list(map(lambda x: str(x) if not isinstance(x, str) else x, given_list))
        return new_list
