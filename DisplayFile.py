import random

import pyglet
from pyglet import shapes
from typing import Tuple, List
from ZipCodeItemFile import ZipcodeItem

Coordinates = Tuple[float, float]
GROUP_COLORS = ((192,0,0),(0,192,0),(0,0,192),(192,192,0),(192,0,192),(0,192,192), (255,128, 0), (128,128,128), (255,128,128), (128,255,0))

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
        self.previous_attractor_group = pyglet.graphics.OrderedGroup(2)
        self.star_outline_group = pyglet.graphics.OrderedGroup(3)
        self.current_star_group = pyglet.graphics.OrderedGroup(4)
        self.circles_list = []
        self.stars_list = []
        self.previous_attractors = []
        self.current_attractors = []
        self.N = 0


    def on_draw(self):
        # print("Drawing.")
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



    def build_batch(self) -> pyglet.graphics.Batch:

        # print("building batch.")
        batch = pyglet.graphics.Batch()

        # draw the texas map
        self.spr = pyglet.sprite.Sprite(self.texas_image, x=0, y=0, batch=batch, group=self.background_group)

        # draw all the dots
        self.circles_list = []

        for i in range(len(self.city_colors)):
            self.circles_list.append(shapes.Circle(x=self.city_coords[i][0],
                                   y=self.city_coords[i][1],
                                   radius=2,
                                   color = self.city_colors[i],
                                   batch=batch,
                                   group = self.foreground_group))

        # OK. Time to draw stars....
        self.star_list = []
        # first, draw the trail of old stars, if any.
        """
        for j in range(len(self.previous_attractors)):
            i = j % self.N
            self.star_list.append(shapes.Star(x=self.previous_attractors[j][0],
                                              y=self.previous_attractors[j][1],
                                              outer_radius=20,
                                              inner_radius=2,
                                              num_spikes=5,
                                              color=GROUP_COLORS[i],
                                              batch=batch,
                                              group=self.previous_attractor_group
                                              ))
        """
        for j in range(self.N, len(self.previous_attractors)):
            i = j % self.N
            self.star_list.append(shapes.Line(x = self.previous_attractors[j-self.N][0],
                                              y = self.previous_attractors[j-self.N][1],
                                              x2 = self.previous_attractors[j][0],
                                              y2 = self.previous_attractors[j][1],
                                              width = 2,
                                              color = GROUP_COLORS[i],
                                              batch = batch,
                                              group = self.previous_attractor_group
                                              ))
        if len(self.previous_attractors) > 0:
            for i in range(self.N):
                self.star_list.append(shapes.Line(x = self.previous_attractors[-1-i][0],
                                                  y = self.previous_attractors[-1-i][1],
                                                  x2= self.current_attractors[-1-i][0],
                                                  y2= self.current_attractors[-1-i][1],
                                                  width = 2,
                                                  color = GROUP_COLORS[self.N-1-i],
                                                  batch = batch,
                                                  group = self.previous_attractor_group
                                                  ))
        # Now draw the current stars -- first the black outlines, then the fills.
        for i in range(self.N):
            self.star_list.append(shapes.Star(x=self.current_attractors[i][0],
                                              y=self.current_attractors[i][1],
                                              outer_radius=8,
                                              inner_radius=5,
                                              num_spikes=5,
                                              rotation=90,
                                              color=(0, 0, 0),
                                              batch=batch,
                                              group=self.star_outline_group,
                                              ))
            self.star_list.append(shapes.Star(x=self.current_attractors[i][0],
                                              y=self.current_attractors[i][1],
                                              outer_radius=5,
                                              inner_radius=2,
                                              num_spikes=5,
                                              rotation=90,
                                              color=GROUP_COLORS[i],
                                              batch=batch,
                                              group=self.current_star_group,
                                              ))

        return batch

    def update_colors(self,zip_code_items:List[ZipcodeItem]):
        for i in range(len(self.city_group_numbers)):
            self.city_colors[i]=GROUP_COLORS[zip_code_items[i].attractor_number]
        self.batch = self.build_batch()

    def update_attractors(self,attractor_locations: List[Coordinates]):
        self.N = len(attractor_locations)
        # print(f"updating_attractors: {self.N}")
        # print(f"{attractor_locations=}")
        self.previous_attractors.extend(self.current_attractors)
        self.current_attractors = attractor_locations
        # print("Previous attractors: ")
        # i=0
        # for att in self.previous_attractors:
        #     print(f"({att[0]:.1f}, {att[1]:.1f})", end="\t")
        #     i+=1
        #     if i%self.N == 0:
        #         print("")

