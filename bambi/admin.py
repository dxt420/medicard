from django.contrib import admin
from . models import *

# Register your models here.
admin.site.register(Agent)
admin.site.register(CustomUser)
admin.site.register(Member)
admin.site.register(Log)
admin.site.register(MemberFunds)
# admin.site.register(Member)