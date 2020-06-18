def open_files(words):
    path_1 = "wikipedia_links/pages.txt"
    path_2 = "wikipedia_links/links.txt"
    pages = []
    rootid = -1
    with open (path_1) as f_1:
        for line in f_1:
            line = line.split()
            pages.append(line[1])
            if line[1] == words['root']:
                rootid = len(pages)-1
    n = len(pages)
    links = [[]for _ in range (n)]
    with open (path_2) as f_2:
        for line in f_2:
            page1, page2 = map(int,line.split())
            links[page1].append(page2)
    return pages, links, rootid

def search_links(pages, links, rootid, words, max_depth):

    path = f"{words['root']}_{words['suffix']}.txt"
    f = open(path, mode='w')
    n = len(pages)
    stack = [rootid]
    flags = [0 for _ in range (n)]
    flags[rootid] = 1
    depth = [-1 for _ in range (n)]
    depth[rootid] = 0
    f.write("|-%s (%d)\n"%(pages[rootid],rootid))
    while len(stack) != 0:
        parent = stack.pop()
        if depth[parent] >= max_depth:
            continue
        for child in links[parent]:
            if flags[child] == 0:
                flags[child] = 1
                condition_1 = True
                condition_2 = True
                if len(words['suffix']) != 0:
                    condition_1 = pages[child].endswith(words['suffix'])
                if len(words['exclude_suffix']) != 0:
                    condition_2 = not pages[child].endswith(words['exclude_suffix'])
                if condition_1 and condition_2:
                    depth[child] = depth[parent]+1
                    stack.append(child)
                    [f.write("  ") for _ in range(depth[child])]
                    f.write("|-%s (%d)\n"%(pages[child],child))
        flags[parent] = 2
    return



if __name__ == "__main__" :
    
    words = {}
    print("enter the following;  root - the page you start search from;  suffix - searches only pages with the suffix;  exclude_suffix - searches only pages without the suffix")
    print("root:",end="")
    words['root'] = input().strip()
    print("suffix:",end="")
    words['suffix'] = input().strip()
    print("exclude_suffix:",end="")
    words['exclude_suffix'] = input().strip()
    print("max_depth:",end="")
    max_depth = int(input().strip())
    if max_depth > 10:
        print("max_depth should be below 10")
        exit(1)

    pages, links, rootid = open_files(words)
    if rootid == -1:
        print("%s not found in wikipedia"%words['root'])
        exit(1)
    search_links(pages, links, rootid, words, max_depth)

