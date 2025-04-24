import re

class PhoneFormatter:
    """ 
    This class is used to validate and format phone numbers.
    It will first validate the phone number if it's in the form (123) 456-7890.
    Then it will format the phone number.
    """

    def __init__(self, phone_number):
        """
        Initialize instance with phone number.
        """
        self.__phone_number = phone_number

    def validate(self):
        """
        Validate the number in the form (123) 456-7890.
        """
        if not isinstance(self.__phone_number, str):
            return False
        pattern = re.compile(r"^\(?\d{3}\)?[-.\s]?\d{3}[-.\s]?\d{4}$")
        return pattern.match(self.__phone_number) is not None

    def format(self):
        """
        Format the phone number.
        """
        digits = re.sub(r"[^\d]", "", self.__phone_number)
        return f"({digits[:3]}) {digits[3:6]}-{digits[6:]}"

class PhoneFormatter:
    """ 
    This class is used to validate and format phone numbers.
    It will first validate the phone number if it's in the form (123) 456-7890.
    Then it will format the phone number.
    """

    def __init__(self, phone_number):
        """
        Initialize instance with phone number.
        """
        self.__phone_number = phone_number

    def validate(self):
        """
        Validate the number in the form (123) 456-7890.
        """
        if not isinstance(self.__phone_number, str):
            return False
        pattern = re.compile(r"^\(?\d{3}\)?[-.\s]?\d{3}[-.\s]?\d{4}$")
        return pattern.match(self.__phone_number) is not None

    def format(self):
        """
        Format the phone number.
        """
        digits = re.sub(r"[^\d]", "", self.__phone_number)
        return f"({digits[:3]}) {digits[3:6]}-{digits[6:]}"

class PhoneFormatter:
    """ 
    This class is used to validate and format phone numbers.
    It will first validate the phone number if it's in the form (123) 456-7890.
    Then it will format the phone number.
    """

    def __init__(self, phone_number):
        """
        Initialize instance with phone number.
        """
        self.__phone_number = phone_number

    def validate(self):
        """
        Validate the number in the form (123) 456-7890.
        """
        if not isinstance(self.__phone_number, str):
            return False
        pattern = re.compile(r"^\(?\d{3}\)?[-.\s]?\d{3}[-.\s]?\d{4}$")
        return pattern.match(self.__phone_number) is not None

    def format(self):
        """
        Format the phone number.
        """
        digits = re.sub(r"[^\d]", "", self.__phone_number)
        return f"({digits[:3]}) {digits[3:6]}-{digits[6:]}"

class PhoneFormatter:

def __init__(self, phone_number):
self.phone_number = phone_number

def validate(self):
if not isinstance(self.phone_number, str):
return False
pattern = re.compile(r"^\(?\d{3}\)?[-.\s]?\d{3}[-.\s]?\d{4}$")
return pattern.match(self.phone_number) is not None

def format(self):
digits = re.sub(r"[^\d]", "", self.phone_number)
return f"({digits[:3]}) {digits[3:6]}-{digits[6:]}"