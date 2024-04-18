UKRAINIAN_ALPHABET_LOWER = 'абвгґдеєжзиіїйклмнопрстуфхцчшщьюя'  # Український алфавіт у нижньому регістрі
UKRAINIAN_ALPHABET_UPPER = UKRAINIAN_ALPHABET_LOWER.upper()  # Український алфавіт у верхньому регістрі


def vigenere_cipher(text, key):
    """
    Шифрування методом Віженера.

    Args:
        text (str): Текст, який треба зашифрувати.
        key (str): Ключ для шифрування.

    Returns:
        str: Зашифрований текст.
    """
    encrypted_text = ""  # Ініціалізація змінної для зберігання зашифрованого тексту
    key_length = len(key)
    for i, char in enumerate(text):  # Ітерація по кожному символу у тексті
        if char in UKRAINIAN_ALPHABET_LOWER:  # Перевірка чи символ є українською буквою у нижньому регістрі
            shift = UKRAINIAN_ALPHABET_LOWER.index(key[i % key_length])  # Визначення зсуву за ключем
            encrypted_char_index = (UKRAINIAN_ALPHABET_LOWER.index(char) + shift) % len(UKRAINIAN_ALPHABET_LOWER)#Додає зсув до індексу символу
            encrypted_text += UKRAINIAN_ALPHABET_LOWER[encrypted_char_index]  # Додавання зашифрованого символу до результату
        elif char in UKRAINIAN_ALPHABET_UPPER:  # Перевірка чи символ є українською буквою у верхньому регістрі
            shift = UKRAINIAN_ALPHABET_LOWER.index(key[i % key_length])  # Визначення зсуву за ключем
            encrypted_char_index = (UKRAINIAN_ALPHABET_UPPER.index(char) + shift) % len(UKRAINIAN_ALPHABET_UPPER)
            encrypted_text += UKRAINIAN_ALPHABET_UPPER[encrypted_char_index]  # Додавання зашифрованого символу до результату
        else:  # У випадку, якщо символ не є українською літерою
            encrypted_text += char  # Додавання символу до результату без змін
    return encrypted_text  # Повернення зашифрованого тексту

def vigenere_decrypt(text, key):
    """
    Розшифрування методом Віженера.

    Args:
        text (str): Зашифрований текст.
        key (str): Ключ для розшифрування.

    Returns:
        str: Розшифрований текст.
    """
    decrypted_text = ""  # Ініціалізація змінної для зберігання розшифрованого тексту
    key_length = len(key)
    for i, char in enumerate(text):  # Ітерація по кожному символу у тексті
        if char in UKRAINIAN_ALPHABET_LOWER:  # Перевірка чи символ є українською буквою у нижньому регістрі
            shift = UKRAINIAN_ALPHABET_LOWER.index(key[i % key_length])  # Визначення зсуву за ключем
            decrypted_char_index = (UKRAINIAN_ALPHABET_LOWER.index(char) - shift) % len(UKRAINIAN_ALPHABET_LOWER)#Віднімає зсув до індексу символу
            decrypted_text += UKRAINIAN_ALPHABET_LOWER[decrypted_char_index]  # Додавання розшифрованого символу до результату
        elif char in UKRAINIAN_ALPHABET_UPPER:  # Перевірка чи символ є українською буквою у верхньому регістрі
            shift = UKRAINIAN_ALPHABET_LOWER.index(key[i % key_length])  # Визначення зсуву за ключем
            decrypted_char_index = (UKRAINIAN_ALPHABET_UPPER.index(char) - shift) % len(UKRAINIAN_ALPHABET_UPPER)
            decrypted_text += UKRAINIAN_ALPHABET_UPPER[decrypted_char_index]  # Додавання розшифрованого символу до результату
        else:  # У випадку, якщо символ не є українською літерою
            decrypted_text += char  # Додавання символу до результату без змін
    return decrypted_text  # Повернення розшифрованого тексту

def main():
    text = """
Ще не вмерла Україна, і слава, і воля,
Ще нам, браття молодії, усміхнеться доля.
Згинуть наші вороженьки, як роса на сонці,
Запануєм і ми, браття, у своїй сторонці.
Душу, тіло ми положим за нашу свободу.
І покажем, що ми, браття, козацького роду. """

    key = input("Введіть ключ для шифрування методом Віженера: ")  # Запит на введення ключа

    encrypted_text = vigenere_cipher(text, key)  # Зашифрування тексту
    print("Зашифрований текст:", encrypted_text, "\n")  # Виведення зашифрованого тексту

    decrypted_text = vigenere_decrypt(encrypted_text, key)  # Розшифрування тексту
    print("Розшифрований текст:", decrypted_text)  # Виведення розшифрованого тексту

if __name__ == "__main__":
    main()
