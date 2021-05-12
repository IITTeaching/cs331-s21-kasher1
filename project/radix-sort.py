import urllib
import requests

def book_to_words(book_url='https://www.gutenberg.org/files/84/84-0.txt'):
    booktxt = urllib.request.urlopen(book_url).read().decode()
    bookascii = booktxt.encode('ascii','replace')
    return bookascii.split()

def radix_a_book(book_url='https://www.gutenberg.org/files/84/84-0.txt'):
    byteWords = book_to_words(book_url)
    #Only does the first 100 words of the book
    byteWords = byteWords[0:100]
    max = 0
    for i in range(1,len(byteWords)):
      if(len(byteWords[i])>len(byteWords[max])):
        max = i
    print(byteWords[max])
    numIter = len(byteWords[max])

    return sort(byteWords,numIter)
def sort(inputs, numIter):
  for y in range(numIter-1,-1,-1):
    print(y)
    counts = [0]*128
    for x in inputs:
      try:  
        counts[x[y]]+=1
      except:
        counts[0]+=1
        
    for i in range(1,len(counts)):
      counts[i] += counts[i-1]
    
    output = [None] * len(inputs)
    for i in inputs[::-1]:
      try:
        t = i[y]
      except:
        t = 0
      idx = counts[t]-1
      while output[idx]!=None:
        idx-=1
      output[idx] = i
    inputs = output
  return inputs

print(radix_a_book())
