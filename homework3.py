#List tasks


# 1. Count Occurrences
def count_occurrences(lst, element):
    return lst.count(element)



# 2. Sum of Elements
def sum_of_elements(lst):
    return sum(lst)



# 3. Max Element
def max_element(lst):
    return max(lst)



# 4. Min Element
def min_element(lst):
    return min(lst)



# 5. Check Element
def check_element(lst, element):
    return element in lst



# 6. First Element
def first_element(lst):
    if len(lst) == 0:
        return None
    return lst[0]



# 7. Last Element
def last_element(lst):
    if len(lst) == 0:
        return None
    return lst[-1]



# 8. Slice List (first three elements)
def slice_list(lst):
    return lst[:3]



# 9. Reverse List
def reverse_list(lst):
    return lst[::-1]



# 10. Sort List
def sort_list(lst):
    return sorted(lst)



# 11. Remove Duplicates
def remove_duplicates(lst):
    return list(set(lst))



# 12. Insert Element
def insert_element(lst, index, element):
    lst.insert(index, element)
    return lst



# 13. Index of Element (first occurrence)
def index_of_element(lst, element):
    if element in lst:
        return lst.index(element)
    return -1



# 14. Check for Empty List
def is_empty(lst):
    return len(lst) == 0



# 15. Count Even Numbers
def count_even_numbers(lst):
    count = 0
    for x in lst:
        if x % 2 == 0:
            count += 1
    return count



# 16. Count Odd Numbers
def count_odd_numbers(lst):
    count = 0
    for x in lst:
        if x % 2 != 0:
            count += 1
    return count



# 17. Concatenate Lists
def concatenate_lists(lst1, lst2):
    return lst1 + lst2



# 18. Find Sublist
def find_sublist(lst, sublist):
    n = len(sublist)
    for i in range(len(lst) - n + 1):
        if lst[i:i+n] == sublist:
            return True
    return False



# 19. Replace Element (first occurrence)
def replace_element(lst, old, new):
    if old in lst:
        index = lst.index(old)
        lst[index] = new
    return lst



# 20. Find Second Largest
def second_largest(lst):
    unique = list(set(lst))
    unique.sort()
    return unique[-2]



# 21. Find Second Smallest
def second_smallest(lst):
    unique = list(set(lst))
    unique.sort()
    return unique[1]



# 22. Filter Even Numbers
def filter_even(lst):
    return [x for x in lst if x % 2 == 0]



# 23. Filter Odd Numbers
def filter_odd(lst):
    return [x for x in lst if x % 2 != 0]



# 24. List Length
def list_length(lst):
    return len(lst)



# 25. Create a Copy
def copy_list(lst):
    return lst.copy()



