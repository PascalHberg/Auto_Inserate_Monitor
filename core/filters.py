from config import MIN_PS, MAX_KM, MIN_YEAR, MAX_PRICE

def matches_rules(car: dict) -> bool:
    try:
        return (
            car.get("power", 0) >= MIN_PS and
            car.get("mileage", 999999) <= MAX_KM and
            car.get("year", 0) >= MIN_YEAR and
            car.get("price", 999999999) <= MAX_PRICE
        )
    except:
        return False
