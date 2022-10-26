class DataBase(object):
    USER = ""
    PASSWORD = ""
    DATABASE = ""
    HOST = ""
    TEST_NAME = "test_api.py"

    TABLE_NAME_FIELD = "table_name"
    COLUMNS_FIELD = "columns"
    VALUES_FIELD = "values"

    ID_COLUMN = "id"
    NAME_COLUMN = "name"
    SESSION_KEY_COLUMN = "session_key"

    DESC_ORDER = "desc"
    ASC_ORDER = "asc"

    RANDOM_STR_LENGTH = 10
    MIN_VALUE_INT = 1
    MAX_VALUE_STAT_ID = 2
    MAX_VALUE = 10

    TEST_RESULT_OUTCOME = "outcome"
    TEST_RESULT_NODEID = "nodeid"
    TEST_RESULT_LOCATION = "location"

    NOT_GIVEN = "'not_given'"

    VALID_TEST_RESULT = ["passed", "failed"]

    AUTHOR = {TABLE_NAME_FIELD: "author",
              COLUMNS_FIELD: "name, login, email",
              VALUES_FIELD: "'Olga T', 'olga_t', 't.olga@gmail.com'",
              "author_name": "'Olga T'"}
    PROJECT = {TABLE_NAME_FIELD: "project",
               COLUMNS_FIELD: "name",
               VALUES_FIELD: "'TypicodeAPI'"}
    DEV_INFO = {TABLE_NAME_FIELD: "dev_info",
                COLUMNS_FIELD: "dev_time, test_id",
                VALUES_FIELD: "1, 3"}
    SESSION = {TABLE_NAME_FIELD: "session",
               COLUMNS_FIELD: "session_key, created_time, build_number",
               VALUES_FIELD: "12345, '2022-07-28 19:00:00', 1",
               "session_key": "12345"}
    STATUS = {TABLE_NAME_FIELD: "status",
              COLUMNS_FIELD: "name"}

    TEST = {"table_name": "test",
            COLUMNS_FIELD: "name, status_id, method_name, project_id, session_id, start_time, end_time, env, browser, author_id"}

    TEST_COLUMNS_LIST = ["name", "status_id", "method_name", "project_id", "session_id", "start_time", "end_time",
                         "env", "browser", "author_id"]

    NUM_OF_RECORDS_TO_COPY = 10

    START_DATE_TIME = "2016-07-25 15:02:46"
    END_DATE_TIME = "2022-08-23 12:02:46"
