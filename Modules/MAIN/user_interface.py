from Modules.SIDE_MODULES import core
from prettytable import PrettyTable
from Modules.ADT.COVID_ADT.Corona_ADT import CoronaADT
import re
from Modules.SIDE_MODULES.Prediction.value_time_prediction import Prediction
import matplotlib.pyplot as plt
import numpy as np
from Modules.ADT.FLU_ADT.FluADT import FluADT
import sys


def main():
    """
    Main function in this module which run project
    :return: None
    """
    run = True
    while run:
        inp = main_interface()
        if inp == '1':
            point_1()
        elif inp == '2':
            point_2()
        elif inp == "3":
            point_3()
        elif inp == "4":
            print("Thank you for using the program.")
            sys.exit(0)


def main_interface() -> str:
    """
    The function represents the main menu interface
    :return: str
    """
    print("\n1 - Get COVID-19 statistic\n"
          "2 - Get Flu statistic in USA\n"
          "3 - Compare Flu and COVID-19 statistic\n"
          "4 - Exit\n")
    inp = input(">>> ")
    return inp


def point_1():
    """
    A function that processes (1) input data combinations
    :return: None
    """
    virus = CoronaADT()
    run = True
    while run:
        print("\n1 - Get COVID-19 statistics for specific country\n"
              "2 - Get COVID-19 statistics for specific date\n"
              "3 - Get COVID-19 affected countries\n"
              "4 - Get COVID-19 world statistics\n"
              "5 - Back\n")
        inp = input('>>> ')
        if inp == '1':
            point_1_1(virus)
        elif inp == '2':
            point_1_2(virus)
        elif inp == '3':
            point_1_3(virus)
        elif inp == '4':
            point_1_4(virus)
        elif inp == '5':
            run = False
        else:
            print('\nIncorrect input')
            return


def point_1_1(virus) -> None:
    """
    A function that processes (1 -> 1) input data combinations
    :return: None
    """
    run = True
    while run:
        countries = virus.get_affected_countries()["affected_countries"]
        countries = sorted(countries, key=lambda x: x[0])

        core.virus_interface(countries)
        print('\nEnter country number\n'
              '0 - Back\n')
        inp_country = input('>>> ')

        if int(inp_country) in range(len(countries)):
            virus.country = countries[int(inp_country) - 1]
            print(virus.country)
            print(virus.__str__())
            print()
            return
        elif int(inp_country) == 0:
            return
        else:
            print('\nInput error')
            return


def point_1_2(virus) -> None:
    """
    A function that processes (1 -> 2) input data combinations
    :return:
    """
    run = True
    while run:
        print("\nEnter a date (yyyy-mm-dd)\n"
              "0 - Back")
        inp_date = input('>>> ')

        match = re.search(r'\d{4}-\d{2}-\d{2}', inp_date)
        try:
            date = match.group()
        except AttributeError:
            print("\nEnter a valid date")
            return
        country = ""

        if len(date) == 10:
            countries = virus.get_affected_countries()["affected_countries"]
            countries = sorted(countries, key=lambda x: x[0])
            core.virus_interface(countries)

            print("\nEnter a country")
            inp_country = input('>>> ')

            if int(inp_country) in range(len(countries)):
                country = countries[int(inp_country) - 1]
            else:
                print("\nEnter a valid country number")
                return
            try:
                print(country)
                print(virus.history_by_date(country, date))
            except:
                print("\nEnter a valid date")
                return
            return
        elif int(inp_date) == 0:
            return
        else:
            print('\nInput error')
            return


def point_1_3(virus):
    """
    A function that processes (1 -> 3) input data combinations
    :param virus:
    :return:
    """
    countries = virus.get_affected_countries()["affected_countries"]
    countries = sorted(countries, key=lambda x: x[0])
    core.virus_interface(countries)
    return


def point_1_4(virus):
    """
    A function that processes (1 -> 4) input data combinations
    :param virus:
    :return:
    """
    print(virus.world_stats())
    return


def point_2() -> None:
    """
    A function that processes (2) input data combinations
    :return: None
    """
    flu_stat = FluADT()

    run = True
    while run:
        print('\n1 - Statistics for a specific year\n'
              '2 - Average statistic for 2010-2016\n'
              '3 - Statistic for 2010-2016\n'
              '4 - Back\n')
        inp = input('>>> ')
        if inp == '1':
            point_2_1(flu_stat)
        elif inp == '2':
            point_2_2(flu_stat)
        elif inp == '3':
            point_2_3(flu_stat)
        elif inp == '4':
            return
        else:
            print('Incorrect input')
            return


