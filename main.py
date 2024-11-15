# Creating and working with a list
my_list = [1, 2, 3, 4, 5]

# Adding elements to the list
my_list.append(6)
print("List after adding an element:", my_list)

# Removing an element from the list
my_list.remove(3)
print("List after removing an element:", my_list)

# Modifying an element in the list
my_list[2] = 10
print("List after modifying an element:", my_list)


# Creating and working with a dictionary
my_dict = {"name": "Alice", "age": 25, "city": "New York"}

# Adding a new key-value pair to the dictionary
my_dict["email"] = "alice@example.com"
print("Dictionary after adding an element:", my_dict)

# Removing a key-value pair from the dictionary
del my_dict["age"]
print("Dictionary after removing an element:", my_dict)

# Modifying an existing value in the dictionary
my_dict["city"] = "San Francisco"
print("Dictionary after modifying an element:", my_dict)


# Creating and working with a set
my_set = {1, 2, 3, 4, 5}

# Adding an element to the set
my_set.add(6)
print("Set after adding an element:", my_set)

# Removing an element from the set
my_set.discard(3)  # discard does not throw an error if the element is not found
print("Set after removing an element:", my_set)

# Modifying elements in a set is not possible, since sets are unordered and unindexed.
# However, we can add or remove elements to change its contents.
