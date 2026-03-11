from colors import PrintColors as c


class Map:

    def __init__(self):
        self.zones = {}
        self.n_zones = {}
        self.connections = {}
        self.drones: int = 0
        self.width: int = 0
        self.heigth: int = 0

    def add_zone(self, zone):
        self.zones[zone.coord] = zone
        self.n_zones[zone.name] = zone

    def show_map(self):
        for y in range(self.heigth):
            print()
            for x in range(self.width):
                if (x,y) in self.zones.keys():
                    if self.zones[(x, y)].zone_type == "priority":
                        c.print_green(f"({x}, {y})")
                    elif self.zones[(x, y)].zone_type == "restricted":
                        c.print_yellow(f"({x}, {y})")
                    elif self.zones[(x, y)].zone_type == "blocked":
                        c.print_red(f"({x}, {y})")
                    else:
                        print(f"({x}, {y})", end=' ')
                else:
                    print("      ", end=' ')

    def has_exit(self, zone):
        if zone.name == "goal":
            return True
        elif zone.name not in self.connections.keys():
            return False
        for z in self.connections[zone.name]:
            result = self.has_exit(self.n_zones[z])
            if result == True:
                return True

    def can_move(self, zone):
        capacity = 0
        prox = [z for z in self.connections[zone.name] if self.has_exit(self.n_zones[z])]
        for con in prox:
            capacity += self.n_zones[con].max_drones - self.n_zones[con].drones
        return capacity > 0
    
    def move_drone(self, moves_from, moves_to):
        
        moves_from.drones -= 1
        moves_to.drones += 1
        print(moves_from.coord, moves_to.coord, end=' | ')
        
    def empty_zone(self, zone):
        prox = self.connections[zone.name]
        for _ in range(zone.drones):
            for z in prox:
                if (self.n_zones[z].drones < self.n_zones[z].max_drones
                    and self.has_exit(self.n_zones[z])):
                    self.move_drone(zone, self.n_zones[z])
                    return
    
    def turn(self):
        occ_zones = [z for z in self.zones.values() if z.drones > 0 and z.name != 'goal']
        for z in occ_zones:
            print(f"\nocc: {z.coord}")
            while self.can_move(z) and z.drones > 0:
                self.empty_zone(z)
        print()
