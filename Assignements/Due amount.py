bill_amount=float(input("Enter the bill amount: "))
customer_payment=float(input("Enter the amount customer paid: "))
DueAmount= bill_amount-customer_payment
if DueAmount > 0:
    print("Customer still needs to pay: ",DueAmount)
elif DueAmount == 0:
    print("Full Amount is paid.")    
else:
    print ("Rs.", -DueAmount,"Extra tip has been received.")    