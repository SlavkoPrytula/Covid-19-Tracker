from corona_adt import Corona

if __name__ == '__main__':
    c = Corona()
    data = c.get_affected_countries()
    print(data)
    print(type(data))
