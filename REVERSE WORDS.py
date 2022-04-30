class Solution:
    def solve(self, sentence):
        words=list(sentence.split())
        rs=''
        while words!=[]:
            w=words.pop()
            if len(words)==0:
                rs=rs+w
            else:
                rs=rs+w+' '
        return rs