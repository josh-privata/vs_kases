from django.db import models

class CaseManager(models.Manager):
    
    def count_cases(self):
        return self.objects.count()
  