import get_infected_countries as countries
import json
import re
import requests
import pprint


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
        data = json.load(f)
    return data


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
    pprint.pprint(country_data)
