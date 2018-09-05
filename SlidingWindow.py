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





class SnapFrame2:
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


class SnapFrame:
    def __init__(self, _selecteditems, _phenotype):
        #self._selecteditems = _selecteditems
        self._selecteditems = []
        for eachitem in _selecteditems:
            self._selecteditems.append(eachitem)
        self._leftdate = _selecteditems[0].TimeStamp
        self._rightdate = _selecteditems[-1].TimeStamp
        self._phenotype = _phenotype
        self._value = None
        self.processvalue1()

    @property
    def Duration(self):
        dt1 = self.LeftDate #self.SelectedItems[0]
        dt2 = self.RightDate #SelectedItems[-1]
        return dt2 - dt1

    @property
    def LeftDate(self):
        return self._leftdate#self.SelectedItems[0].TimeStamp

    @property
    def RightDate(self):
        return self._rightdate #self.SelectedItems[-1].TimeStamp

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
        snapshot = SnapFrame(self.SelectedItems, self._capturephenotype)
        self.SnapFrameList.append(snapshot)

    def AdvanceWindowByItem(self):
        if self.LastPosition < len(self.ParentIterableProperty):
            self.Position += 1
            self._selecteditemarray.pop(0)
            # self._selecteditemarray.append(self.ParentIterableProperty[self.LastPosition])
            self._selecteditemarray.append(self.ParentIterableProperty[self.LastPosition])

###################################################

class SnapShotDynamic:
    def __init__(self, _recordpackageholdingarray, _phenotype, _def_leftbound=None, _def_rightbound=None):
        self._recordpackageholdingarray = _recordpackageholdingarray
        self._phenotype = _phenotype
        self._value = 0.0
        self.processvalue1()
        if self._recordpackageholdingarray is not None and len(self._recordpackageholdingarray) > 0:
            self._leftbound = self._recordpackageholdingarray[0].TimeStamp
            self._rightbound = self._recordpackageholdingarray[-1].TimeStamp
        else:
            self._leftbound = _def_leftbound
            self._rightbound = _def_rightbound

    @property
    def Value(self):
        return self._value

    @property
    def LeftBound(self):
        return self._leftbound

    @property
    def RightBound(self):
        return self._rightbound

    @property
    def IsValid(self):
        if self.LeftBound is None or self.RightBound is None:
            return False
        else:
            return True

    def processvalue1(self):
        hitcount = 0
        totalcount = 0
        for eachrecordpackage in self._recordpackageholdingarray:
            for eachrecordentry in eachrecordpackage.RecordEntries:
                totalcount += 1
                #print(eachrecordentry.ConceptId)
                for eachphenotypeelement in self._phenotype:
                    #print(eachphenotypeelement)
                    if str(eachrecordentry.ConceptId) == str(eachphenotypeelement):
                        hitcount += 1
        if totalcount <= 0:
            self._value = -0.1
        else:
            self._value = float(hitcount) / float(totalcount)


class PhenotypeDynamic:
    def __init__(self, _phenotypes=[]):
        self._phenotypes=_phenotypes

    def __next__(self):
        if self._index >= len(self._phenotypes) - 1:
            raise StopIteration
        else:
            self._index += 1
            return self.__getitem__(self._index)
        # return self.__getitem__(self._index)

    def __getitem__(self, _index):
        return self._phenotypes[_index]


class SlidingCursorDynamic:
    def __init__(self, _parentrecord, _phenotypefilter, _durationwidth=numpy.timedelta64(30, 'm'), _advancementduration=numpy.timedelta64(5, 'm')):
    #datetime.timedelta(minutes=30), _advancementduration=datetime.timedelta(minutes=5)):
        self._parentrecord = _parentrecord # _parentrecord type is of MimicObjects.Record
        self._durationwidth = _durationwidth
        self._phenotypefilter = _phenotypefilter
        #if self._parentrecord is not None and len(self._parentrecord.RecordEntries) > 0:
        self._startdatestamp = self._parentrecord[0].TimeStamp #RecordEntries[0].TimeStamp
        self._enddatestamp = self._parentrecord[-1].TimeStamp #RecordEntries[-1].TimeStamp
        # else:
        #     self._startdatestamp = None
        #     self._enddatestamp = None
        self._leftbound = self._startdatestamp #datetime.datetime(self._startdatestamp)
        self._advancementduration = _advancementduration
        self._captured = []

    @property
    def LeftBound(self):
        return self._leftbound

    @LeftBound.setter
    def LeftBound(self, _boundvalue):
        self._leftbound = _boundvalue

    @property
    def RightBound(self):
        return self.LeftBound + self.CursorWidth

    @property
    def CursorWidth(self):
        return self._durationwidth

    @CursorWidth.setter
    def CursorWidth(self, _newwidth):
        self._durationwidth = _newwidth

    @property
    def AdvancementDuration(self):
        return self._advancementduration

    @AdvancementDuration.setter
    def AdvancementDuration(self, _newduration):
        self._advancementduration = _newduration

    @property
    def Captured(self):
        return self._captured

    @property
    def PhenotypeFilter(self):
        return self._phenotypefilter

    def Capture(self):
        holdingarray = []
        #print("*****************************")
        for eachitem in self._parentrecord:
            #print(str(self.LeftBound) + ", " + str(eachitem.TimeStamp) + ", " + str(self.RightBound))
            if eachitem.TimeStamp >= self.LeftBound:
                if eachitem.TimeStamp < self.RightBound:
                    holdingarray.append(eachitem)

        #print(str(self.LeftBound) + ", " + str(self.RightBound) + " vs " + str(len(holdingarray)))
        asnapshot = SnapShotDynamic(holdingarray, self.PhenotypeFilter, _def_leftbound=self.LeftBound, _def_rightbound=self.RightBound)
        return asnapshot

    def Advance(self): #, _advancementduration=None):
        # first off, confirm that the window can advance at all (e.g. RightBound is less than the actual datetime boundaries of the parent record object
        # then, confirm that you can indeed advance the prescribed amount _advancementduration
        # if one can advance but not as much as _advancementduration, advance to fit the final bit.
        # ** self.RightBound must be less than the RightBound of the parent object (record)** for advancement to occur.
        rightTimeDelta = self._parentrecord.RightBound - self.RightBound
        # if _advancementduration is None:
        #     _advancementduration = self.AdvancementDuration
        # else:
        #     self.AdvancementDuration = _advancementduration

        if rightTimeDelta >= self.AdvancementDuration: #_advancementduration: # then go ahead with regular advancement
            self.LeftBound = self.LeftBound + self.AdvancementDuration
        else: # then must modify the advancement.
            self.LeftBound = self.LeftBound + rightTimeDelta
        advanced = False
        if rightTimeDelta > numpy.timedelta64(0, 'm'):
            advanced = True
        return advanced

    def CaptureAll(self):
        canadvance = True
        capturetemp = None
        while canadvance == True:
            capturetemp = self.Capture()
            if capturetemp.IsValid == True:
                self.Captured.append(capturetemp)
            canadvance = self.Advance()




