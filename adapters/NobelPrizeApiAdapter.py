import requests
import logging


def get_laureate_info():
    """API to get noble laureate information"""
    try:
        r = requests.get('https://api.nobelprize.org/v1/laureate.json')
        if r.status_code == 200:
            return r.json()
        else:
            raise Exception
    except Exception as ex:
        logging.exception(ex)


def get_country_info():
    """API to get noble laureate country information"""
    try:
        r = requests.get('https://api.nobelprize.org/v1/country.json')
        if r.status_code == 200:
            return r.json()
        raise Exception
    except Exception as ex:
        logging.exception(ex)

