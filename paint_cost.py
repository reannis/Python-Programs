#job estimator
import math

def _gallons(square_feet, feet_gallon):
    return math.ceil(square_feet / feet_gallon)

def _hours(gallons, hours_gallon):
    return gallons * hours_gallon

def sales_tax(state):
    state = state.upper()

#sales tax 
    if state == "CT":
        return 0.06
    elif state == "MA":
        return 0.0625
    elif state == "ME":
        return 0.085
    elif state == "NH":
        return 0.0
    elif state == "RI":
        return 0.07
    elif state == "VT":
        return 0.06
    else:
        return 0.0


def estimate():
    print("Paint Job Estimator\n")

    #inputs
    square_feet = float(input("square feet to be painted: "))
    price_gallon = float(input("price per gallon: "))
    feet_gallon = float(input("square feet per gallon: "))
    hours_gallon = float(input("labor hours per gallon: "))
    hour_rate = float(input("labor rate: "))
    state = input("state (2 letter post code): ")
    last_name = input("customer's last name: ")

    #calculations
    gallons = _gallons(square_feet, feet_gallon)
    paint = gallons * price_gallon
    labor_hours = _hours(gallons, hours_gallon)
    labor = labor_hours * hour_rate

    tax_r = sales_tax(state)
    s_tax = paint * tax_r

    total = paint + labor + s_tax

    #results
    print("\n--- Paint Job Estimate ---")
    print("Gallons needed:", gallons)
    print("Paint cost: $", format(paint, ".2f"))
    print("Labor hours:", labor_hours)
    print("Labor cost: $", format(labor, ".2f"))
    print("Sales tax: $", format(s_tax, ".2f"))
    print("Total cost: $", format(total, ".2f"))

    #write to file
    filename = last_name + "_output.txt"
    file = open(filename, "w")

    file.write("Paint Job Estimate\n")
    file.write("------------\n")
    file.write("Gallons needed: " + str(gallons) + "\n")
    file.write("Paint cost: $" + format(paint, ".2f") + "\n")
    file.write("Labor hours: " + str(labor_hours) + "\n")
    file.write("Labor cost: $" + format(labor, ".2f") + "\n")
    file.write("Sales tax: $" + format(s_tax, ".2f") + "\n")
    file.write("Total cost: $" + format(total, ".2f") + "\n")

    file.close()
    print("\noutput saved to", filename)


estimate()
