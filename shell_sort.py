import time

import psutil


process = psutil.Process()


def shell_sort(elements):
    print('\t-----  Shell Sort Algorithm Analyses  -----\n')
    length = len(elements)
    gap = length//2  # Define initial GAP

    # Process monitoring
    cpu_avg = []
    memory_avg = []

    start = time.time()

    # Start looping through the initial gap
    while gap > 0:

        # From current gap go through elements
        for i in range(gap, length):
            aux = elements[i]
            j = i

            # Compare and Swap items with gap index interval
            while j >= gap and aux < elements[j-gap]:
                elements[j] = elements[j-gap]
                j -= gap

            elements[j] = aux

        gap = gap // 2

        # Monitoring
        cpu_avg.append(process.cpu_percent())
        memory_avg.append(process.memory_percent())

    end = time.time()

    print("TOTAL TIME: {}".format(end - start))
    print("\n -- CPU USAGE - {}".format(sum(cpu_avg)/len(cpu_avg)))
    print(" -- MEMORY USAGE - {}".format(sum(memory_avg)/len(memory_avg)))
    print('\n\t-----         END Shell Sort        -----\n\n')

    return elements
