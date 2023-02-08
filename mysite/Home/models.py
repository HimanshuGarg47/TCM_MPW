from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from django.core.validators import MinLengthValidator


# Create your models here.
class Enquiry(models.Model):
    name = models.CharField(max_length=100)
    email_address = models.EmailField()
    phone = PhoneNumberField(null=False, blank=False)
    content = models.TextField(validators=[MinLengthValidator(10)])

    
    def __str__(self):
        return self.name + " | " + str(self.email_address)
    
    