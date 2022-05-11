'''
Hotel information format:
[name, classification, (regular fees), (rewards fees)]

Hotel fee's tuples format: (day of the week, weekend)
'''

HOTELS = [
    ['Lakewood', 3, (110,90), (80,80)],
    ['Bridgewood', 4, (160,60), (110,50)],
    ['Ridgewood', 5, (220,150), (100,40)]
]

def get_cheapest_hotel(number):   #DO NOT change the function's name
    spliter = number.split()
    
    if spliter[0] == "Rewards:":
        client = 3
    else:
        client = 2
    sums=[]
    for hotel in HOTELS:
        sum = 0
        for day in spliter[1:]:
            if 'sun' in day or 'sat' in day:
                sum+=hotel[client][1]
            else:
                sum+=hotel[client][0]
        sums.append(sum)

    cheapest_value = min(sums)
    index = [x for x, y in enumerate(sums) if y == cheapest_value]
    if len(index)>1:
        classification = 0
        for i in index:
            if HOTELS[i][1]> classification:
                best_hotel = i
        index = best_hotel
    else:
        index=index[0]

    cheapest_hotel = HOTELS[index][0]
    return cheapest_hotel
