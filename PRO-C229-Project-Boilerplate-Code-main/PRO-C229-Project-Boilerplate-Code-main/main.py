import hashlib
from itertools import permutations

def find_hash(original_hash):
    word_file = "/absolute/path/to/words.txt"

    word_file = list(word_file)

    anagram = "who outlay thieves"
    words = anagram.count(' ')
    words += 1

    char_list = list(set(anagram))

    if ' ' in char_list:
        char_list.remove(' ')

    final_words = []

    for i in word_file:
        flag = False
        temp_word = i.replace('\n', '')
        temp_char = list(set(temp_word))
        for j in temp_char:
            if j not in char_list:
                flag = True
                break
        if not flag:
            final_words.append(temp_word)

    for elem in permutations(final_words, words):
        hash_elem = " ".join(elem)

        if len(hash_elem) != len(anagram):
            continue

        m = hashlib.md5()
        m.update(hash_elem.encode('utf-8'))
        word_hash = m.hexdigest()

        if word_hash == original_hash:
            return hash_elem

hash_value = '13b382e1a2f8e22535b4730d78bc8591'
answer = find_hash(hash_value)
print(f"Collision! The word corresponding to the given hash is '{answer}'")
