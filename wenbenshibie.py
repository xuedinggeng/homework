#wordsfrequency.py
import jieba
txt = open("三国演义.txt","r",encoding="utf-8").read()
excludes = {"将军","却说","荆州","二人","不可","不能","如此","主公","商议",
            "如何","军士","军马","左右","引兵","次日","大喜","天下","东吴",
            "于是","今日","不敢","魏兵","陛下","一人","都督","人马","不知","汉中","只见"}
words = jieba.lcut(txt)#列表
counts = {}
for word in words:
    if len(word) == 1:
        continue
    elif word =="诸葛亮" or word == "孔明曰":
        rword = ""
    elif word =="关公" or word == "云长":
        rword = "关羽"
    elif word =="玄德" or word == "玄德曰":
        rword = "刘备"
    elif word =="孟德" or word == "丞相":
        rword = "曹操"
    else:
        rword = word
        counts[word] = counts.get(rword,0) + 1
for word in excludes:
    del counts[word]
items = list(counts.items())
items.sort(key=lambda x:x[1],reverse=True)
for i in range(10):
    word, count = items[i]
    print("{0:<10}{1:>5}".format(word,count))
    


