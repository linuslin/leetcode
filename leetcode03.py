def lengthOfLongestSubstring(s):
   """
   :type s: str
   :rtype: int
   """
   print s
   count=0
   max=0
   cdist={}
   last=0
   if len(s) <=0 :
       return 0
   for i in range(len(s)):
       print count,s[i]
       if i==0:
           cdist[s[i]]=i
           count+=1
           continue
       if (s[i] in cdist):
           if count>max:
               max=count
           if s[i-1]==s[i]:
               count=1
               cdist={}
               cdist[s[i]]=i
               last=i
           else:
	       if cdist[s[i]]>last:
                   last=cdist[s[i]]
               elif cdist[s[i]]< last:
                   count+=1
                   cdist[s[i]]=i
                   print "last",last,"i",i
                   continue
               count=i-(last)
               last=cdist[s[i]]+1
               cdist[s[i]]=i
       else:
           print "aaa: ",s[i]
           cdist[s[i]]=i
           count+=1
   if count>max:
       max=count   
   return max

#def __name__ == '__main__':
assert (lengthOfLongestSubstring('abcabcbb')==3)
assert (lengthOfLongestSubstring('bbbbb')==1)
assert (lengthOfLongestSubstring('pwwkew')==3)
assert (lengthOfLongestSubstring('a')==1)
assert (lengthOfLongestSubstring('pw')==2)
assert (lengthOfLongestSubstring('abca')==3)
assert (lengthOfLongestSubstring('abcaef')==5)
assert (lengthOfLongestSubstring('aabcaef')==5)
assert (lengthOfLongestSubstring('dvdf')==3)
assert (lengthOfLongestSubstring('ckilbkd')==5)
assert (lengthOfLongestSubstring('wobgrovw')==6)
