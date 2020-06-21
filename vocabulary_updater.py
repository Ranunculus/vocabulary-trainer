import ielts_word_list_parser as ielts
import abbyy_lingvo_translator as translator
import database_operations as database

def process_data(data):
    words = ielts.extract_words(data)
    translations = translator.get_word_data(words)
    print(translations)
    database.create_new_words(translations)

if __name__ == "__main__":
    database.init_database()

    data = ielts.extract_data()
    process_data(data)
    links = ielts.extract_links(data)
    for link in links:
        print(link)
        process_data(ielts.extract_data(link))


