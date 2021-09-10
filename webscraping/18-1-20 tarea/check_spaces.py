
with open('codigos_sql.txt', 'r', encoding='utf-8') as f:
    data = f.readlines()

for index, row in enumerate(data):
  if (len(row.split("-")) != 3):
    print(index+1, row[:9])