#This script demonstrates the usage and functionalities of four primary data structures in Python: 
# lists, tuples, dictionaries, and sets.





# SETS
st = {"Habeebuddin", "Shahrukh", 56, 8712101952, True, "This is my Bio Data"}

#1. add() - Adds a single element to the set.
st.add("New Item")
print(st)  # Output: {'Habeebuddin', 'Shahrukh', True, 56, "This is my Bio Data", 8712101952, 'New Item'}

#2. update() - Adds multiple elements to the set.
st.update([2.45, "Hola"])
print(st)  # Output: {'Habeebuddin', 'Shahrukh', True, 56, "This is my Bio Data", 2.45, 8712101952, 'Hola', 'New Item'}

#3. remove() - Removes a specific element from the set. Raises a KeyError if the element is not found.
st.remove(56)
print(st)  # Output: {'Habeebuddin', 'Shahrukh', True,"This is my Bio Data", 2.45, 8712101952, 'Hola', 'New Item'}

#4. discard() - Removes a specific element from the set if it is found. Does not raise an error if the element is not found.
st.discard("Espinol")
print(st)  # Output: {'Habeebuddin', 'Shahrukh', True, 'Hola', "This is my Bio Data", 2.45, 8712101952, 'New Item'}

#5. pop() - Removes and returns an arbitrary element from the set.
popped_item = st.pop()
print(popped_item)  # Output: (element that was removed)
print(st)  # Output: (set after the element is removed)

#6. clear() - Removes all elements from the set.
st.clear()
print(st)  # Output: set()

#7. union() - Returns a new set that is the union of two sets.
set1 = {"a", "b", "c"}
set2 = {"c", "d", "e"}
union_set = set1.union(set2)
print(union_set)  # Output: {'a', 'b', 'c', 'd', 'e'}

#8. intersection() - Returns a new set that is the intersection of two sets.
intersection_set = set1.intersection(set2)
print(intersection_set)  # Output: {'c'}

#9. difference() - Returns a new set that contains elements in the first set but not the second.
difference_set = set1.difference(set2)
print(difference_set)  # Output: {'a', 'b'}

#10. symmetric_difference() - Returns a new set that contains elements in either set but not both.
symmetric_difference_set = set1.symmetric_difference(set2)
print(symmetric_difference_set)  # Output: {'a', 'b', 'd', 'e'}

#11. copy() - Returns a shallow copy of the set.
copy_set = set1.copy()
print(copy_set)  # Output: {'a', 'b', 'c'}

print('=======================================================================')


#LISTS
lst = ["Habeebuddin","Shahrukh","2203A51495",56,8712101952,True,"This is my Bio Data" ,False]

#1. append() - Adds a single element to the end of the list
lst.append("It's Okay")
print(lst)  # Output: ['Habeebuddin', 'Shahrukh', '2203A51495', 56, 8712101952, True, 'This is my Bio Data', False, "It's Okay"]

#2. extend() - Adds multiple elements from an iterable to the end of the list.
lst.extend([2.45, "Hola"])
print(lst)  # Output: ['Habeebuddin', 'Shahrukh', '2203A51495', 56, 8712101952, True, 'This is my Bio Data', False, "It's Okay", 2.45, "Hola"]

#3. insert() - Inserts an element at a specified position in the list.
lst.insert(5, "Espinol")
print(lst)  # Output: ['Habeebuddin', 'Shahrukh', '2203A51495', 56, 8712101952, 'Espinol', True, 'This is my Bio Data', False, "It's Okay", 2.45, "Hola"]

#4. remove() - Removes the first occurrence of a value.
lst.remove(56)
print(lst)  # Output: ['Habeebuddin', 'Shahrukh', '2203A51495', 8712101952, 'Espinol', True, 'This is my Bio Data', False, "It's Okay", 2.45, "Hola"]

#5. pop() - Removes and returns an item at a given index.
lst.pop(0)
print(lst)  # Output: ['Shahrukh', '2203A51495', 8712101952, 'Espinol', True, 'This is my Bio Data', False, "It's Okay", 2.45, "Hola"]

#6. index() - Returns index of the first occurrence.
index = lst.index(True) 
print(index)  # Output: 4

#7. count() - Returns number of occurrences of a value.
count = lst.count(True)  
print(count)  # Output: 1

#8. sort() - Sorts the list in place.
# Note: This will raise an error because the list contains elements of different data types that cannot be compared.
# Hence, we need to use a list that contains comparable items.
comparable_lst = [3, 1, 4, 2]
comparable_lst.sort()
print(comparable_lst)  # Output: [1, 2, 3, 4]

