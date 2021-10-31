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

def occurrences(args):
    validate_arg_count(args, 2)
    word = args[1]
    full_text = " ".join(
        [d for d in [l for a, s, l, c in DISCOGRAPHY]]
    ).lower()
    count = full_text.count(word.lower())
    return count

def occurrences_verbose(args):
    validate_arg_count(args, 2)
    word = args[1]
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

def order_songs_by_word_count(args):
    validate_arg_count(args, 2)
    order = args[1]
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

def rando_song(args):
    validate_arg_count(args, 1)
    return "Not implemented yet!"

def validate_arg_count(args, expected) :
    if len(args) != expected :
        print(sys.argv)
        print("Wrong number of arguments specified")
        sys.exit(1)

def main():
    sys.argv = sys.argv[1:]
    load()
    vtable = { "heh"    : occurrences,
               "HEH!"   : occurrences_verbose,
               "huh"    : rando_song,
               "vision" : order_songs_by_word_count } 


    print(vtable[sys.argv[0]](sys.argv))
    if sys.argv[0] not in ["heh","HEH!","huh","vision"]:
        print("Unrecognized command: '" + sys.argv[0] + "'")
        sys.exit(1)

if __name__ == "__main__":
    main()
    
