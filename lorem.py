import sys, re, random

file = open('resource.txt', 'r')
words = file.read()
file.close()

words = re.sub(r'[^ A-Za-z]', ' ', words)
words = re.sub(r'\s+', ' ', words)
words = words.split(' ')

wordcount = 500 if len(sys.argv) == 1 else int(sys.argv[1])
lorem = ''

for i in range(wordcount):
  word = words[random.randint(0, len(words) - 1)]
  lorem += word.strip() + ' '

print(lorem)

