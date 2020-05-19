import requests


class CoronaADT:
    def __init__(self, country=None):
        """
        Define parameters
        :param country:
        """

        self.host = "coronavirus-monitor.p.rapidapi.com"
        self.api = "f34e347e05msha354cec5624fc49p1739" \
                   "cajsn490b038d2abc"

        self.country = country

    def get_affected_countries(self):
        """
        Get all country names where COVID-19 cases
        were diagnosed.
        """

        url = "https://coronavirus-monitor.p." \
              "rapidapi.com/coronavirus/affected.php"

        headers = {
            'x-rapidapi-host': self.host,
            'x-rapidapi-key': self.api
        }
        response = requests.request("GET", url, headers=headers)
        return response.json()

    def get_history_by_particular_country(self, country: str):
        """
        Get the history of cases by country
        :param country: str
        :return:
        """

        url = "https://coronavirus-monitor.p.rapidapi.com" \
              "/coronavirus/cases_by_particular_country.php"

        querystring = {"country": country}

        headers = {
            'x-rapidapi-host': self.host,
            'x-rapidapi-key': self.api
        }
        response = requests.request("GET", url,
                                    headers=headers, params=querystring)
        return response.json()

    def get_history_by_particular_country_by_date(self,
                                                  county: str, date: str):
        """
        Get cases history by the specific country and date
        :param county: str
        :param date: str
        :return:
        """

        url = "https://coronavirus-monitor.p.rapidapi.com" \
              "/coronavirus/history_by_particular_country_by_date.php"

        querystring = {"country": county, "date": date}

        headers = {
            'x-rapidapi-host': self.host,
            'x-rapidapi-key': self.api
        }
        response = requests.request("GET", url,
                                    headers=headers,
                                    params=querystring)
        return response.json()

    def get_cases_by_land(self):
        """
        Get information abount COVID-19 in the mainlands.
        :return:
        """

        url = "https://coronavirus-monitor.p.rapidapi.com" \
              "/coronavirus/cases_by_country.php"

        headers = {
            'x-rapidapi-host': self.host,
            'x-rapidapi-key': self.api
        }
        response = requests.request("GET", url, headers=headers)
        return response.json()

    def get_johns_hopkins_latest_usa_statistic_by_state(self, state: str):
        """
        Get information for specific state in USA
        :param state: str
        :return:
        """

        url = "https://coronavirus-monitor.p.rapidapi.com/coronavirus" \
              "/johns_hopkins_latest_usa_statistic_by_state.php"

        querystring = {"state": state}

        headers = {
            'x-rapidapi-host': self.host,
            'x-rapidapi-key': self.api
        }
        response = requests.request("GET",
                                    url, headers=headers,
                                    params=querystring)
        return response.json()

    def get_latest_stat_by_country_name(self, name: str):
        """
        Get recent statistics in a country
        :param name: str
        :return:
        """

        url = "https://coronavirus-monitor.p.rapidapi.com" \
              "/coronavirus/latest_stat_by_country.php"

        querystring = {"country": name}

        headers = {
            'x-rapidapi-host': self.host,
            'x-rapidapi-key': self.api
        }
        response = requests.request("GET",
                                    url, headers=headers,
                                    params=querystring)
        return response.json()

    def get_world_total_stat(self):
        """
        Get the total information about COVID-19 in the world
        :return:
        """

        url = "https://coronavirus-monitor.p.rapidapi.com" \
              "/coronavirus/worldstat.php"

        headers = {
            'x-rapidapi-host': self.host,
            'x-rapidapi-key': self.api
        }
        response = requests.request("GET", url, headers=headers)
        return response.json()

    def __str__(self):
        """
        Output the recent information in the country
        :return:
        """
        return "Infected: {}\n" \
               "Recovered: {}\n" \
               "Deaths: {}".format(self.get_infected(),
                                   self.get_recovered(),
                                   self.get_deaths())

    def get_infected(self):
        """
        Get all the infected people form the
        beginning of pandemic
        :return:
        """

        data = self.get_history_by_particular_country(
            self.country)["stat_by_country"][0]["total_cases"]
        try:
            data = int(data.replace(",", ""))
        except ValueError:
            data = int(data)
        return data

    def get_recovered(self):
        """
        Get all the recoverd people form the beginning of pandemic
        :return:
        """

        data = self.get_history_by_particular_country(
            self.country)["stat_by_country"][0]["total_recovered"]
        try:
            data = int(data.replace(",", ""))
        except ValueError:
            print(data)
            data = int(data)
        return data

    def get_deaths(self):
        """
        Get all people who have died form the
        beginning of pandemic
        :return: dict
        """

        data = self.get_history_by_particular_country(
            self.country)["stat_by_country"][0]["total_deaths"]
        try:
            data = int(data.replace(",", ""))
        except ValueError:
            data = int(data)
        return data

    def get_new_cases(self):
        """
        Get new cases for a day
        :return:
        """

        data = self.get_history_by_particular_country(
            self.country)["stat_by_country"][0]["new_cases"]
        try:
            data = int(data.replace(",", ""))
        except ValueError:
            data = int(data)
        return data

    def get_active_cases(self):
        """
        Get all active cases in a country
        :return:
        """

        data = self.get_history_by_particular_country(
            self.country)["stat_by_country"][0]["active_cases"]
        try:
            data = int(data.replace(",", ""))
        except ValueError:
            data = int(data)
        return data

    def get_new_deaths(self):
        """
        Get today's number of deaths
        :return:
        """

        data = self.get_history_by_particular_country(
            self.country)["stat_by_country"][0]["new_deaths"]
        try:
            data = int(data.replace(",", ""))
        except ValueError:
            data = int(data)
        return data

    def get_serious_critical(self):
        """
        Get amount of people who are seriously ill
        :return:
        """

        data = self.get_history_by_particular_country(
            self.country)["stat_by_country"][0]["serious_critical"]
        try:
            data = int(data.replace(",", ""))
        except ValueError:
            data = int(data)
        return data

    def get_total_cases_per1m(self):
        """
        Get average number of people infected
        by COVID-19 per 1 million population
        :return:
        """

        data = self.get_history_by_particular_country(
            self.country)["stat_by_country"][0]["total_cases_per1m"]
        try:
            data = int(data.replace(",", ""))
        except ValueError:
            data = int(data)
        return data

    def get_record_date(self):
        """
        Get the most recent time the numbers were updated
        :return:
        """

        data = self.get_history_by_particular_country(
            self.country)["stat_by_country"][0]["record_date"]
        return data

    def history_by_date(self, country, date):
        """
        Output history of cases for a specific year
        :param country:
        :param date:
        :return:
        """

        data = self.get_history_by_particular_country_by_date(
            country, date)["stat_by_country"]
        return "Infected: {}\n" \
               "Recovered: {}\n" \
               "Deaths: {}".format(data[0]["total_cases"],
                                   data[0]["total_recovered"],
                                   data[0]["total_deaths"])

    def world_stats(self):
        """
        Output total world statistics
        :return:
        """

        data = self.get_world_total_stat()
        return "Infected: {}\n" \
               "Recovered: {}\n" \
               "Deaths: {}".format(data["total_cases"],
                                   data["total_recovered"],
                                   data["total_deaths"])


if __name__ == '__main__':
    p = CoronaADT("Ukraine")
    # print(p.get_infected())
    # print(p.get_recovered())
    # print(p.get_deaths())
    print(p)
    print(p.get_record_date())
