import sys

DISCOGRAPHY = []

def load():
    with open('discography.txt', 'r') as f:
        for l in f.readlines():
            raw = l.split('^')
            item = (raw[0], raw[1], raw[2])
            DISCOGRAPHY.append(item)

def occurrences(word):
    full_text = " ".join(
        [d for d in [l for a, s, l in DISCOGRAPHY]]
    ).lower()
    count = full_text.count(word.lower())
    return count

def occurrences_verbose(word):
    song_counts = [] #[album_name, song_name, count]
    album_counts = {} #{album_name: count}
    for a, s, l in DISCOGRAPHY:
        song_occurance = l.count(word.lower())
        if song_occurance > 0:
            song_counts.append([a, s, song_occurance])
            if a in album_counts:
                album_counts[a] += song_occurance
            else: album_counts[a] = song_occurance
    return resultify_verbose_counts(song_counts, album_counts)

def resultify_verbose_counts(song_counts, album_counts):
    result = ""
    for a, c in album_counts.items():
        result += a + ": " + str(c) + "\n"
        for al, s, o in (y for y in song_counts if y[0] == a):
            result += "   " + s + ": " + str(o) + "\n"
    return result

def main():
    if "main.py" in sys.argv: sys.argv.remove("main.py") #for easy debugging
    load()
    if len(sys.argv) != 3 :
        print(sys.argv)
        print("Wrong number of arguments specified")
        sys.exit(1)

    if "heh" in sys.argv[1]:
        print(occurrences(sys.argv[2]))
    elif "HEH!" in sys.argv[1]:
        print(occurrences_verbose(sys.argv[2]))
    else:
        print("Unrecognized command: '" + sys.argv[3] + "'")
        sys.exit(1)

if __name__ == "__main__":
    main()
    