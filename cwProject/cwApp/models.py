from django.db import models


# mom models
class Mom(models.Model):
    mom_fn = models.CharField(max_length=200, default="")
    mom_ln = models.CharField(max_length=200, default="")
    mom_pn = models.CharField(max_length=200, default="")

    def __str__(self):
        return f'{self.mom_fn} {self.mom_ln}'


# kid models
class Child(models.Model):
    child_fn = models.CharField(max_length=200, default="")
    child_ln = models.CharField(max_length=200, default="")
    child_mom = models.ForeignKey(Mom, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.child_fn} {self.child_ln}'
