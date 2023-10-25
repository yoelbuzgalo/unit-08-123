def linear_search(an_array, target):
    """
    Searches an array for a target value.
    """
    for index in range(len(an_array)):
        if an_array[index] == target:
            return index
    return None

def binary_search(an_array, target, start=None, end=None):
    if start is None:
        start = 0
    if end is None:
        end = len(an_array) - 1

    if start > end:
        return None
    else:
        mid = (start + end) // 2
        # print("target =", target, "start =", start, "end =", end,
        #     "mid =", mid, "value =", an_array[mid])
        if an_array[mid] == target:
            return mid
        elif an_array[mid] < target:
            start = mid + 1
            return binary_search(an_array, target, start, end)
        else:
            end = mid - 1
            return binary_search(an_array, target, start, end)

def main():
    an_array = list(range(1, 10000001))
    print(binary_search(an_array, 1))
    print(binary_search(an_array, 5000000))
    print(binary_search(an_array, 10000000))
    print(binary_search(an_array, 0))

if __name__ == "__main__":
    main()