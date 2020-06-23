resultx, resulty, result=-1, -1, -1
for x in range (1000,101,-1):
	for y in range (x,101,-1):
		s=str(x*y)
		l=len(str(s)) // 2
		if (s[0:l]==s[:-l-1:-1]) and x*y>result: 
			resultx, resulty, result=x,y,x*y
print(resultx, resulty, result)