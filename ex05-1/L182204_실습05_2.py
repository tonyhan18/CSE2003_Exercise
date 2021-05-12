word = "Good words cost nothing"
string = input("찾는 단어 입력 : ")
ans = word.count(string)

print("%s 문장에서는 %s 단어가 %d 번 있습니다." % (word,string,ans))