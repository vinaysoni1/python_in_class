U=int(input("enter units: "))
if U<=50:
    bill=U*0.50
    print("bill is :" + str(bill))
elif U<=150:
    bill=U*0.75
    print("bill is :" + str(bill))
elif U<=250:
    bill=U*1.20
    print("bill is :" + str(bill))
else:
    bill=U*1.50
    print("bill is :" + str(bill))
surcharge=bill*0.20
total_bill=bill+surcharge
print("total bill is :" + str(total_bill))