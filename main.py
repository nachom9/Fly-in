#!/usr/bin/env python3

#import pprint
from parse import Map, parse_map
from show import Screen, TerminalOutput

def main():
    map = Map()
    parse_map(map, "challenger_map.txt")
    map.show_map()
    print('\n\n')
    turns = 0
    map.path = map.shortest_path(map.start)

    while len(map.end.drones) < map.drones:
        map.turn()
        turns += 1
    print(f"Turns: {turns}")

if __name__ == "__main__":
    main()