
from app import TshirtSupport,Cash, MoneyBankTranfer,CreditDebit,PayingMethodsStrategy
from T_Shirt import Tshirt

class BlackHoleStrategy(PayingMethodsStrategy):
    def create_payment(self,tshirts: list[Tshirt])->list [Tshirt]:
        return []


def main():
    app=TshirtSupport()
    
    app.add_tshirt(Tshirt("Red", "XXXL  ", "Cotton"))
    
    app.add_tshirt(Tshirt("green", "M  ", "WOOL"))
    
    app.add_tshirt(Tshirt("blue", "S  ", "POLYESTER"))
    
    app.add_tshirt(Tshirt("violet", "XS  ", "CASHMERE"))
    
    app.add_tshirt(Tshirt("indigo", "XXL  ", "LINEN"))
    
    app.add_tshirt(Tshirt("Orange", "L  ", "Rayon"))
    
    app.add_tshirt(Tshirt("Yellow", "XL  ", "Silk"))
    
    app.process_tshirts(MoneyBankTranfer())
    app.process_tshirts(Cash())
    app.process_tshirts(CreditDebit())
    app.process_tshirts(BlackHoleStrategy())
    
    
    
    
    
    

if __name__=="__main__":
    main()
