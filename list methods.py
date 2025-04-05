# 1. extend() – adds elements from another list

colors = ["red", "blue"]
more_colors = ["green", "yellow",45]
colors.extend(more_colors)
print(colors)  # ['red', 'blue', 'green', 'yellow']

# 2. copy() – makes a copy of the list

colors_copy = colors.copy()
print(colors_copy)

  # ['red', 'blue', 'green', 'yellow']
#here actually colors=['red', 'blue', 'green', 'yellow'] because in last code we got a o/p colors= ['red', 'blue', 'green', 'yellow']
#so when we print colors.copy it takes the last color value...

# 3. len() – returns the number of items

print(len(colors))  # 4
# in len method,count the number of items in given list we have four items in color ['red', 'blue', 'green', 'yellow'] so we got o/p 4

# 4. List slicing – get a portion of the list #Accessing mothod


print(colors[2:5])  # ['blue', 'green']
#in this method list will be slicedd based on index number in positive index-start indeex can't be taken

# 5. in operator – check if an item exists

print("red" in colors)  # True

# 6. not in operator – check if item doesn’t exist

print("pink" not in colors)  # True

# 7. Looping through list

for color in colors:
    print(color)
    # in this method it print all datas inside the list

# 8. List comprehension – short & sweet list creation

squares = [x**2 for x in range(5)]
print(squares)  # [0, 1, 4, 9, 16]
#range(5) creates the numbers: 0, 1, 2, 3, 4
# x**2 means: square each number (like x*x)
# The whole thing builds a list of those squares

# 9. max() / min() – largest and smallest values

numbers = [5, 2, 9, 1]
print(max(numbers))  # 9
print(min(numbers))  # 1


# 10. sum() – adds all numbers in the list
print(sum(numbers))  # 17

#11. Append method it add the new item into the list
name=['rm','jin','suga','hobi','jm','v','jk']
name.append('enola')
print(name)

#12.insert method it add the item into the list based on the index num
name.insert(8,'home')
print(name)

#13.remove method it removes particular data from list
name.remove('enola')
print(name)

#14.pop method it remove particular data from the list based on the index num
name.pop(4)
print(name)

#15.sort method it can list the data in decending and ascending order

count=[1,2,3,4,5,6,7,8,9]
count.sort() #it ascending order
print(count)

count.sort(reverse=True) #it desending order
print(count)

#16 reverse method 
numbers.reverse()
print(numbers)

