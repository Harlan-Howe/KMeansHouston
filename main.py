import pyglet
import csv
from DisplayFile import Display
from ZipCodeItemFile import ZipcodeItem
from typing import List


def start_display():
    dsp = Display()
    load_data()
    dsp.set_cities(zip_list)



    pyglet.app.run()

def load_data():
    global zip_list
    tsv_file = open("Texas zips with coordinates.tsv")
    read_tsv = csv.reader(tsv_file, delimiter="\t")
    zip_list = []
    for zipcode in read_tsv:
        zci = ZipcodeItem(zipcode[0],zipcode[1],zipcode[2],int(zipcode[5]),713-int(zipcode[4])) # we skip 3 because it is the name of the city, which we don't need.
        zip_list.append(zci)







# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    start_display()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
