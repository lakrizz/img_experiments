import math

def nearest(pt, others):
    nearest_dist = 999999999999
    nearest_i = -1
    for i in range(len(others)):
        other = others[i]

        if other == pt:
            continue

        dz = distance(pt['x'], pt['y'], other['x'], other['y']) 
        if  dz < nearest_dist and not other['connected']:
            nearest_dist = dz
            nearest_i = i
        
    return nearest_i

def distance(x1,y1,x2,y2):
    return math.dist([x1, y1], [x2, y2])
    