import win32clipboard as w
import win32con
w.OpenClipboard()
cont = w.GetClipboardData(win32con.CF_TEXT)
w.CloseClipboard()
date = cont.decode().replace(' ', '').split('\r\n')
c = ''
date_abc =[]
for x in date:
    for x2 in x.split(':'):
        date_abc.append("'" + x2 + "'")
# print(date_abc)
for x3 in range(0, len(date_abc)-1):
    # print(x3)
    if (x3 + 1) % 2 == 0:
        c = c + date_abc[x3 + 1] + ':' + date_abc[x3] + ',\n'
print(c)

'''
from: AUTO
to: AUTO
smartresult: dict
client: fanyideskweb
salt: 15508107068122
sign: f50dbdd103436e5c7114c1233337f34b
ts: 1550810706812
bv: 617939f69fb18f112aa988d6038ae43f
doctype: json
version: 2.1
keyfrom: fanyi.web
action: FY_BY_CLICKBUTTION
typoResult: false
'''