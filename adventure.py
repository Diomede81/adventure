from data import locations , descriptions, objects, inventory

directions = {
    'west' : (-1, 0),
    'east' : (1, 0),
    'north': (0, -1),
    'south': (0, 1)
}

position = (0, 0)

while True:
    location = locations[position]
    print 'you are at the %s' % location
    print ' %s' % descriptions[position]
    print 'The following items are available %s' % objects[position]

    valid_directions = {}
    for k,v in directions.iteritems():
        possible_position = (position[0] + v[0], position[1] + v[1])
        possible_location = locations.get(possible_position)
        if possible_location:
            print 'to the %s is a %s' % (k, possible_location)

            valid_directions[k] = possible_position

    direction = raw_input('which direction do you want to go? \n')
    if direction in valid_directions:
        if objects[position] == []:
            print "There are no more objects to take"
        else:
            ObjTaken = raw_input('Which Object would you like to take ?')
            if ObjTaken in objects[position]:
                print "You have successfully taken the %s" % ObjTaken
                objects[position].remove(ObjTaken)
                inventory.append(ObjTaken)
                print "This is the content of your inventory: %s" % inventory
                position = valid_directions[direction]

            else:
                print "please select a correct object"
    else:
        print "please select an available location"
