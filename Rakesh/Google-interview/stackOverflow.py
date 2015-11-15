
from itertools import product

def answer(document, search_terms):
    words = document.split(" ")

    search_term_positions = [
        [i for i, word in enumerate(words) if word == term]
        for term in search_terms
    ]

    print search_term_positions

    combos = [sorted(combo) for combo in product(*search_term_positions)]
    if not combos:
        return None    # Could not find all search terms
    best_combo = min(combos, key=lambda combo: combo[-1] - combo[0])

    return " ".join(words[best_combo[0] : best_combo[-1] + 1])


print answer("world there hello hello where world", ["hello", "world"])



