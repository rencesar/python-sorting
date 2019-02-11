from random import randint

from bubble_sort import bubble_sort
from insertion_sort import insertion_sort
from merge_sort import run_merge_sort
from quick_sort import run_quick_sort
from selection_sort import selection_sort
from shell_sort import shell_sort

data = [randint(1, 5000) for _ in range(20000)]

def random_values():
    return data.copy()


# Pay attention on the difference of it/s at the start of the sort and at the end
bubble_sort(random_values())

# Pay attention on the difference of it/s at the start of the sort and at the end
selection_sort(random_values())

insertion_sort(random_values())

shell_sort(random_values())

run_quick_sort(random_values())

run_merge_sort(random_values())
