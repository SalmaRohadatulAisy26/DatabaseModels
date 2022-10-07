from django.db import models

# Create your models here.

class fakultas(models.Model):
    id_fakultas = models.IntegerField()
    nama_fakultas = models.CharField(max_length=200)
    
    def __str__(self):
        return self.id_fakultas

class Dosen(models.Model):
    NIP = models.CharField(max_length=200)
    nama = models.CharField(max_length=200)
    TanggalLahir = models.CharField(max_length=50)
    Photo = models.CharField(max_length=200)
    Email = models.CharField(max_length=200)
    id_fakultas = models.ForeignKey(fakultas, on_delete=models.CASCADE, null=True)
    id_prodi = models.CharField(max_length=200)
    AlamatRumah = models.TextField(max_length=200)
    
    def __str__(self):
        return self.nama
    
class Tendik(models.Model):
    NIP = models.CharField(max_length=200)
    Nama = models.CharField(max_length=200)
    TanggalLahir = models.CharField(max_length=50)
    Photo = models.CharField(max_length=200)
    Email = models.CharField(max_length=200)
    Unit = models.CharField(max_length=200)
    Prodi = models.CharField(max_length=200)
    AlamatRumah = models.TextField(max_length=200)

    def __str__(self):
        return self.NIP

class Mahasiswa(models.Model):
    NIM = models.CharField(max_length=200)
    Nama = models.CharField(max_length=200)
    TanggalLahir = models.CharField(max_length=50)
    Photo = models.CharField(max_length=200)
    Email = models.CharField(max_length=200)
    Fakultas = models.CharField(max_length=200)
    Prodi = models.CharField(max_length=200)
    AlamatRumah = models.TextField(max_length=200)

    def __str__(self):
        return self.NIM

