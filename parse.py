
class Map:

    def __init__(self):
        self.zones = {}
        self.connections = {}
        self.drones: int = 0

    def add_zone(self, zone):
        self.zones[zone.name] = zone


class Zone:

    def __init__(self, name, x, y, color, zone_type, max_drones):
        self.name = name
        self.x = x
        self.y = y
        self.color = color
        self.zone_type = zone_type
        self.max_drones = max_drones

    @classmethod
    def process_metadata(cls, name, x, y, metadata):
        zone_type = 'normal'
        max_drones = 1
        color = None
        data = metadata.split()
        for item in data:
            key, value = item.strip('[]').split('=')
            if key == 'color':
                color = value
            elif key == 'zone':
                zone_type = value
            elif key == 'max_drones':
                max_drones = int(value)

        return cls(name, x, y, color, zone_type, max_drones)


def parse_map(map):
    import_map = "map_example.txt"
    with open(import_map, 'r') as file:
        for line in file:
            line = line.strip()
            if ':' in line:
                key, value = [x.strip() for x in line.split(':', 1)]
                if key in ('hub', 'start_hub', 'end_hub'):
                    data = value.split()
                    metadata = value.split('[')[1]
                    zone = Zone.process_metadata(data[0], data[1], data[2], metadata)
                    map.add_zone(zone)
                elif key == 'connection':
                    zone_a, zone_b = value.split('-', 1)
                    map.connections.setdefault(zone_a, []).append(zone_b)
                    map.connections.setdefault(zone_b, []).append(zone_a)
                elif key == 'nb_drones':
                    map.drones = int(value)



                
                


        
    

