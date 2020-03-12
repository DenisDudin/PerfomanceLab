import sys


if __name__ == '__main__':
    file = sys.argv[1]
    a=[]
    with open(file, 'r') as f:
        for line in f:
                a.append([x for x in line.split()])

    times = []
    for call in a:
        startTime, endTime = call
        times.append((startTime, 'start'))
        times.append((endTime, 'end'))
    times = sorted(times)

    max_start = []
    max_end = []
    count = 0
    maxCount = 0
    for i in range(len(times)):
        if times[i][1] == 'start':
            count += 1
            if maxCount <= count and len(max_end) == 0:
                max_start = []
                max_start.append(times[i])
            elif maxCount < count and max_end[-1][0] != times[i][0]:
                max_start = []
                max_start.append(times[i])
            elif maxCount <= count and max_end[-1][0] != times[i][0]:
                max_start.append(times[i])
        else:
            if maxCount == count and times[i+1][1] != 'start':
                max_end.append(times[i])
            count -= 1
        maxCount = max(count, maxCount)

    for i in range(len(max_end)):
        print(max_start[i][0], max_end[i][0])
