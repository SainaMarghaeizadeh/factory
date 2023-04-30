from flask import render_template, request, redirect
from controller.device_controller import DeviceController


class DeviceView:
    @classmethod
    def create(cls):
        if request.method == "POST":
            device_name = request.form["device_name"]
            device_model = request.form["device_model"]
            device_count = int(request.form["device_count"])
            device_available = int(request.form["device_available"])
            DeviceController.save(device_name, device_model, device_count, device_available)
            return redirect('/devices')
        else:
            return render_template("devices/create.html")

    @classmethod
    def index(cls):
        return render_template("devices/index.html", devices=DeviceController.find_all())

    @classmethod
    def edit(cls, id):
        if request.method == "POST":
            device_name = request.form["device_name"]
            device_model = request.form["device_model"]
            device_count = int(request.form["device_count"])
            device_available = int(request.form["device_available"])
            DeviceController.edit(id, device_name, device_model, device_count, device_available)
            return redirect('/devices')
        else:
            return render_template("devices/edit.html", device=DeviceController.find_by_code(id))

    @classmethod
    def remove(cls, id):
        DeviceController.remove(id)
        return redirect('/devices')
