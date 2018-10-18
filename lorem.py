import sys, re, random

file = open('resource.txt', 'r')
words = file.read()
file.close()

words = re.sub(r'[^ A-Za-z]', ' ', words)
words = re.sub(r'\s+', ' ', words)
words = words.split(' ')

wordcounts = ['500'] if len(sys.argv) == 1 else sys.argv[1:]
lorem = ''

for wordcount in wordcounts:
  for i in range(int(wordcount)):
    word = words[random.randint(0, len(words) - 1)]
    lorem += word.strip() + ' '

  print(lorem + '\n')


