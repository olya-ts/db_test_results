import random
import string
from datetime import timedelta, datetime
from random import randrange

from framework.utils.logger import Logger


class RandomUtils:
    @staticmethod
    def generate_random_capital_letter():
        Logger.info("Generating a random capital letter")
        return random.choice(string.ascii_uppercase)

    @staticmethod
    def generate_random_digit():
        Logger.info("Generating a random digit")
        return random.choice(string.digits)

    @staticmethod
    def generate_random_int(min_value: int, max_value: int):
        Logger.info("Generating a random int within a range of " + str(min_value) + " and " + str(max_value))
        return random.randint(min_value, max_value)

    @staticmethod
    def generate_random_letters_and_digits_str(length: int):
        Logger.info("Generating a random string")
        return ''.join(random.choices(string.ascii_letters + string.digits, k=length))

    @staticmethod
    def generate_random_credentials(length: int, *args):
        Logger.info("Generating a random credential")
        conditions = ""
        for arg in args:
            conditions += arg

        credential = conditions + RandomUtils.generate_random_letters_and_digits_str(length - len(args))

        credential_list = list(credential)
        random.shuffle(credential_list)

        return ''.join(credential_list)

    @staticmethod
    def select_random_item_from_list(given_list: list):
        Logger.info("Selecting one item from the given list")
        return random.choice(given_list)

    @staticmethod
    def select_random_items_from_list_without_repetition(given_list: list, num: int):
        Logger.info("Selecting one item from the given list")
        return random.sample(given_list, num)

    @staticmethod
    def generate_random_datetime(start: str, end: str, given_format: str):
        Logger.info("Generating a random date and time")
        start = datetime.strptime(start, given_format)
        end = datetime.strptime(end, given_format)
        delta = end - start
        int_delta = (delta.days * 24 * 60 * 60) + delta.seconds
        random_second = randrange(int_delta)
        return start + timedelta(seconds=random_second)
