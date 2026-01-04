
# from abc import ABC, abstractmethod

# class Vehicle(ABC):
#     def __init__(self, color, capacity):
#         self.color = color
#         self.capacity = capacity

#     @abstractmethod
#     def get_fare(self, distance):
#         pass

#     def info(self):
#         print(f"Color: {self.color}")
#         print(f"Capacity: {self.capacity}")

# class Bus(Vehicle):
#     def get_fare(self, distance):
#         return distance * 0.5
# class Taxi(Vehicle):
#     def get_fare(self, distance):
#         return distance * 1.5
# class Bike(Vehicle):
#     def get_fare(self,distance):
#         return distance * 0.7
# class Truck(Vehicle):
#     def __init__(self, color, capacity , load_capacity):
#         super().__init__(color, capacity)
#         self.load_capacity = load_capacity
#     def get_fare(self, distance):
#             return distance * 2.5
#     def info(self):
#         super().info()
#         print(f"Load capacity: {self.load_capacity} kg")
    
# bus = Bus("Yellow", 40)
# taxi = Taxi("Black", 4)
# bike = Bike("Red", 1)
# truck = Truck("White", 2, 10000)

# print("BUS")
# bus.info()
# print("Fare:", bus.get_fare(5))
# print()

# print("TAXI")
# taxi.info()
# print("Fare:", taxi.get_fare(5))
# print()

# print("BIKE")
# bike.info()
# print("Fare:", bike.get_fare(5))
# print()

# print("TRUCK")
# truck.info()
# print("Fare:", truck.get_fare(5))\

#-Home-Work-

