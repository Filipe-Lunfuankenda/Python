import phonenumbers
from phonenumbers import geocoder

phone_number1 = phonenumbers.parse("+244938258038")
phone_number2 = phonenumbers.parse("+33 6 05 90 44 22")

print(geocoder.description_for_number(phone_number1, "pt"))
print(geocoder.description_for_number(phone_number2, "pt"))