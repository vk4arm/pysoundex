# -*- coding: utf-8 -*-

import re

from lang_soundconfig import soundconfig

version = '0.1'
name = "Simple multilanguage soundex"
author = "Victor Kuriashkin"
description = "You can modify lang_soundconfig file for adding new language. Initial contains English and Russian"


def soundex(word, lang="en_US"):
    """
    Really simple soundex realisation. Multilanguage - configurable
    """
    if len(word) == 0:
        return "0000"
    
    cfg = soundconfig[lang]
    word = word.decode("utf-8").lower()    
    snd_arr = [word[0], 0, 0, 0]
    
    word = word[1:]    
    word = re.sub('[%s]' % ''.join(cfg["vowels"]), '', word)
    i=1
    for c in word:
        if cfg["codes"].has_key(c):
            char_code = cfg["codes"][c]
            if snd_arr[i-1] != char_code:
                snd_arr[i] = char_code
                i += 1
            if i==4: break
    return ''.join(map(lambda x: unicode(x), snd_arr))
