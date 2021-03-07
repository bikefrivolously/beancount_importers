from os import path

from beancount.ingest.importers import csv

Col = csv.Col

class Importer(csv.Importer):
    def __init__(self, account_type, account, currency):
        # init csv.Importer: https://github.com/beancount/beancount/blob/v2/beancount/ingest/importers/csv.py
        super().__init__(
            {
            Col.DATE: 0,
            Col.PAYEE: 1,
            Col.AMOUNT_DEBIT: 2,
            Col.AMOUNT_CREDIT: 3,
            Col.BALANCE: 4,
            }, account, currency
        )
        self.account_type = account_type

    def identify(self, f):
       return path.basename(f.name) == 'accountactivity-td-{}.csv'.format(self.account_type)

    # rename the file when running bean-file
    def file_name(self, f):
        return 'td-{}.csv'.format(self.account_type)
