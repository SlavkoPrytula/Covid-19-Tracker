import http.client


def get_countries():
    """
    Get all country names where coronavirus cases
    were diagnosed.
    """
    conn = http.client.HTTPSConnection("coronavirus-monitor.p.rapidapi.com")

    headers = {
        'x-rapidapi-host': "coronavirus-monitor.p.rapidapi.com",
        'x-rapidapi-key': "API"
        }

    conn.request("GET", "/coronavirus/affected.php", headers=headers)

    res = conn.getresponse()
    data = res.read()

    return data.decode("utf-8")