def point_2_1(st):
    """
    A function that processes (2 -> 1) input data combinations
    :param st: FluADT object
    :return: None
    """
    run = True
    while run:
        print('Enter year\n'
              '1 - Back\n')
        year = input('>>> ')
        if year in st.get_years():
            st.data[year].draw()
            return
        elif year == '1':
            return
        else:
            print('Incorrect year (2010 - 2016 is correct)')
            return


def point_2_2(st):
    """
    A function that processes (2 -> 2) input data combinations
    :param st: FluADT object
    :return: None
    """
    illnesses = st.get_avr_illnesses()
    recovered = st.get_avr_recovered()
    deaths = st.get_avr_deaths()
    t = PrettyTable(['Symptomatic Illnesses', 'Recovered', 'Deaths'])
    t.add_row([illnesses, recovered, deaths])
    print(t)
    return


def point_2_3(st):
    """
    A function that processes (2 -> 3) input data combinations
    :param st: FluADT object
    :return: None
    """
    st.draw()
    return


def point_3():
    """
    A function that processes (3) input data combinations
    :return: None
    """
    virus_c = CoronaADT()
    virus_f = FluADT()
    run = True
    while run:
        print('1 - COVID-19 prediction\n'
              '2 - Compare Flu and COVID-19 statistic without prediction\n'
              '3 - Compare Flu and COVID-19 statistic with prediction\n'
              '4 - Back\n')
        inp = input('>>> ')
        if inp == '1':
            point_3_1()
        elif inp == '2':
            point_3_2(virus_c, virus_f)
        elif inp == '3':
            point_3_3(virus_c, virus_f)
        elif inp == '4':
            return
        else:
            print('Incorrect input')
            return


def point_3_1():
    """
    A function that processes (3 -> 1) input data combinations
    :return: None
    """
    p = None
    country = "USA"  # default

    print("\n1 - Total Cases\n"
          "2 - Total Recovered\n"
          "3 - Total Deaths\n"
          "4 - Back\n")

    inp = input('>>> ')
    if inp == '1':
        gamma = 0.00001
        p = Prediction(gamma, 4000000, country, "total_cases")
    elif inp == '2':
        gamma = 0.00002
        p = Prediction(gamma, 50000000, country, "total_recovered")
    elif inp == '3':
        gamma = 0.00001
        p = Prediction(gamma, 4000000, country, "total_deaths")
    elif inp == '4':
        return

    # get the proceeded data:
    data = p.define_numpy()

    # get the new dates:
    number_days = p.get_days(["2021", "01", "01"])
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
    return


def point_3_2(virus_c, virus_f):
    """
    A function that processes (3 -> 2) input data combinations
    :return:
    """

    years = virus_f.get_years()
    cases = []
    virus_c.country = "USA"

    print("\n1 - Total Cases\n"
          "2 - Total Recovered\n"
          "3 - Total Deaths\n"
          "4 - Back\n")

    inp = input('>>> ')

    if inp == '1':
        for item in years:
            cases.append(virus_f.get_total_symptoms(item))
        covid_infected = virus_c.get_infected()
        cases.append(covid_infected)
    elif inp == '2':
        for item in years:
            cases.append(virus_f.get_total_recovered(item))
        covid_recovered = virus_c.get_recovered()
        cases.append(covid_recovered)
    elif inp == '3':
        for item in years:
            cases.append(virus_f.get_total_Deaths(item))
        covid_deaths = virus_c.get_deaths()
        cases.append(covid_deaths)
    elif inp == '4':
        return

    # get flu data
    years = [item + " (Flu)" for item in years]
    years.append("2020 (COVID-19)")

    x_pos = np.arange(len(years))

    # plot the data given:
    draw(x_pos, cases, years, inp)

    text = compute_similarity(virus_c, virus_f, "prediction")

    # print out:
    show(text)
    return


def point_3_3(virus_c, virus_f):
    """
    A function that processes (3 -> 3) input data combinations
    :return: None
    """

    years = virus_f.get_years()
    cases = []
    virus_c.country = "USA"
    p = None

    print("\n1 - Total Cases\n"
          "2 - Total Recovered\n"
          "3 - Total Deaths\n"
          "4 - Back\n")

    inp = input('>>> ')

    if inp == '1':
        for item in years:
            cases.append(virus_f.get_total_symptoms(item))
        p = Prediction(0.00001, 4000000, "USA", "total_cases")
    elif inp == '2':
        for item in years:
            cases.append(virus_f.get_total_recovered(item))
        p = Prediction(0.00002, 50000000, "USA", "total_recovered")
    elif inp == '3':
        for item in years:
            cases.append(virus_f.get_total_Deaths(item))
        p = Prediction(0.00001, 4000000, "USA", "total_deaths")
    elif inp == '4':
        return

    prediction = get_prediction(p)

    # add the predicted value of cases to the plotting list:
    cases.append(int(prediction))

    # get flu data
    years = [item + " (Flu)" for item in years]
    years.append("2020 (COVID-19)")

    x_pos = np.arange(len(years))

    # plot the data given:
    draw(x_pos, cases, years, inp)

    text = compute_similarity(virus_c, virus_f, "no prediction")

    # print out:
    show(text)
    return


