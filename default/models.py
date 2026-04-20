from django.db import models

class check_form(models.Model):
    name       = models.CharField(max_length=100)
    email      = models.EmailField()
    message    = models.TextField()
    ip_address = models.GenericIPAddressField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
