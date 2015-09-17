from __future__ import division
from __future__ import unicode_literals

from wordutils.base import BaseLanguage
from wordutils.utils import split_num


_ones_teens = ['', 'one', 'two', 'three', 'four',
         'five', 'six', 'seven', 'eight', 'nine',
         'ten', 'eleven', 'twelve', 'thirteen', 'fourteen',
         'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen']

_tens = [None, None, 'twenty', 'thirty', 'forty',
         'fifty', 'sixty', 'seventy', 'eighty', 'ninety']

_exponents = [None, 'thousand', 'million', 'billion', 'trillion']

MAX_NUM = 10 ** (len(_exponents) * 3) - 1


class EnglishUS(BaseLanguage):
    @classmethod
    def number_spoken_full(cls, n):
        """
        The basic algorithm is to split the number into groups
        of 3. Pronounce each group of 3 and then append the exponent
        part.

        So 9999 gets split into [9, 999]. The first group is
        "nine thousand". The second group is "nine hundred ninety nine"

        """
        if n > MAX_NUM:
            raise ValueError(
                "{} is too large. Largest number is {}".format(n, MAX_NUM)
            )
        if n == 0:
            return 'zero'

        parts = []
        for g, exp in zip(reversed(split_num(n, 3)), _exponents):
            s = cls.lt_1000_spoken_full(g)
            if s:
                if exp:
                    s += " " + exp
                parts.append(s)

        return ' '.join(reversed(parts))

    @classmethod
    def number_spoken_casual(cls, n):
        """
        Split the number in groups of 2. Pronounce each one separately
        but say "oh 5" for the final group if it's less than 10.

        >>> EnglishUS.number_spoken_casual(302)
        "three oh two"
        >>> EnglishUS.number_spoken_casual(1267)
        "twelve sixty seven"

        """
        if n > 9999 or n % 1000 == 0:
            return cls.number_spoken_full(n)
        if n == 0:
            return 'zero'

        groups = split_num(n, 2)
        if len(groups) > 1 and groups[-1] == 0:
            s = "{} hundred".format(cls.lt_1000_spoken_full(groups[0]))
        elif len(groups) > 1 and groups[-1] < 10:
            s = "{} oh {}".format(
                cls.lt_1000_spoken_full(groups[0]),
                cls.lt_1000_spoken_full(groups[1])
            )
        else:
            s = " ".join([cls.lt_1000_spoken_full(g) for g in groups])
        return s

    @classmethod
    def lt_1000_spoken_full(cls, n):
        """ Spoken form of numbers where 0 < n < 1000 """
        parts = []
        if n >= 100:
            parts.append(_ones_teens[n // 100] + ' hundred')
            n %= 100
        if n >= 20:
            parts.append(_tens[n // 10])
            n %= 10
        if n:
            parts.append(_ones_teens[n])
        return " ".join(parts)