def compute_similarity(virus_c, virus_f, mark=None):
    """
    Compares the average results of Flu virus spread,
    people recovered, and deaths to the COVID-19 data.
    Gives the percentage of similarity.

    :param mark: Indicates if we should get
                 the predicted data comparision.
    :param virus_c: CoronaADT
    :param virus_f: FluADT
    :return:
    """

    av_cases_c = av_recovers_c = av_deaths_c = None

    if mark == "no prediction":
        av_cases_c = virus_c.get_infected()
        av_recovers_c = virus_c.get_recovered()
        av_deaths_c = virus_c.get_deaths()
    elif mark == "prediction":
        p = Prediction(0.00001, 4000000, "USA", "total_cases")
        av_cases_c = get_prediction(p)
        p = Prediction(0.00002, 50000000, "USA", "total_recovered")
        av_recovers_c = get_prediction(p)
        p = Prediction(0.00001, 4000000, "USA", "total_deaths")
        av_deaths_c = get_prediction(p)

    av_cases_f = virus_f.get_avr_illnesses()
    cases_p = round((av_cases_f - av_cases_c) * 100 / av_cases_c, 3)

    av_recovers_f = virus_f.get_avr_recovered()
    recovers_p = round((av_recovers_f - av_recovers_c) * 100 / av_recovers_c, 3)

    av_deaths_f = virus_f.get_avr_deaths()
    deaths_p = round((av_deaths_c - av_deaths_f) * 100 / av_deaths_c, 3)

    return cases_p, recovers_p, deaths_p


def show(text):
    """
    Prints out the text to a User that represents
    all the comparisons made. (COVID-19 vs Flu)

    :param text: data
    :return:
    """

    print("\nIn average, in USA there are:      \n"
          "{}% more infected people with Flu than COVID-19.\n"
          "{}% more people have successfully recovered from Flu "
          "compared to COVID-19.\n{}% more people have "
          "died from COVID-19 compared to regular Flu.\n".format(text[0],
                                                                 text[1],
                                                                 text[2]))
    return


def get_prediction(p):
    """
    Get the last value predicted for plotting and
    getting the difference between Flu and COVID-19 statistics.

    :param p: Prediction object
    :return:
    """

    # get the proceeded data:
    data = p.define_numpy()

    # get the new dates:
    number_days = p.get_days(["2020", "12", "01"])
    new_dates = [i for i in range(len(data[0]))]
    dates_to_predict = [i + len(new_dates) for i in range(number_days[2] + 1)]

    # get values ready for plotting:
    predictions = []

    # predict:
    for i in range(len(number_days[1])):
        pred = p.prediction(new_dates, data[1], [dates_to_predict[i]])
        predictions.append(pred)

    return int(predictions[-1][0])


def draw(x_pos, cases, years, inp):
    """
    Basic plotting on the bar - chart - like graph
    the information about COVID-19 and Flu cases.

    :param x_pos: numpy array of years
    :param cases: all the cases of viruses
    :param years: all the years
    :param inp: the indicator for colors
    :return:
    """

    colors_1 = ("orange", "orange", "orange", "orange",
                "orange", "orange", "orange", "red")
    colors_2 = ("green", "green", "green", "green",
                "green", "green", "green", "red")
    colors_3 = ("blue", "blue", "blue", "blue",
                "blue", "blue", "blue", "red")

    WIDTH = 11.5
    HEIGHT = 8.5

    fig = plt.gcf()
    fig.set_size_inches(WIDTH, HEIGHT)

    plt.bar(x_pos, cases, color=colors_1 if inp == "1"
            else colors_2 if inp == "2" else colors_3)
    plt.xticks(x_pos, years)
    plt.xlabel("USA, Infected" if inp == "1"
               else "USA, Recovered" if inp == "2"
               else "USA, Deaths")
    plt.ylabel("Cases", fontsize=13)
    for i, j in enumerate(cases):
        plt.text(i - 0.3, j + j / 100, str(j))
    plt.show()
    return


if __name__ == '__main__':
    main()
