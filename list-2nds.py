#return the second smallest and second largest numbers from a given list of numbers
import sys

numlist = [2, 4, 6, 8, 9, 255, 11, 13, 1, 3]
numlist.sort()
print("Sorted: ", numlist)

print("2nd smallest", numlist[1])
print("2nd largest", numlist[-2])
