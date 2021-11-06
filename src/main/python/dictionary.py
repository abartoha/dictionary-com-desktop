from json import load
from difflib import get_close_matches
# testing where is the root
# open("test.txt","w+").close()

data = load(open('dictionary.json'))

def get_word(word:str):
    for i in data:
        if i['word'].lower() == word.lower():
            return i
    return "N\A"

def close_matches(word:str):
    words = [i['word'] for i in data]
    return (get_close_matches(word, words))
    # pass

# word = "Cheese"
# while word:
#     print('\n')
#     word = input("Please Enter your query word: ")
#     print('\n')
#     if word:
#         for i in data:
#             if i['word'].lower() == word.lower():
#                 x = 1
#                 for j in i['results']:
#                     print(f"{x}\t{j['pos']}")
#                     x += 1
#                     y = 1
#                     print('\n')
#                     for k in j['defs']:
#                         print(f"\t{y}\t{k}")
#                         y += 1
#                     print('\n')


if __name__=="__main__":
    from pprint import pprint
    pprint(close_matches(input("Enter Word:\t")))
