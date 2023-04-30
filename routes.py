from flask import Blueprint, render_template, views
from view.devices_view import DeviceView
from view.costumer_view import CostumerView
from view.sell_view import SellsView

routes = Blueprint(__name__, "routes")


@routes.route("/")
def home(): return render_template("login.html")


# devices start ###########
@routes.route("/devices")
def devices(): return DeviceView.index()


@routes.route("/devices/create", methods=["POST", "GET"])
def create_device(): return DeviceView.create()


@routes.route("/devices/edit/<id>", methods=["POST", "GET"])
def edit_device(id): return DeviceView.edit(id)


@routes.route("/devices/remove/<id>")
def remove_device(id): return DeviceView.remove(id)


# costumers start ###########
@routes.route("/costumers")
def costumers(): return CostumerView.index()


@routes.route("/costumers/create", methods=["POST", "GET"])
def create_costumer(): return CostumerView.create()


@routes.route("/costumers/edit/<id>", methods=["POST", "GET"])
def edit_costumer(id): return CostumerView.edit(id)

@routes.route("/costumers/remove/<id>", methods=["POST", "GET"])
def remove_costumer(id): return CostumerView.remove(id)


# sells start ##############

@routes.route("/sells/")
def sells_index(): return SellsView.index()

@routes.route("/sells/create", methods=["POST", "GET"])
def sells_create(): return SellsView.create()

