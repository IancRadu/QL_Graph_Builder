import matplotlib.pyplot as plt
import matplotlib
import numpy as np

matplotlib.use('Agg')

import matplotlib.dates as mdates  # used for tikers
import mpld3
import base64
from io import BytesIO
from matplotlib.figure import Figure
import main


# TODO: Make new plot each time date is not available in under 60seconds

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

def graph(date, temperature_0, **kwargs):
    fig = plt.figure(figsize=(18, 8), dpi=80)  # plt.plot needs to receive an array of values

    temperature_0_float = [float(i) for i in temperature_0]
    new_start_plot = 0
    end_plot = 0
    # -----------------------------Plot a new line if no values are recorded for 300 seconds before a new point arise.
    for i in range(0, len(date)):
        # print(f"{i} try with {i+1}")
        if i < len(date) - 1:
            time_difference = (date[i + 1] - date[i]).seconds
            if time_difference > 660:
                end_plot = i
                print(f"New graph: {time_difference} between {date[i+1]} and {date[i]} with start:{new_start_plot} and end: {end_plot}")
                plot_date = [value for value in date if date[new_start_plot] <= value <= date[end_plot]]
                plot_temperature_0_float = [value for x, value in enumerate(temperature_0_float) if
                                            new_start_plot <= x <= end_plot]
                # print(plot_temperature_0_float)
                plt.plot(plot_date, plot_temperature_0_float, label="Temperature(°C)",
                         color="red")  # values have to be of type float for temperature
                new_start_plot = i + 1

                # print(f"{i} {len(date)}")
    # plt.plot(date, temperature_0_float, label="Temperature(°C)",
    #          color="red")  # values have to be of type float for temperature
    plt.xlabel('Time', color="black", fontsize="30")
    plt.ylabel('Temperature', color="red", fontsize="30")
    plt.grid(color='grey', linestyle='--', visible=True)  # Color can be changed to white to hide grid
    min_value = min(temperature_0_float)
    max_value = max(temperature_0_float)
    plt.yscale('linear')
    plt.yticks(np.arange(round(min_value - 15, -1), round(max_value + 15, 1), 5.0))
    plt.ylim(min_value - 10, max_value + 10)
    # plt.ylim(bottom=-50,top=150)
    # plt.axis(ymin=-40, ymax=200)
    # plt.minorticks_off()
    # plt.tick_params(direction='out', length=6, width=2, colors='r')
    # months = mdates.MonthLocator()
    # weeks = mdates.WeekdayLocator()
    # ax.grid(True)
    # ax.xaxis.set_major_formatter(mdates.DateFormatter("%m"))
    # ax.xaxis.set_major_locator(locator=months)
    # ax.xaxis.set_minor_locatorlocator=weeks)
    # ax.xaxis.set_major_formatter(
    #     mdates.ConciseDateFormatter(ax.xaxis.get_major_locator()))
    # try:
    #     x = kwargs['humidity_1']  # Used just to trow error faster, in case kwargs not sent
    #     ax1 = plt.gca()  # get current axes
    #     ax2 = ax1.twinx()  # create another axis that shares the same x-axis
    #     plt.plot(dates, kwargs['humidity_1'], label="Humidity(rH%)", color="blue")  # kwargs['humidity_1'] represents
    #     # humidity which is optional to be shown in graph
    #     # plt.grid(color='grey', linestyle='--')  # Color can be changed to white to hide grid
    #     # plt.plot(dates, temperature_0, label="Temperature(°C)", color="red")
    #     # ax2.minorticks_off() #Remove minor ticks from the current plot.
    #     ax2.set_ylabel('Humidity', color="blue", fontsize="30")
    #     # ax2.set_ylim([0, 100])
    #     # ax2.grid(True)
    #     # ax2.xaxis.set_major_formatter(mdates.DateFormatter("%m"))
    #     # ax2.xaxis.set_major_locator(locator=months)
    #     # ax2.xaxis.set_minor_locator(locator=weeks)
    #     # ax.xaxis.set_major_formatter(
    #     #     mdates.ConciseDateFormatter(ax.xaxis.get_major_locator()))
    # except KeyError:
    #     print("No humidity")
    #     pass
    # Save it to a temporary buffer.
    buf = BytesIO()
    fig.savefig(buf, format="png")
    #     # Embed the result in the html output.
    figs = plt.savefig('graph.png')
    data = base64.b64encode(buf.getbuffer()).decode("ascii")
    # return f"<img src='data:image/png;base64,{data}'/>"
    # graph_result = plt.show() # to show graph
    html_str = mpld3.fig_to_html(fig)  # library which converts figure as html
    return html_str
