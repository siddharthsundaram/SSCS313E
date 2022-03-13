import sys
import time


# Input: v an integer representing the minimum lines of code and
#        k an integer representing the productivity factor
# Output: computes the sum of the series (v + v // k + v // k**2 + ...)
#         returns the sum of the series
def sum_series (v, k):
  exp = 0
  total = 0
  while v // (k**exp) != 0:       #use integer division on v/k^exp until it reaches 0
    total += v // (k**exp)
    exp += 1
  return total                    #returns min number of lines to write


# Input: n an integer representing the total number of lines of code
#        k an integer representing the productivity factor
# Output: returns v the minimum lines of code to write using linear search
def linear_search (n, k):
  v = 1
  while sum_series(v, k) < n: #linear search of min number of lines to write
    v += 1
  return v


# Input: n an integer representing the total number of lines of code
#        k an integer representing the productivity factor
# Output: returns v the minimum lines of code to write using binary search
def binary_search (n, k):
  v = n//2
  count = 2
  a = sum_series(v, k) < n and sum_series(v + 1, k) < n
  b = sum_series(v, k) > n and sum_series(v - 1, k) >= n
  while (a or b):
    if sum_series(v, k) < n:              #binary search for left side
      if n // (2 ** count) == 0: v += 1
      else:
        v += n//(2**count)
        count += 1
    if sum_series(v, k) > n:              #binary search for right side
      if n // (2 ** count) == 0: v -= 1
      else:
        v -= n//(2**count)
        count += 1
    a = sum_series(v, k) < n and sum_series(v + 1, k) < n
    b = sum_series(v, k) > n and sum_series(v - 1, k) >= n
  if sum_series(v, k) < n: v += 1         #returns correct v by adding 1
  return v



def main():
  line = sys.stdin.readline()
  line = line.strip()
  num_cases = int (line)

  for i in range (num_cases):
    line = sys.stdin.readline()
    line = line.strip()
    inp =  line.split()
    n = int(inp[0])
    k = int(inp[1])

    start = time.time()
    print("Binary Search: " + str(binary_search(n, k)))
    finish = time.time()
    print("Time: " + str(finish - start))

    print()

    start = time.time()
    print("Linear Search: " + str(linear_search(n, k)))
    finish = time.time()
    print("Time: " + str(finish - start))

    print()
    print()

if __name__ == "__main__":
  main()
