import logging

from dao import NoblePrizeApiDao
from exception import FirstNameNotFoundException
from writer import CSVFileWriter


def set_to_str(set_items):
    res_str = ""
    if set_items is not None:
        for item in set_items:
            res_str += item + ";"
        res_str = res_str[:-1]
    return res_str


def generate_noble_laureate_info(laureate_info):
    id = laureate_info.get("id")
    try:
        firstname = laureate_info.get("firstname")
        if firstname is None:
            raise FirstNameNotFoundException
        surname = laureate_info.get("surname", "")
        name = firstname + ' ' + surname
        dob = laureate_info.get("born")
        unique_years = set()
        unique_cat = set()
        prizes = laureate_info.get("prizes")
        for prize in prizes:
            year = prize.get("year")
            cat = prize.get("category")
            unique_years.add(year)
            unique_cat.add(cat)

        unique_years_str = set_to_str(unique_years)
        unique_cat_str = set_to_str(unique_cat)

        gender = laureate_info.get("gender")
        country_code = laureate_info.get("bornCountryCode")
        country = countryNameByCode.get(country_code)

        # list of strings
        return [id, name, dob, unique_years_str, unique_cat_str, gender, country]
    except UnicodeEncodeError:
        logging.error("Invalid character found for id - " + id)
    except FirstNameNotFoundException:
        logging.error("First Name is missing for id - " + id)
    except Exception as ex:
        logging.exception(ex)


if __name__ == '__main__':
    try:
        laureates = NoblePrizeApiDao.get_laureate_info()
        countryNameByCode = NoblePrizeApiDao.get_country_info()
        csv_rows = list()
        for laureate in laureates:
            result_row = generate_noble_laureate_info(laureate)
            if result_row is not None:
                csv_rows.append(result_row)

        CSVFileWriter.write_csv(csv_rows)
    except Exception as ex:
        logging.exception(ex)
    # call country api
