# Warpaint

A medieval fantasy population sumulator.

## components

### time

- year
- season
- month
- day

### population:

- race
- family
- desires
- fears

### grography:

- height map
- temprature
- persipitation
- hemosphear
- weather
- tides

### social:

#### religion:

- gods
    - harolds
    - saints
    - champions

#### social hierarchies:

- lord
- king
- pesent
- priest


## Goals:

1. generate a random distributed population
    - generate `n` civilions
    - ranomply decide `race`
    - distribut ages based on a bell curve
2. iterate through time
    - increment for `n` years
3. implemnet death of citizens
4. implement creation of new citizens
5. save and log simulation
    - log by year
    - log family tree of all citizens
6. log explorer
    - some sort of way to traverse the log files