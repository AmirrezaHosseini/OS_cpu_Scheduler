import copy

import task


def SortHRRN(q, time, tasks):
    return q.sort(key=lambda x: (((time + x[1]) / x[1]), -tasks.index(x)), reverse=True)


def HRRN(tasks):
    Qtask = copy.deepcopy(tasks)
    time = 0

    print("Start Highest Response Ratio next")
    print("Ready Queue ")

    while len(Qtask) > 0:
        Qtask.sort(key=lambda x: (((time + x[1]) / x[1]), -tasks.index(x)), reverse=True)
        print("Next Task ")
        while Qtask[0][1] > 0:
            Qtask[0][1] -= 1
            print(str(time) + ': task ' + Qtask[0][0] + ', left overtime : ' + str(Qtask[0][1]))
            time += 1
        Qtask.pop(0)


def shortestJobFirst(tasks):
    Qtask = copy.deepcopy(tasks)
    time = 0
    Qtask.sort(key=lambda x: x[1])
    print("start shortestJobFirst")
    print("Ready Queue ")

    for i in Qtask:
        print("Next Task ")
        while i[1] > 0:
            i[1] -= 1
            time += 1
            print(str(time) + ': task ' + i[0] + ', left overtime : ' + str(i[1]))


def FCFS(tasks):
    Qtask = copy.deepcopy(tasks)
    s = 0
    print('FCFS Start')
    print("Ready Queue ")

    for i in Qtask:
        print("Next Task ")
        while i[1] > 0:
            i[1] -= 1
            s += 1
            print(str(s) + ': task ' + i[0] + ', left overtime : ' + str(i[1]))

    print('FCFS Finish\n\n')


def RoundRobin(tasks, quantum):
    Qtask = copy.deepcopy(tasks)
    time = 0

    print("Start RoundRobin")
    print("Ready Queue ")

    while len(Qtask) > 0:
        finished = False
        for i in range(quantum):
            Qtask[0][1] -= 1
            time += 1
            print(str(time) + ': task ' + Qtask[0][0] + ', left overtime : ' + str(Qtask[0][1]))

            if Qtask[0][1] == 0:
                finished = True
                break

        tt = Qtask.pop(0)
        if not finished:
            Qtask.append(tt)


if __name__ == '__main__':
    algorithm = str(input())

    n = int(input())
    tasks = []
    quantum = 0
    for i in range(n):
        tasks.append(input().split(' '))
        tasks[i][1] = int(tasks[i][1])

    if algorithm == "hrrn":
        HRRN(tasks)
    elif algorithm == "sjf":
        shortestJobFirst(tasks)
    elif algorithm == "fcfs":
        FCFS(tasks)
    elif algorithm == "rr":
        RoundRobin(tasks, 1)
