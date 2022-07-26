import requests
import urllib
from pypinyin import lazy_pinyin
import romajitable

#四国めたん: 2064
#ずんだもん: 3175
#春日部つむぎ：8
#もち子さん： 20
#雨晴はう： 10
#冥鳴ひまり：14

speaker=3
speed=1
tmp = """
给阿姨倒杯茶好吧，给阿姨倒一杯茶。

阿姨给你倒一杯卡布奇诺。

开始你的炸弹秀！

炸他炸他，漂亮！

十七张牌你能秒我，你能秒杀我？

你今天要是十七张牌把我秒了, 我卢本伟当场，把这个电脑屏幕吃掉！
""".strip()

def pinyin2kana(s):
    pinyin = lazy_pinyin(s)
    # print(pinyin)
    o=""
    for i in pinyin:
        if i.isalpha():
            # if i[:3] == 'shi': i = "shy" + i[3:]
            if i[:2]=='di' : i = "dei"+i[2:]
            if i[:2]=='qi' : i = "ti"+i[2:]
            if 'xu' in i : i = i.replace('xu','shu')
            if 've' in i : i = i.replace('ve','yu')
            if 'ie' in i : i = i.replace('ie','ye')
            if 'ia' in i : i = i.replace('ia','ya')
            if 'io' in i : i = i.replace('io','yo')
            if 'iu' in i : i = i.replace('iu','yu')
            if 'ui' in i : i = i.replace('ui','uei')
            if 'ao' in i : i = i.replace('ao','o')
            if 're' in i : i = i.replace('re','ye')
            if 'er' in i : i = i.replace('er','a')

            if i[-1]=='g': i = i[:-1]
            if i[-1]=='e': i = i[:-1]+'a'
            if i[0]=='c' and i[:2]!='ch': i = "ts"+i[1:]

            # if i[:2]=='xi' : i = "shy"+i[2:]
            if i[0] == 'x': i = "s" + i[1:]
            if i[0]=='q' : i = "ch"+i[1:]
            if i[:2]=='zh' : i = "j"+i[2:]

            if i[-1] in "aoiuv" and len(i)>1 and i[-2] not in 'aoeiuv' : i += i[-1]
            if 'v' in i : i = i.replace('v','yu')

            kana = romajitable.to_kana(i).hiragana
            o+=kana
        else:
            o+=i
    print(o)
    return o

tmp = pinyin2kana(tmp)
txt = urllib.parse.quote(tmp, safe='/', encoding=None, errors=None)

vve_read =  "localhost:50021/read"


requests.post(f"{vve_read}?speaker={speaker}&speed={speed}&text={txt}").content
