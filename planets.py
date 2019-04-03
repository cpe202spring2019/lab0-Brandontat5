def weight_on_planets():
    weight = input("What do you weigh on earth? ")
    weight = float(weight)
    print('\nOn Mars you would weigh %s pounds.\nOn Jupiter you would weigh %s pounds.'
          % (weight * 0.38, weight * 2.34))


if __name__ == '__main__':
    weight_on_planets()
