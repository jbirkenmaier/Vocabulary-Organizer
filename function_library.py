import csv
import random
from bs4 import BeautifulSoup
import requests
import csv



def read_word_ressources(dictionary_file):
    words = []
    with open(dictionary_file, mode='r',encoding='utf-16') as file:
        # Create a CSV reader object
        csv_reader = csv.reader(file)

        for row in csv_reader:
            row=row[0].replace('"', '').strip().split('\t')
            words.append(row)

    return words

def read_learned_words(learned_file):
    past_learned_words = []
    try:
        with open(learned_file, mode='r',encoding='utf-16') as file:
            # Create a CSV reader object
            csv_reader = csv.reader(file)
            for row in csv_reader:
                #random_number = random.randint(0,len(words)-1)
                row=row[0].replace('"', '').strip().split('\t')
                past_learned_words.append(row)
    except:
        pass

    return past_learned_words

def check_if_all_voc_learned(words, past_learned_words, all_learned = True):
    for element in words:
        if (element not in past_learned_words) and (past_learned_words != []):
            all_learned = False
            break
        else:
            continue
        
        if past_learned_words == []:
            all_learned = False

        if all_learned  == True:
            print('You learned all vocabulary, congratulations!')
            input('Press ENTER to finish')
            quit()

def num_of_words():
    while True:
        num_of_random_words = input('How many words would you like to learn? ')
        try:
            eval(num_of_random_words)
            if type(eval(num_of_random_words)) == int:
                break
            else:
                print('Wrong input, please try again')
        except:
            print('Wrong input, please try again')
    return num_of_random_words

def choose_random(words, past_learned_words, num_of_random_words):
    learned_words = []
    for i in range(int(num_of_random_words)):
        while True:
            random_number = random.randint(0,len(words)-1)
            if words[random_number] in past_learned_words:
                if len(past_learned_words)==len(words):
                    write_to_learned(past_learned_words, 'learned_words.csv')
                    print('You learned all vocabulary, congratulations!')
                    input('Press ENTER to finish')
                    quit()
                continue
            else:
                print(words[random_number])
                past_learned_words.append(words[random_number])
                learned_words.append(words[random_number])
                break
    return learned_words, past_learned_words

def write_to_learned(word_list, filename):
    with open(filename, mode='w', newline ='',encoding='utf-16')  as data_file:
        csv_data_writer = csv.writer(data_file, delimiter = '\t')
        for element in word_list:
            csv_data_writer.writerow(element)

def webscrape_dictionary(word,language1, language2, typ):
    #url = f"https://tureng.com/en/{language1}-{language2}/{word}"
    url = f"https://en.wiktionary.org/wiki/{word}"

    #<span class="mw-headline" id="Turkish">Turkish</span>
    #<a href="https://en.wiktionary.org/wiki/good_morning#English" title="good morning">good morning</a>
    #<span class="mw-headline" id="Interjection">Interjection</span>
    
    print(url)
    page = requests.get(url)
    soup = BeautifulSoup(page.content, "html.parser")
    language_section = soup.find('strong', attrs={'lang':language2})
    next_ordered_list = language_section.find_next('ol')
    list_items = next_ordered_list.find_all('li')
    for item in list_items:
        hyperlink = item.find('a')
        if hyperlink:
            title = hyperlink.string

        print('translation:', title)
    #for element in ordered_lists:
    #    if element.id
        
    #print(soup)
    #interjection = soup.find_all('span', {'class':'mw-headline', 'id':'Interjection'})
    #print(interjection)


