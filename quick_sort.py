import time


def swap(elements, left, right):
    elements[left], elements[right] = elements[right], elements[left]


def partition(elements, left, right, pivot):
    while left <= right:
        while elements[left] < pivot:
            left += 1
        while elements[right] > pivot:
            right -= 1
        if left <= right:
            swap(elements, left, right)
            left += 1
            right -= 1
    return left


def quick_sort(elements, left, right):
    if left >= right:
        return
    
    pivot = elements[(left+right)//2]
    index = partition(elements, left, right, pivot)
    quick_sort(elements, left, index - 1)
    quick_sort(elements, index, right)


def run_quick_sort(elements):
    print('\t-----  Quick Sort Algorithm Analyses  -----\n')
    start = time.time()

    quick_sort(elements, 0, len(elements) - 1)

    end = time.time()
    print("TOTAL TIME: {}".format(end - start))
    print('\n\t-----         END Quick Sort        -----\n\n')

    return elements
