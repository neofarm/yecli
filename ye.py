#!/usr/bin/env python

import sys

DISCOGRAPHY = []

def load():
    with open('discography.txt', 'r') as f:
        for l in f.readlines():
            raw = l.split('^')
            lyrics = raw[2]
            word_count = len(lyrics.split())
            item = (raw[0], raw[1], lyrics, word_count)
            DISCOGRAPHY.append(item)

def occurrences(word):
    full_text = " ".join(
        [d for d in [l for a, s, l, c in DISCOGRAPHY]]
    ).lower()
    count = full_text.count(word.lower())
    return count

def occurrences_verbose(word):
    song_counts = [] #[album_name, song_name, count]
    album_counts = {} #{album_name: count}
    for a, s, l, c in DISCOGRAPHY:
        song_occurance = l.lower().count(word.lower())
        if song_occurance > 0:
            song_counts.append([a, s, song_occurance])
            if a in album_counts:
                album_counts[a] += song_occurance
            else: album_counts[a] = song_occurance
    return resultify_verbose_counts(song_counts, album_counts)

def order_songs_by_word_count(order):
    sort_asc = order.lower() == 'asc'
    sorted_songs = sorted(DISCOGRAPHY, key=lambda x: x[3], reverse=not sort_asc)
    return resultify_ordered_songs(sorted_songs)

def resultify_ordered_songs(sorted_songs):
    result= ""
    for a, s, l, c in sorted_songs: 
        result += "Word Count: " + str(c) + ", " + s + " (" + a + ")\n"
    return result

def resultify_verbose_counts(song_counts, album_counts):
    result = ""
    for a, c in album_counts.items():
        result += a + ": " + str(c) + "\n"
        for al, s, o in (y for y in song_counts if y[0] == a):
            result += "   " + s + ": " + str(o) + "\n"
    return result

def main():
    #if "ye.py" in sys.argv: sys.argv.remove("ye.py") #for easy debugging
    load()
    if len(sys.argv) != 3 :
        print(sys.argv)
        print("Wrong number of arguments specified")
        sys.exit(1)

    if "heh" in sys.argv[1]:
        print(occurrences(sys.argv[2]))
    elif "HEH!" in sys.argv[1]:
        print(occurrences_verbose(sys.argv[2]))
    elif "vision" in sys.argv[1]:
        print(order_songs_by_word_count(sys.argv[2]))
    else:
        print("Unrecognized command: '" + sys.argv[3] + "'")
        sys.exit(1)

if __name__ == "__main__":
    main()
    