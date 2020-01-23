from googlesearch import search
import requests


# def google_search_for_web_sites(query, list_of_words):
#     for web_page in search(query, tld="com", lang='en', num=100, stop=100, pause=2):
#         try:
#             score = []
#             r = requests.get(web_page).text.lower()
#             for word in list_of_words:
#                 list_of_examples = case_generator(word)
#                 count = 0
#                 for example in list_of_examples:
#                     count = r.count(example) + count
#                 score.append(word)
#                 score.append(count)
#             print('{},{}'.format(web_page, score))
#         except:
#             print('Error: ' + web_page)


def google_search_for_web_sites(query, list_of_words):
    possitive = 0
    for web_page in search(query, tld="com", lang='en', num=100, stop=100, pause=2):
        try:
            score = []
            r = requests.get(web_page).text.lower()
            for word in list_of_words:
                list_of_examples = case_generator(word)
                count = 0
                for example in list_of_examples:
                    count = r.count(example) + count
                score.append(count)
            if sum(score) != 0:
                print('{}: True'.format(web_page, score))
                possitive = possitive+1

            else:
                print('{}: False'.format(web_page, score))
        except:
            print('Error: ' + web_page)
    print(possitive)




def generate_csv_from_list(list):
    string = ','.join(str(emelent) for emelent in list)
    return string



def case_generator(the_word):
    list_of_examples = []
    spaces = ' ' + the_word + ' '
    dot = ' ' + the_word + '.'
    comma = ' ' + the_word + ','
    bracelet1 = '(' + the_word + ' '
    bracelet2 = ' ' + the_word + ')'
    list_of_examples.append(spaces)
    list_of_examples.append(dot)
    list_of_examples.append(comma)
    list_of_examples.append(bracelet1)
    list_of_examples.append(bracelet2)
    return list_of_examples

def main():
    list = ['war','ii word war','cyclone','vietnam','agent orange']
    google_search_for_web_sites('monsanto', list)



if __name__ == '__main__':
    main()
