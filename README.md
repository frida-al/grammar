# Evidence 2.
# Generating and Cleaning a Restricted Context Free Grammar
# Frida Alexia Arcadia Luna A01711615
---
# Context & Description
Grammars are 'a set of instructions about how to write statements that are valid for a programming language' (Grandinetti, 2019). This set of instructions are rules that dictate the order of characters and words in senteneces so that these will be valid.

For this evidence, I will develop a context-free grammar based on the German language, specifically, the basic sentence structure in German. This structure uses the first slot of the phrase for the subject, the second for the verb and the third for a complement. It is important to understand that the first two slots can never have antything else on them, at least for a basic phrase.

For the main sentence, I will be handling the structure S -> Sub V Comp, that stands for Sub = subjetc, V = verb and Comp = complement. The complemente will generate most of the complexity of this grammar, given that is the only non-terminal in the main sentence. 
Here are the words translations I will be working with:

## Subjects

| German | English |
|--------|---------|
| Ich | I |
| Du | you (informal) |
| Sie | you (formal) |
| Er | he |

## Verbs

| German | English |
|--------|---------|
| gehe | go |
| will | will |
| kann | can |
| läuft | run |
| fahren | drive |
| kaufst | buy |
| esse | eat |
| zeigt | show |

## Articles

| German | English |
|--------|---------|
| dem | the (undergoing declension) |
| der | the (undergoing declension) |
| das | the |
| einem | a (undergoing declension) |
| einer | a (undergoing declension) |
| einen | a (undergoing declension) |
| ein | a |

<mark>In English, we cannot see the difference between some of the articles, because in German, they take different forms depending on the declension. It also chenges with tha fact that German has a third gender, which is the neutral gender.</mark>

## Prepositions

| German | English |
|--------|---------|
| an | on |
| zu | to |
| um | to |
| in | in |
| mit | with |
| nach | to |

## Nouns 

| German | English |
|--------|---------|
| Samstag | saturday |
| Bruder | brother |
| Strand | beach |
| Schule | school |
| 6 Uhr | Six o clock |
| Deutschland | Germany |
| Freitag | Friday |
| Mutter | Mother |
| Supermarkt | supermarket |
| Frau | woman |
| Apfel | apple |
| Buch | book |
| Brot | bread |
| Kino | cinema |

<mark>In German, all of the nouns are written with capital letter, however, to avoid certain mistakes, I will handle the grammar in lowercase.</mark>

## Time adverbs 

| German | English |
|--------|---------|
| heute | today |
| morgen | tomorrow |
| morgens | in the mornings |

## Possessive Pronouns

| German | English |
|--------|---------|
| meinem | my |
| deiner | your | 
| deinem | your (undergoing declension) |

## Conjunction

| German | English |
|--------|---------|
| und | and |
| oder | or |

---

# Grammar

When designing a compiler, we first need to understand the lexical analysis, which was presented on the previous evidence, and then to understand the syntax analysis of the language. For that, we will need parsing trees, specifically, the LL(1), that does not support ambiguity nor left recursion.

### Initial grammar

The following is the ambiguos and with left recursion grammar that recognizes the language:

>   S -> Sub V Comp
> 
>  Comp -> Comp Conj Comp | PrepPhrase | M | T
>
>  PrepPhrase -> Contrac Noun | Pre A Noun | Pre PP Noun
> 
> M -> A Noun
> 
>  T -> AT | PrepPhrase | Noun Conj Noun
> 
>  A -> AD | AI
> 
>  Sub -> 'ich' | 'du' | 'sie' | 'er'
> 
>  V -> 'gehe' | 'will' | 'kann' | 'läuft' | 'fahren' | 'kaufst' | 'zeigt' | 'esse'
>
> AD -> 'dem' | 'der' | 'das'
>
> AI -> 'einem' | 'einer' | 'einen' | 'ein'
>
> Pre -> 'an' | 'zu' | 'um' | 'in' | 'mit' | 'nach'
>
> Noun -> 'samstag' | 'bruder' | 'strand' | 'schule' | '6 uhr' | 'deutschland' | 'freitag' | 'mutter' | 'supermarkt' | 'frau' | 'apfel' | 'buch' | 'brot' | 'kino'
>
> AT -> 'heute' | 'morgen' | 'morgens'
>
> PP -> 'meinem' | 'deiner' | 'deinem'
>
> Conj -> 'und' | 'oder'
>
> Contrac -> 'zum' | 'zur'

