import random as rand

class Block():

    def __init__(self,name):
        self.name = name
        self.size = 0
        self.words = []
        self.translates = []

    def get_size(self):
        return self.size

    def get_words(self):
        return self.words

    def get_translates(self):
        return self.translates

    def get_name(self):
        return self.name

    def get_random_word(self):
        if self.size != 0:
            return self.words[rand.randint(0,self.size)]
        else:
            return 'NULL'

    def add(self,word,translate):
        word = word.lower()
        translate = translate.lower()
        if word not in self.words and translate not in self.translates:
            self.words.append(word)
            self.translates.append(translate)
            self.size += 1
            return True
        else:
            return False

    def check_translate(self,word,translate):
        word = word.lower()
        translate = translate.lower()
        if translate in self.translates:
            if self.words.index(word) == self.translates.index(translate):
                return True
            else:
                return False
        else:
            return False

    def save(self):
        with  open(self.name + '.txt','w',encoding='windows-1251') as f:
             for i in range(self.size):
                 f.write(self.words[i] + ':' + self.translates[i] + '\n')

    def load(self):
        try:
            with  open(self.name + '.txt','r',encoding='windows-1251') as f:
                for line in f:
                    splited_str = line.split(':')
                    sz = len(splited_str[1])
                    splited_str[1] = splited_str[1][0:sz-1]
                    self.words.append(splited_str[0])
                    self.translates.append(splited_str[1])
        except FileNotFoundError:
            return False
        else:
            return True
