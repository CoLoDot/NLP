import spacy


class Nlp:
    """'Nlp' is for Natural Language Processing.
    AVAILABLE LANGUAGES : french or english"""

    def __init__(self, lang: str):
        """Nlp.__init__() constructs
        an object by loading the
        choosen language : 'fr' or 'en'"""
        if lang == 'fr':
            self.lang = spacy.load('fr_core_news_sm')
        elif lang == 'en':
            self.lang = spacy.load('en_core_web_sm')

    def french(self, sentence: str) -> []:
        """Nlp.french() takes an str obj and returns a list"""
        fr = [(word.text, word.pos_) for word in self.lang(sentence)]
        return fr

    def english(self, sentence: str) -> []:
        """Nlp.english() takes an str obj and returns a list"""
        en = [(word.text, word.pos_) for word in self.lang(sentence)]
        return en

    def get_index(self, sentence: str) -> str:
        """Nlp.get_index() takes an str obj and returns a str"""
        treat = self.lang(sentence)
        token = treat[1]
        return token.text
