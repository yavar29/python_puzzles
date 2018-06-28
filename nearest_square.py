# Program to complute the nearest square to a given number 

given_number = 56

i=1
num=i
while num<limit:
    low=num
    i+=1
    num=i*i
    
high=i*i
print("the value of high is {}".format(high))
print("the value of low is {}".format(low))
if (high-given_number)>(given_number-low):
    print(low)
else:
    print(high)
