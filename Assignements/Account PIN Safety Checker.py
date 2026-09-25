class Account:
    def __init__(self, owner, pin):
        self.owner = owner
        self.pin = pin

    def show_pin_status(self):
        print("Account Owner:", self.owner)
        print("Pin is safe and secure.")

    def set_pin(self, new_pin):
        if len(new_pin) == 4 and new_pin.isdigit():
            self.pin = new_pin
            print("Pin updated successfully.")
        else:
            print("Invalid pin. Pin must be a 4 digit number.")

    def check_pin(self):
        if len(self.pin) == 4 and self.pin.isdigit():
            print("Pin is valid and secure.")
        else:
            print("Pin is invalid. Pin must be a 4 digit number.")

    def __str__(self):
        return "Account Owner: " + self.owner


my_account = Account("John Doe", "5678")

print(my_account)

my_account.show_pin_status()

my_account.pin = "9999"
print("Tried Changing Pin directly from outside")

my_account.check_pin()

my_account.set_pin("9999")
my_account.check_pin()
