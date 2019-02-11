import time


def swap(elements, left, right):
    elements[left], elements[right] = elements[right], elements[left]


def merge(elements_1, elements_2):
    # Merge Two arrays into one
    elements_aux = []

    while len(elements_1) and len(elements_2):
        if elements_1[0] < elements_2[0]:
            elements_aux.append(elements_1[0])
            elements_1.pop(0)
        else:
            elements_aux.append(elements_2[0])
            elements_2.pop(0)

    if len(elements_1) == 0:
        elements_aux += elements_2
    else:
        elements_aux += elements_1

    return elements_aux


def merge_sort(elements):
    length = len(elements)
    if length <= 1:
        return elements

    half = length//2
    return merge(merge_sort(elements[:half]), merge_sort(elements[half:]))


def run_merge_sort(elements):
    print('\t-----  Merge Sort Algorithm Analyses  -----\n')
    start = time.time()

    elements = merge_sort(elements)

    end = time.time()
    print("TOTAL TIME: {}".format(end - start))
    print('\n\t-----         END Merge Sort        -----\n\n')

    return elements
