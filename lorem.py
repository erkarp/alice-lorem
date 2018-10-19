import sys, re, random

def get_words(filename='default.txt'):
  try:
    file = open(filename, 'r')
    words = file.read()
    file.close()

    words = re.sub(r'[^ A-Za-z]', ' ', words)
    words = re.sub(r'\s+', ' ', words)
    words = words.split()

    return words
    
  except:
    print('Invalid filename\n')
    sys.exit()

def get_lorem(wordcount):
  lorem = ''
  for i in range(wordcount):
    randmax = len(words) - 1
    word = words[random.randint(0, randmax)]
    lorem += word.strip() + ' '
  return lorem 


arguments = sys.argv[1:] if len(sys.argv) > 1 else ['500']
words = get_words()
wordcount = 500

for argument in arguments:
  try:
    wordcount = int(argument)

  except:
    words = get_words(argument)

  

  print(get_lorem(wordcount) + '\n')
