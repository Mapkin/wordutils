wordutils
=========

Helper classes and utilities for manipulating numbers to work with
text-to-speech (TTS) engines

Usage
-----
`wordutils` provides a class for different languages although only US
English is provided at the moment.

Most methods are provided as class methods to make things easier

Basic manipulation methods are:
* `number_spoken_full()`
* `number_spoken_casual()`
* `ordinal_text()`

```
In [1]: from wordutils.en_us import EnglishUS

In [2]: EnglishUS.number_spoken_full(102)
Out[2]: u'one hundred two'

In [3]: EnglishUS.number_spoken_casual(102)
Out[3]: u'one oh two'

In [4]: EnglishUS.ordinal_text(102)
Out[4]: u'102nd'

```

See Also
--------
https://github.com/savoirfairelinux/num2words

Project skeleton from [pyskel](https://github.com/mapbox/pyskel)
