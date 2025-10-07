# import copy
#
#
# def cach_word(funk):
#     cach = {}
#     def warped(sentens, sord_list):
#         cach_key = sentens + str(sorted(sord_list))
#         if cach_key in cach:
#             result = {}
#             for key, valeue in cach[cach_key].items():
#                 result[key] = valeue
#             result = cach[cach_key]
#         result = funk(sentens, sord_list)
#         cach[cach_key] = {}
#         for key, valeue in result.items():
#            cach[cach_key][key] = valeue
#         #[cach_key][key] = copy.deepcopy(result)
#
#         print("cach_word")
#         return result
#
#     return warped
#
# @cach_word
# def count_words(sentens, sord_list):
#     clean_sentence = ""
#     for char in sentens:
#         if char not in "!@#%*()_+-=[]{};:\|,.<>?/":
#             clean_sentence += char
#
#     clean_sentence = clean_sentence.lower()
#     words = clean_sentence.split()
#
#     words_count = {}
#     for word in sord_list:
#         word_lower = word.lower()
#         count = 0
#         for y in words:
#             if y == word_lower:
#                 count += 1
#         words_count[word] = count
#
#     return words_count
#
#
# sentence = "my i STAND UNSHAKE DOWN !!"
# words_to_count = ["MY", "I", "STAND", "unshake", "down"]
#
# print(count_words(sentence, words_to_count))
#
#
#
#
#
#
#
# import itertools


import copy
from unittest.util import sorted_list_difference


def cach_word(funk):
    cach = {}

    def warped(sentens, sord_list):
        cach_key = sentens + str(sorted(sord_list))
        if cach_key in cach:
            result = copy.deepcopy(cach[cach_key])
            return result
        result = funk(sentens, sord_list)
        cach[cach_key] = copy.deepcopy(result)
        print("cach_word")
        return result
    return warped


@cach_word
def count_words(sentens, sord_list):
    clean_sentence = ""
    for char in sentens:
        if char not in "!@#%()_+-=[]{}:\|,.<>?/":
         var = clean_sentence == char
    clean_sentence = clean_sentence.lower()
    words = clean_sentence.split()

    words_count = {}
    for word in sord_list:
        word_lower = word.lower()
        count = 0
        for y in words:
         if y == word_lower:
          count += 1
          words_count[word] = count

    return words_count


sentence = "my i STAND UNSHAKE DOWN !!"
print(count_words(sentence))











