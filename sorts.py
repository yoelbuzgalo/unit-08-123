import random

def random_list(length):
    return [random.randint(0,length) for x in range(length)]

def main():
    print(random_list(100))

if __name__ == "__main__":
    main()