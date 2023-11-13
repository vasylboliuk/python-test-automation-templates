import random
import string


class Faker:

    _default_number_length = 10

    @staticmethod
    def get_random_string_len(length):
        letters = string.ascii_lowercase
        return ''.join(random.choice(letters) for i in range(length))

    @staticmethod
    def get_random_string():
        return Faker.get_random_string_len(Faker._default_number_length)