import numpy
import pandas
import MimicObjects
import MockingWrapper
import datetime
import SlidingWindow
import queue

class EventDetector(SlidingWindow.CompositeCursor):
    def __init__(self, _parentrecord, _phenotypefilters, _lowerbound=0, _durationwidth=numpy.timedelta64(180, 'm'), _advancementduration=numpy.timedelta64(60, 'm'), _fullcapture=False):
        super().__init__(_parentrecord, _phenotypefilters, _durationwidth=_durationwidth, _advancementduration=_advancementduration)
        self._lowerbound = _lowerbound
        self._fullcapture = _fullcapture # FULLCAPTURE - on "ending" a started region (or event), if _fullcapture is true, this class object will set the end datetime stamps to the RIGHTBOUND of the captured region. This is to ensure that any shenanigans between narrow and wide are not missed (a smaller window may fall AFTER the LeftBound of a larger window, thus being missed on backtracking)
        #backtracking is the process of searching the high-res (or narrow-window) cursor's snapshots for events rather than relying on the wide-window timestamps, which are not as accurate.
        # note that there are exceptions. This is a temporary heuristic model. this class is simply for identification of event start/end points. A subclass needs to be made in order to accomodate heuristic identification.
        # list of inherited attr (for iteration of enumerables):
        # PhenotypeFilters, LeftBound, RightBound, Length (of capturearray, most likely), CurrentTimeSpanIndex (duplicate of TimeSpanIndex), CurrentTimeSpanLeftBound, CurrentTimeSpanCaptures, CurrentValueEffective, *CaptureArray*
        # list of inherited attr (for browsing the cursor): CanAdvance,

    def FindErasParallel(self):
        eralist = []
        phenotypestatedict = {}
        for eachphenotype in self.PhenotypeFilters:
            phenotypestatedict.update({eachphenotype.Name: False})

        while self.CanAdvance is True:
            pass
        pass



    def FindEras(self, _phenotypename):
        eralist = []

        while self.CanAdvance is True:
            pass
        pass
        # eralist = []
        # while self.CanAdvance is True:

        # note that this class inherits from CompositeCursor and thus supports cursor-browsing (index-based)


    # def __init__(self, _compcursor, _lowerbound=0, _fullcapture=False):
    #     self._compcursor = _compcursor
    #     self._eralist = None
    #     self._eralistdates = None
    #     self._lowerbound = _lowerbound
    #     self._timeordered = None
    #     self._fullcapture = _fullcapture




class MimicCursor(SlidingWindow.CompositeCursor):
    def __init__(self, _parentrecord, _phenotypefilters, _durationwidth=numpy.timedelta64(180, 'm'), _advancementduration=numpy.timedelta64(60, 'm')):
        super().__init__(_parentrecord, _phenotypefilters, _durationwidth=_durationwidth, _advancementduration=_advancementduration)

    # indexing attributes:
    # SlidingCursorDynamic object - we have a list of these: attr.Captured (a list of captured SnapShotDynamic objects)
    # CompositeCursor - stream-like object across the chart. attr.CaptureArray (dictionary of numpy.datetime64-keyed dictionary of phenotype.name-keyed dictionaries (of slidingcursor.attr.Captured)
    # CompositeCursor.attr.CaptureArray:
    #  this is a numpy.datetime64-keyed dictionary of phenotype.name-keyed dictionaries (of slidingcursor.attr.Captured)
    #         # example:
    #         # {9/11/2001-09:00:00: {intubated: SnapShotDynamic.instance,
    #         #                       extubated: SnapShotDynamic.instance,
    #         #                       trached  : SnapShotDynamic.instance,
    #         #                       SBT      : SnapShotDynamic.instance}}
    # EventDetection - encapsulates CompositeCursor. main attributes built on top of CompositeCursor:
    # EventDetection.attr.EraList - non-ordered list of 2-item arrays containing 2x4-item tuples (start, end); each tuple has the following:
    # (index_capture_element, current_capture_element_indexdate, "start"/"end" keyword string, phenotype_name)
    # this is then ordered into the below attr:
    # EventDetection.attr.TimeOrderedEvents - list/array of list/array from the 4-tuple, except time-ordered. sorted via python.list.sort(key= lambda timestamp: timestamp[0]) method.
    # NOTE - i switched the order around so that current_capture_element goes from the [1] position in the tuple to the [0] position in the 4-tuple array of TimeOrderedEvents.
    # this is an oversight that may complicate things, will need to patch this up later.

