# Make a class LatLon that can be passed parameters `lat` and `lon` to the
# constructor

# YOUR CODE HERE
class LatLon:
    def __init__(self, lat, lon):
        self.lat = lat
        self.lon = lon


# Make a class Waypoint that can be passed parameters `name`, `lat`, and `lon` to the
# constructor. It should inherit from LatLon. Look up the `super` method.

# YOUR CODE HERE
class Waypoint(LatLon):
    def __init__(self, name, lat, lon):
        self.name = name
        self.lat = lat
        self.lon = lon
    
    def print_waypoint(self):
        print(self.name, self.lat, self.lon)
        
    def __str__(self):
        space_dat_stuff_out = ", "
        return self.name + space_dat_stuff_out + str(self.lat) + space_dat_stuff_out + str(self.lon) + space_dat_stuff_out

# Make a class Geocache that can be passed parameters `name`, `difficulty`,
# `size`, `lat`, and `lon` to the constructor. What should it inherit from?

# YOUR CODE HERE

class Geocache(Waypoint):
    def __init__(self, name, difficulty, size, lat, lon):
        self.name = name
        self.difficulty = difficulty
        self.size = size
        self.lat = lat
        self.lon = lon
    
    def print_geocache(self):
        print(self.name, self.difficulty, self.size, self.lat, self.lon)
    def __str__(self):
        space_it = ", "
        return self.name + space_it + self.difficulty + space_it + self.size + space_it + str(self.lat) + space_it + str(self.lon)

# Make a new waypoint and print it out: 
waypoint = Waypoint("Catacombs", 41.70505, -121.51521 )

# YOUR CODE HERE
waypoint.print_waypoint()

# Without changing the following line, how can you make it print into something
# more human-readable? Hint: Look up the `object.__str__` method

print(waypoint)

# Make a new geocache "Newberry Views", diff 1.5, size 2, 44.052137, -121.41556
geocache = Geocache("Newberry Views", "diff 1.5", "size 2", 44.052137, -121.41556)
# YOUR CODE HERE
geocache.print_geocache()
# Print it--also make this print more nicely
print(geocache)

