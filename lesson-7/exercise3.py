# from bitbucket

def rot_13():
    """
    a way to create the initial dictionary
    """
    encoding = {}
    abc = 'abcdefghijklmnopqrstuvwxyzabcdefghijklm'
    abc_capital = 'ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLM'

    for i in range(0, 26):
        encoding.update({abc[i]: abc[i + 13]})
        encoding.update({abc_capital[i]: abc_capital[i + 13]})

    return encoding


print(rot_13())  # note that since dictionaaries are not sorted, it might look a bit different from


# what is written in the exercise. What matters is that the encoding is the same.
def decode(s):
    key = rot_13()
    sentence = []

    for i in range(0, len(s)):
        if key.get(s[i], 'none') != 'none':
            sentence.append(key[s[i]])
        else:
            sentence.append(s[i])
    new_sentence = ''.join(sentence)

    return new_sentence


print(decode('V NZ YRNEAVAT CLGUBA JVGU FUR PBQRF NPNQRZL!'))

"""
Other solutions, proposed by your fellow participant Merav Friedland from Bar Ilan branch, makes use
of the update and get methods of dictionries:
"""


def char_frequency(word):
    freq = {}

    for char in word:
        if freq.get(char):
            value = freq[char]
            freq.update({char: value + 1})
        else:
            freq.update({char: 1})

    return freq


print(char_frequency('abzz'))


def rot_13():
    """
    a way to create the initial dictionary
    """
    result_dictionary = {}
    abc = 'abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz'
    abc_capital = abc.upper()
    for i in range(0, 26):
        result_dictionary.update({abc[i]: abc[i + 13]})
        result_dictionary.update({abc_capital[i]: abc_capital[i + 13]})
    return result_dictionary


def decode(sentence):
    new_sentence = []
    result_dictionary = rot_13()
    for i in sentence:
        if result_dictionary.get(i) is None:
            new_sentence.append(i)
        else:
            new_sentence.append(result_dictionary.get(i))
    new_sentence = "".join(new_sentence)
    return new_sentence


print(decode('V NZ YRNEAVAT CLGUBA JVGU FUR PBQRF NPNQRZL!'))