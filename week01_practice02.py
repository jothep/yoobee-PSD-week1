import numpy as np

def calculate_average(values):

    average_score = round(sum(values)/len(values),1)
    print("Average temperature:", average_score)

def determine_highest_and_lowest(values):

    temp_array = np.array(values)
    max_temp = np.max(temp_array)
    min_temp = np.min(temp_array)

    print("The highest temerature:", max_temp)
    print("The lowest temerature:", min_temp)

def convert_to_Fah(values):

    temp_array = np.array(values)
    Fahrenheit = temp_array * 9 / 5 + 32

    print("Fahrenheit are:",Fahrenheit)

def find_the_day(values):

    temp_array = np.array(values)
    indices = np.where(temp_array > 20)[0] + 1

    print("the days where the temp excedded 20:", indices)

if __name__ == "__main__":
    temperature = [18.5, 19, 20, 25.0, 2, 30, 13.9]
    print("The temperatures of the week are:",temperature)

    calculate_average(temperature)
    determine_highest_and_lowest(temperature)
    convert_to_Fah(temperature)
    find_the_day(temperature)