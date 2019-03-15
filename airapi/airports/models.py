import json
from django.db import models


class Airport(models.Model):
    code = models.CharField(max_length=3)
    name = models.CharField(max_length=200)

    def toJSON(self):
        data = {'name': self.name, 'code': self.code}
        return json.dumps(data)

