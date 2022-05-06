class Step1:

    def lets_do(self):
        print('Preheat the oven to 350 degrees F (175 degrees C). Grease and flour a 9-inch square cake pan.Preheat the oven to 350 degrees F (175 degrees C). Grease and flour a 9-inch square cake pan.Preheat the oven to 350 degrees F (175 degrees C). Grease and flour a 9-inch square cake pan.')


class Step2:

    def lets_do(self):
        print('Cream sugar and butter together in a mixing bowl. Add eggs, one at a time, beating briefly after each addition. Stir in vanilla.')


class Step3:

     def lets_do(self):
         print('Combine flour and baking powder in a separate bowl. Add to the wet ingredients and mix well. Add milk and stir until smooth. Pour batter into the prepared cake pan.')        


class Step4:
    def lets_do(self):
         print('Bake in the preheated oven until the top springs back when lightly touched, 30 to 40 minutes.')

class BakingCakeFacade:
    
    def __init__(self):
        self.step1=Step1()
        self.step2=Step2()
        self.step3=Step3()
        self.step4=Step4()

    def start_baking(self):
        self.step1.lets_do()
        self.step2.lets_do()
        self.step3.lets_do()
        self.step4.lets_do()
    

if __name__ == '__main__':
        BakingCakeFacade().start_baking()
        

    











