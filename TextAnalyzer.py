
# Class definition:
class TextAnalyzer(object):
    
    def __init__ (self, text):
        self.fmtText = text.lower().replace('.','').replace('!','').replace('?','').replace(',','')
        
    def freqAll(self):        
        # split text into words
        wordList = self.fmtText.split()
        # Create dictionary
        myDict = {}
        for word in set(wordList): 
            myDict[word] = wordList.count(word)
        return(myDict)

# Example how the class can be used: 
myAnal = TextAnalyzer("One two one oNe tWo thREE")
print(list(myAnal.freqAll().items()))
