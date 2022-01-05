import random

import pyglet
import csv
from DisplayFile import Display
from ZipCodeItemFile import ZipcodeItem
from typing import List

N = 5

def start_display():
    global dsp, steps
    steps = 0
    dsp = Display()
    load_data()
    dsp.set_cities(zip_list)
    initialize_stars()

    pyglet.clock.schedule_interval(do_update,1.0)
    pyglet.app.run()

def load_data():
    global zip_list
    tsv_file = open("Texas zips with coordinates.tsv")
    read_tsv = csv.reader(tsv_file, delimiter="\t")
    zip_list = []
    for zipcode in read_tsv:
        zci = ZipcodeItem(zipcode[0],zipcode[1],zipcode[2],int(zipcode[5]),713-int(zipcode[4])) # we skip 3 because it is the name of the city, which we don't need.
        zci.attractor_number = random.randrange(N)
        zip_list.append(zci)

def initialize_stars():
    indices = []
    locs = []
    for i in range(N):
        index = random.randrange(len(zip_list))
        while index in indices:
            index = random.randrange(len(zip_list))
        indices.append(index)
        locs.append((zip_list[index].x,zip_list[index].y))
    # print(f"{indices=}")
    dsp.update_attractors(locs)

def do_update(dt):
    # print(dt)
    global steps
    print(f"{steps}")
    did_update = update_zip_items()
    update_attractors()
    steps += 1
    if not did_update:
        pyglet.clock.unschedule(do_update)
        print("No More Changes.")

def update_zip_items() -> bool:
    did_update = False
    for z in zip_list:
        att_num = z.findClosestAttractor(dsp.current_attractors)
        if att_num != z.attractor_number:
            z.attractor_number = att_num
            did_update = True
    dsp.update_colors(zip_list)
    return did_update

def update_attractors():
    x_sum = [0,] * N
    y_sum = [0,] * N
    counts = [0,] * N
    for z in zip_list:
        x_sum[z.attractor_number] += z.x
        y_sum[z.attractor_number] += z.y
        counts[z.attractor_number] += 1

    attractors = []
    for i in range(N):
        if (counts[i]==0):
            attractors.append((0,0))
        else:
            attractors.append((x_sum[i]/counts[i], y_sum[i]/counts[i]))

    dsp.update_attractors(attractors)



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    start_display()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
