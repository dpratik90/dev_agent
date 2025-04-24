import phone_formatter from phone_formatter

try:
    phone_formatter = PhoneFormatter()
except Exception as e:
    print(f'Error occurred while initializing PhoneFormatter: {e}')