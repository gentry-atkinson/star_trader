# TODO organize into groups and comment a little

import os

SCREEN_SIZE = (1200, 800)
START_DATE = 2276.0
IMG_DIR = os.path.join("utils", "imgs")
START_PLANET = "Earth"
START_SCREEN = "cockpit"
PLANET_LIST = ["Venus", "Earth", "Mars"]
PLANET_ICON_SIZE = (40, 40)
SELECTOR_ICON_SIZE = (40, 40)
PRODUCT_LIST = ["iron", "methane", "clothing", "medicine"]
IRON_GLOBAL_START_AVG = 100
METHANE_GLOBAL_START_AVG = 20
CLOTHING_GLOBAL_START_AVG = 150
MEDICINE_GLOBAL_START_AVG = 300
SCREEN_LIST = ["navigation", "cockpit", "local", "economy", "jump"]
TRAVEL_TIME_PER_PIXEL = 0.001
ECON_ICON_SIZE = (40, 40)
ECON_PRODUCT_SIZE = (60, 30)
DIS_BETWEEN_LINE_DOTS = 40
DOT_SIZE = 10
ECON_GRAPH_ORIGIN = (100, 700)
ECON_GRAPH_HEIGHT = 600
ECON_GRAPH_WIDTH = 1000
JUMP_TIME_MS = 500

COLOR_CODES = {
    "green" : (0, 255, 0),
    "red" : (255, 0, 0),
    "blue" : (0, 0, 255),
    "purple" : (255, 0, 255)
}

PRODUCT_COLORS = {
    "iron" : "red",
    "methane" : "green",
    "clothing" : "blue",
    "medicine" : "purple"
}