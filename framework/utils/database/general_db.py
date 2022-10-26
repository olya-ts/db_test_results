from mysql.connector import connect, Error
from mysql.connector import errorcode

from framework.utils.logger import Logger


class GeneralDataBase:
    @staticmethod
    def establish_db_connection(user: str, password: str, host: str, database: str):
        try:
            Logger.info("Connecting to a MySQL database")
            connection = connect(user=user, password=password, host=host, database=database)
            setattr(GeneralDataBase, "connection", connection)
        except Error as err:
            if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                Logger.error("Connection to the DB has failed. Either user name or password are incorrect")
            elif err.errno == errorcode.ER_BAD_DB_ERROR:
                Logger.error("Connection to the DB has failed. DB doesn't exist")
            else:
                Logger.error(err)

    @staticmethod
    def create_cursor():
        Logger.info("Creating the DB cursor")
        cursor = GeneralDataBase.get_connection().cursor()
        setattr(GeneralDataBase, "cursor", cursor)

    @staticmethod
    def get_connection():
        Logger.info("Getting the established connection")
        connection = getattr(GeneralDataBase, "connection")
        return connection

    @staticmethod
    def get_cursor():
        Logger.info("Getting the created cursor")
        cursor = getattr(GeneralDataBase, "cursor")
        return cursor

    @staticmethod
    def close_db_connection():
        Logger.info("Closing the DB connection")
        GeneralDataBase.get_connection().close()

    def commit_to_db(self):
        Logger.info("Committing to a database")
        self.get_connection().commit()

    def execute_cursor(self, operation: str, params=()):
        Logger.info("Executing the DB cursor")
        self.get_cursor().execute(operation, params)

    @staticmethod
    def close_cursor():
        Logger.info("Closing the DB cursor")
        GeneralDataBase.get_cursor().close()

    def fetch_all_records(self):
        Logger.info("Fetching all records")
        return self.get_cursor().fetchall()

    def create_new_record(self, data: dict):
        Logger.info("Creating a new record in the table " + data["table_name"])
        query = ("INSERT INTO {table_name} "
                 "({columns}) "
                 "VALUES ({values});".format(table_name=data["table_name"],
                                             columns=data["columns"],
                                             values=data["values"]))
        self.execute_cursor(query)

    def create_several_new_records(self, table_name, columns, values):
        Logger.info("Creating new record in the table " + table_name)
        query = ("INSERT INTO {table_name} "
                 "({columns}) "
                 "VALUES {values};".format(table_name=table_name,
                                           columns=columns,
                                           values=values))
        self.execute_cursor(query)

    def retrieve_records_from_table(self, field_names: str, table_name: str, condition: str = None):
        Logger.info("Retrieving records from the table " + table_name)
        if not condition:
            query = ("SELECT {field_names} FROM {table_name};".format(field_names=field_names, table_name=table_name))
        else:
            query = ("SELECT {field_names} FROM {table_name} WHERE {condition};".format(field_names=field_names,
                                                                                        table_name=table_name,
                                                                                        condition=condition))
        self.execute_cursor(query)
        return self.fetch_all_records()

    def retrieve_limited_records_num(self, field_names: str, table_name: str, order_by: str, limit: str,
                                     ordered: str = "asc"):
        Logger.info("Retrieving a limited number of records from the table " + table_name)
        if ordered == "asc":
            query = f"SELECT {field_names} FROM {table_name} ORDER BY {order_by} ASC LIMIT {limit};"
        else:
            query = f"SELECT {field_names} FROM {table_name} ORDER BY {order_by} DESC LIMIT {limit};"

        self.execute_cursor(query)
        return self.fetch_all_records()

    def update_table(self, table_name: str, data: str, condition: str = None):
        Logger.info("Updating records in the table " + table_name)
        if not condition:
            query = f"UPDATE {table_name} SET {data};"
        else:
            query = f"UPDATE {table_name} SET {data} WHERE {condition};"

        self.execute_cursor(query)

    def delete_record(self, table_name: str, condition: str):
        Logger.info("Deleting records from the table " + table_name)
        query = f"DELETE FROM {table_name} WHERE {condition};"

        self.execute_cursor(query)

    def count_affected_rows(self):
        Logger.info("Counting the number of affected by the query rows")
        return self.get_cursor().rowcount

    def get_count_of_records(self, table_name):
        Logger.info("Getting the count of records in the table " + table_name)
        self.execute_cursor(f"SELECT COUNT(*) FROM {table_name};")
