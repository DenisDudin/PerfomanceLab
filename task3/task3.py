from os import listdir
from os.path import isfile, join
import sys

if __name__ == '__main__':
    directory = sys.argv[1]
    queue_in_shop = []
    files_queue = [f for f in listdir(directory) if isfile(join(directory, f))]

    for i in range(5):
        queue_in_checkout = []
        if 'Cash' in files_queue[i]:
            with open(files_queue[i], 'r') as f:
                queue_in_checkout = [float(line) for line in f.readlines()]

            if queue_in_shop:
                for i in range(len(queue_in_checkout)):
                    queue_in_shop[i] += queue_in_checkout[i]
            else:
                queue_in_shop = queue_in_checkout

    max_queue = 0
    for i in range(len(queue_in_shop)):
        if max_queue < queue_in_shop[i]:
            max_queue = queue_in_shop[i]
            number_interval = i
    print(number_interval + 1)