def add_value_to_list(my_list, value):
    for i in range(len(my_list)):
        a = my_list[i] + value
        my_list[i] = a

        # uproszczone --> my_list[i] += value  # zamiast my_list[i] = my_list[i] + value

    return my_list

new_list = add_value_to_list([1, 2, 3], 1 )
print(new_list)

# [1, 2, 3], 1 --> [2, 3, 4]
