from django.apps import apps
from django.db import connections
from django.core.management import call_command

def run_migrations():
    try:
        # Run only after all apps are ready and DB is connected
        if apps.ready and connections['default'].connection:
            call_command("migrate", interactive=False)
            print("✅ Migrations applied successfully")
    except Exception as e:
        print("❌ Migration error:", e)
