import numpy as np

def analyze_rainfall(data):
    array = np.array(data)
    print("The numpy array is:", array)

    total = round(np.sum(array), 1)
    print("The total rainfall for the week is:", total)

    if len(array) > 0:
        average = round(np.mean(array), 1)
        print("The average rainfall for the week is:", average)
    else:
        average = 0
        print("The average rainfall for the week is:", average)

    no_rain_days = np.sum(array == 0)
    print("The days had no rain are:", no_rain_days)

    indices = np.where(array > 5.0)[0]
    days_above_5mm = (indices + 1).tolist()
    print("Days with >5mm rainfall:", days_above_5mm)

    percentile_75th = np.percentile(array, 75)
    print("75th percentile:", round(percentile_75th, 1))

    values_above_75th = array[array > percentile_75th].tolist()
    print("Values above 75th percentile:", values_above_75th)

    return array, total, average, no_rain_days, days_above_5mm, percentile_75th, values_above_75th

if __name__ == "__main__":
    rainfall_data = [0.0, 5.2, 3.1, 0.0, 12.4, 0.0, 7.5]
    analyze_rainfall(rainfall_data)