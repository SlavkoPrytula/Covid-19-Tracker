import requests

url = "https://coronavirus-monitor.p.rapidapi.com/coronavirus/history_by_particular_country_by_date.php"

querystring = {"country":"Ukraine","date":"2020-03-20"}

headers = {
    'x-rapidapi-host': "coronavirus-monitor.p.rapidapi.com",
    'x-rapidapi-key': "API"
    }

response = requests.request("GET", url, headers=headers, params=querystring)

print(response.text)
