from qgis.core import QgsGeometry, QgsPointXY

class Wire():
    def __init__(self, instr):
        self.geom = QgsGeometry.fromPolylineXY(self.line_walker(instr))

    def line_walker(self, instr):
        coords = [QgsPointXY(0,0)]
        for i in instr:
            steps = int(i[1:])
            last = coords[-1]
            if i.startswith('R'):
                coords.append(QgsPointXY(last.x() + steps, last.y()))
            if i.startswith('L'):
                coords.append(QgsPointXY(last.x() - steps, last.y()))
            if i.startswith('U'):
                coords.append(QgsPointXY(last.x(), last.y() + steps))
            if i.startswith('D'):
                coords.append(QgsPointXY(last.x(), last.y() - steps))
        return coords

    def distance_to_point_on_wire(self, point):
        point_geom = QgsGeometry.fromPointXY(point)
        # test to see if point is on the wire
        return int(self.geom.lineLocatePoint(point_geom))


def distance(a, b = QgsPointXY(0,0)):
    x = abs(a.x() - b.x())
    y = abs(a.y() - b.y())
    return (x + y)



with open('input', 'r') as f:
    lines = f.readlines()

wires = [Wire(l.split(',')) for l in lines]

intersection = wires[0].geom.intersection(wires[1].geom)

points = [x for x in intersection.asMultiPoint() if x != QgsPointXY(0,0)]

dis = int(min([distance(p) for p in points if distance(p) > 0]))
print(dis)

dis2 = [wires[0].distance_to_point_on_wire(p) + wires[1].distance_to_point_on_wire(p)
        for p in points]

print(min(dis2))
