from django.db import models

class wagon (models.Model) :

    id = models.AutoField(primary_key = True)
    horaire_plan = models.CharField(max_length = 50)
    voyage = models.CharField(max_length = 500)
    img = models.CharField(max_length = 5000)
