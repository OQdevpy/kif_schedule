from django.db import models


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
    number = models.CharField(max_length=55, verbose_name="O'quv xonasi")
    size = models.IntegerField(verbose_name="Xona o'lchami")
    room_type = models.CharField(max_length=50, choices=(('Amaliyot', 'Amaliyot'), (
        "Maru'za", "Maru'za"), ('Laboratoriya', 'Laboratoriya')), verbose_name="Xona turi")

    def __str__(self):
        return f"{self.number} - xona"

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
    academic_code = models.CharField(max_length=50, verbose_name="Grurh code")

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


class Schedule(BaseModel):
    group = models.ForeignKey(
        Group, on_delete=models.CASCADE, verbose_name="Guruh")
    subject = models.ForeignKey(
        Subject, on_delete=models.CASCADE, verbose_name="Fan")
    teacher = models.ForeignKey(
        Teacher, on_delete=models.CASCADE, verbose_name="O'qituvchi")
    room = models.ForeignKey(
        Room, on_delete=models.CASCADE, verbose_name="Xona")
    day = models.CharField(max_length=50, choices=(('Dushanba', 'Dushanba'), ('Seshanba', 'Seshanba'), (
        'Chorshanba', 'Chorshanba'), ('Payshanba', 'Payshanba'), ('Juma', 'Juma')), verbose_name="Kun")
    para = models.CharField(max_length=50, choices=(
        ('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6')), verbose_name="Para")

    def __str__(self):
        return f"{self.group} - {self.subject}"

    class Meta:
        verbose_name = "Dars jadvali"
        verbose_name_plural = "Dars jadvali"

class Document(BaseModel):
    title = models.CharField(max_length=50, verbose_name="Fayl nomi")
    file_url = models.URLField(verbose_name="Fayl url")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Fayl"
        verbose_name_plural = "Fayllar"

    


class BotUser(BaseModel):
    tg_id = models.IntegerField(verbose_name="Telegram id",unique=True)
    username = models.CharField(
        max_length=50, verbose_name="Telegram username",
        null=True, blank=True,
        unique=True, db_index=True,
        error_messages={
            "unique": "A user with that username already exists.",
        },)
    full_name = models.CharField(
        max_length=50, verbose_name="Telegram full name",null=True,blank=True)
    phone_number = models.CharField(
        max_length=50, verbose_name="Tel raqam", null=True, blank=True)
    
    

    def str(self):
        if self.full_name:
            return self.full_name
        return self.tg_id

    class Meta:
        verbose_name = "Foydalanuvchi"
        verbose_name_plural = "Foydalanuvchilar"
