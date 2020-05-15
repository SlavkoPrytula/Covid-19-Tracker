import requests
from prettytable import PrettyTable


class Corona:
    def __init__(self, country):
        self.host = "coronavirus-monitor.p.rapidapi.com"
        self.api = "f34e347e05msha354cec5624fc49p1739cajsn490b038d2abc"

        self.country = country

    def get_affected_countries(self):
        """
        Get all country names where coronavirus cases
        were diagnosed.
        """
        url = "https://coronavirus-monitor.p.rapidapi.com/coronavirus/affected.php"

        headers = {
            'x-rapidapi-host': self.host,
            'x-rapidapi-key': self.api
        }
        response = requests.request("GET", url, headers=headers)
        return response.json()

    def get_history_by_particular_country(self, country: str):
        url = "https://coronavirus-monitor.p.rapidapi.com/coronavirus/cases_by_particular_country.php"

        querystring = {"country": country}

        headers = {
            'x-rapidapi-host': self.host,
            'x-rapidapi-key': self.api
        }
        response = requests.request("GET", url, headers=headers, params=querystring)
        return response.json()

    def get_history_by_particular_country_by_date(self, county: str, date: str):
        url = "https://coronavirus-monitor.p.rapidapi.com/coronavirus/history_by_particular_country_by_date.php"

        querystring = {"country": county, "date": date}

        headers = {
            'x-rapidapi-host': self.host,
            'x-rapidapi-key': self.api
        }
        response = requests.request("GET", url, headers=headers, params=querystring)
        return response.json()

    def get_cases_by_country(self):
        url = "https://coronavirus-monitor.p.rapidapi.com/coronavirus/cases_by_country.php"

        headers = {
            'x-rapidapi-host': self.host,
            'x-rapidapi-key': self.api
        }
        response = requests.request("GET", url, headers=headers)
        return response.json()

    def get_johns_hopkins_latest_usa_statistic_by_state(self, state: str):
        url = "https://coronavirus-monitor.p.rapidapi.com/coronavirus/johns_hopkins_latest_usa_statistic_by_state.php"

        querystring = {"state": state}

        headers = {
            'x-rapidapi-host': self.host,
            'x-rapidapi-key': self.api
        }
        response = requests.request("GET", url, headers=headers, params=querystring)
        return response.json()

    def get_latest_stat_by_country_name(self, name: str):
        url = "https://coronavirus-monitor.p.rapidapi.com/coronavirus/latest_stat_by_country.php"

        querystring = {"country": name}

        headers = {
            'x-rapidapi-host': self.host,
            'x-rapidapi-key': self.api
        }
        response = requests.request("GET", url, headers=headers, params=querystring)
        return response.json()

    def get_world_total_stat(self):
        url = "https://coronavirus-monitor.p.rapidapi.com/coronavirus/worldstat.php"

        headers = {
            'x-rapidapi-host': self.host,
            'x-rapidapi-key': self.api
        }
        response = requests.request("GET", url, headers=headers)
        return response.json()

    def __str__(self):
        return "Infected: {}\n" \
               "Recovered: {}\n" \
               "Deaths: {}".format(self.get_infected(),
                                   self.get_recovered(),
                                   self.get_deaths())

    def get_infected(self):
        data = self.get_history_by_particular_country \
            (self.country)["stat_by_country"][0]["active_cases"]
        return data

    def get_recovered(self):
        data = self.get_history_by_particular_country \
            (self.country)["stat_by_country"][0]["total_recovered"]
        return data

    def get_deaths(self):
        data = self.get_history_by_particular_country \
            (self.country)["stat_by_country"][0]["total_deaths"]
        return data

    def get_new_cases(self):
        data = self.get_history_by_particular_country \
            (self.country)["stat_by_country"][0]["new_cases"]
        return data

    def get_active_cases(self):
        data = self.get_history_by_particular_country \
            (self.country)["stat_by_country"][0]["active_cases"]
        return data

    def get_new_deaths(self):
        data = self.get_history_by_particular_country \
            (self.country)["stat_by_country"][0]["new_deaths"]
        return data

    def get_serious_critical(self):
        data = self.get_history_by_particular_country \
            (self.country)["stat_by_country"][0]["serious_critical"]
        return data

    def get_total_cases_per1m(self):
        data = self.get_history_by_particular_country \
            (self.country)["stat_by_country"][0]["total_cases_per1m"]
        return data

    def get_record_date(self):
        data = self.get_history_by_particular_country \
            (self.country)["stat_by_country"][0]["record_date"]
        return data


class CoronaInterface:
    def __init__(self, year):
        self.year = year

    def display(self):
        # print(f'                      ______________{self.year}_____________')
        # t = PrettyTable(['Age group', 'Symptomatic Illnesses', 'Medical Visits',
        #                  'Hospitalizations', 'Deaths'])
        # for age in self.data:
        #     row = self.data[age].to_list()
        #     t.add_row(row)
        # print(t)
        pass

if __name__ == '__main__':
    p = Corona("Ukraine")
    # print(p.get_infected())
    # print(p.get_recovered())
    # print(p.get_deaths())
    print(p)
