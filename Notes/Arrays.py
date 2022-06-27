""" _______________________________ """
#!""" Lists (Array) """

""" You can put string, number, and array inside the array """
my_list = ["Hope" , 24 , ["Drawing","Swimming"]]
print("Hi There! \nMy name is " + my_list[0] + ". I'm " + str(my_list[1]) + " years old. My hobbies are " + my_list[2][0] + " and " + my_list[2][1] + ".")

my_data = ["HTML" , "CSS" , "JAVASCRIPT" , "REACT" , "NODE"]

print(my_data[1:3])
""" The output is --> ['CSS', 'JAVASCRIPT'] => take the values from my_data[1] to my_data[3-1] = my_data[2]  """

print(my_data[1:])
""" The output is --> ['CSS', 'JAVASCRIPT', 'REACT', 'NODE'] => take the values from my_data[1] to last item  """

print(my_data[-1])   #* The output is --> NODE

""" You can change the value of any items in the array """
my_data[0] = "HTML3" 

""" Add the second array to first array use { array1.extend(array2) OR array1 += array2 OR array1 = array1 + array2} """
array1 = ["Hope" , "Amal"]
array2 = ["Yuki" , "Akira"]
array1.extend(array2)
print(array1)   #* The output is --> ['Hope', 'Amal', 'Yuki', 'Akira']

""" Add new item to the array (last item) use { array.append(item_value) } """
array2.append("Yuyu")
print(array2)   #* The output is --> ['Yuki', 'Akira', 'Yuyu']

""" Add new item to the array (any place) use { array.insert(place , item_value) } """
array2.insert(1,"Moshy")
print(array2)   #* The output is --> ['Yuki', 'Moshy', 'Akira', 'Yuyu']

""" Remove any item from array use { array.remove(item_value) } """
array2.remove("Yuyu")
print(array2)  #* The output is --> ['Yuki', 'Moshy', 'Akira']

""" Remove last item from array use { array.pop() } """
last_item = array2.pop()
print(last_item)   #* The output is --> Akira
print(array2)  #* The output is --> ['Yuki', 'Moshy']

""" Clear the array use {array.clear()} """
array2.clear()  
print(array2)   #* The output is --> []

""" (to know the place of the item in the array --> number) & (to check if this item is in the array --> Error (we can't find the item)) use { array.index("item_value")} """
print(array1.index("Amal"))  #* The output is 1

""" Count the item in the array use { array.count(item_value) } """
arr = ["hope","amal","hope","yuki"]
print(arr.count("hope"))   #* The output is 2

""" Sorting (a -> z) OR ( -infinite -> infinite ) use { array.sort() } """
arr1 = ["hope","amal","yuki","mashal"]
arr1.sort()
print(arr1)   #* The output is ['amal', 'hope', 'mashal', 'yuki']

arr2 = [55,3,4,65]
arr2.sort()
print(arr2)   #* The output is [3, 4, 55, 65]

""" Shallow copy the array use { array.copy() } """
old_arr = ["Hi","Hello"]
new_arr = old_arr.copy()
old_arr.append("There!")
print(new_arr)   #* The output is ['Hi', 'Hello']
print(old_arr)   #* The output is ['Hi', 'Hello', 'There!']

""" Copy the array use { new_array = old_array } """
old_arr1 = ["Hi!!","Hello!!"]
new_arr1 = old_arr1
old_arr1.append("There!!!")
print(new_arr1)   #* The output is ['Hi!!', 'Hello!!', 'There!!!']
print(old_arr1)   #* The output is ['Hi!!', 'Hello!!', 'There!!!']

""" _______________________________ """
