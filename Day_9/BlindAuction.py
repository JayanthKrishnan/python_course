def find_highest_bid(bid_records):
    highest_bid = 0
    bidder_name = ""
    for bidder in bid_records:
        bid_amount = bid_records[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            bidder_name = bidder
    print(f"The highest bidder is {bidder_name} with a bid of ${highest_bid}")


bids = {}
bidding_finished = False
while not bidding_finished:
    name = input("Enter your name? : ")
    bid = int(input("Enter your bid : $"))
    bids[name] = bid
    biddingContinue = input("If there is any other bidder type 'Yes' or 'No' : \n").lower()
    if biddingContinue == 'no':
        bidding_finished = True
    elif biddingContinue == 'yes':
        print('\n'*20)
find_highest_bid(bids)
