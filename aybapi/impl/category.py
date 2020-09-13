from ..utils.errors import *


class Category:
    def __init__(self, info):
        self.success = info['success']

        if (self.success):
            self.id = info['id']
            self.name = info['name']
            self.slug = info['slug']
        else:

            raise APIError(info['note'])

    def __str__(self):
        attrs = [

            ("id", self.id),
            ("name", self.name),
            ("slug", self.slug)
        ]
        return "%s<%s>" % (
            self.__class__.__name__,
            " ".join(f"{i[0]}={i[1]}," for i in attrs if i[1] != None),
        )
