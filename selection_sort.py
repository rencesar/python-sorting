import psutil

from tqdm import trange


process = psutil.Process()


def selection_sort(elements):
    print('\t-----  Selection Sort Algorithm Analyses  -----\n')
    length = len(elements)

    # Process monitoring
    cpu_avg = []
    memory_avg = []

    for i in trange(length, desc="Main Loop"):
        min_index = i

        for j in range(i+1, length):
            if elements[j] < elements[min_index]:
                min_index = j

        elements[i], elements[min_index] = elements[min_index], elements[i]

        # Monitoring
        cpu_avg.append(process.cpu_percent())
        memory_avg.append(process.memory_percent())

    print("\n -- CPU USAGE - {}".format(sum(cpu_avg)/len(cpu_avg)))
    print(" -- MEMORY USAGE - {}".format(sum(memory_avg)/len(memory_avg)))
    print('\n\t-----         END Selection Sort        -----\n\n')

    return elements
