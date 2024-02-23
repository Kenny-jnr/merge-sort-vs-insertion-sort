import timeit
import random


# making the sorting algorithms

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key


def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]

        merge_sort(left_half)
        merge_sort(right_half)

        i = j = k = 0

        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            j += 1

        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1


# experiment
if __name__ == '__main__':
    values_of_n = [10, 50, 100, 500, 1000]

    for n in values_of_n:
        random_array = random.sample(range(1, 10000), n)
        num_repeats = 1000

        # checking time for insertion sort
        time_insertion = timeit.timeit(lambda: insertion_sort(random_array.copy()), number=num_repeats)

        # checking time for merge sort
        time_merge = timeit.timeit(lambda: merge_sort(random_array.copy()), number=num_repeats)

        print(f"n = {n}: Insertion sort time = {time_insertion:.8f} seconds, Merge sort Time = {time_merge:.8f} seconds")
