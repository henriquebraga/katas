

DIAL_CODES = [
    (86, 'China'),
    (91, 'India'),
    (55, 'Brazil'),
]

def list_comprehension(countries_and_dial_codes=DIAL_CODES):
    return list(str(code) + ' - ' + country.upper()
                for code, country
                in countries_and_dial_codes
                )

def dict_comprehension(countries_and_dial_codes=DIAL_CODES):
    return {
            code : country.upper()
             for code, country in
             countries_and_dial_codes
            }

