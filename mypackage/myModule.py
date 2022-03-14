def top_n(items, n):
    ''' Return the top no items in an array, in descending order.
    
    Args:
        items (array): list or array like object
        n (int): num of items to return
    
    Return:
        array: top n items, in descending order

    Egs:
        >>> top_n([1, 5, 9, 10, 23, 3, 6], 4)
        [23, 10, 9, 6]
    '''
    sorted_list = sorted(items, reverse=True)
    
    return sorted_list[:n]


