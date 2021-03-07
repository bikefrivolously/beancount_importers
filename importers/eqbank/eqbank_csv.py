from os import path

from beancount.ingest.importers import csv
from beancount.core.number import D

Col = csv.Col

class Importer(csv.Importer):
    def __init__(self, account_type, account, currency):
        # init csv.Importer: https://github.com/beancount/beancount/blob/v2/beancount/ingest/importers/csv.py
        super().__init__(
            {
                Col.DATE: 0,
                Col.PAYEE: 1,
                Col.AMOUNT_CREDIT: 2,
                Col.AMOUNT_DEBIT: 3,
                Col.BALANCE: 4,
            }, account, currency,
            debug=True
        )
        self.account_type = account_type

    def identify(self, f):
        return path.basename(f.name) == 'EQ Details.csv'

    def file_name(self, f):
        return 'EQ Details.csv'

    # override parse_amount from csv.Importer to strip off the dollar sign
    def parse_amount(self, string):
        print(string)
        if string.startswith('$'):
            return D(string[1:])
        else:
            return D(string)
