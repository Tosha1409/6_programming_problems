import math

#finding maximum power that smallest number in A can get without reaching limits of A
#and returning 2 arrays. First one include maximum numbers that fits to 'powers'. 
#2nd one includes numbers that must be checked.
#for example if function returns arrays [10,4,3,2,2] and [2,3,5,6,7,10] then:
#it means that for squares of numbers up to 10 doesnt go over limits of A, cubes of numbers up to 4 
#doesnt go over limits of A etc.. and 2nd arrays include numbers that must be checked, and in this 
#example it omits 4,8 and 9, because 4 is square of 2, 8 is cube of 2 and 9 is square of 3. 
def max_roots(a):
	i=2 #smallest/starting power
	max_numbers=[]
	while int(a**(1/i))>1: #finding/storing numbers for first array
		max_numbers.append(int(a**(1/i)))
		i = i+1
	y=int(a**(1/2)) #maximum number that needs to be checked
	numbers= [x for x in range (2,y+1)] #writing down all numbers from 2 
	for x in range (2, int(y**(1/2))+1): #removing extra numbers
		number=x**2
		while (number<=y):
			numbers.remove(number)
			number *=x
	return(max_numbers, numbers)

#finding amount of original values for power, and then returning amount of repeats.
def original_values(a,power):
	values=[]
	for x in range (1,power+1): #finding all non repeated values for same number with different powers.
		for y in range(2,a+1):
			if y*x not in values: values.append(y*x)
	return (power*(a-1)-len(values))

#main function that calculate amount of distinct terms
def find_powers2(a,b):
	sum=(b-1)*(a-1) #maximum possible amount
	powers, numbers = max_roots(a)
	for x in range (len(powers)+1, 1, -1):
		current=original_values(a,x) #finding amount of repeats for current power that must be removed 
		#if there is match then counting total amounts and repeating number from array to count it only once
		while (numbers!=[]) and (powers[x-2]>=numbers[0]): 
			numbers.pop(0)
			sum -= current
	return (sum)
	    
print (find_powers2(5,5))
print (find_powers2(100,100))

