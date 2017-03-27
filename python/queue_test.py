import multiprocessing as mp

def washer(dishes, output):
    for dish in dishes:
        print('Washing', dish, 'dish')
        output.put(dish)


def dryer(input):
    while True:
        dish = input.get()
        print('Drying', dish, 'dish')
        input.task_done()


# dish_queue = mp.JoinableQueue() # get error undefined JoinableQueue
dish_queue = mp.Queue() 
dryer_proc = mp.Process(target=dryer, args=(dish_queue,))
dryer_proc.deamon = True
dryer_proc.start()


dishes = ['salad', 'bread', 'entree', 'dessert']
washer(dishes, dish_queue)
dish_queue.join()
