
class Car:
    def __init__(self,brand,type_byke):
        # self.care_name = care_name
        # self.car_price = car_price
        # self.care_type = care_type
        # self.brand = brand
        self.type_byke = type_byke
        
    def car_details(self):
        car = f"This is a {self.care_name} which price is {self.car_price} and type is {self.care_type}"
        return car
    # def brand_name(self):
    #     return f"This is One of the best brand which name is {self.brand}"
    def type_vehicle(self):
        return f"This is One of the best vehicle which name is {self.type_byke}"

class Product(Car):
    def __init__(self,brd,type_byke):
        # self.brand = brd
        super().__init__(brd,type_byke)
        
    
pr = Product("Tata","kawasaki")       

    
# tata_nano = Car("tata_nano","3 lakhs","small")
print(pr.type_vehicle())
