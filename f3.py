from math import(
    sqrt
)
a = int(input("Kiriting: "))
b = int(input("Kiriting: ")) 
c = int(input("Kiriting: "))
d = int(input("Kiriting: "))

MEAN = lambda a:(a + b) / 2
print(a ,"bilan", b ,"ning o`rta arifmetigi: ",MEAN(a))


MEAN = lambda a:(a + c) / 2
print(a ,"bilan", c ,"ning o`rta arifmetigi: ",MEAN(a))


MEAN = lambda a:(a + d) / 2
print(a ,"bilan", d ,"ning o`rta arifmetigi: ",MEAN(a))


MEAN = lambda a:sqrt(a * b)
print(a ,"bilan", b ,"ning o`rta geometrigi: ",MEAN(a))


MEAN = lambda a:sqrt(a * c)
print(a ,"bilan", c ,"ning o`rta geometrigi: ",MEAN(a))


MEAN = lambda a:sqrt(a * d)
print(a ,"bilan", d ,"ning o`rta geometrigi: ",MEAN(a))

