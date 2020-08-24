# python3


def max_pairwise_product(numbers):
    max_index = 0
    for i, number in enumerate(numbers):
        if number > numbers[max_index]:
            max_index = i
    if max_index == 0:
        second_max_index = 1
    else:
        second_max_index = 0
    for i, number in enumerate(numbers):
        if i != max_index and number > numbers[second_max_index]:
            second_max_index = i

    return numbers[max_index] * numbers[second_max_index]


if __name__ == '__main__':
    input_n = int(input())
    input_numbers = [int(x) for x in input().split()]
    print(max_pairwise_product(input_numbers))
