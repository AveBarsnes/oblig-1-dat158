from collections import defaultdict

case_text = "Molta er proppfull av C-vitaminer og antioksidanter. Den inneholder også næringsstoffer som jern, kobber, mangan, sink, magnesium, kalium, kalsium og fosfat. Og vi kunne ha nevnt mer av det som leger sier er bra for kroppen din."
case_pattern = "kunne"

char_map = defaultdict(list)

def map_chars():
    for i, c in enumerate(case_pattern):
        char_map[c].append(i)

def next_char(char):
    entries = char_map[char]

    if entries:
        return max(entries)

    return -1

def boyer_moore(text, pattern):
    print("lengde av teks:", len(text))

    map_chars()

    comps = 0

    i = len(pattern) - 1

    while i < len(text):

        j = len(pattern) - 1
        k = i

        while j >= 0:
            comps += 1

            if text[k] != pattern[j]:
                break

            k -= 1
            j -= 1


        if j < 0:
            return comps

        bad_char = text[k]
        last = next_char(bad_char)

        shift = max(1, j - last)
        i += shift

    return -1

print("sammenligninger:", boyer_moore(case_text, case_pattern))