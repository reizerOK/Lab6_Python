import urllib.parse
import pyperclip

def decode_url():
    encoded_url = "https://uk.wikipedia.org/wiki/%D0%A8%D1%82%D1%83%D1%87%D0%BD%D0%B8%D0%B9_%D1%96%D0%BD%D1%82%D0%B5%D0%BB%D0%B5%D0%BA%D1%82"

    decoded_url = urllib.parse.unquote(encoded_url)
    
    print("Закодоване посилання:")
    print(encoded_url)
    print("\nРозкодоване посилання:")
    print(decoded_url)

    try:
        pyperclip.copy(decoded_url)
        print("\nРозкодоване посилання скопійовано до буфера обміну")
    except pyperclip.PyperclipException as e:
        print(f"\nНе вдалося скопіювати до буфера обміну: {e}")

if __name__ == "__main__":
    decode_url()
