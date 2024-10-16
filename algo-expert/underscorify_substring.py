"""Solution to Underscorify Substring problem from Algo Expert"""


def underscorify_substring(input_str: str, keyword: str) -> str:
    words = input_str.split()
    constructed_result = ''
    for word in words:
        if keyword in word:
            constructed_word = ''
            i = 0
            positive_str = False
            keyword_counter = 0
            while i < len(word):
                print(word)
                if word[i: i+len(keyword)] == keyword:
                    keyword_counter = 0
                    if not positive_str:
                        if constructed_word and constructed_word[-1] == '_':
                            constructed_word = constructed_word[:-1]
                        else:
                            constructed_word += '_'
                        positive_str = True
                    else:
                        constructed_word += word[i]
                elif positive_str:
                    keyword_counter += 1
                constructed_word += word[i]
                if keyword_counter == len(keyword)-1:
                    constructed_word += '_'
                    positive_str = False
                    keyword_counter = 0
                i += 1
            constructed_result += ' ' + constructed_word
        else:
            constructed_result += ' ' + word

    return constructed_result[:-1]


if __name__ == "__main__":
    print(underscorify_substring('testthis is a testyomaamatesthelo to see if testestest works', 'test'))
