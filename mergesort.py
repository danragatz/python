import random

def sort_helper(s_list, beg, end):
    #base case: 1 item in list
    if (end - beg) > 1:
        mid = (beg + end) // 2

        sort_helper(s_list, beg, mid)
        sort_helper(s_list, mid, end)

        # working list
        w_list = list(alist[beg:end])
        
        # merge back together    
        merge_helper(s_list, beg, mid, end, w_list)
    
def merge_helper(s_list, beg, mid, end, w_list):
    i = beg
    j = mid
    k = 0
    while i < mid and j < end:
        if s_list[i] < s_list[j]:
            w_list[k] = s_list[i]
            i += 1
        else:
            w_list[k] = s_list[j]
            j += 1
        k += 1

    while i < mid:
        w_list[k] = s_list[i]
        i += 1
        k += 1

    while j < end:
        w_list[k] = s_list[j]
        j += 1
        k += 1

    # copy sorted list back to original
    i = beg
    j = 0
    while i < end:
        s_list[i] = w_list[j]
        i += 1
        j += 1
    
def merge_sort(alist):
    # split and sort
    sort_helper(alist, 0, len(alist))

# test mergesort    
#alist = [8,4,27,7]
alist = [x for x in range(1000)]
random.shuffle(alist)
print(alist)
merge_sort(alist)
print(alist)
