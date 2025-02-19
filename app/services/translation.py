from translate import Translator


def translate(text: str, from_lang: str, to_lang: str) -> str:
    translator = Translator(to_lang=to_lang, from_lang=from_lang)
    translation = translator.translate(text)
    return translation