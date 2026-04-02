import re

def ukrainian_latin_sort_key(word):
    word_lower = word.lower()

    if re.match(r'[а-яіїєґ]', word_lower):
        priority = 0
    else:
        priority = 1

    ukr_alphabet = "абвгґдеєжзиіїйклмнопрстуфхцчшщьюя"
    char_weights = {char: i for i, char in enumerate(ukr_alphabet)}

    weight = []
    for char in word_lower:
        if char in char_weights:
            weight.append(char_weights[char])
        else:
            weight.append(ord(char))
            
    return (priority, weight)

def main():
    try:
        with open('text_data.txt', 'r', encoding='utf-8') as file:
            text = file.read()
    except FileNotFoundError:
        print("Файл text_data.txt не знайдено.")
        return

    print("Вхідний текст:")
    print(text)
    print("-" * 20)

    cleaned_text = re.sub(r'[^\w\s-]', '', text)
    words = cleaned_text.split()

    unique_words = list(set(words))

    sorted_words = sorted(unique_words, key=ukrainian_latin_sort_key)

    print("\nВідсортований список слів:")
    print(sorted_words)

if __name__ == "__main__":
    main()
