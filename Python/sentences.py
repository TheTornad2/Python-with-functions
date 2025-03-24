import random


def make_sentence(quantity, tense):
    """Build and return a sentence with three words:
    a determiner, a noun, and a verb. The grammatical
    quantity of the determiner and noun will match the
    number in the quantity parameter. The grammatical
    quantity and tense of the verb will match the number
    and tense in the quantity and tense parameters.
    """
    determiner = get_determiner(quantity)
    noun = get_noun(quantity)
    verb = get_verb(quantity, tense)
    prepositional_phrase1 = get_prepositional_phrase(quantity)
    prepositional_phrase2 = get_prepositional_phrase(quantity)
    return f"{determiner} {noun} {verb} {prepositional_phrase1} {prepositional_phrase2}"


def get_determiner(quantity):
    """Return a randomly chosen determiner. A determiner is
    a word like "the", "a", "one", "some", "many".
    If quantity is 1, this function will return either "a",
    "one", or "the". Otherwise this function will return
    either "some", "many", or "the".
    Parameter
        quantity: an integer.
            If quantity is 1, this function will return a
            determiner for a single noun. Otherwise this
            function will return a determiner for a plural
            noun.
    Return: a randomly chosen determiner.
    """
    if quantity == 1:
        words = ["a", "one", "the"]
    else:
        words = ["some", "many", "the"]

    word = random.choice(words)
    return word


def get_noun(quantity):
    """Return a randomly chosen noun.
    If quantity is 1, this function will
    return one of these ten single nouns:
        "bird", "boy", "car", "cat", "child",
        "dog", "girl", "man", "rabbit", "woman"
    Otherwise, this function will return one of
    these ten plural nouns:
        "birds", "boys", "cars", "cats", "children",
        "dogs", "girls", "men", "rabbits", "women"
    Parameter
        quantity: an integer that determines if
            the returned noun is single or plural.
    Return: a randomly chosen noun.
    """
    if quantity == 1:
        words = [
            "bird",
            "boy",
            "car",
            "cat",
            "child",
            "dog",
            "girl",
            "man",
            "rabbit",
            "woman",
        ]
    else:
        words = [
            "birds",
            "boys",
            "cars",
            "cats",
            "children",
            "dogs",
            "girls",
            "men",
            "rabbits",
            "women",
        ]

    word = random.choice(words)
    return word


def get_verb(quantity, tense):
    """Return a randomly chosen verb. If tense is "past",
    this function will return one of these ten verbs:
        "drank", "ate", "grew", "laughed", "thought",
        "ran", "slept", "talked", "walked", "wrote"
    If tense is "present" and quantity is 1, this
    function will return one of these ten verbs:
        "drinks", "eats", "grows", "laughs", "thinks",
        "runs", "sleeps", "talks", "walks", "writes"
    If tense is "present" and quantity is NOT 1,
    this function will return one of these ten verbs:
        "drink", "eat", "grow", "laugh", "think",
        "run", "sleep", "talk", "walk", "write"
    If tense is "future", this function will return one of
    these ten verbs:
        "will drink", "will eat", "will grow", "will laugh",
        "will think", "will run", "will sleep", "will talk",
        "will walk", "will write"
    Parameters
        quantity: an integer that determines if the
            returned verb is single or plural.
        tense: a string that determines the verb conjugation,
            either "past", "present" or "future".
    Return: a randomly chosen verb.
    """
    if tense == "past":
        words = [
            "drank",
            "ate",
            "grew",
            "laughed",
            "thought",
            "ran",
            "slept",
            "talked",
            "walked",
            "wrote",
        ]
    elif tense == "present" and quantity == 1:
        words = [
            "drinks",
            "eats",
            "grows",
            "laughs",
            "thinks",
            "runs",
            "sleeps",
            "talks",
            "walks",
            "writes",
        ]
    elif tense == "present" and quantity != 1:
        words = [
            "drink",
            "eat",
            "grow",
            "laugh",
            "think",
            "run",
            "sleep",
            "talk",
            "walk",
            "write",
        ]
    elif tense == "future":
        words = [
            "will drink",
            "will eat",
            "will grow",
            "will laugh",
            "will think",
            "will run",
            "will sleep",
            "will talk",
            "will walk",
            "will write",
        ]
    word = random.choice(words)
    return word


def get_prepositional_phrase(quantity):
    """Return a randomly chosen prepositional phrase.
    A prepositional phrase consists of a preposition,
    a determiner, and a noun.
    Parameter
        quantity: an integer that determines if
            the returned noun is single or plural.
    Return: a randomly chosen prepositional phrase.
    """
    prepositions = [
        "about",
        "above",
        "across",
        "after",
        "along",
        "around",
        "at",
        "before",
        "behind",
        "below",
        "beyond",
        "by",
        "despite",
        "except",
        "for",
        "from",
        "in",
        "into",
        "near",
        "of",
        "off",
        "on",
        "onto",
        "out",
        "over",
        "past",
        "to",
        "under",
        "with",
        "without",
    ]
    preposition = random.choice(prepositions)
    determiner = get_determiner(quantity)
    noun = get_noun(quantity)
    return f"{preposition} {determiner} {noun}"


def get_adjective():
    """Return a randomly chosen adjective.
    Return: a randomly chosen adjective.
    """
    adjectives = [
        "quick",
        "lazy",
        "sleepy",
        "noisy",
        "hungry",
        "happy",
        "sad",
        "angry",
        "excited",
        "bored",
    ]
    return random.choice(adjectives)


def main():
    print(make_sentence(1, "past"))
    print(make_sentence(1, "present"))
    print(make_sentence(1, "future"))
    print(make_sentence(2, "past"))
    print(make_sentence(2, "present"))
    print(make_sentence(2, "future"))


if __name__ == "__main__":
    main()
