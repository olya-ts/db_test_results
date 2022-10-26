from framework.utils.logger import Logger


class BaseModel(object):
    def __init__(self, **kwargs):
        for key in kwargs:
            setattr(self, key, kwargs[key])

    def get_field_data(self, field):
        Logger.info("Getting value from the field " + field + " of the " + self.__class__.__name__)
        return getattr(self, field)

    def get_all_variables(self):
        Logger.info("Getting all variables of the instance of " + self.__class__.__name__)
        return self.__dict__

    def check_if_field_data_exists(self, field):
        Logger.info("Checking if the variable " + field + " has been created" + " in the " + self.__class__.__name__)
        try:
            return True if self.get_field_data(field) else False
        except AttributeError:
            Logger.error("Variable " + field + " doesn't exist in the instance of " + self.__class__.__name__)
            return False

    def check_if_instance_has_no_variables(self):
        Logger.info("Checking if the instance of " + self.__class__.__name__ + " has variables")
        return len(self.__dict__) == 0
