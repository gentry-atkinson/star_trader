import json
import os
import event_handler

class Screen:
    def __init__(self, name: str) -> None:
        with open(os.path.join("config", name+".ini"), 'r') as f:
            configs = dict(json.load(f))
            self.name = name
            self.background_file = str(configs["background_file"])
            self.event_handler = event_handler()


if __name__ == "__main__":
    config_dic = {
        "background_file" : "navigation_screen.png"
    }
    with open("config/navigation.ini", 'w+') as f:
        f.write(json.dumps(config_dic))
