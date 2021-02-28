from django.shortcuts import render
from django.template import RequestContext
from django.views.decorators.csrf import csrf_protect

from .models import SystemState, SystemState_2, SystemState_3
from pymodbus.payload import BinaryPayloadBuilder
from pymodbus.constants import Endian
from pymodbus.client.sync import ModbusTcpClient as ModbusClient

IP_MODBUS = '18.156.13.209'
PORT_MODBUS = 10883

building = "B1"
state = SystemState.objects.all()


def write_32b_float(cli, reg, value):
    builder = BinaryPayloadBuilder(byteorder=Endian.Big, wordorder=Endian.Big)
    builder.add_32bit_float(value)
    cli.write_registers(reg, builder.build(), skip_encode=True)


# Create your views here.

def home(response):
    return render(response, "main/home.html", {})


def chart(response):
    global building, state
    client = ModbusClient(host=IP_MODBUS, port=PORT_MODBUS)
    if response.method == "POST":

        client.connect()
        if response.POST.get("failure"):
            # button clicked, send info about failure via MODBUS TCP/IP
            client.write_register(19, 5)
        elif response.POST.get("repair"):
            # button clicked, send info about failure's end via MODBUS TCP/IP
            client.write_register(19, 0)
        elif response.POST.get("B1"):
            building = "B1"
        elif response.POST.get("B2"):
            building = "B2"
        elif response.POST.get("B3"):
            building = "B3"
        client.close()

    if building == "B1":
        state = SystemState.objects.all()
    elif building == "B2":
        state = SystemState_2.objects.all()
    elif building == "B3":
        state = SystemState_3.objects.all()

    temps = list(state.values_list('temperature', flat=True))
    recent_temp = 0
    if temps:
        recent_temp = temps[-1]
    client.connect()
    write_32b_float(client, 2000, recent_temp)
    client.close()
    time = state.values_list('date', flat=True)
    time_str = [t.strftime("%d-%m %H:%M") for t in time]

    return render(response, "main/chart.html", {'temps': temps, 'time': time_str, 'building': building})


def others(response):
    return render(response, "main/others.html", {})


@csrf_protect
def chart_button_clicked(request):
    csrfContext = RequestContext(request)
    return render("main/chart.html", csrfContext)
