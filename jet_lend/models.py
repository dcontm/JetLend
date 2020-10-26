from django.db import models
from . import utils
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.

class Investor(models.Model):

    first_name = models.CharField(max_length = 200)
    last_name = models.CharField(max_length = 200)
    patponymic = models.CharField(max_length = 200)

    def __str__(self):        
        return f'{self.last_name} {self.first_name} {self.patponymic}'

    class Meta:
        verbose_name = 'Инвестор'
        verbose_name_plural = 'Инвесторы'


class Passport(models.Model):

    investor = models.ForeignKey('Investor',
                                 related_name = 'passports',
                                 on_delete=models.CASCADE
                                 )
    serial = models.PositiveSmallIntegerField()
    number = models.PositiveIntegerField()
    date_of_birth = models.DateField()
    place_of_birth = models.CharField(max_length = 3000)
    date_of_issue = models.DateField()
    issued_by = models.CharField(max_length = 3000)
    code_subdivision = models.PositiveIntegerField()
    registration_address = models.CharField(max_length = 3000)

    screen_part1 = models.FileField(upload_to=utils.upload_to)
    screen_part2 = models.FileField(upload_to=utils.upload_to)

    def __str__(self):        
        return f'{self.serial}_{self.number}'

    class Meta:
        verbose_name = 'Паспорт'
        verbose_name_plural = 'Паспорта'


class Document(models.Model):

    investor = models.ForeignKey('Investor',
                          related_name = 'documents',
                          on_delete=models.CASCADE
                          )
    doc_title = models.CharField(max_length = 500)
    doc_screen = models.FileField(upload_to=utils.upload_to)

    def __str__(self):        
        return f'{self.doc_name}'

    class Meta:
        verbose_name = 'Квалификационный документ'
        verbose_name_plural = 'Квалификационные документы'


class Qualification(models.Model):

    ST1 = 'ST1' # шаг 1 завершен
    ST2 = 'ST2' # шаг 2 завершен
    ST31 = 'ST31' # шаг 3 завершен загрузкой документа
    ST32 = 'ST32' # шаг 3 завершен отказом от квалификации

    STATE = [
        (ST1, 'Первый этап завершен'),
        (ST2, 'Второй этап завершен'),
        (ST31, 'Третий этап завершен загрузкой документа'),
        (ST32, 'Третий этап завершен отказом от квалификации'),
    ]
    
    state = models.CharField(max_length=4, choices=STATE, default=ST1)
    accept_rules =models.BooleanField(default=False)
    investor = models.ForeignKey('Investor',
                                 related_name = 'qualifications',
                                 on_delete=models.CASCADE
                                 )

    def __str__(self):        
        return f'{self.investor} {self.state}'

    def create_qualification(sender, instance, created, **kwargs):
    # создание объекта квалификафии происходит одновременно с созданием
    # объекта паспорта 
        if created:
            Qualification.objects.create(investor=instance.investor)
    post_save.connect(create_qualification, sender=Passport)

    class Meta:
        verbose_name = 'Квалификация'
        verbose_name_plural = 'Квалификации'




