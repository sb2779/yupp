class Grocery():
    def __init__(self,origin,colour,seasonal,calories,price):
        self.origin   = origin
        self.colour   = colour
        self.seasonal = seasonal
        self.calories = calories
        self.price    = price

    def __str__(self):
        return f'{self.origin} {self.colour} {self.seasonal}'

class fruits(Grocery):
    def __init__(self,origin,colour,seasonal,seeds,riped,calories,price):
        super().__init__(origin,colour,seasonal,calories,price)
        self.seeds = seeds
        self.riped = riped

    def __str__(self):
        return super().__str__() + f' {self.seeds} seeds,'\
               f' {str(self.riped)} riped,'\
               f' {str(self.calories)} kcal,'\
               f' price is {self.price} /kg'
        
