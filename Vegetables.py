from Grocery import *

class Vegetables(Grocery):
    def __init__(self,origin,colour,seasonal,root_stem_leaves,calories,taste,price):
        super().__init__(origin,colour,seasonal,calories,price)
        self.root_stem_leaves = root_stem_leaves
        self.taste = taste

    def __str__(self):
        return super().__str__() + f'{str(self.root_stem_leaves)} ,'\
               f' {str(self.calories)} kcal,'\
               f' taste is {str(self.taste)} ,'\
               f' price is {str(self.price)} \kg'
