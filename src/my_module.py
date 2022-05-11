HOTELS = [
    ['Lakewood', 3, (110,90), (80,80)],
    ['Bridgewood', 4, (160,60), (110,50)],
    ['Ridgewood', 5, (220,150), (100,40)]
]

def get_cheapest_hotel(reservation_string):   #DO NOT change the function's name
    '''
    Input format:
    <customer_type>: <date1>, <date2>, <date3>,...

    Output format:
    <cheapest_hotel_name>

    Hotel information format:
    [<name>, <classification>, <(regular fees)>, <(rewards fees)>]

    Hotel fee's tuples format: (<day of the week>, <weekend>)
    '''
    reservation_info = reservation_string.split()                                   # Extracting the input info
    
    client = 3 if reservation_info[0] == "Rewards:" else 2                          # Classifying the customers

    reservation_costs = []                                                          # Creating a list of each total cost of the reservation for each Hotel

    for hotel in HOTELS:                                                            # Getting the data of each hotel and use it... --->
        total_cost = 0
        for day in reservation_info[1:]:                                            # ---> for each reservation's day
            if 'sun' in day or 'sat' in day:                                        # Add the cost for weekends 
                total_cost+=hotel[client][1]
            else:                                                                   # Add the cost for regular days
                total_cost+=hotel[client][0]
        reservation_costs.append(total_cost)                                        # Append in order the total cost of the reservation for each Hotel

    cheapest_value = min(reservation_costs)                                         # Select the minimum cost from reservation_costs list so... --->
    index = [x for x, y in enumerate(reservation_costs) if y == cheapest_value]     # ---> we may create a list which has only the values that equals to the minimum value selected and then... --->
    if len(index)>1:                                                                # ---> if it has more than one value in it... --->
        classification = 0
        for i in index:
            if HOTELS[i][1]> classification:                                        # ---> Select the index of the hotel that has the highest classification
                best_hotel = i
        index = best_hotel
    else:
        index=index[0]

    cheapest_hotel = HOTELS[index][0]                                               # Get the name of the Hotel using the index selected.
    return cheapest_hotel