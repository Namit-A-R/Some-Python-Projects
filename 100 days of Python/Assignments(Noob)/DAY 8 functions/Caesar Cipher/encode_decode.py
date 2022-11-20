alphabets = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
             'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i']


def encode(your_message, shift_number):

    final_message = []

    for i in range(0, len(your_message)):
        for n in range(0, len(alphabets)):

            if your_message[i] == alphabets[n]:
                final_message.append(alphabets[n + shift_number])
                break

            elif your_message[i] not in alphabets:
                final_message.append(your_message[i])
                break

    print(f"Here is your encoded result: ")
    list_to_string(final_message)


def decode(your_message, shift_number):

    final_message = []

    for i in range(0, len(your_message)):
        for n in range(0, len(alphabets)):

            if your_message[i] == alphabets[n]:
                final_message.append(alphabets[n + shift_number])
                break

            elif your_message[i] not in alphabets:
                final_message.append(your_message[i])
                break

    print(f"Here is your decoded result: ")
    list_to_string(final_message)


def list_to_string(final_message):
    new_final_message = ""
    new_final_message = new_final_message.join(final_message)
    print(new_final_message)
