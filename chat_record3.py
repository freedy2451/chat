#清單分割也可使用於字串上
lines = []
with open('./對話紀錄相關檔案/對話紀錄3/3.txt', 'r', encoding = 'utf-8-sig') as f:
    for line in f:
        lines.append(line.strip())
    print(lines)

for line in lines:
    s = line.split(' ')
    name = s[0][5:]
    time = s[0][:5]        
    #print(time)
    print(name)