try:
    for i in ['a', 'b', 'c']:
        print(i ** 2)

except TypeError:
    print("Looks like you have a type error.")



try:
    x = 5
    y = 0

    z = x / y

except ZeroDivisionError:
    print("Looks like you are trying to divide by zero")

finally:
    print("All done.")



def ask():

    while True:
        try:
            user_input = int(input("Input an integer: "))
            print(f"Thank you, your number squared is: {user_input ** 2}.")

        except ValueError:
            print("An error occurred! Please try again.\n")
            continue

        else:
            break
