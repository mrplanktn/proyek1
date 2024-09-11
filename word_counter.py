import re

def count_words(text):
    words = re.findall(r'\b\w+\b', text)
    return len(words)

def count_sentences(text):
    sentences = re.split(r'[.!?]', text)
    return len([s for s in sentences if s.strip()])

def count_paragraphs(text):
    paragraphs = text.split('\n\n')
    return len([p for p in paragraphs if p.strip()])

def analyze_text(file_path):
    try:
        with open(file_path, 'r') as file:
            text = file.read()
            num_words = count_words(text)
            num_sentences = count_sentences(text)
            num_paragraphs = count_paragraphs(text)

            print(f'Jumlah Kata: {num_words}')
            print(f'Jumlah Kalimat: {num_sentences}')
            print(f'Jumlah Paragraf: {num_paragraphs}')
    except FileNotFoundError:
        print("File tidak ditemukan. Pastikan path file benar.")

if __name__ == '__main__':
    file_path = input('Masukkan path file teks: ')
    analyze_text(file_path)
