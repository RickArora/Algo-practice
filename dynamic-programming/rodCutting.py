# Given a rod length n inches an an array that contain prices of all pieces of size smaller then n. 
# Determine the maximum value obtainable by cutting up the rod and selling the pieces 
import sys

# A Utility function to get the max of 2 ints
def max(a,b):
    return a if (a > b) else b 
  
  #Returns the best obtainable price for a rod of length n and price[] as prices of different pieces
def cutRod(price, n) : 
  if(n <= 0): # base case
    return 0
  max_val = -sys.maxsize-1 # max python integer -1 
  
  # Recursivley cut the rod in different pieces and compare different configurations
  # we set max max size to the most negative integer possible
  for i in range(0,n): # iterates from 0 to n, using the variable i for the values in between
    max_val = max(max_val, price[i] + cutRod(price, n - i - 1))  # assigns max val the max val between the previous max val and the new one gained by adding
    # cutRod(price n - i - 1 )
  return max_val


arr = [1, 5, 8, 9, 10, 17, 17, 20]
size = len(arr)
print("Maximum Obtainable Value is " + str(cutRod(arr, size)))
