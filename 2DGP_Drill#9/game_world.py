# world[0]: 백그라운드 객체들
# world[1]' foreground 객체들

world = [[], []]

def add_object(o, depth = 0):
    world[depth].append(o)

def remove_object(o):
    for layer in world:
        if o in layer:
            layer.remove(o)
            return

    raise ValueError(f'CRITICAL: 존재하지 않는 객체{o}을 지우려고 합니다')

def update():
    for layer in world:
        for o in layer:
            o.update()

def render():
    for layer in world:
        for o in layer:
            o.draw()

