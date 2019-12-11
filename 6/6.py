class OrbitMap:
    def __init__(self, map):
        self.map = map

    def total_orbits(self):
        """ calculate the number of total orbits. """
        total_orbits = 0
        for key in self.map:
            k = self.map.get(key)
            n = 0
            while k:
                n += 1
                k = self.map.get(k)
            total_orbits += n
        return total_orbits

    def path(self, node):
        """ calculate the path from given node to center of mass."""
        k = self.map.get(node)
        path = []
        while k:
            path.append(k)
            k = self.map.get(k)
        return path

    def orbital_transfers(self, src, dst):
        src_path = self.path(src)[::-1]
        dst_path = self.path(dst)[::-1]
        zipped = list(zip(range(len(dst_path)), src_path, dst_path))
        for (i, s, d) in zipped:
            if s != d:
                return len(src_path[i:] + dst_path[i:])



with open("input", "r") as f:
    lines = f.readlines()

orbit_l = [l.split()[0].split(')') for l in lines]
orbit_dict = { l[1] : l[0]  for l in orbit_l}

orbit_map = OrbitMap(orbit_dict)
print(orbit_map)
print(type(orbit_map.map))

print(orbit_map.total_orbits())

print(orbit_map.orbital_transfers("SAN","YOU"))
