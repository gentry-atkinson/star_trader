import os
import json

class Planet:
    def __init__(self, name: str) -> None:
        with open(os.path.join("config", name+".ini"), 'r') as f:
            configs = dict(json.load(f))
            self.name = name
            self.ports = list(configs["ports"])
            self.wealth = float(configs["wealth"])
            self.corruption = float(configs["corruption"])
            self.small_image = str(configs["small_image"])
            self.large_image = str(configs["small_image"])
            self.year_len = float(configs["year_len"])

