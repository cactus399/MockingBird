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


class SignificantEvent:
    def __init__(self):
        self._eventname = ""
        self._leftbound = None
        self._rightbound = None


class EventDetectionStack:
    def __init__(self, _compcursorstack, _lowerbound=0):
        self._eventdetectionstack = []
        for eachitem in _compcursorstack:
            tempdetection = EventDetection(eachitem, _lowerbound=_lowerbound)
            self._eventdetectionstack.append(tempdetection)


class EventDetectionPair:
    def __init__(self, widecursor, narrowcursor, _lowerbound=0):
        #self._widecursor = widecursor
        #self._narrowcursor = narrowcursor
        self._widedetection = EventDetection(widecursor, _lowerbound=_lowerbound, _fullcapture=True)
        self._narrowdetection = EventDetection(narrowcursor, _lowerbound=_lowerbound)

    @property
    def WideEventDetector(self):
        return self._widedetection

    @property
    def NarrowEventDetector(self):
        return self._narrowdetection

    def adjustWideDetectororderedlist(self):
        pass # not necessary at this time, bandaid fix with "_fullcapture" argument for EventDetection constructor
        # temporderedlist = self.WideEventDetector.TimeOrderedEvents
        # for eachitem in temporderedlist: # change the end-event spans for wide windows to rightbound dates.
        #





