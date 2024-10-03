# Furniture.py - This program calculates profits and sales prices for a furniture company.

itemName = "TV Stand"                # Name of the item
retailPrice = 325.00                 # Retail price of the item
wholesalePrice = 200.00              # Wholesale price of the item

# Calculate profit, salePrice, and saleProfit
profit = retailPrice - wholesalePrice  # Calculate profit
salePrice = retailPrice * 0.75         # Assuming a 25% discount for sale
saleProfit = salePrice - wholesalePrice  # Calculate sale profit

# Output the results
print("Item Name: " + itemName)                     # Output the item name
print("Retail Price: $" + str(retailPrice))         # Output the retail price
print("Wholesale Price: $" + str(wholesalePrice))   # Output the wholesale price
print("Profit: $" + str(profit))                     # Output the calculated profit
print("Sale Price: $" + str(salePrice))              # Output the calculated sale price
print("Sale Profit: $" + str(saleProfit))            # Output the calculated sale profit
