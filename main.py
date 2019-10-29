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
    print("'ye HEH!' is not implemented yet.")

def main():
    load()
    if len(sys.argv) != 3 :
        print("Wrong number of arguments specified")
        sys.exit(1)

    if "heh" in sys.argv[1]:
        print(occurrences(sys.argv[2]))
    elif "HEH!" in sys.argv[1]:
        occurrences_verbose(sys.argv[2])
    else:
        print("Unrecognized command: '" + sys.argv[3] + "'")
        sys.exit(1)

if __name__ == "__main__":
    main()
    