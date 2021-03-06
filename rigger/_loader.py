import csv
import us
import os
os.environ.setdefault("DC_STATEHOOD", "1")
DIR = os.path.dirname(__file__)

AREA = []
PHONE = {}
MGIVEN = []
FGIVEN = []
FAMILY = []
DOMAIN = []
NOUN = []
COLOR = []
ADDRESS = []
AGE = ["Old", "New", "Olde"]


def __load_area():
    with open(f"{DIR}/fixtures/area", "rt") as raw:
        reader = csv.reader(raw)
        for row in reader:
            zip_code = f"{int(row[0]):05d}"
            city = row[1]
            state_code = row[2]
            AREA.append((zip_code, city, state_code))


def __load_phone():
    with open(f"{DIR}/fixtures/phone", "rt") as raw:
        reader = csv.reader(raw)
        for row in reader:
            state_code = us.states.lookup(row[0]).abbr
            phone_codes = [x for x in row[1:] if x]
            PHONE[state_code] = phone_codes


def __load_basic(container, name):
    with open(f"{DIR}/fixtures/{name}", "rt") as raw:
        reader = csv.reader(raw)
        for row in reader:
            container.append(row[0].strip().title())


__load_area()
__load_phone()
__load_basic(MGIVEN, "mgiven")
__load_basic(FGIVEN, "fgiven")
__load_basic(FAMILY, "family")
__load_basic(NOUN, "noun")
__load_basic(ADDRESS, "address")
__load_basic(COLOR, "color")
__load_basic(DOMAIN, "domain")
