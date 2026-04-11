from art import logo
import os

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def highest_bidder(data):
    highest_bid = 0
    user = ""
    for bids in data["bids"]:
        if int(bids["bid"]) > highest_bid:
            highest_bid = int(bids["bid"])
            user = bidders["user"]
    return f"The winner is {user} with bid of {highest_bid}"

bidders = {
    "bids": []
}
run = True
while run:
    print(logo)
    name = input("What's your name?: ")
    bid = input("What's your bid?: ")
    bidder = input("Are there any other bidders? Type 'yes' or 'no'.")
    bidders["bids"].append({"user": name, "bid": bid})
    clear()
    if bidder.lower() == "no":
        run = False
        print(highest_bidder(bidders))