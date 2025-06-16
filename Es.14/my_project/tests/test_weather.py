from my_project.weather import check_weather

def test_check_weather():
    assert check_weather(21.00) == "hot", "Temperatures greater than 20 degree \ must be considered as Hot"

def test_check_weather():
    assert check_weather(5.00) == "average", "Temperatures between 10 and 20 degree \ must be considered as average temperature"

def test_check_weather():
    assert check_weather(5.00) == "cold", "Temperatures lower than 10 degree must be considered as cold"

def test_check_weather():
    assert check_weather(11.00) == "average", "Temperatures between 10 and 20 degree must be considered as average temperature"

    