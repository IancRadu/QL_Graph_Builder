import pandas as pd



class get_data:

    def read_config_xlsx(self):
        try:
            df = pd.read_excel("./Config.xlsx", "Config", header=0).to_dict()
            config = {}
            path = df["Data_Folder"][0]
            for i in df["Chamber_Name"]:
                config[df["Chamber_Name"][i]] = df["Chamber_Number"][i]
            return config, path
        except PermissionError:
            pass  # returns None if Config excel file is open

    def read_values(self, path):
        pass

# data = get_data()
# print(data.read_config_xlsx())
# print(data.read_values(data.read_config_xlsx()[1]))