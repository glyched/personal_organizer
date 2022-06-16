num_of_tasks = int(input('how many tasks are you required to do today:'))
tasks = []
times = []
y = 0
for i in range(num_of_tasks):
    x = input('enter task:')
    time = input('how much time do you take to do this(hrs):')
    tasks.append(x)
    times.append(time)
print(' is the following correct?')
for i in range(num_of_tasks):
    print('task: ', tasks[i])
    print('time: ', times[i])


