class Binary_Calculator:
  def __init__ (self,num): 
    self.num = num

  def binary(self):
    num = self.num;
    l = []
    temp = num;
    
    while(temp): 
        last_digit = temp % 2;
        temp = int(temp / 2);
        l.append(last_digit);
    l.reverse()
    
    # initialize an empty string 
    str1 = ""  
    
    # traverse in the string   
    for ele in l:  
        str1 += str(ele)   
    print(str1)
 
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

## Main
## Intro 
  
print("::::::::::::::::::::::::::::::::::")
print(":::                            :::")
print("::: Tech Tool-Kit              :::")
print("::: Current version: 1.0       :::")
print("::: Authors: John M., Matt R.  :::")
print(":::                            :::")
print("::: Tool-Kit:                  :::")
print("::: 1. Power-Of Tool           :::")
print("::: 2. Binary Conversion Tool  :::")
print("::: 3. File generator          :::")
print(":::                            :::")
print("::::::::::::::::::::::::::::::::::")
print()
print(" PRESS ANY KEY TO CONTINUE ")
input()
print("Select: ")
print("a. Power-Of Tool")
print("b. Binary Conversion Tool")
print("c. File generator")
selection = input()
while(True):
  if(selection == 'a' or selection == 'b' or selection == 'c'):
    break
  print("Enter a valid selection: ")
  selection = input()

if(selection == 'a'):
  print("::: Power Of Tool :::")
  print("Please Enter a number: ")
  number = int(input())
  print("Please Enter a Power: ")
  power = int(input())
  num1 = Power_Of(number, power).checker()  

elif(selection == 'b'):
  print("::: BINARY CONVERSION TOOL 1.0 :::")
  print("Enter a number for conversion: ")
  number = int(input())
  Binary_Calculator(number).binary()
elif(selection == 'c'):
  print("::: FILE GENERATOR :::")
  print("Enter the text to print in file: ")
  text = input()
  f = open("myFile.txt", "w")
  f.write(text)
  f.close()
  print("Would you like to open the file?")
  print("Press 'y' for yes and 'n' for no ")
  yn = input()
  if(yn == 'y'):
    f = open("myFile.txt", "r")
    print("The file contents: ")
    print(f.read()) 
    f.close()
print("THANK YOU =)")
