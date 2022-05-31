from openpyxl import load_workbook

def load_data():
    wb = load_workbook("Naive_S_P500.xlsx", data_only=True)
    ws = wb['return']
    assets_nums = 100
    days = 60
    assets_obs = []
    # for col in list(ws.columns)[2:2 + assets_nums]:
    #     assets_obs.append([x.value for x in list(col)[1:1 + days]])
    for col in list(ws.columns)[2:2+assets_nums]:
        assets_obs.append([x.value for x in list(col)[1:1 + days]])
    print(assets_obs)
    return assets_obs

load_data()

