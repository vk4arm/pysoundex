# -*- coding: utf-8 -*-

soundconfig = {
    "ru_RU": {
        "vowels": ['у', 'е', 'ы', 'а', 'о', 'э', 'я', 'и', 'ю', 'ь', 'ъ', 'й'],
        "consonants": {
            1: ['б', 'п', 'ф', 'в'],
            2: ['с', 'ц', 'з', 'к', 'г', 'х'],
            3: ['т', 'д'],
            4: ['л', 'й'],
            5: ['м', 'н'],
            6: ['р'],
        }
    },
    "en_US": {
        "vowels": ['a', 'e', 'h', 'i', 'o', 'u', 'w', 'y'],
        "consonants": {
            1: ['b', 'f', 'p', 'v'],
            2: ['c', 'g', 'j', 'k', 'q', 's', 'x', 'z'],
            3: ['d', 't'],
            4: ['l'],
            5: ['m', 'n'],
            6: ['r']
        }
    },
}


def revert_config():
    for k in soundconfig:
        soundconfig[k]["codes"] = {}
        for (code) in soundconfig[k]["consonants"].keys():
            for c in soundconfig[k]["consonants"][code]:
                c = c.decode("utf-8") if hasattr(c, 'decode') else c
                soundconfig[k]["codes"][c] = code


revert_config()
