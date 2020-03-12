import sys

def positionPoint(x, y, quad):
    c = 2
    for i in range(len(quad)):
        if x == quad[i][0] and y == quad[i][1]:
            return ('точка на одной из вершин')

        if (((quad[i][1] <= y and y <= quad[i-1][1]) or (quad[i - 1][1] <= y and y <= quad[i][1])) and \
                (x >= (quad[i - 1][0] - quad[i][0]) * (y - quad[i][1]) / (quad[i - 1][1] - quad[i][1]) + quad[i][0])):
            c -= 1

        if (((quad[i][1] <= y and y < quad[i-1][1]) or (quad[i - 1][1] <= y and y < quad[i][1])) and \
                (x > (quad[i - 1][0] - quad[i][0]) * (y - quad[i][1]) / (quad[i - 1][1] - quad[i][1]) + quad[i][0])):
            c -= 1

    if c == 2:
        return ('точка снаружи')
    elif c == 1:
        return ('точка на одной из сторон')
    else:
        return ('точка внутри')


if __name__ == '__main__':
    coord_quad = sys.argv[1]
    coord_points = sys.argv[2]
    mas_coord_quad = []
    mas_coord_points = []

    with open(coord_quad, 'r') as f:
        for line in f:
            mas_coord_quad.append([float(x) for x in line.split()])

    with open(coord_points, 'r') as f:
        for line in f:
            mas_coord_points.append([float(x) for x in line.split()])

    if len(mas_coord_points)>=1 or len(mas_coord_points)<=100:
        for i in range(len(mas_coord_points)):
            print(i, '-', positionPoint(mas_coord_points[i][0], mas_coord_points[i][1], mas_coord_quad))
