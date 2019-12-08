class Customer:
    def __init__(self, name, age, gender, address, email):
        self.gender = gender
        self.name = name
        self.age = age
        self.address = address
        self.email = email

    def get_customer_detail(self):
        if self.gender == 'Male':
            _gender = "He"
        elif self.gender == 'Female':
            _gender = "She"
        else:
            _gender = "it"
        return f"Customer Name is {self.name}, {_gender}  is {self.age} years old ,\nlive in {self.address}, email address is {self.email}"


class CustomerA(Customer):
    pass

customerA = CustomerA('Ben','26','Male','Adddress1','zw2yc@hotmail.com')

print (customerA.get_customer_detail())