We can observe that this grammar isn't fit for an LL(1) parser, given that its ambiguity leads to generating more that one tree per phrase, as we can see in the following examples.

![image](https://github.com/user-attachments/assets/ee62caa6-b5f0-4606-8a82-3de10a6319ba)
![image](https://github.com/user-attachments/assets/2a46a3e0-3d4d-4c38-a088-1837d7a98eac)

In this case, we are trying to parse the phrase `Ich gehe zum strand und zum kino`, and we can observe that it generates four different trees, because a prepPhrase can be reached in several ways. 

We can also aprreciate this with the following example:

![image](https://github.com/user-attachments/assets/c07a792c-a89f-49ae-9430-2c91574c7be8)


In this case, we are trying to parse the phrase `sie läuft mit der mutter oder mit dem bruder`.


For the grammar to be an LL(1) parser, I need to eliminate ambiguity.


### Eiminate ambiguity

To eliminate ambiguity, a new non-terminal, to aid in differentiating the Comp -> T -> PrepPhrase -> Contrac Noun | Pre A Noun | Pre PP Noun path from the Comp -> PrepPhrase -> Contrac Noun | Pre A Noun | Pre PP Noun path. This new terminal allows Comp -> T -> PrepPhrase to go only to Pre A Noun | Pre PP Noun, while the newly introduced non-terminal allows Contrac Noun. 
I also added another intermediate non-terminal in Comp, to remove another ambiguos rule.

The following is the new grammar once I removed ambiguity.

> S -> Sub V Comp
> 
>  Comp -> Comp Conj CompP | CompP
>
>  CompP ->  PrepPhrase2 | M | T
> 
>  PrepPhrase -> Pre A Noun | Pre PP Noun
> 
>  M -> A Noun
> 
>  T -> AT | PrepPhrase | Noun Conj Noun
> 
>  PrepPhrase2 -> Contrac Noun
> 
>  A -> AD | AI
> 
>  Sub -> 'ich' | 'du' | 'sie' | 'er'
> 
>  V -> 'gehe' | 'will' | 'kann' | 'läuft' | 'fahren' | 'kaufst' | 'zeigt' | 'esse'
> 
>  AD -> 'dem' | 'der' | 'das'
> 
>  AI -> 'einem' | 'einer' | 'einen' | 'ein'
> 
>  Pre -> 'an' | 'zu' | 'um' | 'in' | 'mit' | 'nach'
> 
>  Noun -> 'samstag' | 'bruder' | 'strand' | 'schule' | '6 uhr' | 'deutschland' | 'freitag' | 'mutter' | 'supermarkt' | 'frau' | 'apfel' | 'buch' | 'brot' | 'kino'
> 
>  AT -> 'heute' | 'morgen' | 'morgens'
> 
>  PP -> 'meinem' | 'deiner' | 'deinem'
> 
>  Conj -> 'und' | 'oder'
> 
>  Contrac -> 'zum' | 'zur'

### Eiminate left recursion

We can find left recursion in the second line of the grammar, so I will add another intermidiate non-terminal, that will be named Comp_A, and will eliminate recursion on the left side of Comp, changing it instead to right recursion on the auxiliar.

This is the resulting grammar (clean grammar)

>  S -> Sub V Comp
> 
>  Comp -> CompP Comp_A
> 
>  Comp_A -> Conj CompP Comp_A | Empty
> 
>  CompP ->  PrepPhrase2 | M | T
> 
>  PrepPhrase -> Pre A Noun | Pre PP Noun
> 
>  M -> A Noun
> 
>  T -> AT | PrepPhrase | Noun Conj Noun
> 
>  PrepPhrase2 -> Contrac Noun
> 
>  A -> AD | AI
> 
>  Sub -> 'ich' | 'du' | 'sie' | 'er'
> 
>  V -> 'gehe' | 'will' | 'kann' | 'läuft' | 'fahren' | 'kaufst' | 'zeigt' | 'esse'
> 
>  AD -> 'dem' | 'der' | 'das'
> 
>  AI -> 'einem' | 'einer' | 'einen' | 'ein'
> 
>  Pre -> 'an' | 'zu' | 'um' | 'in' | 'mit' | 'nach'
> 
>  Noun -> 'samstag' | 'bruder' | 'strand' | 'schule' | '6 uhr' | 'deutschland' | 'freitag' | 'mutter' | 'supermarkt' | 'frau' | 'apfel' | 'buch' | 'brot' | 'kino'
> 
>  AT -> 'heute' | 'morgen' | 'morgens'
> 
>  PP -> 'meinem' | 'deiner' | 'deinem'
> 
>  Conj -> 'und' | 'oder'
> 
>  Contrac -> 'zum' | 'zur'
> 
>  Empty ->

---

### Final grammar

The final version of the grammar that no longer has ambiguity nor left recursion will be implemented in Python, with the help of the nltk library. Inside this library, exists the CFG class, which stands for Context Free Grammar, that is just what I need. This implementation has 8 examples of phrases that are accepted by the grammar once it is clean, and 7 phrases that aren´t fit for it. 

`Correct phrases`
- ich gehe zum strand und zum kino
- du kaufst einen apfel oder ein brot
- ich esse freitag oder samstag
- er läuft morgens
- sie fahren zur schule und zum supermarkt
- sie läuft mit der mutter oder mit dem bruder
- ich gehe zum strand und zum kino und zum supermarkt
- sie zeigt dem apfel

`Incorrect phrases`
- ich gehe und
- du kann strand
- ich esse und der strand
- ich esse zum strand mit meinem mutter
- einem frau esse
- du will läuft
- ein bruder gehe ein supermarkt

The command to run this program is 'python grammar.py', and these are the following outputs,generated for both the correct and incorrect answers.

![image](https://github.com/user-attachments/assets/e372c205-5aae-4040-b217-b8cf6eced7c2)

![image](https://github.com/user-attachments/assets/5b477364-8f4c-4970-b1f7-5c7e0b0103d8)

![image](https://github.com/user-attachments/assets/6edc003a-4f16-4e33-bec9-36de5cf0b781)

![image](https://github.com/user-attachments/assets/106cd99f-aa09-4a24-9f59-693691c8ac40)





---
## Chomsky Hierarchy
Professor Noam Chomsky is an American professor and public intellectual known for his work in linguistics, political activism, and social criticism. He is also know as "the father of modern linguistics". Even if in the beginning his work was mainly focused on the analysis of languages, it is now relevant to computer science, since it helps analyze programming languages and understand more complex languages. 
The Chomsky Hierarchy states that the Type 3 grammars are restricted and not so powerful, while Type 0 grammars are completly unrestricted and can be recognized by a Turing Machine.
The grammar I have worked on for this evidence is catalogued as a Context-Free grammar, or Type 2 according to the Chomsky Hierarchy. This, on one hand, is because I have eliminated non-terminals on the left side of the grammar. On the other hand, given that the grammar has both terminals and non terminas on its right side, it can´t classify as a Type 0 grammar, a regular grammar.

---
## References

Grandinetti, P. (2019, september 30). *What is a programming language grammar?*. Compilers. https://pgrandinetti.github.io/compilers/page/what-is-a-programming-language-grammar/ 

Schoen, K., PhD. (2024, 1 october). What Are the Rules for German Sentence Structure? Duolingo Blog. https://blog.duolingo.com/german-sentence-structure/

Premios Fundación BBVA Fronteras del Conocimiento. (s. f.). Entrevista con Noam Chomsky, Premio Fronteras del Conocimiento en Humanidades [Vídeo]. Premios Fronteras. https://www.premiosfronterasdelconocimiento.es/galardonados/noam-chomsky/
