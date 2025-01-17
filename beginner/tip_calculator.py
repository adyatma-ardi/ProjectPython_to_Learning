print("Hello, welcome to Tip Calculator Program")
while True:
    user_input = input("Press Enter to Start")
    if user_input == "":
        break
    else:
        print("Please press only Enter to Start.")


while True:
    try:
        total_bill = int(input("What was the total bill ?"))
        print(f"total bill : ${total_bill}")
        break
    except ValueError:
        print("Error: That is not a valid number. Please try again.")

valid_choices= [10,12,15]

while True:
    try:
        percentage_tip = int(input("How much tip would you like to give ? 10, 12 or 15 ? (Please enter a number (10, 12, or 15))"))
        if percentage_tip in valid_choices:
            print(f"Thank you ! you chose {percentage_tip}% tip")
            break
        else:
            print("Error : Please enter one of the valid choices (10, 12, or 15.)")
    except ValueError:
        print("Error: Invalid input. Please enter a number.")

while True:
    try:
        split_people = int(input("How many people to split the bill ?"))
        print(f"{split_people} peoples")
        break
    except ValueError:
        print("Error: That is not a valid number. Please try again.")


tip = percentage_tip / 100
each_pay = (total_bill * (1 + tip) / split_people)
rounded_each_pay = round(each_pay,2)

print(f"Each person should pay: ${rounded_each_pay}")