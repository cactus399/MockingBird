import numpy
import pandas
import MimicObjects
import MockingWrapper
import datetime

class Phenotype:
    def __init__(self, _featurelist=None):
        self._featurelist = _featurelist

#
# class WindowBorder:
#     def __init__(self, _):


class SlidingCursorTime:
    def __init__(self, _parentobject, _cursorwidth=numpy.timedelta64(5, 'm'), _cursorjump=numpy.timedelta64(1, 'm'), _capturephenotype=None):
        self._parentobject = _parentobject
        self._capturephenotype = _capturephenotype
        self._cursorwidth = _cursorwidth
        self._cursorjump = _cursorjump
        


class SlidingCursorSimple:
    def __init__(self, _parentobject, _cursorwidth=1, _startposition=0, _capturephenotype=None):
        self._parentobject = _parentobject # parentobject must have an iterable property called RecordPackageList, Length, Count
        self._capturephenotype = _capturephenotype
        self._cursorwidth = _cursorwidth
        self._position = _startposition
        self._selecteditemarray = []
        for ix in range(_startposition, self._cursorwidth):
            self._selecteditemarray.append(self._parentobject.RecordPackageList[ix])

    @property
    def ParentIterableProperty(self):
        return self._parentobject.RecordPackageList

    @property
    def CursorWidth(self):
        return self._cursorwidth

    # @property
    # def PositionFractional(self): # gives % through the parentobject's list it has gone through (convenience - implement later)
    #     pass

    @property
    def Position(self):
        return self._position

    @Position.setter
    def Position(self, _posvalue):
        self._position = _posvalue

    @property
    def LastPosition(self):
        return self.Position + self.CursorWidth - 1

    @property
    def SelectedItems(self):
        return self._selecteditemarray
        # itemlist = []
        # for ix in range(self.Position, self.CursorWidth):
        #     itemlist.append(self.ParentIterableProperty.RecordPackagelist[ix])
        # return itemlist

    @property
    def CursorPositionCount(self): # number of positions that this cursor can slide over in the ParentObject
        cpc = self.ParentIterableProperty.Length - self.CursorWidth + 1
        if cpc >= 0:
            return cpc
        else:
            return 0

    def AdvanceWindowByItem(self):
        if self.LastPosition < len(self.ParentIterableProperty):
            self.Position += 1
            self._selecteditemarray.pop(0)
            # self._selecteditemarray.append(self.ParentIterableProperty[self.LastPosition])
            self._selecteditemarray.append(self.ParentIterableProperty[self.LastPosition])

