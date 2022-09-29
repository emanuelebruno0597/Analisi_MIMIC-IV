f = open('./converter_icd-9/icd9to10dictionaryOLD.txt', 'r')
o = open('./converter_icd-9/icd9to10dictionary.txt', 'a')

lines = f.readlines()

for line in lines:
    o.write(line.replace('.', ''))


f.close()
o.close()

