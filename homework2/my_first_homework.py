my_list = [7, 8, 9, 2, 3, 1, 4, 10, 5, 6]
print(sorted(my_list))  # prints my_list sorted in ascending order
print(sorted(my_list, reverse=True))  # prints my_list sorted in descending order
print(my_list)  # prints my_list
print(sorted(my_list)[1::2])  # prints only even numbers from my_list
print(sorted(my_list)[0::2])  # prints only uneven numbers from my_list
print(sorted(my_list)[2::3])  # prints only multiples of 3 from my_list
