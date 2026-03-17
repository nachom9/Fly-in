#!/usr/bin/env python3

#import pprint
from parse import Map, parse_map
from show import Screen, TerminalOutput

def main():
    map = Map()
    parse_map(map, "hard_map.txt")
    map.show_map()
    print('\n\n')
    turns = 0
    #pprint.pprint(map.connections)
    #return
    while len(map.n_zones['goal'].drones) < map.drones:
        map.turn()
        turns += 1
    print(f"\nTurns: {turns}")

if __name__ == "__main__":
    main()