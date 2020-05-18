import requests
from bs4 import BeautifulSoup
from prettytable import PrettyTable


class FluData:
    """
    A class that contains flu statistics for a specific age
    """
    def __init__(self, age: int, symptoms: int, visits: int,
                 hospitalizations: int, deaths: int):
        self.age = age
        self.symptoms = symptoms
        self.visits = visits
        self.hospitalizations = hospitalizations
        self.deaths = deaths

    def to_list(self: object) -> list:
        """
        Creates list of FLU_ADT attributes value
        :return: list of FLU_ADT attributes value
        """
        return [self.age, self.symptoms, self.visits,
                self.hospitalizations, self.deaths]

    def __str__(self: object) -> str:
        rez =  f"Age: {self.age}: \nSymptoms - {self.symptoms}\n" \
               f"Visits - {self.visits}\n" \
               f"Hospitalizations - {self.hospitalizations}" \
               f"\nDeaths - {self.deaths}\n"
        return rez


class ScrapADT:
    """
    A class that contains flu statistics for a specific year
    """
    def __init__(self, link: str):
        self._link = link
        self.data = self.scrap_table(link)
        self.years = self.get_year()
        self.prepare_data()
        self.write_in_FluData()

    def draw(self: object) -> None:
        """
        The function that visualizes ScrapADT data
        :return: None
        """
        print(f'                      ______________{self.years}_____________')
        t = PrettyTable(['Age group', 'Symptomatic Illnesses', 'Medical Visits',
                         'Hospitalizations', 'Deaths'])
        for age in self.data:
            row = self.data[age].to_list()
            t.add_row(row)
        print(t)

    def get_year(self: object) -> int:
        """
        The function gets year from the ScrapADT link attribute
        :return: year for which the ScrapADT object contains statistics
        """
        str_years = self._link.split('/')[-1][:-5]
        int_years = int(str_years.split('-')[0])
        return int_years

    def get_link(self: object) -> str:
        """
        The function returns link ScrapADT attribute
        :return: link attribute
        """
        return self._link

    def prepare_data(self: object) -> None:
        """
        The function removes a comma and converts to integers in ScrapADT statistics
        :return: None
        """
        for key in self.data:
            for ind in range(len(self.data[key])):
                self.data[key][ind] = self.remove_coma(self.data[key][ind])

    def __str__(self: object) -> str:
        rez = ''
        for i in self.data:
            rez += str(self.data[i])
        return rez

    def write_in_FluData(self: object) -> None:
        """
        The function rewrites data in FLU_ADT
        :return: None
        """
        for k in self.data:
            FluObj = FluData(k, self.data[k][0], self.data[k][1],
                             self.data[k][2], self.data[k][3])
            self.data[k] = FluObj

    @staticmethod
    def scrap_table(link):
        """
        The function scraps data from a web page and writes it to the dictionary
        :param link: Link to web page with data
        :return: Dictionary with data from web page
        """
        rez = {}
        source = requests.get(link).text
        soup = BeautifulSoup(source, 'lxml')
        table = soup.find('tbody')
        for tr in table.find_all('tr'):
            for td in tr.find_all('td'):
                if '-' in td.text:
                    curr_key = td.text.strip().split()[0]
                elif '+' in td.text:
                    curr_key = td.text[:3]
                elif td.text[:3] == 'All':
                    curr_key = 'All'
                else:
                    if curr_key in rez:
                        if ')' not in td.text:
                            rez[curr_key].append(td.text)
                    else:
                        rez[curr_key] = [td.text]
        return rez

    @staticmethod
    def check_age(str_key: str, age: int) -> bool:
        """
        The function checks if age is in a key range
        :param str_key: dictionary key
        :param age: age
        :return: bool result
        """
        if '+' not in str_key:
            int_age = list(map(int, str_key.split('-')))
            if int_age[0] <= age <= int_age[1]:
                return True
            return False
        else:
            return True

    @staticmethod
    def remove_coma(exp):
        """
        The function accepts string and convert them to integer
        :param exp: string expresion
        :return: converted expression
        """
        if ',' in exp:
            return int(''.join(exp.split(',')))
        elif exp == '—':
            return 0
        return exp

    @staticmethod
    def get_ages(key):
        """
        The function returns list of ages keys converted to
        :param key:
        :return:
        """
        if '-' in key:
            return list(map(int, key.split('-')))
        elif '+' in key:
            return int(key[:-1])
        return key
