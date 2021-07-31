from django.contrib import admin
from .models import Tests
from .models import General_Test
from .models import Advance_Test
from .models import College
from .models import Review
# Register your models here.
admin.site.register(Tests)
admin.site.register(General_Test)
admin.site.register(Advance_Test)
admin.site.register(College)
admin.site.register(Review)