class EventDetection:
    def __init__(self, _compcursor, _lowerbound=0, _fullcapture=False):
        self._compcursor = _compcursor
        self._eralist = None
        self._eralistdates = None
        self._lowerbound = _lowerbound
        self._timeordered = None
        self._fullcapture = _fullcapture

    @property
    def EraList(self):
        if self._eralist is None:
            self._eralist = EventDetection.FindErasAll(self._compcursor, _lowerbound=self._lowerbound, _fullcapture=self._fullcapture)
        return self._eralist

    @property
    def CompCursor(self):
        return self._compcursor

    @property
    def TimeOrderedEvents(self):
        if self._timeordered is None:
            self._timeordered = self.OrderEventsByTime()
        return self._timeordered

    def OrderEventsByTime(self):
        col1 = []
        col2 = []
        col3 = []
        col4 = []
        count = 0
        experiment = []
        for eachkey, eachitem in self.EraList.items():
            for eachtuplearray in eachitem:
                for eachtuple in eachtuplearray:
                    experiment.append([eachtuple[1],eachtuple[0],eachtuple[2],eachtuple[3]])
                    col1.append(eachtuple[1])
                    col2.append(eachtuple[0])
                    col3.append(eachtuple[2])
                    col4.append(eachtuple[3])
                    count += 1
        experiment.sort(key= lambda timestamp: timestamp[0])
        return experiment
        # dumpyarray = numpy.array(experiment, order='C', dtype=[("timestamp", 'M'), ("index", 'i'), ("state",'S')])
        # return dumpyarray

    def widen(self):
        pass # need to make all "end" points to be RightBounded. Implement later. Right now we'll just re-list and then re-order each time.

    # @property
    # def CurrentTimeSpanCaptures(self):
    #     return self.CompCursor.Curr

    @classmethod
    def FindEras(cls, cursor, phenotypename, _lowerbound=0, _fullcapture=False):
        openindexstack = []
        closeindexstack = []
        currentopenedindex = -1
        currentopenedindexdate = None
        opened = False
        erapairs = []
        currenttravelindex = 0
        capturearraylength = len(cursor.CaptureArray)

        for eachdate, eachcapturearray in cursor.CaptureArray.items():
            thiscap = eachcapturearray[phenotypename]
            checksummed = False
            if thiscap.Value > _lowerbound:
                if opened == False:
                    currentopenedindex = currenttravelindex
                    currentopenedindexdate = eachdate
                    openindexstack.append((currenttravelindex, eachdate, "start"))
                    opened = True
            if thiscap.Value <= _lowerbound:
                if opened == True:
                    closeindexstack.append((currenttravelindex, eachdate, "end"))
                    opened = False
                    if _fullcapture == False:
                        erapairs.append([(currentopenedindex, currentopenedindexdate, "start", phenotypename), (currenttravelindex, eachdate, "end", phenotypename)])
                    else:
                        erapairs.append([(currentopenedindex, currentopenedindexdate, "start", phenotypename), (currenttravelindex, thiscap.RightBound, "end", phenotypename)])
                    checksummed = True
            currenttravelindex += 1
            if currenttravelindex >= capturearraylength:
                if opened == True:
                    if checksummed == False:
                        closeindexstack.append(currenttravelindex)
                        if _fullcapture == False:
                            erapairs.append([(currentopenedindex, currentopenedindexdate, "start", phenotypename), (currenttravelindex, eachdate, "end", phenotypename)])
                        else:
                            erapairs.append([(currentopenedindex, currentopenedindexdate, "start", phenotypename),
                                             (currenttravelindex, thiscap.RightBound, "end", phenotypename)])
                    break
        return erapairs

    @classmethod
    def FindErasAll(cls, cursor, _lowerbound=0, _fullcapture=False):
        eradict = {}
        for eachitem in cursor.PhenotypeFilters:
            eralist = cls.FindEras(cursor, eachitem.Name, _fullcapture=_fullcapture)
            if eachitem.Name not in eradict.keys():
                eradict.update({eachitem.Name: eralist})
        return eradict

    # @property
    # def EraListDates(self):
    #     if self._eralistdates is None:
    #         self._eralistdates = EventDetection.FindErasAllDates(self._compcursor, _lowerbound=self._lowerbound)
    #     return self._eralistdates

    # datedict = {}
    # for eachkey, eachitem in self.EraList:
    #     if len(eachitem) > 0:
    #         tempaa = []
    #         for eachpair in eachitem:
    #             d1 = self.CompCursor.CaptureArray[eachkey][eachpair[0]].LeftBound
    #             d2 = self.CompCursor.CaptureArray[eachkey][eachpair[1]].LeftBound
    #             tempa = [d1, d2]
    #             tempaa.append(tempa)
    #         if eachkey not in datedict.keys():
    #             datedict.update({eachkey: tempaa})
    # return datedict
    # @classmethod # preserved code 9-9-2018
    # def FindEras(cls, cursor, phenotypename, _lowerbound=0):
    #     openindexstack = []
    #     closeindexstack = []
    #     currentopenedindex = -1
    #     opened = False
    #     erapairs = []
    #     currenttravelindex = 0
    #     capturearraylength = len(cursor.CaptureArray)
    #
    #     for eachdate, eachcapturearray in cursor.CaptureArray.items():
    #         thiscap = eachcapturearray[phenotypename]
    #         checksummed = False
    #         if thiscap.Value > _lowerbound:
    #             if opened == False:
    #                 currentopenedindex = currenttravelindex
    #                 openindexstack.append(currenttravelindex)
    #                 opened = True
    #         if thiscap.Value <= _lowerbound:
    #             if opened == True:
    #                 closeindexstack.append(currenttravelindex)
    #                 opened = False
    #                 erapairs.append([currentopenedindex, currenttravelindex])
    #                 checksummed = True
    #         currenttravelindex += 1
    #         if currenttravelindex >= capturearraylength:
    #             if opened == True:
    #                 if checksummed == False:
    #                     closeindexstack.append(currenttravelindex)
    #                     erapairs.append([currentopenedindex, currenttravelindex])
    #                 break
    #     return erapairs
    #
    # @classmethod
    # def FindErasAll(cls, cursor, _lowerbound=0):
    #     eradict = {}
    #     for eachitem in cursor.PhenotypeFilters:
    #         eralist = cls.FindEras(cursor, eachitem.Name)
    #         if eachitem.Name not in eradict.keys():
    #             eradict.update({eachitem.Name: eralist})
    #     return eradict
    #
    # @classmethod
    # def FindErasDates(cls, cursor, phenotypename, _lowerbound=0):
    #     anarray = EventDetection.FindEras(cursor, phenotypename, _lowerbound=_lowerbound)
    #     datearray = []
    #     for eachitem in anarray:
    #         d1 = cursor.CaptureArray[phenotypename][eachitem[0]].LeftBound # shit. CaptureArray is keyed by Date, not by phenotype name. Phenotypename is the sub-key for each keyed date.
    #         d2 = cursor.CaptureArray[phenotypename][eachitem[1]].LeftBound
    #         datearray.append([d1,d2])
    #     return datearray
    #
    # @classmethod
    # def FindErasAllDates(cls, cursor, _lowerbound=0):
    #     datedict = {}
    #     for eachitem in cursor.PhenotypeFilters:
    #         namekey = eachitem.Name
    #         eradates = EventDetection.FindErasDates(cursor, eachitem.Name, _lowerbound=_lowerbound)
    #         if namekey not in datedict.keys():
    #             datedict.update({namekey: eradates})
    #     return datedict




