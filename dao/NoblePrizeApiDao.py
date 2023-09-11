import logging

from adapters import NobelPrizeApiAdapter


def get_laureate_info():
    """Convert API to get noble laureate information to required format"""
    try:
        laureate_info = NobelPrizeApiAdapter.get_laureate_info()
        if laureate_info is not None:
            return laureate_info.get("laureates")
        else:
            logging.error("Nobel info is not available")
    except Exception as ex:
        logging.error("Error while processing Nobel info - " + ex)


def get_country_info():
    """Return country code to name map from API"""
    country_code_info = NobelPrizeApiAdapter.get_country_info()
    country_name_by_code = dict()
    try:
        if country_code_info is not None:
            country_code_name_list = country_code_info.get("countries")
            for country_item in country_code_name_list:
                name = country_item.get("name")
                code = country_item.get("code")
                country_name_by_code[code] = name
        else:
            logging.error("Country info is empty")
        return country_name_by_code
    except Exception as ex:
        logging.error("Error while processing Nobel country info - " + ex)
