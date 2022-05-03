# Beauty Salon

class BeautySalonCommandInterface :

    def __init__(self, receiver ):
        self.receiver =receiver 


    def execute(self):
        print('execute')


class HairDress(BeautySalonCommandInterface):
    def execute(self):
        print('execute HairDress {}'.format(self.receiver))

class Manicure(BeautySalonCommandInterface):
        def execute(self):
            print('execute Manicure for{}'.format(self.receiver))


# receiver
class Customer:
        def __init__(self,name):
            print(f"hi {name}")
            

# invoker
class BeautySalon:
    listOfTasks=[]
    def newCustomer(self,listOfTasks):
        self.listOfTasks=listOfTasks

    def perform_action(self):
        for item in self.listOfTasks:
            item.execute()
            
  

if __name__ == '__main__':
    
    customer=Customer('emily')

    invoker=BeautySalon()

    invoker.newCustomer([
        HairDress(customer),
        HairDress(customer),
        Manicure(customer)
        ]
    )
    invoker.perform_action()



    
    




