from bs4 import BeautifulSoup


file = open('for_parsing.html', 'r', encoding='utf-8')
data = file.read()
file.close()

soup = BeautifulSoup(data, 'lxml')

#  С файла for_parsing.html достать все содержимое тегов “а”.
tags1 = soup.findAll('a')

print(tags1)

for tag in tags1:
    text1 = tag.text
    print(f'<a> contains: {text1}')

# С файла for_parsing.html достать все содержимое тегов “li”.
tags2 = soup.findAll('li')

print(tags2)

for tag in tags2:
    text2 = tag.text
    print(f'<li> contains: {text2}')

