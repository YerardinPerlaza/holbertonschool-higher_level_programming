#!/usr/bin/python3
"""write a first class Base"""
import json


class Base:
    """ create a Base class"""
    __nb_objects = 0

    def __init__(self, id=None):
        """ initialize class"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """ return json string representation"""
        if list_dictionaries is None:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """ write the json representation on a file"""
        file_name = cls.__name__ + ".json"
        content = []
        if list_objs is not None:
            for item in list_objs:
                item = item.to_dictionary()
                json_dict = json.loads(cls.to_json_string(item))
                content.append(json_dict)

        with open(file_name, mode="w") as myfile:
            json.dump(content, myfile)

    @staticmethod
    def from_json_string(json_string):
        """return the list of the json representation"""
        if json_string is None or len(json_string) == 0:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """returns an instance with all attributes already set"""
        from models.rectangle import Rectangle
        from models.square import Square

        if cls.__name__ == "Rectangle":
            res = Rectangle(1, 1)
        elif cls.__name__ == "Square":
            res = Square(1)
        res.update(**dictionary)
        return (res)

    @classmethod
    def load_from_file(cls):
        """returns a list of instances"""
        file_name = cls.__name__ + ".json"
        try:
            with open(file_name, encoding="UTF8") as myfile:
                content = cls.from_json_string(myfile.read())
        except:
            return []

        instances = []
        for instance in content:
            tmp = cls.create(**instance)
            instances.append(tmp)
        return instances
