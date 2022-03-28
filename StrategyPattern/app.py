from ast import Pass
import random 
from abc import abstractmethod 
import abc
from T_Shirt import  Tshirt

class PayingMethodsStrategy(metaclass=abc.ABCMeta):
    @abstractmethod
    def create_payment(self,tshirts:list[ Tshirt]) -> list[Tshirt] :
        
        pass
         
         
class CreditDebit(PayingMethodsStrategy):
    def create_payment(self,tshirts:list[ Tshirt]) -> list[Tshirt] :
        return tshirts.copy()
    
class MoneyBankTranfer(PayingMethodsStrategy):
    def create_payment(self,tshirts:list[ Tshirt]) -> list[Tshirt] :
        return list(reversed(tshirts))
     

    
class Cash(PayingMethodsStrategy):
    def create_payment(self,tshirts:list[ Tshirt]) -> list[Tshirt] :
        return random.sample(tshirts,len(tshirts))
    
    
class TshirtSupport:
    def __init__(self):
        self.tshirts:list[Tshirt]=[]
        
    def add_tshirt(self,tshirt:Tshirt):
        self.tshirts.append(tshirt) 
        
    def process_tshirts(self,payment_strategy:PayingMethodsStrategy):
        tshirt_list= payment_strategy.create_payment(self.tshirts)
        
        if len(tshirt_list)==0:
            print("There are no t-shirts left.Well done!!")
            return
        
        for tshirt in tshirt_list:
            tshirt.process() 
            
        self.tshirts=[]             
           