class CompositeCursorStack:
    def __init__(self, _compcursorstack):
        self._compcursorstack = _compcursorstack
        for eachitem in self._compcursorstack:
            if eachitem.CaptureArray is None:
                eachitem.GetAllCaptureArrays()
            eachitem.ResetTimeSpanIndex()
        self._theindex = 0
        self._largestdurationwidthcompcursorindex = -1
        self.LargestDurationWidth

    @property
    def LeftBound(self):
        return self._compcursorstack[0].LeftBound

    @property
    def RightBound(self):
        return self._compcursorstack[0].RightBound

    @property
    def CurrentTimeSpanIndex(self):
        return self._compcursorstack[0].CurrentTimeSpanIndex

    @property
    def LargestDurationWidth(self):
        if self._largestdurationwidthcompcursorindex < 0:
            largest = numpy.timedelta64(0,'m')
            counter = 0
            theindex = 0
            for eachitem in self._compcursorstack:
                if largest < eachitem._durationwidth:
                    theindex = counter
                    largest = eachitem._durationwidth
                counter += 1
            self._largestdurationwidthcompcursorindex = theindex
        return self._largestdurationwidthcompcursorindex

    @property
    def CurrentTimeSpanCapturesArray(self):
        slicedic = []
        for eachitem in self._compcursorstack:
            slicedic.append(eachitem.CurrentTimeSpanCaptures)
        return slicedic

    def CurrentTimeSpanCapturesArrayVertical(self, _phenotypekey):
        slicedic = []
        currentcaps = self.CurrentTimeSpanCapturesArray
        for eachitem in currentcaps:
            avalue = eachitem[_phenotypekey].Value
            slicedic.append(avalue)
        return slicedic

    def Advance(self):
        dumbadvanceboolean = False
        for eachitem in self._compcursorstack:
            dumbadvanceboolean = eachitem.Advance()
        return dumbadvanceboolean

    def Retreat(self):
        dumbadvanceboolean = False
        for eachitem in self._compcursorstack:
            dumbadvanceboolean = eachitem.Retreat()
        return dumbadvanceboolean


