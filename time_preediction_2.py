# basic imports:
import numpy as np
from sklearn import linear_model
from corona_adt import Corona
from sklearn.svm import SVR
import matplotlib.pyplot as plt
from datetime import date as days
from datetime import timedelta


class Prediction:
    def __init__(self):
        self.c = Corona("USA")
        self.new_data = self.c.get_history_by_particular_country("USA")

        self.data = self.extract_data()
        self.predict = [year for year in range(len(self.data))]

    def extract_data(self):
        cases = {}
        for item in self.new_data["stat_by_country"]:
            cases.update({item["record_date"]: item["total_cases"]})
        return cases

    def chop_data(self):
        chopped_data = {}
        for item in self.data:
            last_item = item
            item = int(item.split(" ")[0].replace("-", ""))
            if self.data[last_item] not in chopped_data.values():
                chopped_data.update({item: self.data[last_item]})
        return chopped_data

    def define_numpy(self):
        data = self.chop_data()
        dates = [date for date in data]
        str_dates = ["{}-{}-{}".format(str(item)[:4], str(item)[4:6], str(item)[6:]) for item in data][::-1]
        dates = dates[::-1]
        items = []

        for k in data:
            items.append(int(data[k].replace(",", "")))
        items = items[::-1]

        return dates, items, str_dates

    def best_fitted_line(self):
        arr = self.define_numpy()
        linear = linear_model.LinearRegression()
        linear.fit(arr[0], arr[1])
        acc = linear.score(arr[2], arr[3])
        print(acc)

    def get_days(self, today):
        # print(self.data.get())
        year_now = int(list(self.data.keys())[0][:4])
        try:
            month_now = int(list(self.data.keys())[0][5:7])
        except TypeError:
            month_now = int(list(self.data.keys())[0][6:7])
        try:
            day_now = int(list(self.data.keys())[0][8:10])
        except TypeError:
            day_now = int(list(self.data.keys())[0][9:10])

        day_0 = days(year_now, month_now, day_now)
        day_1 = days(int(today[0]), int(today[1]), int(today[2]))
        delta = day_1 - day_0

        dates_int = []
        dates_str = []
        for d in range(delta.days + 1):
            dates_str.append((day_0 + timedelta(days=d)).__str__())
            dates_int.append([int((day_0 + timedelta(days=d)).__str__().replace("-", ""))])

        return dates_str, dates_int, delta.days

    @staticmethod
    def prediction(dates, values, x):
        predictions = []
        dates = np.reshape(dates, (len(dates), 1))
        x = np.reshape(x, (len(x), 1))

        svr_rbf = SVR(kernel="rbf", C=1e7, gamma=0.005)
        svr_rbf.fit(dates, values)
        # print(svr_rbf.score(dates, values))
        # print(svr_rbf.predict(x)[0], "- rfb")
        # print()


        svr_poly = SVR(kernel="poly", C=1e3, degree=1.1)
        svr_poly.fit(dates, values)
        # print(svr_poly.score(dates, values))
        # print(svr_poly.predict(x)[0], "- poly")
        # print()

        svr_lin = SVR(kernel="linear", C=1e3)
        svr_lin.fit(dates, values)
        # print(svr_lin.score(dates, values))
        # print(svr_lin.predict(x)[0], "- hello")
        # print()

        # predictions.append(svr_rbf.predict(x)[0])
        # plt.show()
        predictions.append(svr_rbf.predict(x)[0])



        return predictions

    @staticmethod
    def plot_graph(str_dates, values, dates, prediction):

        # d = "{}-{}-{}".format(str(dates)[:4], str(dates)[4:6], str(dates)[6:])

        fig = plt.gcf()
        fig.set_size_inches(10.5, 7.5)

        print(len(str_dates), str_dates)
        print(len(values), values)

        plt.scatter(str_dates, values, edgecolors="black")
        plt.plot(str_dates, values, color='green')

        ox = [str_dates[0]]
        for item in (sorted(list(set(i for i in str_dates
                                     if i[-2] == "0" and i[-1] == "1"
                                     or i[-2] == "1" and i[-1] == "5")))):
            ox.append(item)
        ox.append(str_dates[-1])
        arr_y = np.arange(min(values), max(values) + 1, max(values) / 10)
        oy = np.append(arr_y, [])

        plt.xticks(ox)
        plt.yticks(oy)
        plt.gcf().autofmt_xdate()

        plt.scatter(dates, prediction, edgecolors="orange")
        plt.plot(dates, prediction)
        plt.show()


if __name__ == '__main__':
    p = Prediction()
    date = 20200515

    # date = "2020-05-15"

    data = p.define_numpy()


    number_days = p.get_days(["2021", "01", "01"])
    print(number_days)
    # for i in range()
    item = [i for i in range(len(data[0]))]
    print(item)
    # a = p.prediction(data[0], data[1], number_days[1])
    f = [i + len(item) for i in range(number_days[2] + 1)]
    print(f)
    # print(number_days[2], len(number_days[1]))
    # print()
    # print(item)
    # print(data[1])

    predictions = []

    # copy of data numbers for saving (the data[1] is a dynamic array):
    data_plus = [i for i in data[1]]
    print(data[1])

    for i in range(len(number_days[1])):
        # print()
        # print(item)
        # print(data[1])

        a = p.prediction(item, data[1], [f[i]])
        # item.append(item[-1] + 1)
        # data[1].append(a[0])

        # print(a)
        predictions.append(a)

        # print(a)

    print(a, "here")
    print("ok")


    p.plot_graph(data[2], data_plus, number_days[0], predictions)
