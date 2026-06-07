import random

class rail:
    def __init__(self,train_no):
        self.train_no=train_no
    def book(self):
        print(f"Your ticket is booked in train number {train_no}")
    def cancel(self):
        print("Do you want to cancel your ticket?")
        choice = input("Enter 'yes' to cancel or 'no' to keep the ticket: ")
        if choice.lower() == 'yes':
            print("Your ticket has been cancelled.")
        else:
            print("Your ticket is still booked.")
    def status(self):
        status = random.choice(["On Time", "Delayed", "Cancelled"])
        print(f"Train number {train_no} is currently: {status}")
    def fare(self):
        fare = random.randint(100, 500)
        print(f"The fare for train number {train_no} is: {fare} INR")

train_no = input("Enter the train number you want to book: ")
my_ticket = rail(train_no)
my_ticket.book()
my_ticket.status()
my_ticket.fare()
my_ticket.cancel()


    