import random

import pyglet
from pyglet import shapes
from typing import Tuple, List
from ZipCodeItemFile import ZipcodeItem

Coordinates = Tuple[float, float]
GROUP_COLORS = ((192,0,0),(0,192,0),(0,0,192),(128,128,0),(128,0,128),(0,128,128), (192,0, 64), (0,64,192))

class Display (pyglet.window.Window):

    def __init__(self):

        super(Display,self).__init__(791,713,"Zip Codes")

        self.texas_image = pyglet.image.load('texas56.png')
        self.spr = None

        self.city_coords = None
        self.city_group_numbers = None
        self.city_colors = None
        self.vector_list = None
        self.background_group = pyglet.graphics.OrderedGroup(0)
        self.foreground_group = pyglet.graphics.OrderedGroup(1)
        self.circles_list = []


    def on_draw(self):
        # self.image_sprite.draw()
        # if self.vector_list is not None:
        #     self.vector_list.draw(pyglet.gl.GL_POINTS)
        print("Drawing.")
        self.clear()
        self.batch.draw()




    def set_cities(self, zip_code_item_list: List[ZipcodeItem]):
        self.city_coords = []
        self.city_group_numbers = []
        self.city_colors = []
        for zip in zip_code_item_list:
            self.city_coords.append((int(zip.x),int(zip.y)))
            self.city_group_numbers.append(zip.attractor_number)
            self.city_colors.append(GROUP_COLORS[self.city_group_numbers[-1]])
        self.batch = self.build_batch()

        # num_cities = len(self.city_colors)
        # print(f"{num_cities=}")
        # print(f"{len(self.city_coords)}\t{len(self.city_colors)}")
        # print(f"{self.city_coords[0:10]=}")
        # print(f"{self.city_colors[0:10]=}")
        # self.vector_list = pyglet.graphics.vertex_list(int(num_cities/3),
        #                                                ('v2i',self.city_coords),
        #                                                ('c3B',self.city_colors))

    def build_batch(self) -> pyglet.graphics.Batch:

        print("building batch.")
        batch = pyglet.graphics.Batch()


        self.spr = pyglet.sprite.Sprite(self.texas_image, x=0, y=0, batch=batch, group=self.background_group)

        self.circles_list = []

        for i in range(len(self.city_colors)):
            print(f"{self.city_coords[i]=}")
            self.circles_list.append(shapes.Circle(x=self.city_coords[i][0],
                                   y=self.city_coords[i][1],
                                   radius=2,
                                   color = self.city_colors[i],
                                   batch=batch,
                                   group = self.foreground_group))

        """
        vertex_list = batch.add(2, pyglet.gl.GL_LINES, None,
                                ('v2i', (10, 15, 30, 35)),
                                ('c3B', (0, 0, 255, 0, 255, 0))
                                )

        co_x = 150
        co_y = 150

        # width of rectangle
        width = 300

        # height of rectangle
        height = 200

        # color = green
        color = (50, 225, 30)

        # creating a rectangle
        rec1 = shapes.Rectangle(co_x, co_y, width, height, color=color, batch=batch)#, group=foreground_group)
        """
        return batch

    def update_colors(self):
        for i in len(self.city_group_numbers):
            self.city_colors[i]=GROUP_COLORS[self.city_group_numbers[i]]
        self.batch = self.build_batch()

