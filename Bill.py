bill_no = 100000100

while True:

    on_off = input("Press Y/N ").upper()

    if on_off == "Y":
        
        tea = water = coffee = bunmaska = 0
        user = input("Do you want order: (Y/N) ").upper()

        if user == "Y":

            tea = int(input("Tea \t 12 \t"))
            coffee = int(input("Coffee \t 15 \t"))
            bunmaska = int(input("Bun Maska \t 25 \t"))
            water = int(input("Water \t 10 \t"))

            # Print the Bill

            bill_no += 1
            print("Bill No: ", bill_no)
            print("---------------------------------")
            
            if tea > 0:
                print("Tea \t 12 \t", (tea * 12))
            if coffee > 0:
                print("Coffee \t 15 \t", (coffee * 15))
            if bunmaska > 0:
                print("Bun Maska \t 25 \t", (bunmaska * 15))
            if water > 0:
                print("Water \t 10 \t", (water * 15))
            
            print("---------------------------------")

            total = (tea * 12) + (coffee * 15) + (bunmaska * 25) + (water * 10)
            print("Total Amount is : \t\t", total)
            
        elif user == 'N':
            print("Switch OFf")
            break
        
        else:
            print("Press Correct Option Please")