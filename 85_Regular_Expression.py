import re

pattern = "[A-Z]+ ang"
text = '''Para ilmuwan Yunani kuno memberikan kontribusi yang amat besar dalam perkembangan astronomi. Mereka berhasil menghitung keliling bumi, memahami bahwa bulan mengitari bumi, dan memperkirakan jarak bulan dari bumi. Beberapa astronom Yunani yang terkenal adalah Thales, yang menemukan bahwa bumi itu bulat, Anaxagoras, yang menemukan penyebab gerhana, dan Aristarkhos, yang menemukan bahwa bumi mengelilingi matahari. ('''

match = re.search(pattern, text)
print(match) 

""" matches  = re.finditer(pattern, text)
for match in matches:
    print(match)
    #print(match.span())
    #print(type(match.span()))
    #print(match.span()[0])
    print(text[match.span()[0]:match.span()[1]]) """