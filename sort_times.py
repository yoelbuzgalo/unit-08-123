import sorts
import time

def sort_function_timer(a_list, sort_function):
    start = time.perf_counter()
    sort_function(a_list)
    end = time.perf_counter()
    return (end-start)

def main():
    length = 3000
    a_list = list(range(length))

    # Insertion sort WITH swap
    print(sort_function_timer(a_list, sorts.insertion_sort))
    a_list = sorts.random_list(3000)
    print(sort_function_timer(a_list, sorts.insertion_sort))
    a_list = list(range(length, 0))
    print(sort_function_timer(a_list, sorts.insertion_sort))

    # Insertion sort WITHOUT swap
    print(sort_function_timer(a_list, sorts.insertion_sort_wo_swap))
    a_list = sorts.random_list(3000)
    print(sort_function_timer(a_list, sorts.insertion_sort_wo_swap))
    a_list = list(range(length, 0))
    print(sort_function_timer(a_list, sorts.insertion_sort_wo_swap))

if __name__ == "__main__":
    main()