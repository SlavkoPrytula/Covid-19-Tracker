from Modules.ADT.FLU_ADT.ScrapADT import ScrapADT

# Create ScrapADT object
ScrapADTObject = ScrapADT('https://www.cdc.gov'
                          '/flu/about/burden/2010-2011.html')

# Draw ScrapADTObject
ScrapADTObject.draw()
print()

# Get link attribute
link_attribute = ScrapADTObject.get_link()
print('Link:')
print(link_attribute)
print()

# Get year from link
print('Year: ')
print(ScrapADTObject.get_year())
print()
