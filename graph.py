import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('Agg')

import matplotlib.dates as mdates  # used for tikers
import mpld3
import base64
from io import BytesIO
from matplotlib.figure import Figure
import main

date = [1, 2, 3, 4, 5, 6]
temperature_0 = [23, 42, 43, 44, 41, 23]
humidity_1 = [82, 83, 84, 81, 85, 54]
Temperature_y_min = 20
Temperature_y_max = 90


# def graph(date, temperature_0, **kwargs):
#     # Generate the figure **without using pyplot**.
#     fig = Figure()
#     ax = fig.subplots()
#     ax.plot([1, 2, 3, 5, 6, 7, 8, 9, 0])
#
#     # Save it to a temporary buffer.
#     buf = BytesIO()
#     fig.savefig(buf, format="png")
#     # Embed the result in the html output.
#     data = base64.b64encode(buf.getbuffer()).decode("ascii")
#     # return f"<img src='data:image/png;base64,{data}'/>"
#     html_str = mpld3.fig_to_html(fig)  # library which converts figure as html
#     return html_str

# ------------------------- Old version implemented with pyplot-------------------------------------------------
def graph(date, temperature_0, **kwargs):
    fig = plt.figure(figsize=(18, 8)) # set the size of the matplotlib canvas
    #  plt.plot needs to receive an array of values
    plt.plot(date, temperature_0, label="Temperature(°C)", color="red")
    plt.xlabel('Time', color="black", fontsize="16")
    plt.ylabel('Temperature', color="red", fontsize="16")
    plt.grid(color='grey', linestyle='--') # Color can be changed to white to hide grid
    plt.ylim(kwargs['Temperature_y_min'], kwargs['Temperature_y_max'])
    try:
        x = kwargs['humidity_1']  # Used just to trow error faster, in case kwargs not sent
        ax1 = plt.gca()  # get current axes
        ax2 = ax1.twinx()  # create another axis that shares the same x-axis
        plt.plot(date, kwargs['humidity_1'], label="Humidity(rH%)", color="blue")  # kwargs['humidity_1'] represents
        # humidity which is optional to be shown in graph
        plt.plot(date, temperature_0, label="Temperature(°C)", color="red")
        ax2.set_ylabel('Humidity', color="blue", fontsize="16")
        ax2.set_ylim(0, 100)
    except KeyError:
        pass
    # graph_result = plt.show() # to show graph
    # fig = plt.savefig('graph.png')
    html_str = mpld3.fig_to_html(fig)  # library which converts figure as html
    return html_str


# graph(date, temperature_0, humidity_1=humidity_1, Temperature_y_min=Temperature_y_min,
#       Temperature_y_max=Temperature_y_max)
