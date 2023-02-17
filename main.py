def read_list_numbers():
    input_list = []

    quantity_numbers = int(input("Enter quantity numbers : "))

    for i in range(quantity_numbers):
        input_list.append(int(input()))
    # input_list = [9, 7, -1, 5, 4, 12, 7, 8, 1, -10, 3]

    return input_list


def get_maximum_sequence(initial_list):
    sorted_list = []

    for number in initial_list:
        sorted_list.append(number)

    sorted_list.sort()

    result_beginning_index = 0
    maximum_length_sequence = 0

    current_beginning_index = 0
    current_length_sequence = 1

    for i in range(1, len(initial_list)):
        if sorted_list[i - 1] + 1 != sorted_list[i]:
            if current_length_sequence > maximum_length_sequence:
                result_beginning_index = current_beginning_index
                maximum_length_sequence = current_length_sequence
            current_beginning_index = i
            current_length_sequence = 1
        else:
            current_length_sequence += 1

    if current_length_sequence > maximum_length_sequence:
        if current_beginning_index != result_beginning_index:
            result_beginning_index = current_beginning_index
        maximum_length_sequence = current_length_sequence

    result_list = []

    for index in range(result_beginning_index, result_beginning_index + maximum_length_sequence):
        result_list.append(sorted_list[index])

    return result_list


def print_result(r_list, i_list):
    print("Resulting list: ", r_list)
    print("Initial list: ", i_list)


list = read_list_numbers()
print_result(get_maximum_sequence(list), list)
