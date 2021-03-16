SERVICE_CHARGE = 2
TICKET_PRICE = 10

tickets_remaining = 100  

def calculate_price(tickets_required):
    return (tickets_required * TICKET_PRICE) + SERVICE_CHARGE
    
while tickets_remaining > 0:
    print("\nThe remaining number of tickets is {}".format(tickets_remaining))
    name = input("What is your name?  ")
    try:
        tickets_required = int(input("Hi {},\nHow many tickets would you like to purchase?  ".format(name)))
        if tickets_required <= 0:
            raise ValueError("You've requested an invalid number of tickets.  Please enter a number of tickets that is greater than zero.")
        if tickets_required > tickets_remaining:
            raise ValueError("You've requested more tickets than are available.  There are only {} tickets remaining.".format(tickets_remaining))
    except ValueError as err:
        print("Invalid entry. {}.  Please try again".format(err))
    else:
        total_price = calculate_price(tickets_required)
        print("The total price of {} tickets is £{}".format(tickets_required, total_price))
        proceed = input("Would you like to proceed with your purchase?  Y/N:  ")
        if proceed.lower() == 'y':
        # TODO: Gather credit card information and process it.
            print("SOLD!")    
            tickets_remaining -= tickets_required
        else: 
            print("Thank you anyways {}".format(name))

print("\nSorry, the tickets are now sold out :(")