class Solution:
    def sortSentence(self, s: str) -> str:
        words = s.rsplit()
        word_dic = {}
        sentence = ''
        for word in words:
            idx = int(word[-1])
            word_dic.update({idx:word[:-1]})
        for x in range(len(word_dic)):
            sentence += word_dic.get(x+1) + ' '
        return sentence[:-1]