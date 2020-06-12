from collections import deque

def openfiles():
    with open('nicknames.txt') as f1:
        names = {}
        for s in f1.readlines():
            id_, name = s.strip().split()
            id_ = int(id_)
            names[name]=id_
    n = len(names)
    with open('links.txt') as f2:
        follow = [ [] for _ in range (n)]
        for s in f2.readlines():
            s1, s2 = s.strip().split()
            follow[int(s1)].append(int(s2))
    return names, follow, n


def search_ways(id1, id2, follow, n):

    if id1 == id2:
        return True
    flg = ['UNDONE' for _ in range(n)]
    q = deque()
    q.append(id1)
    flg[id1] = 'DOING'
    while len(q) != 0:
        person = q.popleft()
        for sb in follow[person]:
            if flg[sb] == 'UNDONE':
                #print(sb, end = " ")
                if sb == id2:
                    return True
                else:
                    q.append(sb)
                    flg[sb] = 'DOING'
        flg[person] = 'DONE'

    return False

def main(from_name, to_name, names, follow, n):

    if from_name in names:
        id1 = names[from_name]
    else:
        print("%s does not exist" % from_name)
        return
    if to_name in names:
        id2 = names[to_name]
    else:
        print("%s does not exist" % to_name)
        return

    ans  = search_ways(id1, id2, follow, n)
    if ans == 1:
        print("%s to %s: found!" % (from_name, to_name))
    else:
        print("%s to %s: not found.." % (from_name, to_name))
    return


def runTest(names, follow, n):

    main("adrian", "judith", names, follow, n)
    main("adrian", "cynthia", names, follow, n)
    main("cynthia", "cynthia", names, follow, n)
    main("adrian", "abracadabra", names, follow, n)
    main("xxxx", "adrian", names, follow, n)


if __name__ == "__main__":

    names, follow, n = openfiles()
    runTest(names, follow, n)
    while(1):
        print("> from:", end="")
        name1 = input().strip()
        print("> to:", end="")
        name2 = input().strip()
        main(name1, name2, names, follow, n)