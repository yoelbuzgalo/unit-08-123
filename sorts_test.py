import sorts

def test_merge_sort_1():
    # Setup
    a_list = [2]
    expected = a_list

    # Invoke
    result = sorts.merge_sort(a_list)

    # Analysis
    assert result == expected

def test_merge_sort_2elements():
    # Setup
    a_list = [5,2]
    expected = [2,5]

    # Invoke
    result = sorts.merge_sort(a_list)

    # Analysis
    assert result == expected

def test_merge_sort_3elements():
    # Setup
    a_list = [5,2,2]
    expected = [2,2,5]

    # Invoke
    result = sorts.merge_sort(a_list)

    # Analysis
    assert result == expected

def test_merge_sort_unsorted():
    # Setup
    a_list = [1,3,2,5,6,8,10]
    expected = [1,2,3,5,6,8,10]

    # Invoke
    result = sorts.merge_sort(a_list)

    # Analysis
    assert result == expected

def test_merge_sort_sorted():
    # Setup
    a_list = [1,2,3,5,6,8,10]
    expected = [1,2,3,5,6,8,10]

    # Invoke
    result = sorts.merge_sort(a_list)

    # Analysis
    assert result == expected