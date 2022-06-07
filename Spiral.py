# Input: n is an odd integer between 1 and 100
# Output: returns a 2-D list representing a spiral
#         if n is even add one to n

def create_spiral(n):
    rows, cols = (n, n)
    arr = [[0 for i in range(cols)]for j in range(rows)]
    center = int((n/2) - 0.5)
    ud = center
    lr = center
    value = 1
    arr[center][center] = value
    value += 1
    counter = 1
    for x in range(center):
        lr += 1
        arr[ud][lr] = value
        value += 1
        for y in range(counter):
            ud += 1
            arr[ud][lr] = value
            value += 1
        counter += 1
        for z in range(counter):
            lr -= 1
            arr[ud][lr] = value
            value += 1
        for a in range(counter):
            ud -= 1
            arr[ud][lr] = value
            value += 1
        for b in range(counter):
            lr += 1
            arr[ud][lr] = value
            value += 1
        counter += 1

    lis = []
    while 1:
        try:
            inp = int(input())
            lis.append(inp)
        except:
           break

    for x in range(len(lis)): sum_adjacent_numbers(arr, lis[x])

# Input: spiral is a 2-D list and n is an integer
# Output: returns an integer that is the sum of the
#         numbers adjacent to n in the spiral
#         if n is outside the range return 0
def sum_adjacent_numbers(spiral, n):
    if n > (len(spiral)**2) or n < 1: print("Error")
    else:
        indx = 0
        indy = 0
        for c in range(len(spiral)):
            for v in range(len(spiral)):
                if spiral[c][v] == n:
                    indy = c
                    indx = v

        a, b, c, d, e, f, g, h = (-1, -1, -1, -1, -1, -1, -1, -1)
        if indy == 0:
            a, b, c = (0, 0, 0)
        if indy == len(spiral) - 1: f, g, h = (0, 0, 0)
        if indx == 0: a, d, f = (0, 0, 0)
        if indx == len(spiral) - 1: c, e, h = (0, 0, 0)
        if a != 0: a = spiral[indy-1][indx-1]
        if b != 0: b = spiral[indy-1][indx]
        if c != 0: c = spiral[indy-1][indx+1]
        if d != 0: d = spiral[indy][indx-1]
        if e != 0: e = spiral[indy][indx+1]
        if f != 0: f = spiral[indy+1][indx-1]
        if g != 0: g =  spiral[indy+1][indx]
        if h != 0: h =  spiral[indy+1][indx+1]
        sum = a + b + c + d + e + f + g + h
        print(sum)

def main():
    create_spiral(int(input()))

main()  
