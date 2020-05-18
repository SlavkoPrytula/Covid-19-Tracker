from Modules.ADT.COVID_ADT.Corona_ADT import CoronaADT

c = CoronaADT()
c.country = "USA"

print("NOTE!!! The information provided "
      "is about a week long in time.")

print("The country we get the information for is:")
print(c.country)

print("Amount of people who wre "
      "infected in {}".format(c.country))
print(c.get_infected())

print("Amount of people who have "
      "recovered in {}".format(c.country))
print(c.get_recovered())

print("Amount of people who have "
      "died in {}".format(c.country))
print(c.get_deaths())

print("Amount of people who got "
      "infected today in {}".format(c.country))
print(c.get_new_cases)

print("Amount of people who have "
      "died today in {}".format(c.country))
print(c.get_new_deaths())

print("Information about the country")
print(c.__str__())

print("The last recorded tame was:")
print(c.get_record_date())

print("Whole world statistics")
print(c.get_world_total_stat())



