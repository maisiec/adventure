from data import locations   # importing locations from data.py

directions = {   # define a dictionary with our directions in
    'west': (-1, 0),
    'east': (1, 0),
    'north': (0, -1),
    'south': (0, 1),
}

position = (0, 0)   # starting position

while True:
    location = locations[position]   # find the name of our location by using locations dictionary we imported
    print 'you are at the %s' % location

    valid_directions = {}
    for k, v in directions.iteritems():  # when iterating through dictionary its helped to read both keys and values
        possible_position = (position[0] + v[0], position[1] + v[1])  # for each direction we calculate new position
        possible_location = locations.get(possible_position)  # check to see if position is in list of locations
        if possible_location:  # if possible locations exists we print it and add it to dicitonary
            print 'to the %s is a %s' % (k, possible_location)
            valid_directions[k] = possible_position

    direction = raw_input('Which direction do you want to go?\n')  # we ask user for a direction and use
    position = valid_directions[direction]  # valid_directions dictionary to move us to that position
