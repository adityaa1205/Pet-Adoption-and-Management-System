from django.apps import apps
from django.core.management import call_command
from django.db import connections

def apply_migrations():
    try:
        if apps.ready and connections['default'].connection:
            call_command("migrate", interactive=False)
            print("✅ Migrations applied")
    except Exception as e:
        print(f"❌ Migration error: {e}")

# Run only after Django boots
from django.core.signals import request_started
request_started.connect(lambda **kwargs: apply_migrations(), dispatch_uid="apply_migrations_once")
