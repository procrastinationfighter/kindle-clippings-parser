import sys


def main():
    if len(sys.argv) < 3:
        print("Correct usage: \npython " + sys.argv[0] + " <input file name> <output file name>")
        exit(1)

    file = open(sys.argv[1], "r")
    result: dict[str, list[str]] = dict()

    while True:
        title = file.readline().rstrip('\n')
        if not title:
            break

        next(file)
        next(file)
        highlight = file.readline().rstrip('\n')
        next(file)

        if title not in result:
            result[title] = []
        result[title].append(highlight)

    file.close()
    file = open(sys.argv[2], "w")

    for title, highlights in result.items():
        file.write(title + "\n")
        file.write(', '.join(map(lambda s : "'" + s + "'", highlights)) + "\n")
        file.write("=========\n")

    file.close()


main()
