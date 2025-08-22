# Define a class
class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def start_engine(self):
        print(f"The {self.brand} {self.model}'s engine is now running.")

# Create objects (instances of the class)
car1 = Car("Toyota", "Corolla")
car2 = Car("Tesla", "Model 3")

# Call methods on the objects
car1.start_engine()
car2.start_engine()

