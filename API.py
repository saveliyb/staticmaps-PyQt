import requests


class ZoomOut(Exception):
    def __init__(self, message="Zoom is not in (0, 17) range"):
        self.message = message
        super().__init__(self.message)


class CoordOut(Exception):
    def __init__(self, message="the coordinates don't exist"):
        self.message = message
        super().__init__(self.message)


class Maps:
    def __init__(self):
        self.coords = (37.620070, 55.753630)
        self.zoom = 10
        self.size = 541, 381
        self.layer = 'map'

        self.step = 0.01
        self.lst_layer = ['map', 'sat',  'sat,skl']

    def get_img(self):
        if 0 <= self.zoom <= 17:
            if (abs(self.coords[0]) <= 180) and (abs(self.coords[1]) <= 90):
                args = {'ll': ','.join([str(_) for _ in self.coords]),
                        'z': self.zoom,
                        'size': ','.join([str(_) for _ in self.size]),
                        'l': self.layer}
                ans = requests.get('http://static-maps.yandex.ru/1.x/', params=args)
                filename = 'abc.jpg'
                print(ans.status_code)
                if ans.status_code == 200:
                    with open(filename, 'wb') as imgfile:
                        imgfile.write(ans.content)
            else:
                raise CoordOut()
        else:
            raise ZoomOut()

    def zoom_up(self):
        if self.zoom < 17:
            self.zoom += 1
            self.get_img()

    def zoom_down(self):
        if self.zoom > 0:
            self.zoom -= 1
            self.get_img()

    def move_left(self):
        step = self.step**(2 ** self.zoom)
        if abs(self.coords[0] - step) < 180:
            self.coords[0] -= step
            self.get_img()

    def move_right(self):
        step = self.step**(2 ** self.zoom)
        if abs(self.coords[0] + step) < 180:
            self.coords[0] += step
            self.get_img()

    def move_down(self):
        step = self.step**(2 ** self.zoom)
        if abs(self.coords[1] - step) < 90:
            self.coords[1] -= step
            self.get_img()

    def move_up(self):
        step = self.step**(2 ** self.zoom)
        if abs(self.coords[1] + step) < 90:
            self.coords[1] += step
            self.get_img()

    def edit_layer(self):
        self.layer = self.lst_layer[(self.lst_layer.index(self.layer) + 1) % len(self.lst_layer)]


map = Maps()
map.get_img()
# map.zoom_down()

