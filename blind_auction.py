from auction_art import logo
print(logo)
import os

def clear():
    # Clears the console screen based on the operating system
    os.system('cls' if os.name == 'nt' else 'clear')

auction_bids = {}
auction_ongoing = True

def identify_top_bidder(bid_data):
    max_bid = 0
    top_bidder = ""
    for participant in bid_data:
        current_bid = bid_data[participant]
        if current_bid > max_bid:
            max_bid = current_bid
            top_bidder = participant
    print(f"The top bidder is {top_bidder} with a bid of ${max_bid}")

while auction_ongoing:
    bidder_name = input("Enter your name: ")
    bid_value = int(input("Enter your bid: $"))
    auction_bids[bidder_name] = bid_value

    more_bidders = input("Are there more bidders? Type 'yes' or 'no':\n")
    if more_bidders.lower() == 'no':
        auction_ongoing = False
        identify_top_bidder(auction_bids)
    elif more_bidders.lower() == 'yes':
        clear() 
