class TestData:
    POST_ID = 99
    POST_DATA_USER_ID = 10
    POST_FIELD_USER_ID = "userId"
    POST_FIELD_ID = "id"
    POST_FIELD_TITLE = "title"
    POST_FIELD_BODY = "body"

    INVALID_POST_ID = 150

    USER_ID_FOR_POST_REQUEST = 1
    BODY_LENGTH_LIMITS = [15, 20]
    TITLE_LENGTH_LIMITS = [10, 15]

    USER_FIELD_ID = "id"
    USER_FIELD_NAME = "name"
    USER_ID = 5
    USER_DATA = {USER_FIELD_ID: USER_ID,
                 "name": "Chelsey Dietrich",
                 "username": "Kamren",
                 "email": "Lucio_Hettinger@annie.ca",
                 "address": {
                    "street": "Skiles Walks",
                    "suite": "Suite 351",
                    "city": "Roscoeview",
                    "zipcode": "33263",
                    "geo": {"lat": "-31.8129",
                            "lng": "62.5342"}
                 },
                 "phone": "(254)954-1289",
                 "website": "demarco.info",
                 "company": {"name": "Keebler LLC",
                             "catchPhrase": "User-centric fault-tolerant solution",
                             "bs": "revolutionize end-to-end systems"}
                 }

    SPECIFIC_USER_ID = 5