class CompositeCursor:
    def __init__(self, _parentrecord, _phenotypefilters, _durationwidth=numpy.timedelta64(180, 'm'), _advancementduration=numpy.timedelta64(60, 'm')):
        self._parentrecord = _parentrecord
        self._slidingcursors = {}
        self._durationwidth = _durationwidth
        self._advancementduration = _advancementduration
        self._phenotypefilters = _phenotypefilters
        for eachitem in _phenotypefilters:
            tempslidingcursor = SlidingCursorDynamic(_parentrecord, eachitem, _durationwidth=_durationwidth, _advancementduration=_advancementduration)
            tempslidingcursor.CaptureAll0906()
            self._slidingcursors.update({tempslidingcursor.PhenotypeFilter.Name: tempslidingcursor})
        self._timespanindex = 0
        self._allcaps = None

    @property
    def PhenotypeFilters(self):
        return self._phenotypefilters

    @property
    def LeftBound(self):
        return self._parentrecord[0].TimeStamp

    @property
    def RightBound(self):
        return self._parentrecord[-1].TimeStamp

    @property
    def Length(self):
        return len(self._slidingcursors[next(iter(self._slidingcursors))].Captured)

    @property
    def CurrentTimeSpanIndex(self):
        return self._timespanindex

    @property
    def CurrentTimeSpanLeftBound(self):
        return self._slidingcursors[next(iter(self._slidingcursors))].Captured[self._timespanindex].LeftBound

    @property
    def CurrentTimeSpanCaptures(self):
        captures = {}
        for eachkey, eachitem in self._slidingcursors.items():
            tempcap = eachitem.Captured[self.CurrentTimeSpanIndex]
            captures.update({eachkey: tempcap})
        return captures

    @property
    def CanAdvance(self):
        if self._timespanindex >= self.Length - 1:
            return False
        else:
            return True

    @property
    def CaptureArray(self): # ALL CAPS - 9-7 at 10PM or so
        return self._allcaps

    def __next__(self):
        if self._timespanindex >= self.Length - 1:
            raise StopIteration
        else:
            self._timespanindex += 1
            return self.__getitem__(self._timespanindex)

    def __getitem__(self, _anindex):
        tempstore = self._timespanindex
        self._timespanindex = _anindex
        aslice = self.CurrentTimeSpanCaptures
        self._timespanindex = tempstore
        return aslice

    def GetAllCaptureArrays(self):
        bigarray = {}
        canadvance = True
        while canadvance == True:
            bigarray.update({self.CurrentTimeSpanLeftBound: self.CurrentTimeSpanCaptures})
            canadvance = self.Advance()
        self._allcaps = bigarray
        return bigarray

    def Advance(self):
        _canadvance = self.CanAdvance
        if _canadvance == True:
            self._timespanindex += 1
        return _canadvance

    def Retreat(self):
        if self._timespanindex <= 0: # means you can't actually go back
            return False
        else:
            self._timespanindex -= 1
            return True

    def ResetTimeSpanIndex(self):
        self._timespanindex = 0

    def ReadForward(self): # advance once, then get currenttimespan capture, and return that. failed advance = return None
        _advanced = self.Advance()
        if _advanced == True:
            return self.CurrentTimeSpanCaptures
        else:
            return None

    def ReadInPlace(self):
        currents = self.CurrentTimeSpanCaptures
        _advanced = self.Advance()
        return currents
        # if _advanced == True:
        #     return currents
        # else:
        #     return None

    # def FindEvents(self, _eventdetection):
    #     for eachkey, eachitem in self.CaptureArray.items(): # eachitem is a dict of N of SnapShotDynamic instances in parallel array. N is # of phenotypes (e.g. intub, extub, trach)
    #
    #     # loop through self._allcaps (propertized by self.CaptureArray)



    @classmethod
    def DisplayConsole(cls, thedata):
        #thestr = ""
        for eachkey, eachitem in thedata.items():
            thisline = ""
            thisline += str(eachkey) + ", "
            for eachkey2, eachitem2 in eachitem.items():
                thisline += str(eachitem2.Value) + ", "
            print(thisline)
            # thestr += thisline
            # thestr += "\n"

    @classmethod
    def DisplayString(cls, thedata):
        thestr = ""
        for eachkey, eachitem in thedata.items():
            thisline = ""
            thisline += str(eachkey) + ", "
            for eachkey2, eachitem2 in eachitem.items():
                thisline += str(eachitem2.Value) + ", "
            thestr += thisline
            thestr += "\n"
        return thestr

    @classmethod
    def WriteToDisk(cls, thedata, outpath, writetofile=False): # "thedata" being "bigarray" in "GetAllCaptureArrays" method return
        if writetofile == True:
            athestr = cls.DisplayString(thedata)
            afile=open(outpath, "x")
            afile.write(athestr)
            afile.close()

