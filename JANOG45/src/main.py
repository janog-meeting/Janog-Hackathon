from .cdp import cdpneighbor
from .render import Render, parse


if __name__ == '__main__':
    hosts = ["192.168.0.1"]
    neighbors = []

    for i in hosts:
        neighbors.append({i: cdpneighbor(i)})

    print(neighbors)

    render = Render('sample.j2')
    connections = parse(neighbors)
    render.write({'connections': connections})

    print(connections)
