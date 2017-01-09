#--------|---------|---------|---------|---------|---------|---------|---------
# Python Dictionaries

## Instructions

# A block of publicly traded stock has a variety of attributes, we'll look at a few of them. A stock has a ticker symbol and a company name. Create a simple dictionary with ticker symbols and company names.

##### Example

stockDict = { 'GM': 'General Motors', 'CAT':'Caterpillar', 'EK':"Eastman Kodak", 'TSLA':"Tesla", 'GE': "General Electric" }

# Create a simple list of blocks of stock. These could be tuples with ticker symbols, number of shares, dates and price.

##### Example

purchases = [ ( 'GE', 100, '10-sep-2001', 48 ), ( 'CAT', 100, '1-apr-1999', 24 ), ( 'GE', 200, '1-jul-1998', 56 ), ('TSLA', 20, '1-may-2016', 246), ('EK', 1000, '1-dec-2009', 1) ]

# Create a purchase history report that computes the full purchase price (shares times dollars) for each block of stock and uses the `stockDict` to look up the full company name. This is the basic relational database join algorithm between two tables.

print('Stock Purchase History Report')
for purchase in purchases:
    print('Purchased ${3} of {1}({0}) on {2}'.format(purchase[0], stockDict.get(purchase[0]), purchase[2], purchase[1]*purchase[3]))

print('Total Stocks Purchased')
stock_block = set()
for purchase in purchases:
    stock_block.add(purchase[0])
print(stock_block)
stocks = dict()
for ticker in stock_block:
    stocks[ticker] = 0
    for purchase in purchases:
        if ticker == purchase[0]:
            stocks[ticker] = stocks[ticker] + purchase[1]*purchase[3]
print(stocks)

# def purchase_history_report(purchase_array, stock_dict=stockDict):

#     '''Print a summary of stock purchases from a list.

#     Keyword arguments:
#     purchase_array -- a list of tuples with format ( 'ticker_symbol', number_of_shares, 'date_of_purchase', price_per_share)
#     stock_dict -- a dictionary of company ticker symbols

#     Returns: a four-line printout of purchases

#     '''

#     print('Stock Purchase History')
#     for purchase in purchase_array:
#             number = purchase[1]
#             amount = purchase[3]
#             total = number * amount
#             print('\n{0}: {1}'.format(purchase[0], stockDict[purchase[0]]))
#             print('Date Purchased: {0}'.format(purchase[2]))
#             print('Amount Purchased: {0} at ${1}'.format(number, amount))
#             print('Total price: ${0}'.format(total))

# purchase_history_report(purchases)

# # Create a second purchase summary which accumulates total investment by ticker symbol. In the above sample data, there are two blocks of GE. These can easily be combined by creating a dict where the key is the ticker and the value is the list of blocks purchased. The program makes one pass through the data to create the dict. A pass through the dict can then create a report showing each ticker symbol and all blocks of stock.

# def purchase_summary(purchase_array, stock_dict=stockDict):

#     '''Print a summary of stock purchases from a list, with totals for each company.

#     Keyword arguments:
#     purchase_array -- a list of tuples with format ( 'ticker_symbol', number_of_shares, 'date_of_purchase', price_per_share)
#     stock_dict -- a dictionary of company ticker symbols

#     Returns: a four-line printout of total purchases

#     '''

#     print('Stock Purchases')
#     total_purchase = []
#     for purchase in purchase_array:
#         for item in total_purchase:
#             if purchase[0]
#             total_purchase.append(purchase)

# loop through the purchases:
# if the purchase ticker matches an existing ticker of the new array, add the purchase amount and price_per_share