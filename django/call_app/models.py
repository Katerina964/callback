from django.db import models


class Crmaccount(models.Model):
    host = models.CharField(max_length=200, verbose_name='host')
    token = models.CharField(max_length=200, verbose_name='token')


class Customer(models.Model):
    name = models.CharField(max_length=50, verbose_name='Имя', default="Друг")
    surname = models.CharField(max_length=50, verbose_name='Фамилия', default="Junior")

    def __str__(self):
        return self.name + " " + self.surname


class Call(models.Model):
    deal_id_megaplan = models.CharField(max_length=50, verbose_name='Сделка')
    tipe_of_deal = models.CharField(max_length=50, verbose_name='Тип сделки')
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, blank=True)
    employee = models.CharField(max_length=50, verbose_name='Сотрудник')
    employee_number = models.CharField(max_length=50, verbose_name='Номер сотрудника',
                                       default="Номер скрыт")
    customer_number = models.CharField(max_length=50, verbose_name='Номер клиента',
                                       default="Номер скрыт")
    call_len = models.CharField(max_length=50,
                                verbose_name='Длительность разговора', default='пока нет данных атс')
    result = models.CharField(max_length=50,
                              verbose_name='Результат звонка', default='пока нет данных атс')
    in_crm = models.CharField(max_length=25,
                              verbose_name=' Добавлено в CRM', default='пока нет данных атс')
