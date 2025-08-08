from bmi_app import calculate_bmi, get_bmi_category, get_health_message

def test_calculate_bmi():
    assert round(calculate_bmi(70,170), 2) == 24.22
    assert round(calculate_bmi(80,172.72), 2) == 26.82
    assert round(calculate_bmi(89, 151.90), 2) == 38.57
    
def test_get_bmi_category():
    assert get_bmi_category(18.37) == "Underweight"
    assert get_bmi_category(19.94) == "Normal Weight"
    assert get_bmi_category(27.04) == "Overweight"
    assert get_bmi_category(35.09) == "Obese"

def test_get_health_message():
    assert "underweight" in get_health_message("Underweight").lower()
    assert "normal weight" in get_health_message("Normal Weight").lower()
    assert "overweight" in get_health_message("Overweight").lower()
    assert "obese" in get_health_message("Obese").lower()

test_calculate_bmi()
test_get_bmi_category()
test_get_health_message()