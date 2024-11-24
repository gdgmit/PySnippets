def remove_duplicates(lst: list) -> list:
    """
    Removes duplicate elements from the list while maintaining the original order.

    Example usage:
    remove_duplicates([1, 2, 2, 3, 4, 4]) -> [1, 2, 3, 4]
    """
    seen = set()
    return [x for x in lst if not (x in seen or seen.add(x))]

def flatten_nested_list(nested_list: list) -> list:
    """
    Flattens a nested list into a single list.

    Example usage:
    flatten_nested_list([[1, 2], [3, 4], [5]]) -> [1, 2, 3, 4, 5]
    """
    return [item for sublist in nested_list for item in sublist]

def list_intersection(lst1: list, lst2: list) -> list:
    """
    Finds the intersection of two lists.

    Example usage:
    list_intersection([1, 2, 3], [2, 3, 4]) -> [2, 3]
    """
    return list(set(lst1) & set(lst2))

def random_shuffle(lst: list) -> list:
    """
    Randomly shuffles the elements of the list.

    Example usage:
    random_shuffle([1, 2, 3, 4]) -> [3, 1, 4, 2] (order will vary)
    """
    import random
    random.shuffle(lst)
    return lst

def sort_by_frequency(lst: list) -> list:
    """
    Sorts the list based on the frequency of elements in descending order.

    Example usage:
    sort_by_frequency([4, 5, 6, 4, 5, 4]) -> [4, 4, 4, 5, 5, 6]
    """
    from collections import Counter
    frequency = Counter(lst)
    return sorted(lst, key=lambda x: frequency[x], reverse=True)

def list_difference(lst1: list, lst2: list) -> list:
    """ 
    Finds the difference of two lists.
    
    Example Usage:
    list_difference([1, 2, 3], [2, 3, 4]) -> [1]
    """
    return list(set(lst1) - set(lst2))

def list_union(lst1: list, lst2: list) -> list:
    """
    Finds the union of two lists.

    Example Usage:
    list_union([1, 2, 3], [2, 3, 4]) -> [1, 2, 3, 4]
    """
    return list(set(lst1) | set(lst2))

def rotate_list(lst: list, count: int, direction: str) -> list:
    """
    Rotate elements left or right by a given number of steps.

    Example Usage:
    rotate_list([1, 2, 3, 4, 5], 2, "right") -> [4, 5, 1, 2, 3]
    """
    if not lst:
        return []
    
    n = len(lst)
    count %= n

    if direction.lower() == 'left':
        return lst[count:] + lst[:count]
    elif direction.lower() == 'right':
        return lst[-count:] + lst[:-count]
    else:
        raise ValueError("Direction must be 'left' or 'right'.")

def random_pick(lst: list):
    """
    Picks a random element from the list.

    Example Usage:
    random_pick([1, 2, 3, 4]) -> 3 (random element from the list)
    """
    import random
    if not lst:
        raise ValueError("The list is empty. Cannot pick a random element.")
    
    return random.choice(lst)

# Example usage of the functions in the script
if __name__ == "__main__":
    sample_list = [1, 2, 2, 3, 4, 4, 5, 5, 5]
    nested_list = [[1, 2], [3, 4], [5]]
    sample = [1, 2, 3, 4]

    print("Original List:", sample_list)
    print("Without Duplicates:", remove_duplicates(sample_list))
    print("Flattened Nested List:", flatten_nested_list(nested_list))
    print("List Intersection:", list_intersection([1, 2, 3], [2, 3, 4]))
    print("Shuffled List:", random_shuffle(sample_list.copy()))  # Using copy to keep original
    print("Sorted by Frequency:", sort_by_frequency(sample_list))
    print("List Difference:", list_difference([1, 2, 3], [2, 3, 4]))
    print("List Union:", list_union([1, 2, 3], [2, 3, 4]))
    print("Rotated List:", rotate_list(sample, 3, "left"))
    print("Random element from list:", random_pick(sample))

