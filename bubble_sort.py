import psutil

from tqdm import tqdm


process = psutil.Process()


def bubble_sort(elements):
    print('\t----- Bubble Sort Algorithm Analyses   -----\n')
    length = len(elements)
    repeat = True

    # Process monitoring
    cpu_avg = []
    memory_avg = []
    perc_element = (1 / length) * 100
    with tqdm(total=100, desc="Main Loop") as loadbar:

        loadbar.update(perc_element)

        # Check if had any swap during the inside loop if yes continue otherwise already sorted
        while repeat:
            repeat = False

            # Loop over the elements
            for i in range(1, length):

                # Compare every par of elements
                if elements[i - 1] > elements[i]:
                    elements[i-1], elements[i] = elements[i], elements[i-1]
                    repeat = True

                    # Get the last swap index and assume the last part of the array is already sorted
                    length = i

            # Monitoring
            cpu_avg.append(process.cpu_percent())
            memory_avg.append(process.memory_percent())

            loadbar.update(perc_element)

    print("\n -- CPU USAGE - {}".format(sum(cpu_avg)/len(cpu_avg)))
    print(" -- MEMORY USAGE - {}".format(sum(memory_avg)/len(memory_avg)))
    print('\n\t-----         END Bubble Sort        -----\n\n')

    return elements
