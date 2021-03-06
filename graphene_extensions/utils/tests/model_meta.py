from django.db import models

from ..model_meta import get_fields, get_related_fields, get_model_select, get_model_prefetch, get_model_columns


class Topping(models.Model):
    name = models.CharField(max_length=128)


class PizzaType(models.Model):
    name = models.CharField(max_length=128)


class Pizza(models.Model):
    type = models.ForeignKey(PizzaType)
    name = models.CharField(max_length=128)
    toppings = models.ManyToManyField(Topping)
    extra_toppings = models.ManyToManyField(Topping, related_name='extra_pizzas')


def test_pizza_type_field_names():
    assert get_fields(PizzaType).keys() == {'id', 'pk', 'name', 'pizza_set'}


def test_pizza_field_names():
    assert get_fields(Pizza).keys() == {'id', 'pk', 'type', 'name', 'toppings', 'extra_toppings'}


def test_topping_field_names():
    assert get_fields(Topping).keys() == {'id', 'pk', 'name', 'pizza_set', 'extra_pizzas'}


def test_related_fields():
    assert {field.name for field in get_related_fields(PizzaType)} == {'pizza'}
    assert {field.name for field in get_related_fields(Pizza)} == {'type', 'toppings', 'extra_toppings'}
    assert {field.name for field in get_related_fields(Topping)} == {'pizza', 'extra_pizzas'}


def test_model_select():
    assert get_model_select(Pizza) == {'type': PizzaType}


def test_model_prefetch():
    assert get_model_prefetch(Pizza) == {'toppings': Topping, 'type': PizzaType, 'extra_toppings': Topping}
    assert get_model_prefetch(PizzaType) == {'pizza_set': Pizza}
    assert get_model_prefetch(Topping) == {'pizza_set': Pizza, 'extra_pizzas': Pizza}


def test_model_columns():
    assert get_model_columns(Pizza) == {'id', 'type_id', 'name'}
    assert get_model_columns(PizzaType) == {'id', 'name'}
    assert get_model_columns(Topping) == {'id', 'name'}
