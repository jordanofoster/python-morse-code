class dictConstructor:
    def __init__(self, sourceTuple):
        self._sourceTuple = sourceTuple
        self._alnumLookupDict = self._constructDict(0,1)
        self._morseLookupDict = self._constructDict(1,0)
    
    def updateLookupDicts(self, sourceTuple):
        self.__init__(sourceTuple)

    def _constructDict(self, key, value):
        constructedDict = {}
        for element in self._sourceTuple:
            constructedDict.update({self._sourceTuple[self._sourceTuple.index(element)][key]:self._sourceTuple[self._sourceTuple.index(element)][value]})
        return constructedDict
    
    def alnumLookup(self, morseStr):
        return self._alnumLookupDict.get(morseStr)
    
    def morseLookup(self, morseStr):
        return self._morseLookupDict.get(morseStr)
    
#    def constructAlnumLookupDict(self): # Make a dictionary with alnumeric as key, morse as value
#        alnumLookupDict = {}
#        for element in self._sourceTuple: # 0 is letter, 1 is morse - enters dictionary as {0:1}
#            alnumLookupDict.update({self._sourceTuple[self._sourceTuple.index(element)][0]:self._sourceTuple[self._sourceTuple.index(element)][1]})
#        return alnumLookupDict
    
#    def constructMorseLookupDict(self): # Make a dictionary with morse as key, alnumeric as value
#        morseLookupDict = {}
#        for element in self._sourceTuple: # enters dictionary as {1:0} this time
#            morseLookupDict.update({self._sourceTuple[self._sourceTuple.index(element)][1]:self._sourceTuple[self._sourceTuple.index(element)][0]})
#        return morseLookupDict

    #TODO: can probably merge these functions into one