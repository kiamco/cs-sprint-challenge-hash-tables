def get_indices_of_item_weights(weights, length, limit):
    """
    YOUR CODE HERE
    """
    # Your code here
    #  weights is array 
    # wieghts + length = target  -> weight = target - length
    
    potential_weights = {}
    
    for weight_index in range(len(weights)):
        sum_length = limit - weights[weight_index] # y = target - x
        weight_val = weights[weight_index] # weigth value at the current index
        
        # # check if sum_length exists in portential weight 
        if sum_length in potential_weights:
            return [weight_index,weights.index(sum_length)]
        else: 
            potential_weights[weight_val] = True

    return None
    

print(get_indices_of_item_weights([0,0,2,0,6],2, 8 ))