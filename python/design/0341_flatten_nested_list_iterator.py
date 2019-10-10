class NestedIterator(object):

    def __init__(self, nestedList):
        """
        Initialize your data structure here.
        :type nestedList: List[NestedInteger]
        """
        self.data = []
        self._flat(nestedList, self.data)
        self.i = 0

    def _flat(self, nestedList, data):
        for nl in nestedList:
            if nl.isInteger():
                self.data.append(nl.getInteger())
            else:
                if nl.getList():
                    self._flat(nl.getList(), data)

    def next(self):
        """
        :rtype: int
        """
        v = self.data[self.i]
        self.i += 1
        return v

    def hasNext(self):
        """
        :rtype: bool
        """
        return self.i < len(self.data)
