# TODO  Напишите функцию count_letters
def count_letters(text):
    l_text = text.lower()

    letter_numbers = {}
    for symbol in l_text:
        if symbol.isalpha():
            if symbol in letter_numbers:
                letter_numbers[symbol] += 1
            else:
                letter_numbers[symbol] = 1
    return letter_numbers

# TODO Напишите функцию calculate_frequency
def calculate_frequency(letter_numbers):
    total_symbol = sum(letter_numbers.values())

    symbol_frequency = {}
    for current_letter, count in letter_numbers.items():
        symbol_frequency[current_letter] = count / total_symbol

    return symbol_frequency

main_str = """
У лукоморья дуб зелёный;
Златая цепь на дубе том:
И днём и ночью кот учёный
Всё ходит по цепи кругом;
Идёт направо — песнь заводит,
Налево — сказку говорит.
Там чудеса: там леший бродит,
Русалка на ветвях сидит;
Там на неведомых дорожках
Следы невиданных зверей;
Избушка там на курьих ножках
Стоит без окон, без дверей;
Там лес и дол видений полны;
Там о заре прихлынут волны
На брег песчаный и пустой,
И тридцать витязей прекрасных
Чредой из вод выходят ясных,
И с ними дядька их морской;
Там королевич мимоходом
Пленяет грозного царя;
Там в облаках перед народом
Через леса, через моря
Колдун несёт богатыря;
В темнице там царевна тужит,
А бурый волк ей верно служит;
Там ступа с Бабою Ягой
Идёт, бредёт сама собой,
Там царь Кащей над златом чахнет;
Там русский дух… там Русью пахнет!
И там я был, и мёд я пил;
У моря видел дуб зелёный;
Под ним сидел, и кот учёный
Свои мне сказки говорил.
"""

# TODO Распечатайте в столбик букву и её частоту в тексте
count_symbol = count_letters(main_str)
frequency_letters = calculate_frequency(count_symbol)

for letter, frequency in frequency_letters.items():
    print(f"{letter}: {frequency:.2f}")
