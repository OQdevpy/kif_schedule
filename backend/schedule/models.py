from django.db import models
from django.utils.safestring import mark_safe

class BaseModel(models.Model):
    created_at = models.DateTimeField(
        auto_now_add=True, verbose_name="Yaratilgan sana")
    updated_at = models.DateTimeField(
        auto_now=True, verbose_name="Yangilangan sana")
    is_active = models.BooleanField(default=True, verbose_name="Aktiv")

    class Meta:
        abstract = True

# Create your models here.


class Room(BaseModel):
    room = models.CharField(max_length=55, verbose_name="O'quv xonasi")
    size = models.IntegerField(verbose_name="Xona o'lchami", default=30)
    room_type = models.CharField(max_length=50, choices=(('Amaliyot', 'Amaliyot'), (
        "Ma'ruza", "Ma'ruza"), ('Laboratoriya', 'Laboratoriya')), verbose_name="Xona turi", default="Amaliyot")

    def __str__(self):
        return f"{self.room} - {self.room_type} ({self.size})"

    class Meta:
        verbose_name = "Xona"
        verbose_name_plural = "Xonalar"


class Teacher(BaseModel):
    name = models.CharField(max_length=50, verbose_name="F.I.O o'qituvchi")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "O'qituvchi"
        verbose_name_plural = "O'qituvchilar"


class Group(BaseModel):
    academic_code = models.CharField(max_length=50, verbose_name="Guruh code")
    kurs = models.IntegerField(verbose_name="Kurs",choices=((1,1),(2,2),(3,3),(4,4),(5,5)), default=1)

    def __str__(self):
        return self.academic_code

    class Meta:
        verbose_name = "Guruh"
        verbose_name_plural = "Guruhlar"


class Subject(BaseModel):
    name = models.CharField(max_length=50, verbose_name="Fan nomi")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Fan"
        verbose_name_plural = "Fanlar"

class Para(BaseModel):    
    para = models.CharField(max_length=50, choices=( ('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'), ('7', '7')), verbose_name="Juftlik", default="1")
    time_start = models.TimeField(verbose_name="Juftlik boshlanish vaqti", default="08:30:00")
    time_end = models.TimeField(verbose_name="Juftlik tugash vaqti", default="09:50:00")

    def __str__(self):
        return f"{self.para} : {self.time_start} - {self.time_end}"

    class Meta:
        verbose_name = "Juftlik"
        verbose_name_plural = "Juftliklar"
    
 
    def get_para_full(self):
        return f"{self.para} - juftlik ({self.time_start} - {self.time_end})"
        
        
class Schedule(BaseModel):
    group = models.ForeignKey(
        Group, on_delete=models.CASCADE, verbose_name="Guruh")
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE, verbose_name="Fan")
    lesson_type = models.CharField(max_length=50, choices=(('Amaliyot', 'Amaliyot'), (
        "Ma'ruza", "Ma'ruza"), ('Laboratoriya', 'Laboratoriya')), verbose_name="Dars turi", default="Amaliyot")
    teacher = models.ForeignKey(Teacher, on_delete=models.SET_NULL, verbose_name="O'qituvchi", null=True)
    room = models.ForeignKey( Room, on_delete=models.CASCADE, verbose_name="Xona")
    day = models.CharField(max_length=50, choices=(('Dushanba', 'Dushanba'), ('Seshanba', 'Seshanba'), (
        'Chorshanba', 'Chorshanba'), ('Payshanba', 'Payshanba'), ('Juma', 'Juma'), ('Shanba', 'Shanba')), verbose_name="Kun", default="Dushanba")
    para = models.ForeignKey(Para, on_delete=models.SET_NULL, verbose_name="Juftlik", null=True)
    week = models.CharField(max_length=20, choices=(('full', 'full'), ('odd', 'odd'), ('even', 'even')), verbose_name="Hafta", default="full")
    semester = models.CharField(max_length=20, choices=(('1', 'Kuzgi'), ('2', 'Bahorgi')), verbose_name="Semestr", default="1")

    def __str__(self):
        return f"{self.group} - {self.subject}"

    class Meta:
        verbose_name = "Dars jadvali"
        verbose_name_plural = "Dars jadvali"
    
    # def get_para_display(self):

class Document(BaseModel):
    title = models.CharField(max_length=50, verbose_name="Fayl nomi")
    description = models.TextField(verbose_name="Fayl haqida", default=" ")
    file_url = models.FileField(upload_to="documents/", verbose_name="Fayl")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Talaba hujjati"
        verbose_name_plural = "Talaba hujjatlari"

    def file_url_tag(self):
        if self.file_url:
            return mark_safe(f'<a href="/media/{self.file_url}" target=True>{self.file_url}</a>')
    
        return "Fayl yo'q"

class BotUser(BaseModel):
    tg_id = models.IntegerField(verbose_name="Telegram id",unique=True)
    username = models.CharField(
        max_length=50, verbose_name="Telegram username",
        null=True, blank=True,
       db_index=True,
        error_messages={
            "unique": "A user with that username already exists.",
        },)
    full_name = models.CharField(
        max_length=50, verbose_name="Telegram full name",null=True,blank=True)
    user_full_name = models.CharField(
        max_length=50, verbose_name="User full name", null=True, blank=True
    )
    phone_number = models.CharField(
        max_length=50, verbose_name="Tel raqam", null=True, blank=True)
    
    

    def str(self):
        if self.full_name:
            return self.full_name
        return self.tg_id

    class Meta:
        verbose_name = "Foydalanuvchi"
        verbose_name_plural = "Foydalanuvchilar"
