def in_place_reverse(a_list):
    '''
    This function reverses a list without using additional memory
    '''
    for i in range(len(a_list)):
        a_list.insert(i, a_list.pop())
    return a_list

# Time complexity of in_place_reverse is O(n) because it has to run one for loop to iterate over indexes and insert what it has popped

def main(): 
    some_list = [x for x in range(100)]
    a_list= in_place_reverse(some_list)
    print(a_list)

    table = make_multiplication_table()
    for row in table:
        print(row)

def make_multiplication_table():
    return [[x*y for x in range(1,10)] for y in range(1,10)]

if __name__ == "__main__":
    main()
    