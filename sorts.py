import random

def random_list(length):
    return [random.randint(0,length) for x in range(length)]

def swap(a_list, a, b):
    temp_val = a_list[a]
    a_list[a] = a_list[b]
    a_list[b] = temp_val
    return a_list

def main():
    # print(random_list(100))
    some_list = [x for x in range(10)]
    print(swap(some_list, 2, 3))


if __name__ == "__main__":
    main()