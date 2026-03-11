from algorithm import Map

class Zone:

    def __init__(self, name, x, y, color, zone_type, max_drones, drones):
        self.name = name
        self.x = x
        self.y = y
        self.coord = (x, y)
        self.color = color
        self.zone_type = zone_type
        self.max_drones = max_drones
        self.drones = drones


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
        if name == 'start':
            drones = max_drones
        else:
            drones = 0

        return cls(name, x, y, color, zone_type, max_drones, drones)


def parse_map(map, map_name):
    with open(map_name, 'r') as file:
        for line in file:
            line = line.strip()
            if ':' in line:
                key, value = [x.strip() for x in line.split(':', 1)]
                if key in ('hub', 'start_hub', 'end_hub'):
                    data = value.split()
                    metadata = value.split('[')[1]
                    zone = Zone.process_metadata(data[0], int(data[1]), int(data[2]), metadata)
                    map.add_zone(zone)
                elif key == 'connection':
                    zone_a, zone_b = value.split('-', 1)
                    map.connections.setdefault(zone_a, []).append(zone_b)
                elif key == 'nb_drones':
                    map.drones = int(value)
                    
    map.width = max(z.x for z in map.zones.values()) + 1
    map.heigth = max(z.y for z in map.zones.values()) + 1
