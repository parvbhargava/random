from random_num_genrator import random_uniform,random
from pi import predict_pi
from matplotlib import pyplot as plt

#Genrate random numbers
random_number = random(seed=12)
#predict value of pi
value = predict_pi()
#print our results
print(f"The random number is {random_number}.\nThe predicted value of pi is {value}.")
#Here are the 10,000 random numbers between -5 and 5 with an an histogram representing them.
numbers = random_uniform(low=-5,high=5,size=10000)
print(numbers)
plt.hist(numbers,bins=20,edgecolor='b')
plt.xlim(-6,6)
plt.show()