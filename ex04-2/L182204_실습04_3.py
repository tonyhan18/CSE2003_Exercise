sample = "abcABCdEFaBCDeFAbC"
a = sample.lower()

fa = "abc"
fb = "def"

fa_find = a.find(fa)
fa_cnt = a.count(fa)
fb_find = a.find(fb)
fb_cnt = a.count(fb)

print("\"%s 문자열 : %d 인덱스, %d 번 존재\"" %(fa, fa_find, fa_cnt))
print("\"%s 문자열 : %d 인덱스, %d 번 존재\"" %(fb, fb_find, fb_cnt))