class SnapShotDynamic:
    def __init__(self, _recordpackageholdingarray, _phenotype, _def_leftbound=None, _def_rightbound=None):
        self._recordpackageholdingarray = _recordpackageholdingarray
        self._phenotype = _phenotype
        self._value = 0.0
        #self.processvalue1()
        self.processvalue2_0906()
        self._leftbound = _def_leftbound
        self._rightbound = _def_rightbound
        # if self._recordpackageholdingarray is not None and len(self._recordpackageholdingarray) > 0:
        #     self._leftbound = self._recordpackageholdingarray[0].TimeStamp
        #     self._rightbound = self._recordpackageholdingarray[-1].TimeStamp
        # else:
        #     self._leftbound = _def_leftbound
        #     self._rightbound = _def_rightbound

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

    def processvalue2_0906(self):
        hitcount = 0
        totalcount = 0
        for eachrecordpackage in self._recordpackageholdingarray:
            for eachrecordentry in eachrecordpackage.RecordEntries:
                totalcount += 1
                passesconditions = self._phenotype.Process(eachrecordentry)
                if passesconditions == True:
                    hitcount += 1
        if totalcount <= 0:
            self._value = -0.001
        else:
            self._value = float(hitcount) / float(totalcount)

# # Commented out 09-06-2018 to make way for modifications to this class
# class PhenotypeDynamic:
#     def __init__(self, _phenotypes=[]):
#         self._phenotypes=_phenotypes
#
#     def __next__(self):
#         if self._index >= len(self._phenotypes) - 1:
#             raise StopIteration
#         else:
#             self._index += 1
#             return self.__getitem__(self._index)
#         # return self.__getitem__(self._index)
#
#     def __getitem__(self, _index):
#         return self._phenotypes[_index]
#
#     def __len__(self):
#         return len(self._phenotypes)



class PhenotypeDynamic:
    #def __init__(self, name, phenotypes={}, _phenotypeitemlist=None):
    def __init__(self, name, _phenotypeitemlist):
        self._phenotypes = {}
        self._name = name
        if _phenotypeitemlist is not None:
            for eachitem in _phenotypeitemlist:
                if type(eachitem) is PhenotypeDynamicItem:
                    tempitem = eachitem
                else:
                    tempitem = PhenotypeDynamicItem(eachitem[0], eachitem[1], conditionlist=eachitem[2])
                if tempitem.Id not in self._phenotypes.keys():
                    self._phenotypes.update({tempitem.Id: tempitem})
                else:
                    self._phenotypes[tempitem.Id] = tempitem
        # {50826: (con1, con2, con3)... , 50813: con1, con2
        # {50826: (">0", isnumeric=True)... , 50813: (="None".tolower(), ="Not applicable".tolower())}
        # NEWEST INCARNATION:
        # {50826: instof.PhenotypeDynamicItem, 50813: instof.PhenotypeDynamicItem}

    @property
    def Name(self):
        return self._name

    def Process(self, processeditem): # processed item must be RecordEntry type
        itemidtag = processeditem.ConceptId
        if itemidtag in self._phenotypes.keys():
            return self._phenotypes[itemidtag].Process(processeditem)
        else:
            return False
        # for eachphenotypeitem in self._phenotypes.items():
        #

    def __next__(self):
        if self._index >= len(self._phenotypes) - 1:
            raise StopIteration
        else:
            self._index += 1
            return self.__getitem__(self._index)
        # return self.__getitem__(self._index)

    def __getitem__(self, _index):
        return self._phenotypes[_index]

    def __len__(self):
        return len(self._phenotypes)


