def merge_dicts(dict1, dict2):
    merged_dict = {**dict1, **dict2}
    return merged_dict

# Taking input for the first dictionary
dict1 = {}
num_entries1 = int(input("Enter the number of key-value pairs for the first dictionary: "))
for _ in range(num_entries1):
    key = input("Enter key: ")
    value = input("Enter value: ")
    dict1[key] = value

# Taking input for the second dictionary
dict2 = {}
num_entries2 = int(input("Enter the number of key-value pairs for the second dictionary: "))
for _ in range(num_entries2):
    key = input("Enter key: ")
    value = input("Enter value: ")
    dict2[key] = value

# Merging the dictionaries
merged_dictionary = merge_dicts(dict1, dict2)

print("Merged dictionary:", merged_dictionary)
