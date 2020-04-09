import requests

url = "https://coronavirus-monitor.p.rapidapi.com/coronavirus/cases_by_particular_country.php"

querystring = {"country":"Ukraine"}

headers = {
    'x-rapidapi-host': "coronavirus-monitor.p.rapidapi.com",
    'x-rapidapi-key': "API"
    }

response = requests.request("GET", url, headers=headers, params=querystring)

print(response.text)
