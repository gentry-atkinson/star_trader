# TODO: use better price generation method. Trend + season + variance
# TODO: add random events that impact prices
# TODO: add a legality mechanism

import os
import json
from random import choice, uniform

from utils.port import Port
from utils.globals import *

TRENDS = {"neutral" : 1., "rising" : 1.05, "falling": 0.95, "booming" : 1.15, "crashing": 0.85}
VOLATILITY = {"very high" : 1.0, "high" : 0.5, "neutral" : 0.1, "low" : 0.05, "very low" : 0.01}

class Planet:
    def __init__(self, name: str) -> None:
        with open(os.path.join("config", name+".ini"), 'r') as f:
            configs = dict(json.load(f))
            self.name = name
            self.ports = {
                p: Port(p) for p in list(configs["ports"])
            }
            self.wealth = str(configs["wealth"])
            self.corruption = str(configs["corruption"])
            self.volatility = str(configs["volatility"])
            self.small_image = str(configs["small_image"])
            self.large_image = str(configs["small_image"])
            self.year_len = float(configs["year_len"])
            self.produces = list(configs["produces"])
            self.consumes = list(configs["consumes"])
            self.base_shipping_cost = float(configs["shipping cost"])

            self.trend = choice(list(TRENDS.keys()))
            self.products = {
                "iron" : [IRON_GLOBAL_START_AVG],
                "methane" : [METHANE_GLOBAL_START_AVG],
                "clothing" : [CLOTHING_GLOBAL_START_AVG],
                "medicine" : [MEDICINE_GLOBAL_START_AVG]
            }
            self._init_product_prices()
            #print(self.products)

    def _init_product_prices(self):
        for prod in self.products:
            if prod in self.produces:
                self.products[prod][0] /= 2.
            elif prod in self.consumes:
                self.products[prod][0] *= 2.

            for i in range(1, 30):
                self.products[prod].append(
                    self.products[prod][i-1] * TRENDS[self.trend]
                )
                self.products[prod][i] = self.products[prod][i] * (1+(uniform(-1, 1) *VOLATILITY[self.volatility]))

    def update(self):
        for prod in self.products:
            self.products[prod].append(
                        self.products[prod][-1] * TRENDS[self.trend]
                    )
            self.products[prod][-1] = self.products[prod][-1] * (1+(uniform(-1, 1) *VOLATILITY[self.volatility]))
            self.products[prod] = self.products[prod][-1]

    def get_num_ports(self):
        return len(self.ports)
    
    def get_port_price(self, port: str, product: str) -> float:
        price = self.products[product][-1] 
        return price + self.ports[port].offsets[product]
    
    def get_port_names(self) -> list:
        return self.ports.keys()

# if __name__ == '__main__':
#     earth = {
#         "ports": ["Boca Chica", "Vandenburg", "Baikonur", "Cape Canaveral", "Wenchang"],
#         "wealth": "very high",
#         "corruption": "high",
#         "volatility": "high",
#         "small_image": "Earth_nav_icon.png",
#         "large_image": "Earth_large.png",
#         "year_len" : 1.0,
#         "produces" : ["medicine", "clothing"],
#         "consumes" : ["methane"]
#     }

#     with open('config/Earth.ini', 'w') as f:
#         json.dump(earth, f)


