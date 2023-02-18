def read_list_numbers_from_file():
    initial_list = []

    with open('input.txt', 'r') as file:
        for number in file.readline().split(", "):
            initial_list.append(int(number))
    # initial_list = [9, 7, -1, 5, 4, 12, 7, 8, 1, -10, 3]

    return initial_list


def get_maximum_sequence(initial_list):
    sorted_list = list(initial_list)

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


def get_str_from_list(name_list, current_list):
    result_str = name_list

    for i in range(len(current_list) - 1):
        result_str += str(current_list[i]) + ", "

    result_str += str(current_list[-1])
    result_str += "\n"

    return result_str


def print_result_to_file(result_list, initial_list):
    with open('output.txt', 'w') as file:
        file.write(get_str_from_list("Resulting list: ", result_list))
        file.write(get_str_from_list("Initial list: ", initial_list))


def main():
    initial_list = read_list_numbers_from_file()
    print_result_to_file(get_maximum_sequence(initial_list), initial_list)


main()
