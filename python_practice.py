# Write a Python function called max_num()to find the maximum of three numbers.
def find_max(a, b, c):
    return max([a, b, c])

print(find_max(12, 390, 3))
print(find_max(52, 36, 11))
print(find_max(7, 3, 109))

# Write a Python function called mult_list() to multiply all the numbers in a list.
def mult_list(lst):
    if len(lst) == 0:
        return 0
    prod = lst[0]
    if len(lst) > 1:
        for i in lst[1:]:
            prod = prod * i
    return prod

print(mult_list([1,2,3]))
print(mult_list([]))
print(mult_list([15]))


# Write a Python function called rev_string() to reverse a string.
def rev_string(str):
    if len(str) == 0:
        print("Nothing to reverse")
    else:
        print(str[::-1])

rev_string("")
rev_string("cheeseburger")
rev_string("a")

# Write a Python function called num_within() to check whether a number falls in a given range.
def num_within(num, start, end):
    within = range(start, end+1)
    if num in within:
        return True
    else:
        return False

print(num_within(1, -2, 3))
print(num_within(23, 22, 23))
print(num_within(0, 3, 13))


# Write a Python function called pascal() that prints out the first n rows of Pascal's triangle.
triangle = [[1],[1,1]]
def pascal(n):
  #base case
  if n < 1:
    print("invalid number of rows")
  elif n == 1:
    print(triangle[0])
  else:
    row_number = 2
    #fill up correct number of rows in triangle
    while len(triangle) < n:
      row = []
      row_prev = triangle[row_number - 1]
      #create correct row, then add to triangle (this row will be 1 longer than row before it)
      length = len(row_prev)+1
      for i in range(length):
        #first number is 1
        if i == 0:
          row.append(1)
        #intermediate nunmbers get added from previous rows
        elif i > 0 and i < length-1:
          row.append(row_prev[i-1]+row_prev[i])
        #   print([i-1])
        #last number is 1
        else:
          row.append(1)
      triangle.append(row)
      row_number += 1

    #print triangle
    for row in triangle:
      print(row)

pascal(1)
pascal(2)
pascal(5)