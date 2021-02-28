import dash
import dash_daq as daq
import dash_html_components as html
import dash_core_components as dcc
from pymodbus.client.sync import ModbusTcpClient as ModbusClient
from pymodbus.payload import BinaryPayloadDecoder
from pymodbus.constants import Endian

IP_MODBUS = '18.156.13.209'
PORT_MODBUS = 10883

client = ModbusClient(host=IP_MODBUS, port=PORT_MODBUS)

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash('display', external_stylesheets=external_stylesheets)
server = app.server


def read_32b_float(cli, reg):
    result = cli.read_holding_registers(reg, 2)
    if result.isError():
        return
    decoder = BinaryPayloadDecoder.fromRegisters(result.registers, byteorder=Endian.Big, wordorder=Endian.Big)
    return decoder.decode_32bit_float()


app.layout = html.Div([
    daq.Gauge(
        color={"gradient": True, "ranges": {"green": [0, 15], "yellow": [15, 30], "red": [30, 50]}},
        showCurrentValue=True,
        id='my-gauge',
        value=0,
        label='Actual temperature',
        max=50,
        min=0,
    ),

    dcc.Interval(id="timing", interval=2000, n_intervals=0),
])


@app.callback(
    dash.dependencies.Output("my-gauge", "value"),
    dash.dependencies.Input("timing", "n_intervals"),
)
def update_temp(n_intervals):
    client.connect()
    tmp = read_32b_float(client, 2000)
    client.close()
    return tmp


if __name__ == '__main__':
    app.run_server(debug=False)
