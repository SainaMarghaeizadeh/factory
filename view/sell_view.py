from flask import Blueprint, render_template, request, redirect

from controller.device_controller import DeviceController
from controller.costumer_controller import CostumerController

from controller.sell_controller import SellController
import jdatetime
import datetime


class SellsView:
    @classmethod
    def index(cls):
        sells = SellController.find_all()
        return render_template("sells/index.html", sells=sells)
        for index, sell in enumerate(sells):
            sells[index] = list(sells[index])
            gregorian_parts = sell[5].strftime("%Y-%m-%d").split('-')
            gregorian_year = int(gregorian_parts[0])
            gregorian_month = int(gregorian_parts[1])
            gregorian_day = int(gregorian_parts[2])
            sells[index][5] = (jdatetime.date.fromgregorian(year=gregorian_year, month=gregorian_month, day=gregorian_day).strftime('%Y/%m/%d'))

    @classmethod
    def create(cls):
        if request.method == "POST":
            costumer_code = request.form["costumer_code"]
            device_code = request.form["device_code"]
            sell_price = request.form["sell_price"]
            sell_count= request.form["sell_count"]
            sell_date = request.form["sell_date"]
            english_text = sell_date.translate(str.maketrans("۰۱۲۳۴۵۶۷۸۹", "0123456789"))
            jdatetime_object = jdatetime.datetime.strptime(english_text, '%Y/%m/%d').date()
            gregorian_date = jdatetime_object.togregorian().strftime('%Y-%m-%d')
            SellController.save(costumer_code,device_code,sell_price,sell_count,gregorian_date)
            return redirect('/sells')
        else:
            devices = DeviceController.find_all_available()
            customers = CostumerController.find_all()
            return render_template("sells/create.html", devices=devices, customers=customers)

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
            birth = (jdatetime.date.fromgregorian(year=gregorian_year, month=gregorian_month, day=gregorian_day).strftime('%Y-%m-%d'))
            return render_template("costumers/edit.html", costumer=costumer, birth=birth)

    @classmethod
    def remove(cls, id):
        CostumerController.remove(id)
        return redirect('/costumers')