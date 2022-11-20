from encode_decode import encode, decode

continuation = 0

while continuation == 0:

    your_message = input("Type your Message: ").lower()
    your_message = list(your_message)
    shift_number = int(input("Enter your desired shift number(1 - 9): "))

    choice = int(input("Do you want to, \n1. Encode\n2.Decode\nChoose(1,2): "))

    match choice:
        case '1':
            encode(your_message, shift_number)
        case '2':
            decode(your_message, shift_number)

    wish = input("Do you want to continue?(y / n): ").lower()

    if wish == "n":
        print("Good Bye")
        continuation = 1
