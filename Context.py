import MimicDictionaries
import MimicBrowsing
import MimicObjects
import MimicServer
import pandas
import datetime


# class CohortBrowser:
#     def __init__(self, _ip="127.0.0.1", _port="5432", _uid="postgres", _upw="postgres", _db="mimic", _sch="mimiciii"):
#         self.mDictionaries = MimicDictionaries.DictionaryFrame.ctorDictionaries(_ip=_ip, _port=_port, _uid=_uid, _upw=_upw, _db=_db, _sch=_sch)
#         self.mObjects = MimicDictionaries.DictionaryFrame.ctorObjects(_ip=_ip, _port=_port, _uid=_uid, _upw=_upw, _db=_db, _sch=_sch)
#
#     @property
#     def Dictionary(self):
#         return self.mDictionaries.Data
#
#     @property
#     def People(self):
#         return self.mObjects.Data
#
#     @property
#     def

class CohortBrowser(MimicBrowsing.PlatformBrowser, MimicBrowsing.MimicCursor):
    def __init__(self, _ip="127.0.0.1", _port="5432", _uid="postgres", _upw="postgres", _db="mimic", _sch="mimiciii", _filters=[], _columnselection=["*"], _tables=["chartevents", "labevents", "cptevents", "datetimeevents"]):
        super().__init__()
        self.mDictionaries = MimicDictionaries.DictionaryFrame.ctorDictionaries(_ip=_ip, _port=_port, _uid=_uid, _upw=_upw, _db=_db, _sch=_sch)
        self.mObjects = MimicDictionaries.DictionaryFrame.ctorObjects(_ip=_ip, _port=_port, _uid=_uid, _upw=_upw, _db=_db, _sch=_sch)

    @classmethod
    def ctor0(cls, _db="mimic", _sch="mimiciii", _ip="127.0.0.1", _filters=[], _columnselection=["*"],
              _tables=["chartevents", "labevents", "cptevents", "datetimeevents"]):
        return cls(_db=_db, _sch=_sch, _ip=_ip, _filters=_filters, _columnselection=_columnselection, _tables=_tables)

    @classmethod
    def ctor1(cls, _db="mimic", _sch="mimiciii", _ip="127.0.0.1", _filters=[], _columnselection=["*"],
              _tables=["chartevents", "labevents", "cptevents", "datetimeevents"]):
        thisguy = CohortBrowser.ctor0(_db=_db, _sch=_sch, _ip=_ip, _filters=_filters, _columnselection=_columnselection, _tables=_tables)
        thisguy.__dict__.update(MimicServer.MimicServerPlatform.ctor1(_ip=_ip, _db=_db, _sch=_sch).__dict__)
        thisguy.__dict__.update(
            MimicBrowsing.MimicCursor.ctor3(_filters=_filters, _columnselection=_columnselection, _tablesearchspace=_tables).__dict__)
        thisguy.connect()
        thisguy._psycocursor = thisguy.connection.cursor()

        # (name="psycocursor")
        # thisguy._psycocursor.execute(thisguy.sqlcommandstring)
        return thisguy

    @property
    def Dictionary(self):
        return self.mDictionaries.Data

    @property
    def People(self):
        return self.mObjects.Data

    def GetPatientChart(self, _subjectid):
        self.Filters = []
        self.focusedtableindex = 0
        newstr = "subject_id="
        newstr += str(_subjectid)
        for eachcounter in range(0, self.tablesearchspaceLength):
            newfilter = MimicBrowsing.Filter(filterstring=newstr)
            self.Filters.extend(newfilter)
        return self.readallpandas()



class Context:
    def __init__(self):
        self.focus = None # a single mimicobject of any kind
        self.contexts = [] # list of mimicobjects related to the Focus - can be any type of object.
        # get contexts via lambda method below

    @property
    def Contexts(self):
        return self.contexts

    @property
    def Focus(self):
        return self.focus

    def SetFocus(self):
        pass # this will take a lambda Func and set the focused event.

    def GatherContexts(self):
        pass # this will take a lambda Func and set values for Contexts






