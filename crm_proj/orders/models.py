from datetime import datetime

from django.core.exceptions import ValidationError
from django.db import models


class Devices(models.Model):
    class Meta:
        db_table = "devices"
        verbose_name = "Доступное оборудование"
        verbose_name_plural = "Доступное оборудование"

    manufacturer = models.TextField(verbose_name="Производитель")
    model = models.TextField(verbose_name="Модель")

    def __str__(self):
        return f"{self.manufacturer} {self.model}"


class Customer(models.Model):
    class Meta:
        db_table = "customers"
        verbose_name = "Описание клиента"
        verbose_name_plural = "Описание клиентов"

    customer_name = models.TextField(verbose_name="Наименование организации")
    customer_address = models.TextField(verbose_name="Адрес")
    customer_city = models.TextField(verbose_name="Город")

    def __str__(self):
        return f"{self.customer_name}"


class DeviceInField(models.Model):
    class Meta:
        db_table = "devices_in_fields"
        verbose_name = "Оборудование в полях"
        verbose_name_plural = "Оборудование в полях"

    serial_number = models.TextField(verbose_name="Серийный номер")
    customer_id = models.ForeignKey(Customer, on_delete=models.RESTRICT, verbose_name="Идентификатор пользователя")
    analyzer_id = models.ForeignKey(Devices, on_delete=models.RESTRICT, verbose_name="Идентификатор оборудования")
    owner_status = models.TextField(verbose_name="Статус принадлежности")

    def __str__(self):
        return f"{self.serial_number} {self.analyzer_id}"


def status_validator(order_status):
    if order_status not in ["open", "closed", "in progress", "need info"]:
        raise ValidationError


class Order(models.Model):
    class Meta:
        db_table = "orders"
        verbose_name = "Заявка"
        verbose_name_plural = "Заявки"

    device = models.ForeignKey(DeviceInField, on_delete=models.RESTRICT, verbose_name="Оборудование")
    customer = models.ForeignKey(Customer, on_delete=models.RESTRICT, verbose_name="Конечный пользователь")
    order_description = models.TextField(verbose_name="Описание")
    created_dt = models.DateTimeField(verbose_name="Создано", auto_now_add=True)
    last_update_dt = models.DateTimeField(verbose_name="Последнее изменение", blank=True, null=True)
    order_status = models.TextField(verbose_name="Статус заявки", validators=[status_validator])

    def save(self, *args, **kwargs):
        self.last_update_dt = datetime.now()
        super().save(*args, **kwargs)
