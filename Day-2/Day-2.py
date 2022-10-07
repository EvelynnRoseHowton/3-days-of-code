print("Welcome to the tip calculator. \n")
bill_total = float(input("What was the total bill? $"))
tip = int(input("What percent tip would you like to give? 10, 12, or 15?"))
split_bill = int(input("How many people split the bill? "))
total = tip / 100 * bill_total + bill_total
print(total)


