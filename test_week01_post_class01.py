from week01_post_class01 import analyze_rainfall
import numpy as np

def test_analyze_rainfall():
    data = [0.0, 5.2, 3.1, 0.0, 12.4, 0.0, 7.5]

    array, total, average, no_rain_days, days_above_5mm, percentile_75th, values_above_75th = analyze_rainfall(data)

    assert isinstance(array, np.ndarray)

    assert np.isclose(total, 28.2, atol=0.01)

    if len(data) > 0:
        expected_avg = 4.0
        assert round(average, 1) == expected_avg
    else:
        assert average == 0

    assert no_rain_days == 3

    expected_days_above_5mm = [2, 5, 7]
    assert days_above_5mm == expected_days_above_5mm

    expected_percentile_75th = np.percentile(data, 75)
    assert np.isclose(percentile_75th, expected_percentile_75th, atol=0.01)

    expected_above_values = [x for x in data if x > expected_percentile_75th]
    assert values_above_75th == expected_above_values