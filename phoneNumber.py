import phonenumbers
from phonenumbers import geocoder, carrier

number = input("Enter phone number with country code (e.g. +254712345678): ")

try:
    phone = phonenumbers.parse(number, None)

    if phonenumbers.is_valid_number(phone):
        location = geocoder.description_for_number(phone, "en")
        network = carrier.name_for_number(phone, "en")

        print("\nPhone number information")
        print("------------------------")
        print("Country/Region:", location)
        print("Carrier:", network)
        print("Valid number: Yes")
    else:
        print("The number is not valid.")

except phonenumbers.NumberParseException:
    print("Could not understand the phone number.")