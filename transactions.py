
class Transaction(object):

    _FIELD = [('type', int), ('datetime', str), ('btc', float),
              ('usd', float), ('1_btc', float), ('fee', float)]

    def __init__(self, line):

        array = line.split(',')
        pos = 0
        for field, cast in self._FIELD:
            setattr(self, field, cast(array[pos]))
            pos = pos + 1


class History(object):

    def __init__(self):

        self._trans_list = []

        with open('Transactions.csv', 'r') as f:
            for line in f:
                self._trans_list.append(Transaction(line))

    def compute(self, max_pos):

        btc, usd = 0, 0

        pos = 0
        for trans in self._trans_list:

            btc = btc + trans.btc
            usd = usd + trans.usd
            usd = usd - trans.fee

            if pos == max_pos:
                break
            pos = pos + 1

        return btc, usd

