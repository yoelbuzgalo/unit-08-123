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

def merge(left_list, right_list):
    merged = []
    i1 = 0
    i2 = 0

    while (i1 < len(left_list)) and (i2 < len(right_list)):
        if left_list[i1] <= right_list[i2]:
            merged.append(left_list[i1])
            i1 += 1
        else:
            merged.append(right_list[i2])
            i2 += 1
    if i1 != len(left_list):
        merged += left_list[i1:]
    else:
        merged += right_list[i2:]

    return merged

def split(a_list):
    mid_point = (len(a_list)+1)//2
    slice_1 = a_list[:mid_point]
    slice_2 = a_list[mid_point:]
    return slice_1, slice_2

def merge_sort(a_list):
    if len(a_list) < 2:
        return a_list
    else:
        l_list, r_list = split(a_list)
        sorted_left = merge_sort(l_list)
        sorted_right = merge_sort(r_list)
        merged = merge(sorted_left, sorted_right)
        return merged
        # return merge (merge_sort(left, merge_sort(right)))

def partition(a_list, pivot):

    less, same, more = [], [], []

    for value in a_list:
        if value < pivot:
            less.append(value)
        elif value == pivot:
            same.append(value)
        elif value > pivot:
            more.append(value)

    return less, same, more

def quicksort(a_list):
    if len(a_list) < 2:
        return a_list
    else:
        pivot = a_list[0]
        less, same, more = partition(a_list, pivot)
        sorted_less = quicksort(less)
        sorted_more = quicksort(more)
        return sorted_less + same + sorted_more

    

def main():
    # print(random_list(100))
    # some_list = list(range(10, 0, -1))
    # print(some_list)
    # print(shift(some_list,9))
    # print(insertion_sort(some_list))
    # print(insertion_sort_wo_swap(some_list))
    # print(split(some_list))

    print(merge([3,4,8], [1,5,9,11]))


if __name__ == "__main__":
    main()