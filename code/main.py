import phonenumbers as phNum
# Importing all necessary libraries from the phonenumbers module
from phonenumbers import carrier, geocoder, timezone  

# visual pattern
print(" ")
patternRows = 4
for i in range(0, patternRows):

    for j in range(0, i + 1):
        print("*", end=' ')
        
    print(" ")

# user input for phone number
phoneNum = input("* Enter your 10 digit phone number with the country code: ")
numDetails = phNum.parse(phoneNum) 

# calling functions from imported libraries to store phone number details
valid = phNum.is_valid_number(numDetails)
timeZone = timezone.time_zones_for_number(numDetails)
carrierName = carrier.name_for_number(numDetails, "en")
numRegion = geocoder.description_for_number(numDetails, "en")

# printing all extracted data to the console
print("*", numDetails)
print("* The Timezone associated with the phone number is:", timeZone)

# using ANSI escape sequences/codes in order to print the desired text color
if (valid):
    # green text on console
    print("*\033[32m Mobile Number is valid\033[0m")
else:
    # red text on console
    print("*\033[31m Mobile Number is invalid\033[0m")

if (carrierName):
    print("* The carrier is:", carrierName)
else:
    print("*\033[31m Carrier information for this phone number is unavailable\033[0m")

print("* The phone number is registered in the following region:", numRegion)

# visual pattern
for i in range(patternRows + 1, 0, -1):

    for j in range(0, i - 1):
        print("*", end=' ')

    print(" ")