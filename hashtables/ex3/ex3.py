def intersection(arrays):
    """
    YOUR CODE HERE
    """
    # flatten arrays into one array
    flat_array = []
    hash_counter = {}
    arrays_count = len(arrays) 

    # flatten array
    for i in arrays:
        flat_array += i
        
    # count elements by elements
    for num in flat_array: 
        if num in hash_counter:
            hash_counter[num] += 1
        else:
            hash_counter[num] = 1
    
    # Your code here
    
    #return if arrays_count is that same as the element counter
    results = [x for x in hash_counter if hash_counter[x] == arrays_count ]

    return results


if __name__ == "__main__":
    arrays = []

    arrays.append(list(range(1000000, 2000000)) + [1, 2, 3])
    arrays.append(list(range(2000000, 3000000)) + [1, 2, 3])
    arrays.append(list(range(3000000, 4000000)) + [1, 2, 3])

    print(intersection(arrays))
