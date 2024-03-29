
from app.operations import addition
from app.operations import subtraction
from app.operations import multiplication
from app.operations import division


class Calculation:  # abstract class
    """Base Calculation Class"""
    result = 0
    val1 = 0
    val2 = 0

    @classmethod
    def create(cls, val1, val2):
        """Factory Method"""
        return cls(val1, val2)

    def __init__(self, val1, val2):
        """This is the base class constructor"""
        self.val1 = val1
        self.val2 = val2

    def set_result(self, result):
        """Get the result of a calculation"""
        self.result = result

    def set_val1(self, val1):
        """Get the result of a calculation"""
        self.val1 = val1

    def set_val2(self, val2):
        """Get the result of a calculation"""
        self.val2 = val2

    def get_val1(self):
        """Get the result of a calculation"""
        return self.val1

    def get_val2(self):
        """Get the result of a calculation"""
        return self.val2

    def get_result(self):
        """Get the result of a calculation"""
        return self.result


class Addition(Calculation):
    """My Addition Calculation Class"""

    def __init__(self, val1, val2):
        """concrete class constructor"""
        super().__init__(val1, val2)
        self.set_result(addition(self.val1, self.val2))


class Subtraction(Calculation):
    """My subtraction Calculation Class"""

    def __init__(self, val1, val2):
        """concrete class constructor"""
        super().__init__(val1, val2)
        self.set_result(subtraction(self.val1, self.val2))


class Multiplication(Calculation):
    """My multiplication Calculation Class"""

    def __init__(self, val1, val2):
        """concrete class constructor"""
        super().__init__(val1, val2)
        self.set_result(multiplication(self.val1, self.val2))


class Division(Calculation):
    """My division Calculation Class"""

    def __init__(self, val1, val2):
        """concrete class constructor"""
        super().__init__(val1, val2)
        self.set_result(division(self.val1, self.val2))
