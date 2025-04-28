import nltk # import NLTK library 
from nltk import CFG # import Context Free Grammar class


# define context free grammar
grammar = CFG.fromstring(""" 
  S -> Sub V Comp
  Comp -> CompP Comp_A
  Comp_A -> Conj CompP Comp_A | Empty
  CompP ->  PrepPhrase2 | M | T
  PrepPhrase -> Pre A Noun | Pre PP Noun 
  M -> A Noun
  T -> AT | PrepPhrase | Noun Conj Noun
  PrepPhrase2 -> Contrac Noun
  A -> AD | AI
  Sub -> 'ich' | 'du' | 'sie' | 'er'
  V -> 'gehe' | 'will' | 'kann' | 'läuft' | 'fahren' | 'kaufst' | 'zeigt' | 'esse'
  AD -> 'dem' | 'der' | 'das'
  AI -> 'einem' | 'einer' | 'einen' | 'ein'
  Pre -> 'an' | 'zu' | 'um' | 'in' | 'mit' | 'nach'
  Noun -> 'samstag' | 'bruder' | 'strand' | 'schule' | '6 uhr' | 'deutschland' | 'freitag' | 'mutter' | 'supermarkt' | 'frau' | 'apfel' | 'buch' | 'brot' | 'kino'
  AT -> 'heute' | 'morgen' | 'morgens'
  PP -> 'meinem' | 'deiner' | 'deinem'
  Conj -> 'und' | 'oder'
  Contrac -> 'zum' | 'zur'
  Empty -> 

""")

parser = nltk.ChartParser(grammar)

def separate(sentence):
    return sentence.lower().split()


# sentences for the automated tests (8 correct, 7 incorrect)
sentences = [
    "ich gehe zum strand und zum kino",  
    "du kaufst einen apfel oder ein brot",
    "ich esse freitag oder samstag ",
    "er läuft morgens",
    "sie fahren zur schule und zum supermarkt", 
    "sie läuft mit der mutter oder mit dem bruder",
    "sie zeigt dem apfel",
    "ich gehe zum strand und zum kino und zum supermarkt",
    "ich gehe und",
    "du kann strand",
    "ich esse und der strand",
    "ich esse zum strand mit meinem mutter",
    "einem frau esse",
    "du will läuft",
    "ein bruder gehe ein supermarkt",
]

# cycle for each sentence contained in sentences
for sentence in sentences:
    print(f"\nAttempting to parse: {sentence}")
    tokens = separate(sentence)
    found = False
    for tree in parser.parse(tokens): # if the phrase is fit for the grammar, it will print the tree 
        tree.pretty_print()
        found = True
    if not found: # if the phrase is not fit for the grammar, it will throw this message
      print("No valid parse found")