#  Hint:  You may not need all of these.  Remove the unused functions.
class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination
        
    def __str__(self):
        return f"source: {self.source}, dest: {self.destination}"


def reconstruct_trip(tickets, length):
    """
    YOUR CODE HERE
    """
    route = [None] * length # fill array 
    
    #using hash for o(n)
    ticket_hash = {}
    
    # keep track of route order
    index = 0 
    
    # fill hash with tickets source is key and value is dest
    for ticket in tickets:
        ticket_hash[ticket.source] = ticket.destination
        
    ######## build route #############
    
    #assign starting point 
    route[index] = ticket_hash["NONE"]
    
    #find next 
    while index != length -1: # runs till route is completed
        
        # save prev route
        prev = route[index]
        
        # assign next route
        next_route = ticket_hash[prev]
        
        # increment index
        index +=1
        
        # assign next route on the route array using incremented index for order
        route[index] = next_route
        
    return route
