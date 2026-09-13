
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
           
    def freqOf(self, word):
        # get frequency map
        word = word.lower()
        myDict = self.freqAll()
        if (word in myDict):
            return(myDict[word])
        else: 
            return 0
            
# User example:        
myAnalyzer = TextAnalyzer("One two one oNe tWo thREE")
myDict = myAnalyzer.freqAll()
myWord = "Z"
myCount = myAnalyzer.freqOf(myWord)
print(list(myAnalyzer.freqAll().items()))
print(f"\"{myWord}\" is used {myCount} times.")
