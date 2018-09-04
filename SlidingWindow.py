import numpy
import pandas
import MimicObjects
import MockingWrapper
import datetime

class Phenotype:
    def __init__(self, _featurelist):
        self._featurelist = _featurelist

    @property
    def FeatureList(self):
        return self._featurelist

    def Contains(self, _item):
        containsit = False
        for eachitem in self.FeatureList:
            if _item == eachitem:
                containsit = True
        return containsit


class SnapFrame:
    def __init__(self, _parentcursor, _phenotype):
        self._selecteditems = _parentcursor.SelectedItems
        self._phenotype = _phenotype
        self._value = None
        self.processvalue1()

    @property
    def Duration(self):
        dt1 = self.SelectedItems[0]
        dt2 = self.SelectedItems[-1]
        return dt2 - dt1

    @property
    def LeftDate(self):
        return self.SelectedItems[0].TimeStamp

    @property
    def RightDate(self):
        return self.SelectedItems[-1].TimeStamp

    @property
    def AvgDate(self):
        durhalf = self.Duration / float(2.0)
        return self.LeftDate + durhalf

    @property
    def SelectedItems(self):
        return self._selecteditems

    @property
    def Phenotype(self):
        return self._phenotype

    @property
    def Value(self):
        if self._value is None:
            self.processvalue1()
        return self._value

    def processvalue1(self):
        hitcount = 0
        totalcount = 0
        for recordpackage in self.SelectedItems:
            # remember that the type of selecteditems is array of recordpackages. each recordpackage has a list of items too.
            for recordentry in recordpackage.RecordEntries:
                if self.Phenotype.Contains(recordentry.ConceptId) == True:
                    hitcount += 1
                totalcount += 1
        self._value = float(hitcount) / float(totalcount)
        return float(hitcount) / float(totalcount)
        # take Phenotype and SelectedItems and set the Value.


class SlidingCursorSimple:
    def __init__(self, _parentobject, _cursorwidth=1, _startposition=0, _capturephenotype=None):
        self._parentobject = _parentobject # parentobject must have an iterable property called RecordPackageList, Length, Count
        self._capturephenotype = _capturephenotype
        self._cursorwidth = _cursorwidth
        self._position = _startposition
        self._selecteditemarray = []
        for ix in range(_startposition, self._cursorwidth):
            self._selecteditemarray.append(self._parentobject.RecordPackageList[ix])
        self._snapframelist = []

    @property
    def ParentRecord(self):
        return self._parentobject

    @property
    def ParentIterableProperty(self):
        return self._parentobject.RecordPackageList

    @property
    def CursorWidth(self):
        return self._cursorwidth

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

    @property
    def CursorPositionCount(self): # number of positions that this cursor can slide over in the ParentObject
        cpc = self.ParentRecord.Length - self.CursorWidth + 1#self.ParentIterableProperty.Length - self.CursorWidth + 1
        if cpc >= 0:
            return cpc
        else:
            return 0

    @property
    def SnapFrameList(self):
        return self._snapframelist

    def TraverseRecord(self):
        for ix in range(1, self.CursorPositionCount):
            self.Snap()
            self.AdvanceWindowByItem()

    def Snap(self):
        snapshot = SnapFrame(self, self._capturephenotype)
        self.SnapFrameList.append(snapshot)

    def AdvanceWindowByItem(self):
        if self.LastPosition < len(self.ParentIterableProperty):
            self.Position += 1
            self._selecteditemarray.pop(0)
            # self._selecteditemarray.append(self.ParentIterableProperty[self.LastPosition])
            self._selecteditemarray.append(self.ParentIterableProperty[self.LastPosition])



class SnapShot:
    def __init__(self):
        pass


class PhenotypeDynamic:
    def __init__(self):
        pass


class SlidingCursorDynamic:
    def __init__(self):
        pass


