from django.db import models

class Karyawan(models.Model):
    no_id = models.CharField(max_length=50, unique=True)  # ID dari QR
    nama = models.CharField(max_length=100)
    departemen = models.CharField(max_length=100)
    nik = models.CharField("No. KTP",max_length=30, blank=True, null=True)
    bpjs_k = models.CharField("BPJS Kesehatan", max_length=30, blank=True, null=True)
    bpjs_tk = models.CharField("BPJS Ketenagakerjaan", max_length=30, blank=True, null=True)
    no_hp = models.CharField("No. HP", max_length=20, blank=True, null=True)

    # Akses perangkat
    akses_hp = models.BooleanField("Izin Membawa HP", default=False)
    akses_laptop = models.BooleanField("Izin Membawa Laptop", default=False)

    def __str__(self):
        return f"{self.no_id}- {self.nama}"

    class Meta:
        permissions = [
            ("can_scan_informasi", "Dapat Scan Informasi Karyawan"),
            ("can_scan_benefit", "Dapat Scan Benefit"),
            ("can_scan_kedisiplinan", "Dapat Scan Kedisiplinan"),
        ]


class Benefit(models.Model):
    JENIS_BENEFIT = [
        ('susu', 'Susu'),
        ('telur', 'Telur'),
        ('lainnya', 'Lainnya'),
    ]

    karyawan = models.ForeignKey(Karyawan, on_delete=models.CASCADE)
    jenis = models.CharField(max_length=20, choices=JENIS_BENEFIT)
    tanggal = models.DateField(auto_now_add=True)
    keterangan = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.karyawan.nama} - {self.jenis} ({self.tanggal})"


class Kedisiplinan(models.Model):
    JENIS_PELANGGARAN = [
        ('A', 'Alpha'),
        ('DT', 'Datang Terlambat'),
        ('PC', 'Pulang Cepat'),
        ('CX', 'Cuti Mendadak'),
    ]
    karyawan = models.ForeignKey(Karyawan, on_delete=models.CASCADE)
    tanggal = models.DateField()
    jenis = models.CharField(max_length=2, choices=JENIS_PELANGGARAN)

    def __str__(self):
        return f"{self.karyawan.nama} - {self.jenis} ({self.tanggal})"


class SuratPeringatan(models.Model):
    SP_CHOICES = [
        ('SP1', 'SP1'),
        ('SP2', 'SP2'),
        ('SP3', 'SP3'),
    ]

    karyawan = models.ForeignKey(Karyawan, on_delete=models.CASCADE)
    jenis = models.CharField(max_length=4, choices=SP_CHOICES)
    tanggal_terbit = models.DateField()
    tanggal_berlaku_sampai = models.DateField()
    keterangan = models.TextField(blank=True, null=True)

    def is_aktif(self):
        from django.utils import timezone
        return self.tanggal_berlaku_sampai >= timezone.now().date()

    def __str__(self):
        return f"{self.jenis} - {self.karyawan.nama} ({self.tanggal_terbit})"
