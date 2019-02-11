import psutil

from tqdm import trange


process = psutil.Process()


def insertion_sort(elements):
    print('\t-----  Insertion Sort Algorithm Analyses  -----\n')
    length = len(elements)

    # Process monitoring
    cpu_avg = []
    memory_avg = []

    # Loop over all elements
    for i in trange(1, length, desc="Main Loop"):
        item = elements[i]
        j = i
        while j > 0 and item < elements[j-1]:
            elements[j] = elements[j-1]
            j -= 1

        elements[j] = item

        # Monitoring
        cpu_avg.append(process.cpu_percent())
        memory_avg.append(process.memory_percent())

    print("\n -- CPU USAGE - {}".format(sum(cpu_avg)/len(cpu_avg)))
    print(" -- MEMORY USAGE - {}".format(sum(memory_avg)/len(memory_avg)))
    print('\n\t-----         END Insertion Sort        -----\n\n')

    return elements
