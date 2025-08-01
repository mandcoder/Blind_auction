

import os

# 🔹 Clear the terminal screen (Mac/Linux only)
def clear_screen():
    os.system('clear')

# 🔹 Force user to only respond with 'y' or 'n'
def get_yes_or_no(prompt):
    while True:
        answer = input(prompt).lower()
        if answer in ["y", "n"]:
            return answer    # ✅ return 'y' or 'n'
        else:
            print("Please type only 'y' or 'n'.")

# 🔹 Make sure the bid is a whole number
def get_valid_bid(prompt):
    while True:
        bid_input = input(prompt)
        if bid_input.isdigit():
            return int(bid_input)   # ✅ ensures only whole numbers
        else:
            print("❌ Please enter whole numbers only (no decimals).")

# 🔹 Find and print the highest bidder and their bid
def get_auction_winner(auction_bids):
    top_offer = 0
    leader_name = ""

    for participant in auction_bids:
        offer = auction_bids[participant]
        if offer > top_offer:
            top_offer = offer
            leader_name = participant
           
    print(f"Winner is {leader_name} with the bid $ {top_offer}")

# 🔹 Dictionary to store all bids { "Name": amount }
auction_bids = {}

clear_screen()
print("Welcome to the blind auction")

bidding_finished = False

# 🔹 Main loop: collect bids until no more bidders
while not bidding_finished:
    bidder_name = input("What is your name: ")
    bid = get_valid_bid("What is your bid?: $ ")   # ✅ ensures only whole numbers
    auction_bids[bidder_name] = bid

    # ✅ use the new function to force only 'y' or 'n'
    other_bidders = get_yes_or_no("Are there any other bidders? Type 'y' or 'n': ")

    if other_bidders == "y":
        clear_screen()
    if other_bidders == "n":
        bidding_finished = True

# 🔹 Determine and print the winner
get_auction_winner(auction_bids)

