import random

from utils.globals import *

class Port:
    def __init__(self, name):
        self.name = name
        self.offsets = {
            p: random.uniform(0.90, 1.1) for p in PRODUCT_LIST
        }