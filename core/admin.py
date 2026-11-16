from django.contrib import admin
from .models import *
for model in [m for m in globals().values() if isinstance(m, type) and hasattr(m, "_meta") and getattr(m, "__module__", "") == "core.models"]:
    try: admin.site.register(model)
    except admin.sites.AlreadyRegistered: pass