# 26. Get Middle Element(s)
def get_middle(lst):
    n = len(lst)
    if n % 2 == 1:
        return lst[n // 2]
    else:
        return (lst[n//2 - 1], lst[n//2])



# 27. Find Maximum of Sublist
def max_of_sublist(lst, start, end):
    return max(lst[start:end])



# 28. Find Minimum of Sublist
def min_of_sublist(lst, start, end):
    return min(lst[start:end])



# 29. Remove Element by Index
def remove_by_index(lst, index):
    if 0 <= index < len(lst):
        lst.pop(index)
    return lst



# 30. Check if List is Sorted
def is_sorted(lst):
    return lst == sorted(lst)



# 31. Repeat Elements
def repeat_elements(lst, n):
    result = []
    for x in lst:
        result.extend([x] * n)
    return result



# 32. Merge and Sort
def merge_and_sort(lst1, lst2):
    return sorted(lst1 + lst2)



# 33. Find All Indices
def find_all_indices(lst, element):
    return [i for i in range(len(lst)) if lst[i] == element]



# 34. Rotate List to the Right
def rotate_list(lst, k):
    k = k % len(lst)
    return lst[-k:] + lst[:-k]



# 35. Create Range List
def create_range_list(start, end):
    return list(range(start, end + 1))



# 36. Sum of Positive Numbers
def sum_positive(lst):
    return sum(x for x in lst if x > 0)



# 37. Sum of Negative Numbers
def sum_negative(lst):
    return sum(x for x in lst if x < 0)



# 38. Check Palindrome
def is_palindrome(lst):
    return lst == lst[::-1]



# 39. Create Nested List
def create_nested_list(lst, size):
    return [lst[i:i+size] for i in range(0, len(lst), size)]



# 40. Get Unique Elements in Order
def unique_in_order(lst):
    result = []
    for x in lst:
        if x not in result:
            result.append(x)
    return result

#----------------------------------------------------------
#Tuple tasks

# 1. Count Occurrences
def count_occurrences(tup, element):
    return tup.count(element)



# 2. Max Element
def max_element(tup):
    return max(tup)



# 3. Min Element
def min_element(tup):
    return min(tup)



# 4. Check Element
def check_element(tup, element):
    return element in tup



# 5. First Element
def first_element(tup):
    if len(tup) == 0:
        return None
    return tup[0]



# 6. Last Element
def last_element(tup):
    if len(tup) == 0:
        return None
    return tup[-1]



# 7. Tuple Length
def tuple_length(tup):
    return len(tup)



# 8. Slice Tuple (first three elements)
def slice_tuple(tup):
    return tup[:3]



# 9. Concatenate Tuples
def concatenate_tuples(tup1, tup2):
    return tup1 + tup2



# 10. Check if Tuple is Empty
def is_empty(tup):
    return len(tup) == 0



# 11. Get All Indices of Element
def all_indices(tup, element):
    return [i for i in range(len(tup)) if tup[i] == element]



# 12. Find Second Largest
def second_largest(tup):
    unique = list(set(tup))
    unique.sort()
    return unique[-2]



# 13. Find Second Smallest
def second_smallest(tup):
    unique = list(set(tup))
    unique.sort()
    return unique[1]



# 14. Create a Single Element Tuple
def single_element_tuple(element):
    return (element,)



# 15. Convert List to Tuple
def list_to_tuple(lst):
    return tuple(lst)



# 16. Check if Tuple is Sorted
def is_sorted(tup):
    return tup == tuple(sorted(tup))



# 17. Find Maximum of Subtuple
def max_of_subtuple(tup, start, end):
    return max(tup[start:end])



# 18. Find Minimum of Subtuple
def min_of_subtuple(tup, start, end):
    return min(tup[start:end])



# 19. Remove Element by Value (first occurrence)
def remove_element(tup, element):
    lst = list(tup)
    if element in lst:
        lst.remove(element)
    return tuple(lst)



# 20. Create Nested Tuple
def create_nested_tuple(tup, size):
    return tuple(tup[i:i+size] for i in range(0, len(tup), size))



# 21. Repeat Elements
def repeat_elements(tup, n):
    result = []
    for x in tup:
        result.extend([x] * n)
    return tuple(result)



# 22. Create Range Tuple
def create_range_tuple(start, end):
    return tuple(range(start, end + 1))



# 23. Reverse Tuple
def reverse_tuple(tup):
    return tup[::-1]



# 24. Check Palindrome
def is_palindrome(tup):
    return tup == tup[::-1]



# 25. Get Unique Elements in Order
def unique_in_order(tup):
    result = []
    for x in tup:
        if x not in result:
            result.append(x)
    return tuple(result)


#--------------------------------------------------------
#Set tasks

# 1. Union of Sets
set1 = {1, 2, 3}
set2 = {3, 4, 5}
union_set = set1 | set2
print("1.", union_set)

# 2. Intersection of Sets
intersection_set = set1 & set2
print("2.", intersection_set)

# 3. Difference of Sets
difference_set = set1 - set2
print("3.", difference_set)

# 4. Check Subset
is_subset = set1.issubset(set2)
print("4.", is_subset)

# 5. Check Element
element_exists = 2 in set1
print("5.", element_exists)

# 6. Set Length
set_length = len(set1)
print("6.", set_length)

# 7. Convert List to Set
lst = [1, 2, 2, 3, 4, 4]
unique_set = set(lst)
print("7.", unique_set)

# 8. Remove Element
set1.discard(2)
print("8.", set1)

# 9. Clear Set
empty_set = set1.copy()
empty_set.clear()
print("9.", empty_set)

# 10. Check if Set is Empty
is_empty = len(empty_set) == 0
print("10.", is_empty)

# 11. Symmetric Difference
symmetric_diff = set1 ^ set2
print("11.", symmetric_diff)

# 12. Add Element
set1.add(10)
print("12.", set1)

# 13. Pop Element
popped_element = set2.pop()
print("13.", popped_element)

# 14. Find Maximum
num_set = {5, 10, 3, 8}
maximum = max(num_set)
print("14.", maximum)

# 15. Find Minimum
minimum = min(num_set)
print("15.", minimum)

# 16. Filter Even Numbers
even_numbers = {x for x in num_set if x % 2 == 0}
print("16.", even_numbers)

# 17. Filter Odd Numbers
odd_numbers = {x for x in num_set if x % 2 != 0}
print("17.", odd_numbers)

# 18. Create a Set of a Range
range_set = set(range(1, 11))
print("18.", range_set)

# 19. Merge and Deduplicate Lists
list1 = [1, 2, 3]
list2 = [3, 4, 5]
merged_set = set(list1 + list2)
print("19.", merged_set)

# 20. Check Disjoint Sets
are_disjoint = set1.isdisjoint(set2)
print("20.", are_disjoint)

# 21. Remove Duplicates from a List
dup_list = [1, 1, 2, 3, 3, 4]
unique_list = list(set(dup_list))
print("21.", unique_list)

# 22. Count Unique Elements
unique_count = len(set(dup_list))
print("22.", unique_count)

# 23. Generate Random Set
import random
random_set = set(random.randint(1, 20) for _ in range(5))
print("23.", random_set)


#---------------------------------------------
#Dictionary tasks

#sample dictionary
my_dict = {"a": 1, "b": 2, "c": 2}
another_dict = {"c": 3, "d": 4}

# 1. Get Value
key = "a"
value = my_dict.get(key, "Key not found")
print("1.", value)

# 2. Check Key
is_present = key in my_dict
print("2.", is_present)

# 3. Count Keys
key_count = len(my_dict)
print("3.", key_count)

# 4. Get All Keys
all_keys = list(my_dict.keys())
print("4.", all_keys)

# 5. Get All Values
all_values = list(my_dict.values())
print("5.", all_values)

# 6. Merge Dictionaries
merged_dict = my_dict | another_dict
print("6.", merged_dict)

# 7. Remove Key
removed_value = my_dict.pop("b", "Key not found")
print("7.", removed_value)

# 8. Clear Dictionary
empty_dict = {}
print("8.", empty_dict)

# 9. Check if Dictionary is Empty
is_empty = len(empty_dict) == 0
print("9.", is_empty)

# 10. Get Key-Value Pair
key = "a"
key_value_pair = (key, my_dict[key]) if key in my_dict else None
print("10.", key_value_pair)

# 11. Update Value
my_dict["a"] = 10
print("11.", my_dict)

# 12. Count Value Occurrences
count_value = 2
value_occurrences = list(my_dict.values()).count(count_value)
print("12.", value_occurrences)

# 13. Invert Dictionary
inverted_dict = {v: k for k, v in my_dict.items()}
print("13.", inverted_dict)

# 14. Find Keys with Value
target_value = 2
keys_with_value = [k for k, v in my_dict.items() if v == target_value]
print("14.", keys_with_value)

# 15. Create Dictionary from Lists
keys = ["x", "y", "z"]
values = [1, 2, 3]
dict_from_lists = dict(zip(keys, values))
print("15.", dict_from_lists)

# 16. Check for Nested Dictionaries
nested_dict = {"a": 1, "b": {"x": 10}}
has_nested = any(isinstance(v, dict) for v in nested_dict.values())
print("16.", has_nested)

# 17. Get Nested Value
nested_value = nested_dict.get("b", {}).get("x")
print("17.", nested_value)

# 18. Create Default Dictionary
from collections import defaultdict
default_dict = defaultdict(int)
print("18.", default_dict["missing_key"])

# 19. Count Unique Values
unique_values_count = len(set(my_dict.values()))
print("19.", unique_values_count)

# 20. Sort Dictionary by Key
sorted_by_key = dict(sorted(my_dict.items()))
print("20.", sorted_by_key)

# 21. Sort Dictionary by Value
sorted_by_value = dict(sorted(my_dict.items(), key=lambda item: item[1]))
print("21.", sorted_by_value)

# 22. Filter by Value
filtered_dict = {k: v for k, v in my_dict.items() if v > 2}
print("22.", filtered_dict)

# 23. Check for Common Keys
common_keys = set(my_dict.keys()) & set(another_dict.keys())
print("23.", len(common_keys) > 0)

# 24. Create Dictionary from Tuple
tuple_data = (("a", 1), ("b", 2))
dict_from_tuple = dict(tuple_data)
print("24.", dict_from_tuple)

# 25. Get the First Key-Value Pair
first_pair = next(iter(my_dict.items()))
print("25.", first_pair)



