from ielts_word_list_parser import extract_data, extract_links, extract_words
from abbyy_lingvo_translator import get_word_data
from database_operations import create_new_words, init_database


def process_data(data):
    words = extract_words(data)
    translations = get_word_data(words)
    create_new_words(translations)


if __name__ == "__main__":
    init_database()

    data = extract_data()
    process_data(data)
    links = extract_links(data)
    for link in links:
        process_data(extract_data(link))
