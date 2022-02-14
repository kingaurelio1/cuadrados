n=int(input())
def sq(m):
	a="yes"
	b= m**0.5
	if m%4==3:
		return "no"
	else:
		if b==int(b):
			return a
		else:
			for i in range(1,int(b)):
				if (m-(i**2))**0.5 == int((m-(i**2))**0.5):
				    return a
				    break
				else:
					continue
	return "no"
	
print(sq(n))
