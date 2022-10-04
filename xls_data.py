from datetime import datetime
import pandas as pd


class get_data:
    @staticmethod
    def read_config_xlsx():
        try:
            df = pd.read_excel("./Config.xlsx", "Config", header=0).to_dict()
            config = {}
            path = df["Data_Folder"][0]
            for i in df["Chamber_Name"]:
                config[df["Chamber_Name"][i]] = df["Chamber_Number"][i]
            return config, path
        except PermissionError:
            pass  # returns None if Config Excel file is open

    @staticmethod
    def read_values(path, chambers):
        try:
            df = pd.read_excel(path, "AMR WinControl", header=0)
            df_as_dict = df.to_dict()
            for value in df_as_dict["Unnamed: 0"]:
                for key in chambers:  # key = Name of climatic chamber
                    for i in df:  # For header name in Excel file
                        if i.split(' ')[0].strip(' ') == f"{chambers[key]}.0":  # .0 represent the values from temp
                            for m in df[i]:  # value from column i
                                temperature_0 = m
                        if i.split(' ')[0].strip(' ') == f"{chambers[key]}.1":  # .1 represent the values from humidity
                            for m in df[i]:  # value from column i
                                humidity_1 = m

        except PermissionError:
            pass  # returns None if Config Excel file is open

# data = get_data()
# print(data.read_config_xlsx())
# print(data.read_values(data.read_config_xlsx()[1]))
