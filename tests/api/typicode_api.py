from framework.utils.api.general_api import GeneralAPI
from framework.utils.logger import Logger
from framework.utils.random_util import RandomUtils
from tests.models.post import Post
from tests.models.user import User
from tests.config.urls import Urls
from tests.config.test_data import TestData


class TypicodeAPI(GeneralAPI):
    def __init__(self):
        super().__init__(base_url=Urls.TEST_STAND_URL)

    def get_all_posts(self):
        Logger.info("Getting all posts")
        response = self.send_get_request(Urls.ALL_POSTS_PATH)
        posts = [Post(**post) for post in response.json()]
        return posts

    def get_post_by_id(self, post_id: int):
        Logger.info("Getting a specific post by id " + str(post_id))
        response = self.send_get_request(Urls.SPECIFIC_POST_PATH.format(id=post_id))
        return Post(**response.json())

    def get_post_with_invalid_id(self, post_id: int):
        Logger.info("Sending a GET request with a non-existing id " + str(post_id))
        response = self.send_get_request(Urls.SPECIFIC_POST_PATH.format(id=post_id))
        return Post(**response.json())

    @staticmethod
    def generate_data_for_post_request():
        Logger.info("Generating data for a post request")
        title_length = RandomUtils.generate_random_int(TestData.TITLE_LENGTH_LIMITS[0], TestData.TITLE_LENGTH_LIMITS[1])
        body_length = RandomUtils.generate_random_int(TestData.BODY_LENGTH_LIMITS[0], TestData.BODY_LENGTH_LIMITS[1])
        data = {"title": RandomUtils.generate_random_letters_and_digits_str(title_length),
                "body": RandomUtils.generate_random_letters_and_digits_str(body_length),
                "userId": TestData.USER_ID_FOR_POST_REQUEST}
        return data

    def create_new_post(self, data):
        Logger.info("Sending a POST request with a random body, title and a user id " +
                    str(TestData.USER_ID_FOR_POST_REQUEST))
        response = self.send_post_request(Urls.ALL_POSTS_PATH, data)
        return Post(**response.json())

    def get_all_users(self):
        Logger.info("Getting all users")
        response = self.send_get_request(Urls.ALL_USERS_PATH)
        users = [User(**user) for user in response.json()]
        return users

    def get_user_by_id(self, user_id: int):
        Logger.info("Getting a specific user by id " + str(user_id))
        response = self.send_get_request(Urls.SPECIFIC_USER_PATH.format(id=user_id))
        return User(**response.json())

    def check_if_json_format(self):
        Logger.info("Checking if the format is JSON")
        return 'application/json' in self.get_header_by_key("content-type")

    @staticmethod
    def get_post_from_all_posts_by_its_field(all_posts: list, field: str, variable):
        Logger.info("Getting one post from the list of posts be its field " + str(variable))
        return list(filter(lambda x: variable == x.get_field_data(field), all_posts))[0]

    @staticmethod
    def check_if_posts_in_ascending_order(all_posts: list):
        Logger.info("Checking if all posts are sorted in ascending order")
        flag = True
        for i in range(len(all_posts)-1):
            if all_posts[i] > all_posts[i+1]:
                flag = False
                break
        return flag
