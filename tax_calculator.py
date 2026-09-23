# This program calculates the tax based on the annual income provided by the user.

income = float(input("Enter the annual income: "))

if income < 85528:
  tax= income * 0.18-556.02 # Calculate tax for income below the threshold

else:
  tax = (income -85528)* 0.32 + 14839.02 # Calculate tax for income above the threshold

if tax <0.0: # Ensure that tax is not negative
  tax =0.0

tax = round(tax, 0) # Round the tax to the nearest whole number
print("The tax is: ", tax, "thalers")