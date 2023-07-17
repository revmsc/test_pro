amount = int(input("Enter Your amount:"))
if amount >= 20000:
    interest = amount*15/100
    print("Your interest amount is" + " " +str(interest))
elif amount >= 7000:
    interest=amount*7/100
    print("Your interest amount is" + " " + str(interest))
elif amount>=5000:
    interest = amount * 5 / 100
    print("Your interest amount is" + " " + str(interest))
else:
    print("Insufficient amount")
print("Thanks for choosing our Bank")
