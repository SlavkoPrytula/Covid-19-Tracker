# SARS COVID-19 Tracker

The program's purpose is to serve as a comparison mechanism for Flu and COVID-19 viruses. The main point of comparing these two is to see how much or less the SARS COVID-19 virus is dangerous from regular Flu in the USA.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. 
```
git clone https://github.com/SlavkoPrytula/Covid-19-Tracker
```

### Prerequisites

For the program to run on your device, you should install the following libraries, modules, etc...
*You may use pip3 for installing if you have Python3 or use pip instead*
```
pip install requests
pip install matplotlib
pip install beautifulsoup4
pip install PrettyTable
pip install numpy
pip install DateTime
pip install sklearn
```

## Deployment

To run the program after cloning in on your machine, go to the _MAIN_ folder and find the file named _user_interface.py_

![The folder and the filee](https://github.com/SlavkoPrytula/Covid-19-Tracker/blob/master/Photos/Screenshot_20200519_150357.png)

After, click _RUN_, and the program will start.

Noy you sould have the program interface on your screen.
![Screen](https://github.com/SlavkoPrytula/Covid-19-Tracker/blob/master/Photos/Screenshot_20200519_152933.png)

Now you can chose what statistics you want to see. The program provides you with statistical data of SARS COVID-19 and Flu viruses. (Cases, Recovers, Daeths, and much more)

![Example_1](https://github.com/SlavkoPrytula/Covid-19-Tracker/blob/master/Photos/Screenshot_20200519_153037.png)

![Example_2](https://github.com/SlavkoPrytula/Covid-19-Tracker/blob/master/Photos/Screenshot_20200519_153130.png)

It can also provede you plotted statistics on the bar charts.


![Predicted number of cases for COVID-19 up till 2021](https://github.com/SlavkoPrytula/Covid-19-Tracker/blob/master/Photos/cases_prediction.png)

![Recovered now comparison from COVID-19 (red) to Flu(green)](https://github.com/SlavkoPrytula/Covid-19-Tracker/blob/master/Photos/total_deaths_comaparison.png)

![Predicted amount of deaths till 2021 for COVID-19 (red) and compared to recet data for Flu(blue)](https://github.com/SlavkoPrytula/Covid-19-Tracker/blob/master/Photos/total_deaths_predicted_comparison.png)




## Running the tests

Here you will find the necessary tests for the program usage. They [modules] show how to work and integrate with the code correctly.
* **Modules**
[test_CoronaADT.py](https://github.com/SlavkoPrytula/Covid-19-Tracker/blob/master/Modules/ADT/COVID_ADT/test_CoronaADT.py)
[test_coronaADT.py](https://github.com/SlavkoPrytula/Covid-19-Tracker/blob/master/Modules/ADT/COVID_ADT/test_coronaADT.py)
[test_FluADT.py](https://github.com/SlavkoPrytula/Covid-19-Tracker/blob/master/Modules/ADT/FLU_ADT/test_FluADT.py)
[test_ScrapADT.py](https://github.com/SlavkoPrytula/Covid-19-Tracker/blob/master/Modules/ADT/FLU_ADT/test_ScrapADT.py)
[test_prediction.py](https://github.com/SlavkoPrytula/Covid-19-Tracker/blob/master/Modules/SIDE_MODULES/Prediction/test_prediction.py)
[API_usages](https://github.com/SlavkoPrytula/Covid-19-Tracker/tree/master/Modules/SIDE_MODULES/API_usage)
## Built With

* [Python](https://www.python.org/download/releases/3.0/)

## Contributing

Please read [CODE_OF_CONDUCT.md](https://github.com/SlavkoPrytula/Covid-19-Tracker/blob/master/CODE_OF_CONDUCT.md) for details on our code of conduct.
If you have any questions, please contact at slavko.prytula@gmail.com

## Authors

* **Yaroslav Prytula** - *Initial work* - [Yaroslav Prytula on GitHub](https://github.com/SlavkoPrytula)
* **Bogdan Sydor** - *Initial work* - [Bogdan Sydor on GitHub](https://github.com/sydorbogdan)

## License

This project is licensed under the MIT License!
It is available in the repository for view and read - see the [LICENSE.md](https://github.com/SlavkoPrytula/Covid-19-Tracker/blob/master/LICENSE) file for more details.

## Acknowledgments

* _Special thanks to Ukrainian Catholic University for giving the opportunity to make the project become a reality. For all the provided help and tips_
