#finding all digits in number, and returning them as array
def get_digits(n):
	division=1000
	numbers=[]
	for x in range (1,5):
		numbers.append(int(n/division))
		n -= numbers[-1]*division
		division /= 10
	return(numbers)

#making number from digits
def make_number(digits):
	n=0
	division=1000
	for x in digits:
		n += x*division
		division /= 10
	return(int(n))

#main function
def calculations(n):
	counter=0
	while (n!=6174):
		numbers=get_digits(n)
		numbers.sort(reverse=True)
		n1=make_number(numbers)
		numbers.sort()
		n2=make_number(numbers)
		n=n1-n2	
		counter +=1
	return (counter)
	
#test
n=3524
print (n,' - ',calculations(n))

n=2111
print (n,' - ',calculations(n))

n=9831
print (n,' - ',calculations(n))
