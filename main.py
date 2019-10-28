
DISCOGRAPHY = []

def load():
    with open('discography.txt', 'r') as f:
        for l in f.readlines():
            raw = l.split('^')
            item = (raw[0], raw[1], raw[2])
            DISCOGRAPHY.append(item)

def main():
    load()

main()
    