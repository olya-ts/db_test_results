from framework.utils.logger import Logger
from framework.models.base_model import BaseModel


class Post(BaseModel):
    def __lt__(self, other):
        Logger.info("Checking if the instance's variable 'id' is lower than the other instance's variable 'id'")
        return self.get_field_data("id") < other.get_field_data("id")
