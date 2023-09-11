import csv
import logging


def write_csv(rows):
    with open('laurete_info.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile, delimiter=',')
        for row in rows:
            try:
                writer.writerow(row)
            except UnicodeEncodeError:
                logging.error("Failed to write row with id - " + row[0])
            except Exception as ex:
                logging.exception(ex)
