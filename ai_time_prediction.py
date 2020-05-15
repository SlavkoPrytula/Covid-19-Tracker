# basic imports:
import numpy as np
import sklearn
from sklearn import linear_model
from sklearn.utils import shuffle
from corona_adt import Corona
from sklearn.svm import SVR
import matplotlib.pyplot as plt

from sklearn.metrics import make_scorer

class Prediction:
    def __init__(self):
        self.c = Corona()
        # self.new_data = self.c.get_history_by_particular_country("Ukraine")
        self.new_data = self.c.get_history_by_particular_country("USA")


        self.data = self.extract_data()
        self.predict = [year for year in range(len(self.data))]

    def extract_data(self):
        cases = {}
        for item in self.new_data["stat_by_country"]:
            cases.update({item["record_date"]: item["total_cases"]})
        return cases

    def chop_data(self):
        used_dates = []
        chopped_data = {}
        # self.data = self.data[::-1]
        print(self.data.keys())
        for item in self.data:
            last_item = item
            item = int(item.split(" ")[0].replace("-", ""))
            # print(item)
            if self.data[last_item] not in chopped_data.values():
                chopped_data.update({item: self.data[last_item]})
        print(chopped_data)
        return chopped_data

    def define_numpy(self):
        data = self.chop_data()
        dates = [date for date in data]

        str_dates = ["{}-{}-{}".format(str(item)[:4], str(item)[4:6], str(item)[6:]) for item in data][::-1]
        print(str_dates)

        # mid_dates = [date for date in self.data]
        # dates = []
        #
        # for item in mid_dates:
        #     # item = int(item.replace("-", "").replace(" ", "").replace(":", "").replace(".", ""))
        #     # print(item, type(item))
        #     # break
        #     dates.append(item)
        dates = dates[::-1]
        #
        items = []
        for k in data:
            item = data[k]
            new_item = ""
            if "," in item:
                for i in item:
                    if i != ",":
                        new_item += i
                item = int(new_item)
            else:
                item = int(item)
            items.append(item)
        items = items[::-1]

        # print(len(dates), dates)
        # print(len(items), items)

        return dates, items, str_dates

        # x = np.array(dates).reshape(1, -1)
        # y = np.array(items).reshape(1, -1)
        # print("hello_1", x)
        # print()
        # print("hello_2", y)
        #
        # x_train, x_test, y_train, y_test = sklearn.model_selection.train_test_split(x, y, test_size=0.25)
        # return x_train, y_train, x_test, y_test

    def best_fitted_line(self):
        arr = self.define_numpy()
        linear = linear_model.LinearRegression()
        linear.fit(arr[0], arr[1])
        acc = linear.score(arr[2], arr[3])
        print(acc)

        # predictions = linear.predict(arr[2])
        # for item in predictions:
        #     print(predictions[item], arr[1][item], arr[2][item])

    def prediction(self, dates, values, x):
        # scorer = make_scorer(mean_squared_error, greater_is_better=False)
        # svr_gs = GridSearchCV(SVR(epsilon=0.01), parameters, cv=K, scoring=scorer)
        data = self.define_numpy()

        # fig = plt.gcf()
        # fig.set_size_inches(10.5, 7.5)
        # plt.scatter(str_dates, values, edgecolors="black")
        # plt.plot(str_dates, values, color='green')
        # plt.xticks(sorted(list(set(i for i in str_dates))))
        # plt.yticks(np.arange(min(values), max(values) + 1, 1000.0))
        # plt.gcf().autofmt_xdate()

        # plt.xticks(sorted(list(set(i for i in dates))))
        # plt.yticks(np.arange(min(values), max(values) + 1, 1000.0))

        # plt.plot(dates, values)
        # plt.show()

        # dates = [i for i in range(len(dates))]
        # x = dates
        # dates  = values
        # values
        # # dates = np.reshape(str_dates, (len(dates), 1))

        dates = np.reshape(dates, (len(dates), 1))
        print(dates)
        x = np.reshape(x, (len(x), 1))
        print(x)

        # # print(len(dates), dates)
        # print(len(dates))





        # svr_lin = SVR(kernel="linear", C=1e5)
        # svr_poly = SVR(kernel="poly", C=1e5, degree=2)




        #
        svr_rbf = SVR(kernel="rbf", C=1e8, gamma=0.0001, epsilon=0.005)
        #
        # svr_lin.fit(dates, values)
        # svr_poly.fit(dates, values)
        svr_rbf.fit(dates, values)
        #
        # plt.scatter(dates, values, edgecolors="black")
        #
        # plt.plot(str_dates, svr_rbf.predict(dates))
        #



        # plt.plot(dates, svr_lin.predict(dates))
        # plt.plot(dates, svr_poly.predict(dates))



        # plt.legend()
        plt.show()

        # return svr_rbf.predict(x)[0], svr_lin.predict(x)[0], svr_poly.predict(x)[0]




        return svr_rbf.predict(x)[0]

    @staticmethod
    def plot_graph(str_dates, values, dates, prediction):
        d = "{}-{}-{}".format(str(dates)[:4], str(dates)[4:6], str(dates)[6:])
        fig = plt.gcf()
        fig.set_size_inches(10.5, 7.5)
        plt.scatter(str_dates, values, edgecolors="black")
        plt.plot(str_dates, values, color='green')
        plt.xticks(sorted(list(set(i for i in str_dates))))
        plt.yticks(np.arange(min(values), max(values) + 1, 15000.0))
        plt.gcf().autofmt_xdate()

        plt.scatter(d, prediction, edgecolors="orange")
        plt.plot(d, prediction)
        plt.show()


if __name__ == '__main__':
    p = Prediction()
    date = 20200515
    # # print(p.extract_data())
    data = p.define_numpy()
    # # print(data[0])
    a = p.prediction(data[0], data[1], [date])
    # # p.best_fitted_line()
    print(a, "here")
    print("ok")
    p.plot_graph(data[2], data[1], date, a)
