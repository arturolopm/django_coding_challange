from django.contrib import admin
from .models import Client, License  # Import your models here

admin.site.register(Client)  # Register the Client model
admin.site.register(License)  # Register the License model
# Register your models here.
