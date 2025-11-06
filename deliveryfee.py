def delivery_fee():
    distance = float(input("Enter distance in kilometers: "))
    rate = float(input("Enter rate per kilometer(₱): "))
    total = distance * rate
    print("Total Delivery Fee: ₱", total)
    
delivery_fee()
