import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")
django.setup()

from django.core.management import call_command

# Jalankan migrate
call_command("migrate")

# Jalankan collectstatic tanpa interaksi
call_command("collectstatic", interactive=False)

# (Opsional) Tambahkan superuser default (jika belum ada)
from django.contrib.auth import get_user_model
User = get_user_model()

if not User.objects.filter(username="admin").exists():
    User.objects.create_superuser("admin", "admin@example.com", "admin123")
    print("✅ Superuser 'admin' berhasil dibuat.")
else:
    print("ℹ️ Superuser 'admin' sudah ada.")

print("✅ Selesai menjalankan migrate + collectstatic.")
