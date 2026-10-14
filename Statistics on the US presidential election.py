import numpy as np
import datetime

def load_data(filename, use_cols_name):
    # 读取表头
    with open(filename, 'r', encoding='utf-8') as f:
        col_names_str = f.readline()[:-1]
    col_name_list = col_names_str.split(',')
    # 获取需要读取列的下标
    use_col_index = [col_name_list.index(name) for name in use_cols_name]
    # 读取数据
    data_array = np.loadtxt(filename,
                            delimiter=',',
                            skiprows=1,
                            dtype=str,
                            usecols=use_col_index)
    return data_array


def process_date(data_array):
    enddate_lst = data_array[:, 0].tolist()
    enddate_lst = [enddate.replace('-', '/') for enddate in enddate_lst]
    date_lst = [datetime.datetime.strptime(enddate, '%m/%d/%Y') for enddate in enddate_lst]
    # 这里改成 f-string
    month_lst = [f"{date_obj.year}-{date_obj.month:02d}" for date_obj in date_lst]

    month_array = np.array(month_lst)
    data_array[:, 0] = month_array
    return data_array


def get_month_stats(data_array):
    months = np.unique(data_array[:, 0])
    for month in months:
        filtered_data = data_array[data_array[:, 0] == month]
        try:
            filtered_poll_data = filtered_data[:, 1:].astype(float)
        except ValueError:
            continue
        result = np.sum(filtered_poll_data, axis=0)
        # print改成 f-string
        print(f'{month},Clinton 票数: {result[0]},Trump 票数: {result[1]}')


# 主程序运行
if __name__ == "__main__":
    cols = ['enddate', 'rawpoll_clinton', 'rawpoll_trump']
    data = load_data("presidential_polls.csv", cols)
    data = process_date(data)
    get_month_stats(data)
