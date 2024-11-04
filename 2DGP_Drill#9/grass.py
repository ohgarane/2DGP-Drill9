from pico2d import load_image

class Grass:
    def __init__(self, y=30):  # y 좌표를 매개변수로 받아 초기화
        self.image = load_image('grass.png')
        self.y = y

    def draw(self):
        self.image.draw(400, self.y)  # 설정된 y 좌표로 그리기

    def update(self):
        pass
