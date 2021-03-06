from ._loader import (AREA, FAMILY, FGIVEN, MGIVEN, PHONE, DOMAIN,
                      COLOR, ADDRESS, NOUN, AGE)
import random


def identity(gender:str = None) -> dict:
    """ Generates a pseudo-random identity.

    Optional args
        gender: 'm' for traditionally male, 'f' for traditionally female.

    Returns a dict with the following keys:
        name -> full name
        given -> given name / first name
        family -> family name / last name
        address -> well formed address (fake of course)
        city -> city of residence
        state -> state of residence
        zip_code -> zip code of residence (matches the city and state)
        phone - > a phone number with an area code from the state of residence.
        email -> a valid email address (fake of course)
    """

    if gender and gender.lower() not in ["m", "f"]:
        raise ValueError("'gender' must be 'm' or 'f'")

    if gender and gender.lower() == "m":
        given = _pluck(MGIVEN)
    elif gender and gender.lower() == "f":
        given = _pluck(FGIVEN)
    else:
        given = _pluck(MGIVEN + FGIVEN)
    family = _pluck(FAMILY)
    email = _make_email(given, family)
    zip_code, city, state_code = _pluck(AREA)
    phone = _make_phone(state_code)
    address = _make_address()

    return dict(name=f"{given} {family}".title(),
                given=given.title(),
                family=family.title(),
                address=address,
                city=city.title(),
                state=state_code.upper(),
                zip_code=zip_code,
                phone=phone,
                email=email)


def _pluck(barrel: list):
    return barrel[random.randint(0, len(barrel) -1)]


def _make_email(given: str, family: str) -> str:
    return f"{given[0]}{family}@{_pluck(DOMAIN)}".lower()


def _make_phone(state_code: str) -> str:
    area_codes = PHONE.get(state_code.upper(), [999])
    head = _pluck(area_codes)
    thorax = f"{random.randint(0, 999):03d}"
    abdomen = f"{random.randint(0, 9999):04d}"
    return f"{head}-{thorax}-{abdomen}"


def _make_address() -> str:
    number = random.randint(0, 9999)
    use_color = random.randint(0, 1)
    adj = _pluck(COLOR) if use_color else _pluck(AGE)
    suffix = _pluck(ADDRESS)
    noun = _pluck(NOUN)
    return f"{number} {adj} {noun} {suffix}"

