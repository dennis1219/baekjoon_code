a = int(input())
z = int(a)
count = 0
c = 0
d = 0

while True:
	try:
		if z==0:
			print("1")
			break
		elif c==z:
			print(count)
			break
		elif d==z:
			print(count)
			break
		elif a<10:
				c=((a%10)*10+a)
				count=count+1
				a=int(c)
		else:
			d=((a%10)*10+(a//10+a%10)%10)
			count=count+1
			a=int(d)
			
				
	except:
		break

#Code became long since I made a mistake while coding since I didn't read the given conditions in the problem precisely. Better not make the same mistake next time.