class PhenotypeDynamicItem:
    def __init__(self, id, type, conditionlist=[]): # conditionlist - list of tuples (a,b,c); a is boolean operator's string, b is standard comparison value, and c is 0 or 1 (0=optional condition [at least 1 out of n must be true], 1=required condition [all reqs must be true])
        self._id = id
        self._type = type
        self._conditionlist = conditionlist
        self._index = 0
        # input is through the method "Process" -> takes a RecordEntry object

    @property
    def Id(self):
        return self._id

    @property
    def Type(self):
        return self._type.lower()

    def Process(self, processeditem):
        # return True or False depending on if processeditem meets conditionlist.
        finalpass = False
        # requiredpass = True
        # optionalpass = False

        requiredpasscount = 0
        optionalpasscount = 0
        requiredpasshits = 0
        optionalpasshits = 0
        for eachitem in self._conditionlist:
            if eachitem[2] == 1:
                requiredpasscount += 1
            if eachitem[2] == 0:
                optionalpasscount += 1

        testvalue = processeditem.Value
        if testvalue is not None:
            if self.Type == "num" or self.Type == "int" or self.Type == "float" or self.Type == "number" or self.Type == "numeric":
                for eachitem in self._conditionlist:
                    conditional = eachitem[0]
                    conditionalvalue = eachitem[1]
                    conditionallock = eachitem[2]
                    typecheck = str(testvalue).replace('.','',1).isdigit()#conditionalvalue.replace('.','',1).isdigit()
                    if typecheck == True:
                        if '.' in str(testvalue):
                            testvalue = float(testvalue)
                        else:
                            testvalue = int(testvalue)
                        if conditional == "==" or conditional == "=":
                            if testvalue == conditionalvalue:
                                if conditionallock == 0: # 0 being 'optional'
                                    optionalpasshits += 1
                                if conditionallock == 1: # 1 being 'required'
                                    requiredpasshits += 1
                        if conditional == "<":
                            if testvalue < conditionalvalue:
                                if conditionallock == 0: # 0 being 'optional'
                                    optionalpasshits += 1
                                if conditionallock == 1: # 1 being 'required'
                                    requiredpasshits += 1
                        if conditional == ">":
                            if testvalue > conditionalvalue:
                                if conditionallock == 0: # 0 being 'optional'
                                    optionalpasshits += 1
                                if conditionallock == 1: # 1 being 'required'
                                    requiredpasshits += 1
                        if conditional == "<=":
                            if testvalue <= conditionalvalue:
                                if conditionallock == 0: # 0 being 'optional'
                                    optionalpasshits += 1
                                if conditionallock == 1: # 1 being 'required'
                                    requiredpasshits += 1
                        if conditional == ">=":
                            if testvalue >= conditionalvalue:
                                if conditionallock == 0: # 0 being 'optional'
                                    optionalpasshits += 1
                                if conditionallock == 1: # 1 being 'required'
                                    requiredpasshits += 1
                        if conditional == "!=":
                            if testvalue != conditionalvalue:
                                if conditionallock == 0: # 0 being 'optional'
                                    optionalpasshits += 1
                                if conditionallock == 1: # 1 being 'required'
                                    requiredpasshits += 1

            if self.Type == "str" or self.Type == "string":
                for eachitem in self._conditionlist:
                    conditional = eachitem[0]
                    conditionalvalue = eachitem[1].lower()
                    conditionallock = eachitem[2]
                    typecheck = str(testvalue).replace('.', '', 1).isdigit()#conditionalvalue.replace('.', '', 1).isdigit()
                    if typecheck == False:
                        testvalue = str(testvalue)
                        testvalue = testvalue.lower()
                        if conditional == "==" or conditional == "=":
                            if testvalue == conditionalvalue:
                                if conditionallock == 0: # 0 being 'optional'
                                    optionalpasshits += 1
                                if conditionallock == 1: # 1 being 'required'
                                    requiredpasshits += 1
                        if conditional == "!=":
                            if testvalue != conditionalvalue:
                                if conditionallock == 0: # 0 being 'optional'
                                    optionalpasshits += 1
                                if conditionallock == 1: # 1 being 'required'
                                    requiredpasshits += 1
            # if requiredpass == True and optionalpass == True:
            #     finalpass = True

        if requiredpasshits == requiredpasscount: # will be true if there are no required conditions
            if optionalpasscount > 0:
                if optionalpasshits > 0:
                    finalpass = True
            else: # if there ARE no optional conditions, just pass true
                finalpass = True

        # print(str(requiredpasscount) + ", " + str(requiredpasshits) + ", " + str(optionalpasscount) + ", " + str(optionalpasshits) + ", " + str(finalpass))


        return finalpass

    def __next__(self):
        if self._index >= len(self._conditionlist) - 1:
            raise StopIteration
        else:
            self._index += 1
            return self.__getitem__(self._index)

    def __getitem__(self, _index):
        return self._conditionlist[_index]

    def __len__(self):
        return len(self._conditionlist)


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
        self._phenotypedictionary = {}

    @property
    def PatientInfo(self):
        return self._parentrecord.PatientInfo

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
    def StartTimeStamp(self):
        return self._startdatestamp

    @property
    def EndTimeStamp(self):
        return self._enddatestamp

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
# ^ Advance is a critical, OG method.
    # @property
    # def PhenotypeValueDictionary(self):
    #     adict = {}
    #     if len(self.PhenotypeFilter) <= 0:
    #         for eachitem in self._parentrecord.RecordEntries:
    #             if eachitem.ConceptId in adict:
    #                 subdict = adict[eachitem.ConceptId]
    #                 if eachitem.Value not in subdict:
    #                     subdict.update({eachitem.Value: 1})
    #                 else:
    #                     subdict[eachitem.Value] += 1
    #             else:
    #                 adict.update({eachitem.ConceptId: {eachitem.Value: 1}})
    #     else:
    #         adict = self.PhenotypeFilter
    #         for eachitem in self._parentrecord.RecordEntries:
    #             if eachitem.ConceptId in adict:
    #                 subdict = adict[eachitem.ConceptId]
    #                 if eachitem.Value not in subdict:
    #                     subdict.update({eachitem.Value: 1})
    #                 else:
    #                     subdict[eachitem.Value] += 1
    #     return adict

    def GetUniqueConceptIds(self):
        adict = dict()

    def Capture0906(self):
        holdingarray = []
        # print("*****************************")
        for eachitem in self._parentrecord:
            # print(str(self.LeftBound) + ", " + str(eachitem.TimeStamp) + ", " + str(self.RightBound))
            if eachitem.TimeStamp >= self.LeftBound:
                if eachitem.TimeStamp < self.RightBound:
                    holdingarray.append(eachitem)
                else:
                    break

        # print(str(self.LeftBound) + ", " + str(self.RightBound) + " vs " + str(len(holdingarray)))
        asnapshot = SnapShotDynamic(holdingarray, self.PhenotypeFilter, _def_leftbound=self.LeftBound,
                                    _def_rightbound=self.RightBound)
        return asnapshot

    def CaptureAll0906(self):
        canadvance = True
        capturetemp = None
        while canadvance == True:
            capturetemp = self.Capture0906()
            if capturetemp.IsValid == True:
                self.Captured.append(capturetemp)
            canadvance = self.Advance()

##############
    def Capture(self):
        holdingarray = []
        # print("*****************************")
        for eachitem in self._parentrecord:
            # print(str(self.LeftBound) + ", " + str(eachitem.TimeStamp) + ", " + str(self.RightBound))
            if eachitem.TimeStamp >= self.LeftBound:
                if eachitem.TimeStamp < self.RightBound:
                    holdingarray.append(eachitem)
                else:
                    break

        # print(str(self.LeftBound) + ", " + str(self.RightBound) + " vs " + str(len(holdingarray)))
        asnapshot = SnapShotDynamic(holdingarray, self.PhenotypeFilter, _def_leftbound=self.LeftBound,
                                    _def_rightbound=self.RightBound)
        return asnapshot

    def CaptureAll(self):
        canadvance = True
        capturetemp = None
        while canadvance == True:
            capturetemp = self.Capture()
            if capturetemp.IsValid == True:
                self.Captured.append(capturetemp)
            canadvance = self.Advance()
############# ^ old capturing system.

#################################################

class PhenotypeItem: # defines conditional "hitscan" rules for a single itemid
    def __init__(self):
        pass

class PhenotypeFeatured:
    def __init__(self):
        pass



