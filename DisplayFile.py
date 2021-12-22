import random

import pyglet
from typing import Tuple, List

Coordinates = Tuple[float, float]
GROUP_COLORS = ((0,0,192),(0,192,0),(192,0,0),(128,128,0),(128,0,128),(0,96,96), (192,0, 64), (0,64,192))

class Display (pyglet.window.Window):



    def __init__(self):
        texas_image = pyglet.image.load('texas56.png')

        pyglet.window.Window.__init__(self, texas_image.width,texas_image.height, "Texas")
        self.image_sprite = pyglet.sprite.Sprite(texas_image,
                                                 x=0, y=0)
        self.city_coords = None
        self.city_group_numbers = None
        self.city_colors = None
        self.vector_list = None

    def on_draw(self):
        self.image_sprite.draw()
        if self.vector_list is not None:
            self.vector_list.draw(pyglet.gl.GL_POINTS)


    def set_cities(self, city_coords: List[Coordinates], N: int ):
        self.city_coords = []
        self.city_colors = []
        for coord in city_coords:
            self.city_coords.extend(coord)
            self.city_group_numbers.append(random.randrange(N))
            self.city_colors.extend(GROUP_COLORS[self.city_group_numbers[-1]])

        num_cities = len(self.city_colors)

        self.vector_list = pyglet.graphics.vertex_list(num_cities,
                                                       ('v2f',self.city_coords),
                                                       ('c3B',self.city_colors))

    def update_colors(self):
        for i in len(self.city_group_numbers):
            self.vector_list[:i]=GROUP_COLORS[self.city_group_numbers[i]]
