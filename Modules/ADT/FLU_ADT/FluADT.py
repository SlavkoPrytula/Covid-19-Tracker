from Modules.ADT.FLU_ADT.ScrapADT import ScrapADT
from prettytable import PrettyTable


class FluADT:
    """
    A class that contains flu statistics for a specific years
    """
    def __init__(self, path=None):
        if path is not None:
            self.data = self.get_data_file(path)
        else:
            self.data = self.get_data(self.get_links_list())

    def get_years(self: object) -> list:
        """
        Creates a list of years about which FluADT have data
        :return: list of years
        """
        return list(self.data.keys())

    def get_statistic_year(self: object, year: str) -> object:
        """
        This function returns statistic about a specific year
        :param year: year about which function will return information
        :return: ScrapADT object
        """
        return self.data[year]

    def get_statistic_year_age(self: object, year: str, age: int) -> int:
        """
        This function returns statistic about a specific year and age
        :param year: year about which function will return information
        :param age: age about which function will return information
        :return: FLU_ADT object
        """
        for key in self.data[year].data:
            if self.data[year].check_age(key, age):
                return self.data[year].data[key]

    def get_total_symptoms(self: object, year: str) -> int:
        """
        The function returns number of symptoms in specific year
        :param year: year about which function will return information
        :return: number of symptoms in specific year
        """
        return self.data[year].data['All'].symptoms

    def get_total_recovered(self, year):
        """
        The function returns number of recovered in specific year
        :param year: year about which function will return information
        :return: number of recovered in specific year
        """
        return self.get_total_symptoms(year) - self.get_total_Deaths(year)

    def get_total_MedVisits(self, year):
        """
        The function returns number of medical visits in specific year
        :param year: year about which function will return information
        :return: number of medical visits in specific year
        """
        return self.data[year].data['All'].visits

    def get_total_hospitalizations(self, year):
        """
        The function returns number of hospitalizations in specific year
        :param year: year about which function will return information
        :return: number of hospitalizations in specific year
        """
        return self.data[year].data['All'].hospitalizations

    def get_total_Deaths(self, year):
        """
        The function returns number of deaths in specific year
        :param year: year about which function will return information
        :return: number of deaths in specific year
        """
        return self.data[year].data['All'].deaths

    def get_avr_illnesses(self):
        """
        The function calculates average number
        of illnesses in 2010-2016 flu seasons
        :return: average number of illnesses in 2010-2016 flu seasons
        """
        rez = 0
        numerator = 0
        for year in self.data:
            rez += self.get_total_symptoms(year)
            numerator += 1
        return int(rez/numerator)

    def get_avr_deaths(self):
        """
        The function calculates average
        number of deaths in 2010-2016 flu seasons
        :return: average number of deaths in 2010-2016 flu seasons
        """
        rez = 0
        numerator = 0
        for year in self.data:
            rez += self.get_total_Deaths(year)
            numerator += 1
        return int(rez/numerator)

    def get_avr_recovered(self):
        """
        The function calculates average
        number of recovered in 2010-2016 flu seasons
        :return: average number of recovered in 2010-2016 flu seasons
        """
        rez = 0
        numerator = 0
        for year in self.data:
            rez += self.get_total_symptoms(year) - self.get_total_Deaths(year)
            numerator += 1
        return int(rez/numerator)

    def __str__(self):
        rez = ''
        for i in self.data:
            rez += str(self.data[i]) + '\n'
        return rez

    def clean(self: object) -> None:
        """
        The function cleans self.data
        :return: None
        """
        self.data = {}

    def draw(self):
        """
        The function that visualizes FluADT data
        :return: None
        """
        for year in self.data:
            print()
            print(f'                      '
                  f'______________{year}_____________')
            t = PrettyTable(['Age group', 'Symptomatic Illnesses',
                             'Medical Visits',
                             'Hospitalizations', 'Deaths'])
            for age in [1, 19, 50, 100]:
                row = self.get_statistic_year_age(year, age).to_list()
                t.add_row(row)
            print(t)

    @staticmethod
    def get_data_file(path):
        """
        The function reads file with links in web page  s and parse them
        :param path: path to file with links
        :return: dict with scraped data
        """
        rez = {}
        file = open(path)
        for line in file:
            line = line.strip()
            years_data = ScrapADT(line)
            rez[str(years_data.years)] = years_data
        return rez

    @staticmethod
    def get_data(lst):
        """
        The function accepts a list with links in web pages and parse them
        :param lst: list with links
        :return: dict with scraped data
        """
        rez = {}
        for link in lst:
            years_data = ScrapADT(link)
            rez[str(years_data.years)] = years_data
        return rez

    @staticmethod
    def get_links_list():
        """
        The function which returns list of links
        :return: list of links
        """
        return ['https://www.cdc.gov/flu/about/burden/2010-2011.html',
                'https://www.cdc.gov/flu/about/burden/2011-2012.html',
                'https://www.cdc.gov/flu/about/burden/2012-2013.html',
                'https://www.cdc.gov/flu/about/burden/2013-2014.html',
                'https://www.cdc.gov/flu/about/burden/2014-2015.html',
                'https://www.cdc.gov/flu/about/burden/2015-2016.html',
                'https://www.cdc.gov/flu/about/burden/2016-2017.html']
