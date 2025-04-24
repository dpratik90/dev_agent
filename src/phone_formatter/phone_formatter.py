import re

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