from collections import deque

def open_files(rootword):
    path_1 = "adrian_links/nicknames.txt"
    path_2 = "adrian_links/links.txt"
    pages = []
    rootid = -1
    with open (path_1) as f_1:
        for line in f_1:
            line = line.split()
            pages.append(line[1])
            if line[1] == rootword:
                rootid = len(pages)-1
    n = len(pages)
    links = [[]for _ in range (n)]
    with open (path_2) as f_2:
        for line in f_2:
            page1, page2 = map(int,line.split())
            links[page1].append(page2)
    return pages, links, rootid

def search_links(pages, links, rootid):

    n = len(pages)
    q = deque()
    q.append(rootid)
    flags = [0 for _ in range (n)]
    flags[rootid] = 1
    depth = [0 for _ in range (n)]
    while len(q) != 0:
        wikipage = q.popleft()
        if depth[wikipage] >= 5:
            continue
        for link in links[wikipage]:
            if flags[link] == 0:
                flags[link] = 1
                depth[link] = depth[wikipage]+1
                q.append(link)
                [print("  ",end = "") for _ in range(depth[link])]
                print("|-"+pages[link])
        flags[wikipage] = 2
    return



if __name__ == "__main__" :
    
    #print("entry: ",end="")
    #input()
    print("entry: adrian")
    rootword = "adrian"
    pages, links, rootid = open_files(rootword)
    if rootid == -1:
        print("%s not found in wikipedia"%rootword)
        exit(1)
    search_links(pages, links, rootid)

