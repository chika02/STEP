def openfiles():
    with open('nicknames.txt') as f1:
        names = {}
        for s in f1.readlines():
            id_, name = s.strip().split()
            id_ = int(id_)
            names[name]=id_
    with open('links.txt') as f2:
        follow = [ [] for _ in range (n)]
        for s in f2.readlines():
            s1, s2 = s.strip().split()
            follow[int(s1)].append(s2)
        print(follow)
    return names, follow

def search_ways(id1,id2):

    return True

def main(from_name, to_name, names, follow):

    if from_name in names:
        id1 = names[from_name]
    else:
        print("cannot find %s" % from_name)
        return
    if to_name in names:
        id2 = names[to_name]
    else:
        print("cannot find %s" % from_name)
        return

    ans  = search_ways(id1, id2)
    if ans == 1:
        print("%s to %s: found!" % (from_name, to_name))
    else:
        print("%s to %s: not found.." % (from_name, to_name))
    return


def runTest(names, follow):

    main("adrian", "judith", names, follow)
    main("adrian", "cynthia", names, follow)
    main("cynthia", "cynthia", names, follow)
    main("adrian", "abracadabra", names, follow)
    main("xxxx", "adrian", names, follow)


if __name__ == "__main__":

    names, follow = openfiles()
    runTest(names, follow)
    while(1):
        print("> from:", end="")
        name1 = input()
        print("> to:", end="")
        name2 = input()
        main(name1, name2, names, follow)