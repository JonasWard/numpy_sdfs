from datetime import date
from os import mkdir
import json

class JSONMaintainer:
    def __init__(self, json_v_save_location = None):
        if json_v_save_location is None:
            self.path = JSONMaintainer.day_base_path()
        else:
            self.path = json_v_save_location

        self.open()

    @staticmethod
    def day_base_path():
        return "saves/{}.json".format(date.today() )

    def save_string(self, a_string):
        json.dump(a_string, self.file)

    def open(self):
        try:
            self.file = open(self.path, "a")
            # self.json = json.loads(self.file)
        except:
            mkdir("saves")
            self.file = open(self.path, "a")
            # self.json = json.

    def close(self):
        self.file.close()

if __name__ == "__main__":
    json_test = JSONMaintainer()
    json_test.save_string("this is a test")