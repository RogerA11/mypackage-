from mypackage.mypackage import myModule

def test_top_n():
    ''' 
    Test code to see if it works 
    '''

    assert myModule.top_n([1, 5, 2, 0, 10], 2) == [10, 5], 'Incorrect'
    assert myModule.top_n([1, 5, 2, 0, 10], 3) == [10, 5, 2], 'Incorrect'
    assert myModule.top_n([1, 5, 2, 0, 10, 22, 55, 101], 5) == [101, 55, 22, 10, 5, 2], 'Incorrect'

test_top_n()



