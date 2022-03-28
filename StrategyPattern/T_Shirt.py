import random
from dataclasses import dataclass, field


@dataclass
class Tshirt:
    color: str = 'red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'violet'
    size: str ='XS','S' ,'M' , 'L','XL' , 'XXL', 'XXXL'
    fabric: str ='WOOL', 'COTTON', 'POLYESTER', 'RAYON', 'LINEN', 'CASHMERE', 'SILK'
    id: str = field (init=False)
    
    def __post_init__(self):
        self.id = random_id(10)
        
    def process(self):
        print("=========================")
        print(f" T-Shirt id: {self.id}")
        print(f" T-Shirt size: {self.size}")
        print(f" T-Shirt fabric : {self.fabric}")
        print(f" T-Shirt color : {self.color}")
        print("==========================")
        
#function to give the id random value        
def random_id(length):
    number = '0123456789'
    alpha = 'abcdefghijklmnopqrstuvwxyz'
    id = ''
    for i in range(0,length,2):
        id += random.choice(number)
        id += random.choice(alpha)
    return id            
        