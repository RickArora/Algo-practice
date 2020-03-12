# Given a rod length n inches an an array that contain prices of all pieces of size smaller then n. 
# Determine the maximum value obtainable by cutting up the rod and selling the pieces 
import sys

INT_MIN = -sys.maxsize-1 #min is initialized to negative numbers
  
def cutRod(price, n): # defining cut rod with 2 parameters price and n which is the length of the rod 
  val = [0 for x in range(n+1)] # initializes an array for 0 to n elements
  val[0] = 0 # trivial statement since all values in the array val were set to 0 anyways
  #bottom-up manner
  for i in range(1, n+1): # iterates from 1 to n+1 in the value i
    max_val = INT_MIN # min possible value assigned to max_val
    for j in range(i): #  iterates from 0 to i
      max_val = max(max_val, price[j] + val[i-j-1]) #assigns max val the maximum value from the current max val and the price[j] +  a precomputed value in val
    val[i] = max_val # assigns val[i] another entry cached in our memo array
    print(val[i])
  return val[n] # returns the last entry, i.e the highest val
#main
price = [2,10,15,16,21]
size = len(price) 
print("Max value is " + str(cutRod(price, size)))
    