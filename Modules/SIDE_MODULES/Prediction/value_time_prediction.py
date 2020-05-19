# basic imports:
import numpy as np
from Modules.ADT.COVID_ADT.Corona_ADT import CoronaADT
from sklearn.svm import SVR
import matplotlib.pyplot as plt
from datetime import date as days
from datetime import timedelta


class Prediction:
    def __init__(self, gamma, c, country, indicator="total_cases"):
        """
        Define parameters
        :param gamma: defines how far the influence of a
        single training example reaches
        """

        self.country = country
        self.c = CoronaADT(self.country)
        self.new_data = self.c.get_history_by_particular_country(self.country)

        self.indicator = indicator
        self.data = self.extract_data()
        self.predict = [year for year in range(len(self.data))]

        self.gamma = gamma
        self.c = c
        self.pred_score = 0

    def extract_data(self):
        """
        Returns dictionary with all the previous information
        about COVID-19 in a country ({record date: cases})

        :return:
        """

        cases = {}
        for item in self.new_data["stat_by_country"]:
            cases.update({item["record_date"]: item[self.indicator]})
        return cases

    def chop_data(self):
        """
        Gets all the dates converted into integers.
        Returns the dictionary with keys as integer dates
        and values as integer number of cases.

        :return:
        """

        chopped_data = {}
        for item in self.data:
            last_item = item
            item = int(item.split(" ")[0].replace("-", ""))
            if self.data[last_item] not in chopped_data.values():
                chopped_data.update({item: self.data[last_item]})
        return chopped_data

    def define_numpy(self):
        """
        Getting all values and dates in specific lists
        for later usage. Also used for plotting the data.

        :return:
        """

        data = self.chop_data()
        dates = [date for date in data]
        str_dates = ["{}-{}-{}".format(
            str(item)[:4], str(item)[4:6],
            str(item)[6:]) for item in data][::-1]
        dates = dates[::-1]
        items = []

        # get int values:
        for k in data:
            items.append(int(data[k].replace(",", "")))
        items = items[::-1]

        return dates, items, str_dates

    def get_days(self, today):
        """
        Gets all the dates staring from today up until the
        day we define. After will predict all cases for all the
        new dates we get.

        :param today: today (now)
        :return:
        """

        # define today:
        year_now = int(list(self.data.keys())[0][:4])
        try:
            month_now = int(list(self.data.keys())[0][5:7])
        except TypeError:
            month_now = int(list(self.data.keys())[0][6:7])
        try:
            day_now = int(list(self.data.keys())[0][8:10])
        except TypeError:
            day_now = int(list(self.data.keys())[0][9:10])

        # define new date:
        day_0 = days(year_now, month_now, day_now)
        day_1 = days(int(today[0]), int(today[1]), int(today[2]))
        delta = day_1 - day_0

        # get all dates:
        dates_int = []
        dates_str = []
        for d in range(delta.days + 1):
            dates_str.append((day_0 + timedelta(days=d)).__str__())
            dates_int.append(
                [int((day_0 + timedelta(days=d)).__str__().replace("-", ""))])

        return dates_str, dates_int, delta.days

    def prediction(self, dates, values, x):
        """
        Uses Kernel algorithm to compute the dot product of two vectors x and y
        Gives the result of probable future based on the past data.
        Radial basis function (RBF) is used for predicting.

        :param dates: the dates we use for prediction
        :param values: the values we use for prediction
        :param x: what we want to predict
        :return:
        """

        predictions = []
        dates = np.reshape(dates, (len(dates), 1))
        x = np.reshape(x, (len(x), 1))

        svr_rbf = SVR(kernel="rbf", C=self.c, gamma=self.gamma)
        svr_rbf.fit(dates, values)
        self.pred_score = svr_rbf.score(dates, values)

        predictions.append(svr_rbf.predict(x)[0])

        return predictions

    @staticmethod
    def plot_graph(str_dates, values, dates, prediction):
        """
        Uses matplotlib library for plotti ng the data.
        Draws all the point corresponded to
        certain dates on the grid.

        :param str_dates: dates from the start of the COVID-19
        pandemic till now
        :param values: all the previous cases
        :param dates: dates we have predicted on the previous data
        :param prediction: all the predicted number of cases
        :return:
        """

        str_dates.extend(dates)
        new_predictions = [item[0] for item in prediction]
        values.extend(new_predictions)

        # define the plotting grid parameters:
        fig = plt.gcf()
        fig.set_size_inches(11.5, 8.5)

        # draw the previous data points:
        plt.scatter(str_dates, values, edgecolors="black", label="given data")
        plt.plot(str_dates, values, color='green')

        # get the values to be shown on the grid's axis:
        ox = [str_dates[0]]
        for item in (sorted(list(set(
                i for i in str_dates if (i[-2] == "0" and i[-1] == "1") or
                                        (i[-2] == "1" and i[-1] == "5"))))):
            ox.append(item)
        arr_y = np.arange(min(values), max(values) + 1, max(values) / 10)
        oy = np.append(arr_y, [])

        # draw axis with its labels:
        plt.xticks(ox)
        plt.yticks(oy)

        # get the time format for the ox axis:
        plt.gcf().autofmt_xdate()

        # draw the new data points:
        plt.scatter(dates, prediction,
                    edgecolors="orange", label="predicted data")
        plt.plot(dates, prediction)
        plt.xlabel("Date", fontsize=13)
        plt.ylabel("Cases", fontsize=13)

        plt.legend(framealpha=1, frameon=True)
        # show the grid:
        plt.show()


if __name__ == '__main__':
    p = Prediction(0.00001, 4000000, "USA", "total_cases")

    # get the proceeded data:
    data = p.define_numpy()

    # get the new dates:
    number_days = p.get_days(["2020", "12", "01"])
    new_dates = [i for i in range(len(data[0]))]
    dates_to_predict = [i + len(new_dates) for i in range(number_days[2] + 1)]

    # get values ready for plotting:
    predictions = []
    prev_values = [i for i in data[1]]
    fut_dates = number_days[0]
    prev_dates = data[2]

    # predict:
    for i in range(len(number_days[1])):
        pred = p.prediction(new_dates, data[1], [dates_to_predict[i]])
        predictions.append(pred)

    # draw the plotted grid:
    p.plot_graph(prev_dates, prev_values, fut_dates, predictions)
