class Power_Of: 
    def __init__(self, base_num, exponent):
        self.base_num = base_num
        self.exponent = exponent
        self.tracker = 0

    def checker(self):
        if self.exponent == 0: 
            print(1)
        elif self.exponent == 1:
            print(self.base_num)
        elif self.exponent < 0:
            self.negative_exponent()
        else:
            self.positive_or_negative_num()

    def positive_or_negative_num(self):
        result = self.multiplication()
        print(result)
    
    def negative_exponent(self):
        result = self.division()
        print(result)

    def division(self):
        countup = self.exponent  
        multiplier = self.base_num  
        tracker = self.tracker 
        if countup == -1:
            multiplier = 1 / multiplier
            return(multiplier)
        else:
            while countup < -1:
                tracker = self.base_num * multiplier
                multiplier = tracker
                countup += 1
        tracker = 1 / tracker
        return(tracker)    
    
    def multiplication(self):
        countdown = self.exponent  
        multiplier = self.base_num  
        tracker = self.tracker 
        while countdown > 1:
            tracker = self.base_num * multiplier
            multiplier = tracker
            countdown -= 1
        return(tracker)        

# Power_Of program gets initialized here. 
# num1 is an object which feeds data to the program.
# x = your base number
# y = your exponent 
# Any number can go on x or y
# Once numbers are placed where x and y are at..
# click RUN (desktop) or the green PLAY button (mobile)! :D 
print("Enter a number: ")
number = int(input())
print("Enter a power: ")
power = int(input())
num1 = Power_Of(number, power).checker()

