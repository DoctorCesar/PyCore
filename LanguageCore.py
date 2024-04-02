from icecream import ic

class Language:
    def __init__(self, defaultLanguage:str, *otherSupportedLanguages:str) -> None:
        self.language = defaultLanguage
        self.supportedLanguages = set([defaultLanguage] + list(otherSupportedLanguages))
    
    def __call__(self, **languages):
        if not self.supportedLanguages == set(languages.keys()):
            unsupportedLanguages = list(set(languages.keys()) - self.supportedLanguages)
            unprovidedLanguages = list(set(self.supportedLanguages) - set(languages.keys()))
            raise Exception(f"All supported languages must be passed in | {unsupportedLanguages} are not supported | {unprovidedLanguages} are not provided")
        else:
            return languages[self.language]
    
    
    def selectLanguage(self, language):
        if language in self.supportedLanguages:
            self.language = language
        else:
            raise Exception("Language not supported")