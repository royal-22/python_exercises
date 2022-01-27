def frequency_sort(items):
    index_sort = sorted(items, key=items.index)
    return sorted(index_sort, key = items.count, reverse = True)
