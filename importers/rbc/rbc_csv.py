from os import path

from beancount.ingest.importers import csv

Col = csv.Col

class Importer(csv.Importer):
    def __init__(self, account_type, account, currency):
        # init csv.Importer: https://github.com/beancount/beancount/blob/v2/beancount/ingest/importers/csv.py
        super().__init__(
            {
                Col.DATE: 2,
                Col.PAYEE: 4,
                Col.NARRATION: 5,
                Col.AMOUNT: 6,
            }, account, currency,
            debug=False
        )
        self.account_type = account_type

    def identify(self, f):
        return path.basename(f.name) == 'rbc-{}.csv'.format(self.account_type)

    def file_name(self, f):
        return 'rbc-{}.csv'.format(self.account_type)

