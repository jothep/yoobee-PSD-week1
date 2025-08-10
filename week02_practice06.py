class StringManipulator:
    def __init__(self):
        name = input("Pls enter your name:")
        age = int(input("Pls enter your age:"))
        address = input("Pls enter your address:")
        self.list = [name, age, address]

    def add_age(self):
        add_number = int(input("Pls enter the number you want to add:"))
        self.list[1] += add_number
        print (self.list)
        return self.list

if __name__ == "__main__":
    StringManipulator().add_age()

