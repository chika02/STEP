# anagram.py
# usage: ./anagram <word>

import sys
import bisect

def open_dictionary():
    with open('dictionary.words.txt') as f:
        dic = [s.strip() for s in f.readlines()]
    return dic

def sort_dictionary(dic):

    sorted_dic = [["".join(sorted(s.lower())),s] for s in dic]
    sorted_dic.sort()
    return sorted_dic

def find_anagram(word,sorted_dic):

    sorted_word = "".join(sorted(word.lower()))
    sorted_dic_slice = [a[0] for a in sorted_dic]  #[' ']を含んだ文字列になっている
    anagram_index = bisect.bisect_left(sorted_dic_slice, sorted_word)

    anagram_count=0
    while(sorted_dic_slice[anagram_index+anagram_count] == sorted_word):
        anagram_count+=1
    return anagram_count, anagram_index

def main(word):

    dic = open_dictionary()
    sorted_dic = sort_dictionary(dic)
    anagram_count, anagram_index = find_anagram(word, sorted_dic)
    if anagram_count == 0:
        print ("no anagrams found")
        return 0
    else:
        for i in range (anagram_count):
            print(sorted_dic[anagram_index+i][1])
        return 0

if __name__ == "__main__":

    args = sys.argv
    if len(args) != 2:
        print("Usage: ./anagram <word>", file=sys.stderr)
        sys.exit()

    main(args[1])





