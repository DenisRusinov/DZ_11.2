def text_in_capital_letters(text=str(input())):
    """функия делающая все буквы заглавными"""
    return text.upper()


def capital_letters_of_words(string):
    """функия делающая каждое слово предложения с заглавной буквы"""
    result = ' '.join(word.capitalize() for word in string.split())
    return result


string = 'big world'
print(capital_letters_of_words(string))
