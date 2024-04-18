UKRAINIAN_ALPHABET_LOWER = 'абвгґдеєжзиіїйклмнопрстуфхцчшщьюя'  # Український алфавіт у нижньому регістрі
UKRAINIAN_ALPHABET_UPPER = UKRAINIAN_ALPHABET_LOWER.upper()  # Український алфавіт у верхньому регістрі

def caesar_cipher(text, shift):
    """
    Шифрування методом Цезаря.

    Args:
        text (str): Текст, який треба зашифрувати.
        shift (int): Зсув для шифрування.

    Returns:
        str: Зашифрований текст.
    """
    encrypted_text = ""  # Ініціалізація змінної для зберігання зашифрованого тексту
    for char in text:  # Ітерація по кожному символу у тексті
        if char in UKRAINIAN_ALPHABET_LOWER:  # Перевірка чи символ є українською буквою у нижньому регістрі
            encrypted_text += UKRAINIAN_ALPHABET_LOWER[(UKRAINIAN_ALPHABET_LOWER.index(char) + shift) % len(UKRAINIAN_ALPHABET_LOWER)]  # Додавання зашифрованого символу до результату
        elif char in UKRAINIAN_ALPHABET_UPPER:  # Перевірка чи символ є українською буквою у верхньому регістрі
            encrypted_text += UKRAINIAN_ALPHABET_UPPER[(UKRAINIAN_ALPHABET_UPPER.index(char) + shift) % len(UKRAINIAN_ALPHABET_UPPER)]  # Додавання зашифрованого символу до результату
        else:  # У випадку, якщо символ не є українською літерою
            encrypted_text += char  # Додавання символу до результату без змін
    return encrypted_text  # Повернення зашифрованого тексту

def decrypt_caesar(text, shift):
    """
    Розшифрування методом Цезаря.

    Args:
        text (str): Зашифрований текст.
        shift (int): Зсув для розшифрування.

    Returns:
        str: Розшифрований текст.
    """
    return caesar_cipher(text, -shift)  # Виклик функції шифрування з від'ємним зсувом для отримання розшифрованого тексту

def main():
    text = """
Ще не вмерла Україна, і слава, і воля,
Ще нам, браття молодії, усміхнеться доля.
Згинуть наші вороженьки, як роса на сонці,
Запануєм і ми, браття, у своїй сторонці.
Душу, тіло ми положим за нашу свободу.
І покажем, що ми, браття, козацького роду. """

    shift = int(input("Введіть зсув для шифрування методом Цезаря (ціле число): "))  # Запит на введення зсуву

    encrypted_text = caesar_cipher(text, shift)  # Зашифрування тексту
    print("Зашифрований текст:", encrypted_text, "\n")  # Виведення зашифрованого тексту

    decrypted_text = decrypt_caesar(encrypted_text, shift)  # Розшифрування тексту
    print("Розшифрований текст:", decrypted_text)  # Виведення розшифрованого тексту

if __name__ == "__main__":
    main()
