"""Calculator Class"""
from app.calculations import Subtraction, Multiplication, Addition, Division


class Calculator:
    """Calculator using static methods"""

    @staticmethod
    def add(val1, val2):
        return Addition.create(val1, val2).get_result()
        """This is method-chaining
        you instantiate with val1 and val2, and once that is complete
        it takes the object and uses the get result to send back
        the result"""
    @staticmethod
    def subtract(val1, val2):
        return Subtraction.create(val1, val2).get_result()

    @staticmethod
    def multiply(val1, val2):
        return Multiplication.create(val1, val2).get_result()

    @staticmethod
    def divide(val1, val2):
        return Division.create(val1, val2).get_result()
