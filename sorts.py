import random

def random_list(length):
    return [random.randint(0,length) for x in range(length)]

def swap(a_list, a, b):
    temp_val = a_list[a]
    a_list[a] = a_list[b]
    a_list[b] = temp_val
    return a_list

def shift(a_list, index):
    while index > 0 and (a_list[index] < a_list[index-1]):
        swap(a_list, index, index-1)
        index -= 1
    return a_list

def shift_wo_swap(a_list, index):
    target = a_list[index]
    while index > 0:
        if target < a_list[index-1]:
            a_list[index] = a_list[index-1]
            index -= 1
        else:
            break
    a_list[index] = target

def insertion_sort(a_list):
    for i in range(1, len(a_list)):
        shift(a_list, i)
    return a_list

def insertion_sort_wo_swap(a_list):
    for i in range(1, len(a_list)):
        shift_wo_swap(a_list, i)
    return a_list

def split(a_list):
    mid_point = len(a_list)//2
    slice_1 = a_list[:mid_point]
    slice_2 = a_list[mid_point:]
    return slice_1, slice_2

def main():
    # print(random_list(100))
    some_list = list(range(10, 0, -1))
    print(some_list)
    # print(shift(some_list,9))
    # print(insertion_sort(some_list))
    print(insertion_sort_wo_swap(some_list))


if __name__ == "__main__":
    main()