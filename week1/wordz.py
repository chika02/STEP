# wordz.py
# usage: wordz.py 
#       a 1 1
#       b 2 2
#       <alphabet> <count> <points>
#       ...

import sys
import bisect

def make_table():
    alphabet = [chr(ord('a')+i) for i in range(26)]
    table = {key: 0 for key in alphabet}
    return table

def count_points(lines):
    count = make_table()
    point = make_table()
    for i in range (len(lines)):
        l = lines[i].split()
        count[l[0]] = int(l[1])
        point[l[0]] = int(l[2])
    return count, point

def open_dictionary():
    with open('dictionary.words.txt') as f:
        dic = [s.strip() for s in f.readlines()]
    return dic

def count_alphabet(word):
    count_table = make_table()
    for i in range (len(word)):
        count_table[word[i].lower()] += 1 
    return count_table

def count_dictionary(dic):
    counted_dic = [[count_alphabet(s),s] for s in dic]
    return counted_dic

def is_included(count,word_struct):
    word_dic = word_struct[0]
    word = word_struct[1].lower()
    for i in range (len(word)):
        a = word[i]
        if word_dic[a] > count[a]:
            return False
    return True

def calc_score(point,word_struct):
    word = word_struct[1].lower()
    score = 0
    for i in range (len(word)):
        score += point[word[i]]
    return score

def find_word(count, point, counted_dic):
    max_score = 0
    max_index = -1
    for i in range (len(counted_dic)):
        word_struct = counted_dic[i]
        if is_included(count, word_struct):
            score = calc_score(point,word_struct)
            if score > max_score:
                max_score = score
                max_index = i
    if max_index == -1:
        return "no word found"
    else:
        return counted_dic[max_index][1]

def main(lines):

    count, point = count_points(lines)
    dic = open_dictionary()
    counted_dic = count_dictionary(dic)
    ans = find_word(count, point, counted_dic)
    print (ans)

    return 0

if __name__ == "__main__":

    lines = []
    for l in sys.stdin:
        lines.append(l.rstrip('\n'))  #ctrl+D で入力終了

    main(lines)





