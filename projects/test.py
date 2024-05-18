import math

a = float(input("請輸入三角形的第1個邊長:"))
b = float(input("請輸入三角形的第2個邊長:"))
c = float(input("請輸入三角形的第3個邊長:"))

if a<b:
    a, b = b, a
if a<c:
    a, c = c, a

d = (a+b+c)/2

if a>=b+c:
    print("illegal\nunavailable")
elif a*a == b*b + c*c:
    print("right\n%0.4f" % math.sqrt(d*(d-a)*(d-b)*(d-c)))
elif a*a > b*b + c*c:
    print("obtuse\n%0.4f" % math.sqrt(d*(d-a)*(d-b)*(d-c)))
elif a*a < b*b + c*c:
    print("acute\n%0.4f" % math.sqrt(d*(d-a)*(d-b)*(d-c)))
