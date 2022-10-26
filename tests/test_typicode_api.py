from framework.utils.logger import Logger
from framework.constants import status_codes
from tests.api.typicode_api import TypicodeAPI
from tests.config.test_data import TestData


class TestPostsAndUsers:
    def test_posts_and_users_with_get_and_post_requests(self):
        Logger.step("Step 1. Sending GET request to get all posts")
        typicode_api = TypicodeAPI()
        all_posts = typicode_api.get_all_posts()
        assert typicode_api.check_status_code() is True, f"Status code isn't {status_codes.STATUS_200_OK}"
        assert typicode_api.check_if_json_format() is True, "The list in response body isn't JSON"
        assert typicode_api.check_if_posts_in_ascending_order(all_posts) is True, \
            "Posts aren't in ascending order by their id"

        Logger.step("Step 2. Sending GET request to get a post with a specific id")
        specific_post = typicode_api.get_post_by_id(TestData.POST_ID)
        assert typicode_api.check_status_code() is True, f"Status code isn't {status_codes.STATUS_200_OK}"
        assert specific_post.get_field_data(TestData.POST_FIELD_USER_ID) == TestData.POST_DATA_USER_ID, \
            f"User id isn't {TestData.POST_DATA_USER_ID}"
        assert specific_post.get_field_data(TestData.POST_FIELD_ID) == TestData.POST_ID, \
            f"Post id isn't {TestData.POST_ID}"
        assert specific_post.check_if_field_data_exists(TestData.POST_FIELD_TITLE) is True, "Title is empty"
        assert specific_post.check_if_field_data_exists(TestData.POST_FIELD_BODY) is True, "Body is empty"

        Logger.step("Step 3. Sending GET request to get a post with an invalid id")
        invalid_post = typicode_api.get_post_with_invalid_id(TestData.INVALID_POST_ID)
        assert typicode_api.check_status_code(expected_status_code=status_codes.STATUS_404_NOT_FOUND) is True, \
            f"Status code isn't {status_codes.STATUS_404_NOT_FOUND}"
        assert invalid_post.check_if_instance_has_no_variables() is True, "Response body is not empty"

        Logger.step("Step 4. Sending POST request to create a post with a specific user id and a random body and title")
        data = typicode_api.generate_data_for_post_request()
        new_post = typicode_api.create_new_post(data)
        assert typicode_api.check_status_code(expected_status_code=status_codes.STATUS_201_CREATED) is True, \
            f"Status code isn't {status_codes.STATUS_201_CREATED}"
        assert new_post.get_field_data(TestData.POST_FIELD_USER_ID) == str(TestData.USER_ID_FOR_POST_REQUEST), \
            f"User id isn't {TestData.USER_ID_FOR_POST_REQUEST}"
        assert new_post.get_field_data(TestData.POST_FIELD_TITLE) == data[TestData.POST_FIELD_TITLE], \
            "Titles aren't identical"
        assert new_post.get_field_data(TestData.POST_FIELD_BODY) == data[TestData.POST_FIELD_BODY], \
            "Bodies aren't identical"
        assert new_post.check_if_field_data_exists(TestData.POST_FIELD_ID) is True, "Id hasn't been created"

        Logger.step("Step 5. Sending GET request to get all users")
        all_users = typicode_api.get_all_users()
        assert typicode_api.check_status_code() is True, f"Status code isn't {status_codes.STATUS_200_OK}"
        assert typicode_api.check_if_json_format() is True, "The list in response body isn't JSON"
        one_user_from_all_users = typicode_api.get_post_from_all_posts_by_its_field(all_users,
                                                                                    TestData.USER_FIELD_ID,
                                                                                    TestData.USER_ID)
        assert one_user_from_all_users == TestData.USER_DATA, "User data sets aren't identical"

        Logger.step("Step 6. Sending GET request to get a user with a specific id")
        specific_user = typicode_api.get_user_by_id(TestData.SPECIFIC_USER_ID)
        assert typicode_api.check_status_code() is True, f"Status code isn't {status_codes.STATUS_200_OK}"
        assert specific_user.get_all_variables() == one_user_from_all_users.get_all_variables(), \
            "User data set from this step and user data step from step 5 aren't identical"
