import json

class Customer:
    def __init__(self, user_id, first_name, last_name):
        self.user_id = user_id
        self.first_name = first_name
        self.last_name = last_name

    def to_json(self):
        return json.dumps({"user_id": self.user_id, "first_name": self.first_name, "last_name": self.last_name})

class Account:
    def __init__(self, account_id, balance):
        self.account_id = account_id
        self.balance = balance

    def to_json(self):
        return json.dumps({"account_id": self.account_id, "balance": self.balance})

class Bank:
    def __init__(self):
        self.customers = []
        self.accounts = []

    def add_customer(self, customer):
        self.customers.append(customer)

    def add_account(self, account):
        self.accounts.append(account)

    def to_json(self):
        customers_json = [customer.to_json() for customer in self.customers]
        accounts_json = [account.to_json() for account in self.accounts]
        return json.dumps({"customers": customers_json, "accounts": accounts_json}, indent=4)

# Test cases
if __name__ == "__main__":
    # Create a Customer
    john = Customer(1, "John", "Smith")
    print("Serialized Customer:")
    print(john.to_json())

    # Create an Account
    first_account = Account(1, 5000)
    print("Serialized Account:")
    print(first_account.to_json())

    # Create a Bank and add customers and accounts
    the_bank = Bank()
    the_bank.add_customer(john)
    the_bank.add_customer(Customer(2, "Jane", "Doe"))
    the_bank.add_account(first_account)

    # Serialize the Bank object
    print("Serialized Bank:")
    print(the_bank.to_json())
