import os
import time
def find_winner(bidder_details):
    highest_bid=0
    winner=""
    
    for bidder in bidder_details:
        bidder_price=bidder_details[bidder]
        if bidder_price>highest_bid:
            highest_bid=bidder_price
            winner=bidder
    print(f"Here is the all list of bidder: {bidder_details}")
    print(f"The winner is {winner} with a bid price of {highest_bid} ")

bidder_data={}
end_of_bidding=False
while not end_of_bidding:
    name=input("Whwt is your name :")
    price=int(input("What is your bid ? "))
    bidder_data[name]=price
    more_bidders=input("Are ther more bidder 'yes'or 'no' : ").lower()
    if more_bidders=='no':
        end_of_bidding=True
        find_winner(bidder_data)
    elif more_bidders=='yes':
        os.system('cls')
        
time.sleep(20)
os.system('cls')


