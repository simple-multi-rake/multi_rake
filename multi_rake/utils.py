try:
    import cld2
    CLD2_INSTALLED = True
except ImportError:
    print("CLD2 is not installed. Language detection won't work.")
    CLD2_INSTALLED = False

import regex

LETTERS_RE = regex.compile(r'\p{L}+')

SENTENCE_DELIMITERS_RE = regex.compile(
    r'[\.,;:¡!¿\?…⋯‹›«»\\"“”\[\]\(\)⟨⟩}{&]'  # any punctuation sign or &
    r'|\s[-–~]+\s',  # or '-' between spaces
    regex.VERBOSE,
)


def detect_language(text, proba_threshold):
    if not CLD2_INSTALLED:
        print("CLD2 is not installed. Language detection won't work.")
        return None

    _, _, details = cld2.detect(text)

    language_code = details[0].language_code
    probability = details[0].percent

    if language_code != 'un' and probability > proba_threshold:
        return language_code


def keep_only_letters(string):
    return ' '.join(token.group() for token in LETTERS_RE.finditer(string))


def separate_words(text):
    words = []

    for word in text.split():
        if not word.isnumeric():
            words.append(word)

    return words


def split_sentences(text):
    sentences = SENTENCE_DELIMITERS_RE.split(text)
    return sentences
