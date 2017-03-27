# import multiprocessing as mp
from pathos.multiprocessing import ProcessingPool as mp


L = 1000

def calc():
    total = 0
    for i in range(L):
        for j in range(L):
            total += i*j

    print(total)


def calc_multi():
    proc = 4

    def subcalc(p):
        subtotal = 0
        ini = L * p / proc
        fin = L * (p + 1) / proc

        for i in range(int(ini), int(fin)):
            for j in range(L):
                subtotal += i * j

        return subtotal

    pool = mp.Pool(proc)

    callback = pool.map(subcalc, range(4))

    total = sum(callback)

    print(total)


calc()
calc_multi()
