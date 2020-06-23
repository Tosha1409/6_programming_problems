def slices(a, target):
	l=len(a)
	for x in range(l):
		for y in range(x+1,l):
			if (a[x]+a[y])==target: return (x,y)
	
#test
print (slices([2, 7, 11, 15], 9))
print (slices([2, 7, 11, 15], 17))
