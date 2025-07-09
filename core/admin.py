from django.contrib import admin
from .models import Karyawan, Benefit, Kedisiplinan, SuratPeringatan

@admin.register(Karyawan)
class KaryawanAdmin(admin.ModelAdmin):
    list_display = ('no_id', 'nama', 'departemen', 'akses_hp', 'akses_laptop')
    search_fields = ('no_id', 'nama', 'departemen')


@admin.register(Benefit)
class BenefitAdmin(admin.ModelAdmin):
    list_display = ('karyawan', 'jenis', 'tanggal')
    list_filter = ('jenis', 'tanggal')
    search_fields = ('karyawan__nama',)


@admin.register(Kedisiplinan)
class KedisiplinanAdmin(admin.ModelAdmin):
    list_display = ('karyawan', 'jenis', 'tanggal')
    list_filter = ('jenis', 'tanggal')
    search_fields = ('karyawan__nama',)


@admin.register(SuratPeringatan)
class SuratPeringatanAdmin(admin.ModelAdmin):
    list_display = ('karyawan', 'jenis', 'tanggal_terbit', 'tanggal_berlaku_sampai', 'is_aktif')
    list_filter = ('jenis', 'tanggal_terbit')