#9. reverse() - Reverses the list in place.
lst.reverse()
print(lst)  # Output: ['Hola', 2.45, "It's Okay", False, 'This is my Bio Data', True, 'Espinol', 8712101952, '2203A51495', 'Shahrukh']

#10. copy() - Returns a shallow copy of the list.
new_lst = lst.copy()
print(new_lst)  # Output: ['Hola', 2.45, "It's Okay", False, 'This is my Bio Data', True, 'Espinol', 8712101952, '2203A51495', 'Shahrukh']

#11. clear() - Removes all items from the list.
lst.clear()
print(lst)  # Output: []

print('=======================================================================')

# TUPLES
tpl = ("Habeebuddin", "Shahrukh", "2203A51495", 56, 8712101952, True, "This is my Bio Data", False)

#1. count() - Returns the number of occurrences of a value
count = tpl.count(True)
print(count)  # Output: 1

#2. index() - Returns the index of the first occurrence of a value
index = tpl.index(56)
print(index)  # Output: 3


print('=======================================================================')

# DICTIONARIES
dct = {
    'name': 'Habeebuddin',
    'friend': 'Shahrukh',
    'id': '2203A51495',
    'age': 56,
    'phone': 8712101952,
    'is_active': True,
    'bio': 'This is my Bio Data'
}

#1. keys() - Returns a view object of all keys
keys = dct.keys()
print(keys)  # Output: dict_keys(['name', 'friend', 'id', 'age', 'phone', 'is_active', 'bio'])

#2. values() - Returns a view object of all values
values = dct.values()
print(values)  # Output: dict_values(['Habeebuddin', 'Shahrukh', '2203A51495', 56, 8712101952, True, 'This is my Bio Data'])

#3. items() - Returns a view object of all key-value pairs
items = dct.items()
print(items)  # Output: dict_items([('name', 'Habeebuddin'), ('friend', 'Shahrukh'), ('id', '2203A51495'), ('age', 56), ('phone', 8712101952), ('is_active', True), ('bio', 'This is my Bio Data')])

#4. get() - Returns the value for a key if it exists
bio = dct.get('bio')
print(bio)  # Output: This is my Bio Data

#5. update() - Updates the dictionary with key-value pairs from another dict or iterable
dct.update({'language': 'Python', 'hobby': 'Coding'})
print(dct)  # Output: {'name': 'Habeebuddin', 'friend': 'Shahrukh', 'id': '2203A51495', 'age': 56, 'phone': 8712101952, 'is_active': True, 'bio': 'This is my Bio Data', 'language': 'Python', 'hobby': 'Coding'}

#6. pop() - Removes and returns the value for a given key
age = dct.pop('age')
print(age)  # Output: 56
print(dct)  # Output: {'name': 'Habeebuddin', 'friend': 'Shahrukh', 'id': '2203A51495', 'phone': 8712101952, 'is_active': True, 'bio': 'This is my Bio Data', 'language': 'Python', 'hobby': 'Coding'}

#7. popitem() - Removes and returns the last inserted key-value pair
last_item = dct.popitem()
print(last_item)  # Output: ('hobby', 'Coding')
print(dct)  # Output: {'name': 'Habeebuddin', 'friend': 'Shahrukh', 'id': '2203A51495', 'phone': 8712101952, 'is_active': True, 'bio': 'This is my Bio Data', 'language': 'Python'}

#8. clear() - Removes all items from the dictionary
dct.clear()
print(dct)  # Output: {}

#9. copy() - Returns a shallow copy of the dictionary
new_dct = dct.copy()
print(new_dct)  # Output: {'name': 'Habeebuddin', 'friend': 'Shahrukh', 'id': '2203A51495', 'phone': 8712101952, 'is_active': True, 'bio': 'This is my Bio Data'}

#10. fromkeys() - Creates a new dictionary from keys in iterable and values set to value
new_dict = dict.fromkeys(['name', 'friend', 'id'], 'unknown')
print(new_dict) # Output: {'name': 'unknown', 'friend': 'unknown', 'id': 'unknown'}

#11. setdefault() - Returns the value of a key if it exists, otherwise sets it to a default value
default_name = dct.setdefault('hobby', 'Reading')
print(default_name)  # Output: Reading
print(dct)  # Output: {'name': 'Habeebuddin', 'friend': 'Shahrukh', 'id': '2203A51495', 'phone': 8712101952, 'is_active': True, 'bio': 'This is my Bio Data', 'hobby': 'Reading'}


