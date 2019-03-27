from django.db import models
import json


class Airport(models.Model):
    code = models.CharField(max_length=3)
    name = models.CharField(max_length=200)

    def dump(self):
        return {"airport": {'code': self.code,
                            'name': self.name}}

    def to_json(self):
        data = {'name': self.name, 'code': self.code}
        return json.dumps(data)

    def get_code(self):
        return self.code

    def get_name(self):
        return self.name
