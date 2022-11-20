import os


def clear():
    return os.system('cls')


def add_new_bidder(name, bid_value):
    new_bidder = {}
    new_bidder["Name"] = name
    new_bidder["bid_value"] = bid_value
    bidders.append(new_bidder)
    
    
logo = '''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
'''


bidders = []
choice = "y"

while choice == "y":
    print(logo)
    name = input("What is your name?: ")
    bid_value = int(input("Enter your bid value: "))
    add_new_bidder(name, bid_value)
    choice = input("Is there any other bidders?(Y,N): ").lower()
    clear()

max_value = 0
max_bidder = ""

for person in bidders:
    if person["bid_value"] > max_value:
        max_bidder = person["Name"]
        max_value = person["bid_value"]

print(logo)   
print(f"\n\n{max_bidder} has won the auction by bidding ${max_value}\n\n")
        
