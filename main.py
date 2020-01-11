from helloworld import Nlp

if __name__ == '__main__':
    # init class with english or french language
    # 'fr' or 'en'
    nlp = Nlp(lang='en')

    if nlp.lang == 'fr':
        print(nlp.french('Bonjour, je suis un chaton'))
        print(nlp.get_index("Chaton très mignon !"))
        print(nlp.get_slice("Chaton très mignon !", 1, 4))
    else:
        print(nlp.english('Hi ! Im Abd'))
        print(nlp.get_index("Cute Kitten !"))
        print(nlp.get_slice("Cute Kitten !", 1, 4))
        print(nlp.attributes("I am a doggy !"))
        print(nlp.check_percentages('There is 90% of population that...'))
