class Solution:
    def countWords(self, words1: list[str], words2: list[str]) -> int:
        '''count=0
        for word in words1:
            if words1.count(word)==1 and words2.count(word)==1:
                count+=1
        return count'''
        '''d1={}
        for word in words1:
            if word in d1:
                d1[word]+=1
            else:
                d1[word]=1
        d2={}
        for word in words2:
            if word in d2:
                d2[word]+=1
            else:
                d2[word]=1
        count=0
        for word in words1:
            if word in words2:
                if d1[word]==1 and d2[word]==1:
                    count+=1
        return count'''
        d={}
        for word in words1:
            if word in d:
                d[word]+=1
            else:
                d[word]=1
        count=0
        for k,v in d.items():
            if v==1 and words2.count(k)==1:
                count+=1
        return count