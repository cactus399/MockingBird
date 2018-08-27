import MimicDictionaries
import MimicBrowsing
import MimicObjects
import MimicServer
import pandas
import datetime
import enum


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
        #"#]):#, "cptevents"]):#, "datetimeevents"]):
        super().__init__()
        self.mDictionaries = MimicDictionaries.DictionaryFrame.ctorDictionaries(_ip=_ip, _port=_port, _uid=_uid, _upw=_upw, _db=_db, _sch=_sch)
        self.mObjects = MimicDictionaries.DictionaryFrame.ctorObjects(_ip=_ip, _port=_port, _uid=_uid, _upw=_upw, _db=_db, _sch=_sch)
        # _dictnames = []
        # for eachthing in self.mDictionaries.Data:
        #     _dictnames.extend(eachthing.name)
        # _objnames = []
        # for eachthing in self.mObjects.Data:
        #     _objnames.extend(eachthing.name)
        # self._dictionaries = pandas.DataFrame(self.mDictionaries.Data, columns=_dictnames)
        # self._people = pandas.DataFrame(self.mObjects.Data, columns=_objnames)
        self._data=None

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
    def dictionary(self):
        #return self._dictionaries
        return self.mDictionaries.Data

    def Dictionary(self, _item=-1):
        if type(_item) == type(0):
            if _item < 0:
                return self.mDictionaries.Data
            else:
                return self.mDictionaries.Data[_item]
        else:
            for eachthing in self.mDictionaries.Data:
                if _item == eachthing.name:
                    return eachthing
                    break
                else:
                    return self.mDictionaries.Data
                    break
            return self.mDictionaries.Data
        return self.mDictionaries.Data

    @property
    def people(self):
        #return self._people
        return self.mObjects.Data

    def People(self, _item=-1):
        if type(_item) == type(0):
            if _item < 0:
                return self.mObjects.Data
            else:
                return self.mObjects.Data[_item]
        else:
            for eachthing in self.mObjects.Data:
                if _item == eachthing.name:
                    return eachthing
                else:
                    return self.mObjects.Data
            return self.mObjects.Data
        return self.mObjects.Data
        # if _item < 0:
        #     return self.mObjects.Data
        # else:
        #     if type(_item) == type(0):
        #         return self.mObjects.Data[_item]
        #     else:
        #         for eachthing in self.mObjects.Data:
        #             if _item == eachthing.name:
        #                 return eachthing
        #             else:
        #                 return self.mObjects.Data
        #         return self.mObjects.Data
        # return self.mObjects.Data

    @property
    def Data(self):
        return self._data

    def data(self, _item=-1):
        if _item < 0:
            return self._data
        else:
            if type(_item) == type(0):
                return self._data
            else:
                for eachthing in self._data:
                    if _item == eachthing.name:
                        return eachthing
                    else:
                        return self._data
                return self._data
        return self._data

    def __getitem__(self, item):
        if self.Data != None:
            if type(item) == type(0):
                return self.Data[item]
            else:
                for eachthing in self.Data:
                    if item == eachthing.name:
                        return eachthing
                return None
        return None

    def GetPatientChart(self, _subjectid):
        self.Filters = []
        self.focusedtableindex = 0
        self._data=None
        newstr = "subject_id="
        newstr += str(_subjectid)
        for eachcounter in range(0, self.tablesearchspaceLength):
            newfilter = MimicBrowsing.Filter(filterstring=newstr)
            self.Filters.append(newfilter)
        self._data = self.readallpandas()
        return self.Data

    def GetPatientChartFiltered(self, _subjectid, *args):
        self.Filters = []
        self.focusedtableindex = 0
        self._data=None
        newstr = "subject_id="
        newstr += str(_subjectid)
        for eacharg in args:
            thisstr = eacharg


    def GetPatientChartFiltered2(self, _subjectid, _flist):
        ptchart = self.GetPatientChart(_subjectid)
        freshchart = []
        chartslen = len(ptchart)
        for eachchart in range(0, chartslen):
            filterstr = _flist[eachchart]
            freshchart.append(ptchart[eachchart][filterstr])
        return freshchart
        #
        #     for eacharg in args:
        #         freshchart.extend(ptchart[eachchart][ptchart])
        #
        # for eacharg in args:

    def ChartFiltered(self, _subjectid, thefunc):
        ptchart = self.GetPatientChart(_subjectid)
        return thefunc(ptchart)

    # def ChartFiltered(self, _subjectid, lambdalist):



    # def GetPatientChartsAll(self, _outrootdir):
    #     for eachpt in self.People[0].iterrows():
    #         subjid = eachpt[1].loc["subject_id"]
    #         ptdat = self.GetPatientChart(subjid)
    #         afilepath = _outrootdir
    #         afilepath += subjid
    #         afilepath += ".txt"
    #         afile = open(afilepath, "x")
    #         afile.write(str(ptdat))

    # def GetCohortPatientList(self, afunc, *args):
    #     filterlist = []
    #     for eachthing in args:


    # def GetCohortPatientList(self, _sqlstringbuilderFunc, *args):
    #     return _sqlstringbuilderFunc(*args)
    #
    # def GetCohortCharts(self, _cohortbinder):
    #     pass


# class CohortBinder:
#     def __init__(self, _):


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






