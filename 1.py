def fractions (a):
	results=[0,0,0]
	l=len(a)
	for x in a:
		if x>0: results[0]+=1
		elif x<0: results[1]+=1
		else: results[2]+=1
	return ([round(results[0]/l,4), round(results[1]/l,4), round(results[2]/l,4)])

#test
print (*fractions ([1, 1, 0, -1, -1]), sep='\n')
print ('--------------------')
print (*fractions ([-4, 3, -9, 0, 4, 1]), sep='\n')
	
	 