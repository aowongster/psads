# write min search algorithms O(n^2) and O(n)

import time

def min_n2(arr):
    """write an algorithm that compares each element against itself"""
    low = arr[0]
    for item in arr:
        for c_item in arr:
            if item == c_item: # skip same comparisons
                continue

            local_low = c_item
            if item < c_item:  # compare elements to eachother
                local_low = item

            if local_low < low: # compare local low vs global low
                low = local_low

    return low

def min_n(arr):
    """write a min search algorithm that takes O(n)"""
    low = arr[0]
    for item in arr:
        if item < low:
            low = item
    return low

if __name__ == "__main__":

    # sample run times
    # 1
    # Run time O(n^2):  8.16705393791
    # 1
    # Run time O(n):  0.000407934188843
    # [Finished in 8.287s]

    items = [i for i in xrange(10000, 0, -1)]

    n2_start = time.time()
    print min_n2(items)
    n2_stop = time.time()
    print "Run time O(n^2): ", n2_stop - n2_start

    n_start = time.time()
    print min_n(items)
    n_stop = time.time()
    print "Run time O(n): ", n_stop - n_start
