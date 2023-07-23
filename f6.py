a = int(input("kiriting: "))

DigitCountSum = lambda a:len(str(a))
print("sonning uzunligi",DigitCountSum(a))

def DigitCountSum(a):
       s=0
       i=1
       while i<=a:
          s+=i
          i+=1
       print("sonning raqamlar yig`indisi:",s)
a = int(input("kiriting: "))
print(DigitCountSum())
