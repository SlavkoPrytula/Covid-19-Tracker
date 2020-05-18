from Modules.ADT.FLU_ADT.FluADT import FluADT

# Create FluADT object
FluADTObject = FluADT('links.txt')

# Get years about which FluADTObject have information
years_list = FluADTObject.get_years()
print('Years about which FluADTObject have information: ')
print(years_list)
print()

# Get statistic by 2013 year
statistic_2013 = FluADTObject.get_statistic_year('2013')
print('Statistic for 2013:')
statistic_2013.draw()
print()

# Get statistic for 2013, 45
statistic_2013_3 = FluADTObject.get_statistic_year_age('2013', 45)
print('Statistic for 2013, 45:')
print(statistic_2013_3)
print()

# Get statistic for 2013
total_symptoms_2013 = FluADTObject.get_total_symptoms('2013')
print('Total symptoms 2013 year:')
print(total_symptoms_2013)
print()

# Get average ill
average_ill = FluADTObject.get_avr_illnesses()
print('Average illnesses: ')
print(average_ill)
print()


# Get average recovered
average_recovered = FluADTObject.get_avr_recovered()
print('Average recovered: ')
print(average_recovered)
print()

# Get average deaths
average_deaths = FluADTObject.get_avr_deaths()
print('Average deaths: ')
print(average_deaths)
print()

# Draw FluADTObject
FluADTObject.draw()


FluADTObject.data['2013'].draw()
