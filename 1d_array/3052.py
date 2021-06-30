x = [int(input())%42, int(input())%42, int(input())%42, int(input())%42, int(input())%42, int(input())%42, int(input())%42, int(input())%42, int(input())%42, int(input())%42]
a=0
b=0
c=0
d=0
e=0
f=0
g=0
h=0
i=0
j=0

for z in range(10):
	if x.count(x[z])==1:
		a=a+1
	elif x.count(x[z])==2:
		b=b+1
	elif x.count(x[z])==3:
		c=c+1
	elif x.count(x[z])==4:
		d=d+1
	elif x.count(x[z])==5:
		e=e+1
	elif x.count(x[z])==6:
		f=f+1
	elif x.count(x[z])==7:
		g=g+1
	elif x.count(x[z])==8:
		h=h+1
	elif x.count(x[z])==9:
		i=i+1
	elif x.count(x[z])==10:
		j=j+1

print(a+b//2+c//3+d//4+e//5+f//6+g//7+h//8+i//9+j//10)

#Make it a set and use len funtion to figure out the number of elements. Also, use for loop for better efficiency.