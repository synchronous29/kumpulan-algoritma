def binary_search(data, search_val, min_idx, max_idx):
    if max_idx < min_idx:
        print("%d not found in list"%search_val)
        return -1

    mid_idx = (min_idx + max_idx) // 2
    if data[mid_idx] > search_val:
        return binary_search(data, search_val, min_idx, mid_idx - 1)
    elif data[mid_idx] < search_val:
        return binary_search(data, search_val, mid_idx + 1, max_idx)
    else:
        print("%d found in index %d"%(search_val, mid_idx))
        return mid_idx
