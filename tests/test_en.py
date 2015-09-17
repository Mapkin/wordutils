from wordutils.en_us import EnglishUS


m_spoken = {
    0: 'zero',
    1: 'one',
    2: 'two',
    3: 'three',
    4: 'four',
    5: 'five',
    6: 'six',
    7: 'seven',
    8: 'eight',
    9: 'nine',
    10: 'ten',
    11: 'eleven',
    12: 'twelve',
    13: 'thirteen',
    14: 'fourteen',
    15: 'fifteen',
    16: 'sixteen',
    17: 'seventeen',
    18: 'eighteen',
    19: 'nineteen',
    20: 'twenty',
    35: 'thirty five',
    41: 'forty one',
    78: 'seventy eight',
    100: 'one hundred',
    112: 'one hundred twelve',
    999: 'nine hundred ninety nine',
    1000: 'one thousand',
    1003: 'one thousand three', 
    9999: 'nine thousand nine hundred ninety nine',
    99999: 'ninety nine thousand nine hundred ninety nine',
    999999: 'nine hundred ninety nine thousand nine hundred ninety nine',
}


def test_en_instance_full():
    en = EnglishUS()
    for n, expected in m_spoken.items():
        assert en.number_spoken_full(n) == expected

def test_en_class_full():
    en = EnglishUS
    for n, expected in m_spoken.items():
        assert en.number_spoken_full(n) == expected

def test_en_casual():
    m = {
        0: 'zero',
        1: 'one',
        2: 'two',
        3: 'three',
        4: 'four',
        5: 'five',
        6: 'six',
        7: 'seven',
        8: 'eight',
        9: 'nine',
        10: 'ten',
        11: 'eleven',
        12: 'twelve',
        13: 'thirteen',
        14: 'fourteen',
        15: 'fifteen',
        16: 'sixteen',
        17: 'seventeen',
        18: 'eighteen',
        19: 'nineteen',
        20: 'twenty',
        35: 'thirty five',
        78: 'seventy eight',
        100: 'one hundred',
        112: 'one twelve',
        999: 'nine ninety nine',
        302: 'three oh two',
        1234: 'twelve thirty four',
        300: 'three hundred',
        2000: 'two thousand',
        5600: 'fifty six hundred',
    }

    en = EnglishUS
    for n, expected in m.items():
        assert en.number_spoken_casual(n) == expected

