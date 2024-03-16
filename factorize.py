import logging
from time import time
from multiprocessing import Pool, cpu_count


logger = logging.getLogger()
stream_handler = logging.StreamHandler()
logger.addHandler(stream_handler)
logger.setLevel(logging.DEBUG)


def factorize(*number):
    my_div_list = list()
    for num in number:
        my_numb_list = list()
        for i in range(1, num + 1):
            if num % i == 0:
                my_numb_list.append(i)
        my_div_list.append(my_numb_list)
    return my_div_list


if __name__ == '__main__':
    start_time = time()

    a, b, c, d  = factorize(128, 255, 99999, 10651060)

    assert a == [1, 2, 4, 8, 16, 32, 64, 128]
    assert b == [1, 3, 5, 15, 17, 51, 85, 255]
    assert c == [1, 3, 9, 41, 123, 271, 369, 813, 2439, 11111, 33333, 99999]
    assert d == [1, 2, 4, 5, 7, 10, 14, 20, 28, 35, 70, 140, 76079, 152158, 304316, \
                 380395, 532553, 760790, 1065106, 1521580, 2130212, 2662765, 5325530, 10651060]
    
    end_time = time()
    logging.debug(f'Time: {end_time - start_time:.6f} sec')

    my_cores = cpu_count()
    with Pool(my_cores) as pl:
        start_tm = time()
        results = pl.map(factorize, (128, 255, 99999, 10651060))
        end_tm = time()
        logging.debug(f'Time for {my_cores} core(s): {end_tm - start_tm:.6f} sec')
        pl.close()
        pl.join()
