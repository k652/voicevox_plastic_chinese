import requests
import urllib
from pypinyin import lazy_pinyin
import romajitable

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


#四国めたん: 2064
#ずんだもん: 3175
#春日部つむぎ：8
#もち子さん： 20
#雨晴はう： 10
#冥鳴ひまり：14

speaker=14
speed=1
tmp = """
吾尝终日而思矣，不如须臾之所学也；吾尝跂而望矣，不如登高之博见也。
登高而招，臂非加长也，而见者远；顺风而呼，声非加疾也，而闻者彰。
""".strip()

tmp = pinyin2kana(tmp)
txt = urllib.parse.quote(tmp, safe='/', encoding=None, errors=None)

vve_audio_query =  "http://127.0.0.1:50021/audio_query"
vve_read =  "http://127.0.0.1:50021/read"
vve_synthesis =  "http://127.0.0.1:50021/synthesis"
vve =  "http://127.0.0.1:50021"


requests.post(f"{vve_read}?speaker={speaker}&speed={speed}&text={txt}").content
