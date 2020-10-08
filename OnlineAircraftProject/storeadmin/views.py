from django.shortcuts import render, redirect
from storeadmin.forms import ServiceForm, ManufactureForm, AircraftForm
from storeadmin.models import Service, Manufacture, Aircraftmodels


# Create your views here.
def manufactureCreate(request):
    form = ManufactureForm()
    context = {"form": form}
    qs = Manufacture.objects.all()
    context["manufacture"] = qs
    if request.method == 'POST':
        form = ManufactureForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return render(request, "storeadmin/manufacture.html", context)

    return render(request, "storeadmin/manufacture.html", context)


def manufactureView(request, pk):
    qs = Manufacture.objects.get(id=pk)
    context = {"view": qs}
    return render(request, "storeadmin/manufactureview.html", context)


def manufactureEdit(request, pk):
    qs = Manufacture.objects.get(id=pk)
    form = ManufactureForm(instance=qs)
    context = {"form": form}
    if request.method == 'POST':
        qs = Manufacture.objects.get(id=pk)
        form = ManufactureForm(instance=qs, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect("manufacture")

    return render(request, "storeadmin/manufactureedit.html", context)


def manufactureDelete(request, pk):
    qs = Manufacture.objects.get(id=pk)
    qs.delete()
    return redirect("manufacture")


def aircraftCreate(request):
    form = AircraftForm()
    context = {"form": form}
    qs = Aircraftmodels.objects.all()
    context["aircraft"] = qs
    if request.method == 'POST':
        form = AircraftForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return render(request, "storeadmin/aircraft.html", context)
    return render(request, "storeadmin/aircraft.html", context)


def aircraftView(request, pk):
    qs = Aircraftmodels.objects.get(id=pk)
    context = {"view": qs}
    return render(request, "storeadmin/aircraftview.html", context)


def aircraftEdit(request, pk):
    qs = Aircraftmodels.objects.get(id=pk)
    form = AircraftForm(instance=qs)
    context = {"form": form}
    if request.method == 'POST':
        qs = Aircraftmodels.objects.get(id=pk)
        form = AircraftForm(instance=qs, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect("aircraft")

    return render(request, "storeadmin/aircraftedit.html", context)


def aircraftDelete(request, pk):
    qs = Aircraftmodels.objects.get(id=pk)
    qs.delete()
    return redirect("aircraft")


def serviceCreate(request):
    form = ServiceForm()
    context = {"form": form}
    qs = Service.objects.all()
    context["service"] = qs
    if request.method == 'POST':
        form = ServiceForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, "storeadmin/service.html", context)
    return render(request, "storeadmin/service.html", context)


def serviceEdit(request, pk):
    qs = Service.objects.get(id=pk)
    form = ServiceForm(instance=qs)
    context = {"form": form}
    if request.method == 'POST':
        qs = Service.objects.get(id=pk)
        form = ServiceForm(instance=qs, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect("service")
    return render(request, "storeadmin/serviceedit.html", context)


def serviceDelete(request, pk):
    qs = Service.objects.get(id=pk)
    qs.delete()
    return redirect("service")


def index(request):
    return render(request, "storeadmin/home.html")
