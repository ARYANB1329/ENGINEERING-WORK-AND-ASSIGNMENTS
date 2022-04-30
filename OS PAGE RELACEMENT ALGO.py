#  FIFO page replacement in Operating Systems.
# ARYAN SIDDHABATHULA 29 B13


from queue import Queue
def pageFaults(pages, n, capacity):
    s = set()
    indexes = Queue()
    page_faults = 0
    for i in range(n):


        if (len(s) < capacity):
            if (pages[i] not in s):
                s.add(pages[i])
                page_faults += 1
                indexes.put(pages[i])

        else:
            if (pages[i] not in s):
                val = indexes.queue[0]
                indexes.get()
               # Remove the indexes page
                s.remove(val)
                # insert the current page
                s.add(pages[i])
                # push the current page into
                # the queue
                indexes.put(pages[i])
                # Increment page faults
                page_faults += 1

    return page_faults



pages = list(map(int, input("Enter values: ").split()))
n = len(pages)
capacity = int(input("Capacity:"))
print(pageFaults(pages, n, capacity))