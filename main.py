import function_library as fl



fl.webscrape_dictionary("teşekkürler","en", "tr", 1)

dict_file = "words_ressource.csv"
learned_file = "learned_words.csv"

words = fl.read_word_ressources(dict_file)
past_learned_words = fl.read_learned_words(learned_file)

fl.check_if_all_voc_learned(words, past_learned_words)
num_of_random_words = fl.num_of_words()

(learned_words, past_learned_words)=fl.choose_random(words, past_learned_words, num_of_random_words)

fl.write_to_learned(past_learned_words,'learned_words.csv')

