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


def graph(date, temperature_0, **kwargs):
    def new_plot(y_axis_values, label, color):
        new_start_plot = 0
        end_plot = 0
        # -------------------------Plot a new line if no values are recorded for 300 seconds before a new point arise.
        plot_w_time_difference = False
        for i in range(0, len(date)):
            if i < len(date) - 1:
                time_difference = (date[i + 1] - date[i]).seconds
                if time_difference > 300:
                    plot_w_time_difference = True
                    end_plot = i
                    print(
                        f"New graph: {time_difference} between {date[i]} and {date[i + 1]} with start:{new_start_plot} and end: {end_plot}")
                    plot_date = [value for value in date if date[new_start_plot] <= value <= date[end_plot]]
                    plot_y_values = [value for xvalue, value in enumerate(y_axis_values) if
                                     new_start_plot <= xvalue <= end_plot]
                    plt.plot(plot_date, plot_y_values, label=label,
                             color=color)  # values have to be of type float for temperature
                    new_start_plot = i + 1
        # -----------------------------Plot a single line if values found each 60 seconds
        if not plot_w_time_difference:  # If values found every 300 seconds then all values will be plotted
            plt.plot(date, y_axis_values, label=label,
                     color=color)  # values have to be of type float for temperature

    fig = plt.figure(figsize=(18, 8), dpi=80)  # plt.plot needs to receive an array of values
    temperature_0_float = [float(i) for i in temperature_0]
    new_plot(temperature_0_float, 'Temperature(°C)', 'red')
    # ---------------------Format color, tick distance of axis
    plt.xlabel('Time', color="black", fontsize="30")
    plt.ylabel('Temperature', color="red", fontsize="30")
    plt.grid(color='grey', linestyle='--', visible=True)  # Color can be changed to white to hide grid
    min_value = min(temperature_0_float)
    max_value = max(temperature_0_float)
    plt.yscale('linear')
    plt.yticks(np.arange(round(min_value - 15, -1), round(max_value + 15, 1), 5.0))
    plt.ylim(min_value - 10, max_value + 10)
    plt.gcf().autofmt_xdate()

    # plt.xticks(np.arange(min(date), max(date)))
    # ----------------------------- To format the date for x axis
    # plt.gcf().autofmt_xdate()
    # myFmt = mdates.DateFormatter('%d-%m-%Y')  # %H:%M
    # plt.gca().xaxis.set_major_formatter(myFmt)
    # myFmtDay = mdates.DateFormatter('%d-%m-%Y')  # %H:%M
    # plt.gca().xaxis.set_minor_formatter(myFmtDay)
    # plt.gca().xaxis.set_major_locator(mdates.MonthLocator())
    # plt.gca().xaxis.set_minor_locator(mdates.DayLocator())
    # # plt.xlim(min(date),max(date))
    # # plt.minorticks_off()
    # # plt.tick_params(axis="x",direction='out', length=6, width=2)
    # # months = mdates.MonthLocator()
    # # weeks = mdates.WeekdayLocator()
    try:
        # humidity_float =[float(i) for i in kwargs['humidity_1']]
        ax1 = plt.gca()  # get current axes
        ax2 = ax1.twinx()  # create another axis that shares the same x-axis
        new_plot(kwargs['humidity_1'], 'label="Humidity(rH%)', 'blue')
        # plt.plot(date, kwargs['humidity_1'], label="Humidity(rH%)", color="")  # kwargs['humidity_1'] represents
        # humidity which is optional to be shown in graph
        # plt.grid(color='grey', linestyle='--')  # Color can be changed to white to hide grid
        # plt.plot(dates, temperature_0, label="Temperature(°C)", color="red")
        # ax2.minorticks_off() #Remove minor ticks from the current plot.
        ax2.set_ylabel('Humidity', color="blue", fontsize="30")
        ax2.set_ylim([0, 100])
        ax2.set_yscale('linear')
        ax1.set_yscale('linear')
        # ax2.xaxis.set_major_formatter(mdates.DateFormatter("%m"))
        # ax2.xaxis.set_major_locator(locator=months)
        # ax2.xaxis.set_minor_locator(locator=weeks)
        # ax.xaxis.set_major_formatter(
        #     mdates.ConciseDateFormatter(ax.xaxis.get_major_locator()))
    except KeyError:
        print("No humidity")
        pass
    # Save it to a temporary buffer.
    buf = BytesIO()
    fig.savefig(buf, format="png")
    #     # Embed the result in the html output.
    # figs = plt.savefig('graph.png')
    data = base64.b64encode(buf.getbuffer()).decode("ascii")
    return f"<img src='data:image/png;base64,{data}'/>"
    # graph_result = plt.show() # to show graph
    # html_str = mpld3.fig_to_html(fig)  # library which converts figure as html
    # return html_str
