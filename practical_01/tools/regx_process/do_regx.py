import re
s='{"account": "${normal_tel}", "password": "test12345"}'
# res=re.search("(\$.{1,25})(\})",s)
# res=re.search("(\$.*?)(\})",s)
res=re.search("(\$.{1,25}?)(\})",s)
if res != None:
    print(res.group(0))
    print(res.group(1))
    print(res.group(2))
