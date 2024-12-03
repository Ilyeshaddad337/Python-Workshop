# like usual : + , - , * , /
x = 2 + 3
y = 2 - x
z = 2/8
s = 8*6
# div //
z = 8 // 2

# mod  %
mod = 8 % 2

# power
x= 2 ** 10

# concat two strings

str1 = "hello "
str2 = " sbah nour"

str3 = str1 + str2

# manipulate lists

arr = [1, 6, 9]

# length
len(arr)
# access an element
print(arr[2])

# last elm
print(arr[-1]) # or arr[len(arr)-1]


arr.append(6)
arr.remove(6)
arr.insert(2, 5)
print(arr)

# reverse a list

rev_arr = arr[::-1]
print(rev_arr)

# slice an array 
new_arr = rev_arr[1:3]
print(new_arr)

# combine two arrays
arr2 = rev_arr + arr
print(arr2)
# sort a list

arr.sort() # or  sorted(arr)
print(arr)