sales = float(input("What are your sales for the year? "))

if sales >= 50000.0:
    QuotaMet = True

else:
    QuotaMet = False

if QuotaMet:
    print("You have met the quota")

else:
    print("You have not met the quota")
