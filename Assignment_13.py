import threading
import time

def count_numbers(limit):
    for i in range(1, limit + 1):
        print(f"Counting: {i}")
        time.sleep(0.1)

def calculate_squares(numbers):
    for n in numbers:
        print(f"Square of {n}: {n * n}")
        time.sleep(0.1)

def calculate_cubes(numbers):
    for n in numbers:
        print(f"Cube of {n}: {n ** 3}")
        time.sleep(0.1)

def main():
    nums = [1, 2, 3, 4, 5]
    
    t1 = threading.Thread(target=count_numbers, args=(5,))
    t2 = threading.Thread(target=calculate_squares, args=(nums,))
    t3 = threading.Thread(target=calculate_cubes, args=(nums,))
    
    t1.start()
    t2.start()
    t3.start()
    
    t1.join()
    t2.join()
    t3.join()

if __name__ == "__main__":
    main()
