from __future__ import division
from __future__ import unicode_literals


class BaseLanguage(object):
    def number_spoken_full(self, n):
        raise NotImplementedError()

    def number_spoken_casual(self, n):
        raise NotImplementedError()

    def ordinal_spoken(self, n):
        raise NotImplementedError()

    @classmethod
    def ordinal_text(cls, n):
        ones = n % 10
        tens = (n // 10) % 10
        if tens == 1 or ones == 0 or ones >= 4:
            suffix = 'th'
        else:
            m = {
                1: 'st',
                2: 'nd',
                3: 'rd',
            }
            suffix = m[ones]
        return '{}{}'.format(n, suffix)
