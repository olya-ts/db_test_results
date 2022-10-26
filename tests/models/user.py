from framework.utils.logger import Logger
from framework.models.base_model import BaseModel


class User(BaseModel):
    def __eq__(self, other: dict):
        Logger.info("Checking if the instance's set of variables equals to the other set of data")
        return self.get_all_variables() == other
