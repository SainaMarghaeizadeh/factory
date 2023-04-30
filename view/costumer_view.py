from flask import Blueprint, render_template, request, redirect
from controller.costumer_controller import CostumerController
import jdatetime
import datetime

from controller.device_controller import DeviceController

class CostumerView:
    @classmethod
    def index(cls):
        costumers = list(CostumerController.find_all())
        for index, costumer in enumerate(costumers):
            costumers[index] = list(costumers[index])
            gregorian_parts = costumer[3].strftime("%Y-%m-%d").split('-')
            gregorian_year = int(gregorian_parts[0])
            gregorian_month = int(gregorian_parts[1])
            gregorian_day = int(gregorian_parts[2])
            costumers[index][3] = (
                jdatetime.date.fromgregorian(year=gregorian_year, month=gregorian_month, day=gregorian_day).strftime(
                    '%Y/%m/%d'))
        return render_template("costumers/index.html", costumers=costumers)

    @classmethod
    def create(cls):
        if request.method == "POST":
            costumer_name = request.form["costumer_name"]
            costumer_family = request.form["costumer_family"]
            costumer_birth_date = request.form["costumer_birth_date"]
            english_text = costumer_birth_date.translate(str.maketrans("۰۱۲۳۴۵۶۷۸۹", "0123456789"))
            jdatetime_object = jdatetime.datetime.strptime(english_text, '%Y/%m/%d').date()
            gregorian_date = jdatetime_object.togregorian().strftime('%Y-%m-%d')
            CostumerController.save(costumer_name, costumer_family, gregorian_date)
            return redirect('/costumers')
        else:
            return render_template("costumers/create.html")

    @classmethod
    def edit(cls, id):
        if request.method == "POST":
            costumer_name = request.form["costumer_name"]
            costumer_family = request.form["costumer_family"]
            costumer_birth_date = request.form["costumer_birth_date"]
            english_text = costumer_birth_date.translate(str.maketrans("۰۱۲۳۴۵۶۷۸۹", "0123456789"))
            jdatetime_object = jdatetime.datetime.strptime(english_text, '%Y/%m/%d').date()
            gregorian_date = jdatetime_object.togregorian().strftime('%Y-%m-%d')
            CostumerController.edit(id, costumer_name, costumer_family, gregorian_date, 1)
            return redirect('/costumers')
        else:
            costumer = CostumerController.find_by_code(id)
            birth = costumer.birth_date
            gregorian_parts = birth.strftime("%Y-%m-%d").split('-')
            gregorian_year = int(gregorian_parts[0])
            gregorian_month = int(gregorian_parts[1])
            gregorian_day = int(gregorian_parts[2])
            birth = (
                jdatetime.date.fromgregorian(year=gregorian_year, month=gregorian_month, day=gregorian_day).strftime(
                    '%Y-%m-%d'))
            return render_template("costumers/edit.html", costumer=costumer, birth=birth)

    @classmethod
    def remove(cls, id):
        CostumerController.remove(id)
        return redirect('/costumers')
