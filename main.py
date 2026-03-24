#!/usr/bin/env python3

#import pprint
from parse import Map, parse_map
from show import Screen, TerminalOutput

def main():
    map = Map()
    parse_map(map, "challenger_map.txt")
    turns = 0
    map.path = map.shortest_path(map.start)
    while len(map.end.drones) < map.drones:
        map.turn()
        turns += 1

if __name__ == "__main__":
    main()