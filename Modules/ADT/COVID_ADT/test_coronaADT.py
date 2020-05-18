from Modules.ADT.COVID_ADT.Corona_ADT import CoronaADT
import unittest


class TestCoronaADT(unittest.TestCase):
    def setUp(self) -> None:
        self.country = "USA"
        self.corona = CoronaADT(self.country)

    def test_APIs(self):
        # test all the APIs:
        self.assertIsInstance(self.corona.get_affected_countries(), dict)
        self.assertIsInstance(self.corona.get_history_by_particular_country(self.country), dict)
        self.assertIsInstance(self.corona.get_cases_by_land(), dict)
        self.assertIsInstance(self.corona.get_latest_stat_by_country_name(self.country), dict)
        self.assertIsInstance(self.corona.get_world_total_stat(), dict)

    def test_all_cases(self):
        # Get test results based on recorded information from beginning
        self.assertIsInstance(self.corona.get_infected(), int)
        self.assertIsInstance(self.corona.get_recovered(), int)
        self.assertIsInstance(self.corona.get_deaths(), int)
        try:
            self.assertIsInstance(self.corona.get_total_cases_per1m(), float)
        except AssertionError:
            self.assertIsInstance(self.corona.get_total_cases_per1m(), int)

    def test_day_cases(self):
        # Get test results based on recorded information from the current day
        self.assertIsInstance(self.corona.get_new_cases(), int)
        self.assertIsInstance(self.corona.get_active_cases(), int)
        self.assertIsInstance(self.corona.get_new_deaths(), int)
        self.assertIsInstance(self.corona.get_serious_critical(), int)
        self.assertIsInstance(self.corona.get_record_date(), str)

    def test_interface(self):
        pass


if __name__ == '__main__':
    unittest.main()
