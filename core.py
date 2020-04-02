import get_infected_countries as countries
import json
import re
import requests
import pprint
import matplotlib.pyplot as plt
import math
import numpy as np


def extract_list(data):
    """
    Extract all country names properly.
    """
    result = []
    s = re.findall('(?<=,"|\[").*?(?=\",|\"])', data)
    for item in s:
        result.append(item)
    return result


def data(country):
    """
    Get the data about all cases of new_cases, death and recoveries
    in a country.
    New data roughly every 10 minutes
    """
    url = "https://coronavirus-monitor.p.rapidapi.com/coronavirus/cases_by_particular_country.php"

    querystring = {"country": country}
    headers = {
        'x-rapidapi-host': "coronavirus-monitor.p.rapidapi.com",
        'x-rapidapi-key': "f34e347e05msha354cec5624fc49p1739cajsn490b038d2abc"
    }

    response = requests.request("GET", url, headers=headers, params=querystring)
    return response.json()


def read_json(file):
    """
    This function reads an existing .json file and returns it as a dictionary.
    """
    with open(file) as f:
        c_data = json.load(f)
    return c_data


def write_country_data(country_d):
    """
    Writes the new converted dictionary to a .json file.
    """
    country = country_d["country"]
    with open("{}_virus.json".format(country), "w", encoding='utf-8') as outfile:
        json.dump(country_d, outfile, ensure_ascii=False, indent=4)


def extract_var(json_file):
    """
    Get all the needed data from every line of the json file
    Gets time as base and users choice (number of people curred,
    number of deaths, number of new cases of COVID-19)
    """
    time_data = []
    total_cases_data = []
    for data_line in json_file:
        case_data = data_line.pop("total_cases")
        # round the numbers for better appearance (!!!!!note: causes slight defection in numbers):
        # total_cases_data.append(math.ceil(int(case_data.replace(",", "")) /
        #                                   10 ** (len(case_data) - 4)) *
        #                         10 ** (len(case_data) - 4))

        total_cases_data.append(int(case_data.replace(",", "")))
        # get only the month:
        time_data.append(data_line.pop("record_date")[:10])
    return time_data, total_cases_data


def plot_var(plot_data):
    """
    Draws the graph by putting points on it that
    correspond to date and value
    The growth is ought to be exponential
    """
    fig = plt.gcf()
    fig.set_size_inches(15.5, 7.5)

    x = plot_data[0]
    y = plot_data[1]
    # plot (dotted graph):
    plt.plot(x, y, "o")

    ax = plt.axes()
    # ax.xaxis.set_major_formatter(plt.NullFormatter())

    # set labels:
    ax.set_xlabel("Dates")
    ax.set_ylabel("Cases")

    # change ticks:
    plt.yticks(np.arange(min(y), max(y) + 1, 15000.0))

    plt.gcf().autofmt_xdate()

    # show:
    plt.show()


if __name__ == '__main__':
    # get countries:
    country_data = countries.get_countries()
    countries_list = re.compile("\{.*?(?=\[)").split(country_data)[1]
    print(countries_list)
    print(type(countries_list))
    # extract:
    countries_exc = extract_list(countries_list)

    # get data about the country:
    country_data = data(countries_exc[0])

    print(country_data)
    print(country_data["country"])

    cases_data = extract_var(country_data["stat_by_country"])
    plot_var(cases_data)
