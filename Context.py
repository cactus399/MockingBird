import MimicDictionaries
import MimicBrowsing
import MimicObjects
import MimicServer
import pandas
import datetime
import enum
from collections import Counter


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
        # thisguy.__dict__.update(MimicServer.MimicServerPlatform.ctor0(_db=_db, _sch=_sch).__dict__)
        #         thisguy.__dict__.update(MimicCursor.ctor1(_schema=_sch).__dict__)
        # MimicServer.MimicServerPlatform.ctor3 -     def ctor3(cls, _db, _sch, _ip="127.0.0.1", _filters=[], _columnselection=["*"], _tables=["chartevents", "labevents", "cptevents", "datetimeevents"]):
        self.__dict__.update(MimicBrowsing.PlatformBrowser.ctor3(_db=_db, _sch=_sch, _ip=_ip, _filters=_filters, _columnselection=_columnselection, _tables=_tables).__dict__)
        # self.__dict__.update(MimicBrowsing.MimicCursor.ctor)
        #         thisguy.__dict__.update(MimicCursor.ctor3(_filters=_filters, _columnselection=_columnselection, _tablesearchspace=_tables).__dict__, _schema=_sch)

        self.__dict__.update(MimicBrowsing.MimicCursor.ctor3(_filters=_filters, _columnselection=_columnselection, _tablesearchspace=_tables, _schema=_sch).__dict__)

        self.mDictionaries = MimicDictionaries.DictionaryFrame.ctorDictionaries(_ip=_ip, _port=_port, _uid=_uid, _upw=_upw, _db=_db, _sch=_sch)
        self.mObjects = MimicDictionaries.DictionaryFrame.ctorPeople(_ip=_ip, _port=_port, _uid=_uid, _upw=_upw, _db=_db, _sch=_sch)
        self.mSpans = MimicDictionaries.DictionaryFrame.ctorHospitalStays(_ip=_ip, _port=_port, _uid=_uid, _upw=_upw, _db=_db, _sch=_sch)
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
              _tables=["chartevents", "labevents", "cptevents", "datetimeevents", "microbiologyevents", "noteevents", "procedureevents_mv", "procedures_icd"]):
        return cls(_db=_db, _sch=_sch, _ip=_ip, _filters=_filters, _columnselection=_columnselection, _tables=_tables)

    @classmethod
    def ctor1(cls, _db="mimic", _sch="mimiciii", _ip="127.0.0.1", _filters=[], _columnselection=["*"],
              _tables=["chartevents", "labevents", "cptevents", "datetimeevents", "microbiologyevents", "noteevents", "procedureevents_mv", "procedures_icd"]):
        thisguy = CohortBrowser.ctor0(_db=_db, _sch=_sch, _ip=_ip, _filters=_filters, _columnselection=_columnselection, _tables=_tables)
        thisguy.__dict__.update(MimicServer.MimicServerPlatform.ctor1(_ip=_ip, _db=_db, _sch=_sch).__dict__)
        thisguy.__dict__.update(
            MimicBrowsing.MimicCursor.ctor3(_filters=_filters, _columnselection=_columnselection, _tablesearchspace=_tables, _schema=_sch).__dict__)
        thisguy.connect()
        thisguy._psycocursor = thisguy.connection.cursor()

        # (name="psycocursor")
        # thisguy._psycocursor.execute(thisguy.sqlcommandstring)
        return thisguy

    @property
    def dictionary(self):
        #return self._dictionaries
        return self.mDictionaries._rawdata_unordered

    def Dictionary(self, _item=-1):
        if type(_item) == type(0):
            if _item < 0:
                return self.mDictionaries._rawdata_unordered
            else:
                return self.mDictionaries._rawdata_unordered[_item]
        else:
            for eachthing in self.mDictionaries._rawdata_unordered:
                if _item == eachthing.name:
                    return eachthing
                    break
                else:
                    return self.mDictionaries._rawdata_unordered
                    break
            return self.mDictionaries._rawdata_unordered
        return self.mDictionaries._rawdata_unordered

    @property
    def people(self):
        #return self._people
        return self.mObjects._rawdata_unordered

    def People(self, _item=-1):
        if type(_item) == type(0):
            if _item < 0:
                return self.mObjects._rawdata_unordered
            else:
                return self.mObjects._rawdata_unordered[_item]
        else:
            for eachthing in self.mObjects._rawdata_unordered:
                if _item == eachthing.name:
                    return eachthing
                else:
                    return self.mObjects._rawdata_unordered
            return self.mObjects._rawdata_unordered
        return self.mObjects._rawdata_unordered
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

    @property
    def admissions(self):
        return self.mSpans._rawdata_unordered["admissions"]

    @property
    def icustays(self):
        return self.mSpans._rawdata_unordered["icustays"]

    @property
    def patients(self):
        return self.mObjects._rawdata_unordered["patients"]

    @property
    def caregivers(self):
        return self.mObjects._rawdata_unordered["caregivers"]

    @property
    def d_cpt(self):
        return self.mDictionaries._rawdata_unordered["d_cpt"]

    @property
    def d_items(self):
        return self.mDictionaries._rawdata_unordered["d_items"]

    @property
    def d_labitems(self):
        return self.mDictionaries._rawdata_unordered["d_labitems"]

    @property
    def d_icd_procedures(self):
        return self.mDictionaries._rawdata_unordered["d_icd_procedures"]

    @property
    def d_icd_diagnoses(self):
        return self.mDictionaries._rawdata_unordered["d_icd_diagnoses"]

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

    def GetPatientChartGeneral(self, _filterstr):
        self.Filters = []
        self.focusedtableindex = 0
        self._data = None
        for eachcounter in range(0, self.tablesearchspaceLength):
            newfilter = MimicBrowsing.Filter(filterstring=_filterstr)
            self.Filters.append(newfilter)
        self._data = self.readallpandas()
        return self.Data

    def GetPatientChartByAdmission(self, _subjectid):
        thechart = self.GetPatientChart(_subjectid)
        hadm_for_patient = []
        #admpt = self.mSpans.Data[]
        # print(self.mSpans.Data["admissions"]["hadm_id"==_subjectid])

        # for eachentry in self.mSpans.Data["admissions"]:



        #tc = pandas.DataFrame(thech)

    def OrganizePatient(self, _subjectid, fileoutputbase=""):
        bigdata = self.GetPatientChartByAdmissions(_subjectid)
        #itemidX = "itemid_"
        #itemidX += "\\"
        #cptidX = "cptid_"
        #cptidX += "\\"
        #icd9idX = "icd9id_"
        #icd9idX += "\\"

        tally_itemid = {}
        tally_cptid = {}
        tally_icd9id = {}

        genout = {}

        itemidFilestr = fileoutputbase
        itemidFilestr += "\\"
        #itemidFilestr += itemidX
        for eachkey, eachrecarray in bigdata.items():
            filestr_this_itemid = itemidFilestr
            filestr_this_itemid += "subjectid_"
            filestr_this_itemid += str(_subjectid)
            filestr_this_itemid += "_"
            filestr_this_itemid += "hadmid_"
            filestr_this_itemid += str(eachkey)
            filestr_this_itemid += "_itemidset"
            filestr_this_itemid += ".csv"
            if len(fileoutputbase) > 0:
                itemidtally = self.process1(eachrecarray, filestr_this_itemid)
            else:
                itemidtally = self.process1(eachrecarray)
                if eachkey not in tally_itemid:
                    tally_itemid.update({eachkey: itemidtally})

        genout.update({"itemid": tally_itemid})
        genout.update({"d_cpt": tally_cptid})
        genout.update({"d_icd9code": tally_icd9id})
        return genout

    def ProcessChart(self, thechart, afunc):
        return afunc(thechart)

    def dictionary_to_file(self, adictionary, filepathway):
        afile = open(filepathway, "x")

        afile.close()

    def process1(self, thechart, filepath=""):
        tally_itemid = {}
        # chartevents, labevents, datetimeevents, procedureevents_mv
        accepting_list = ["chartevents", "labevents", "datetimeevents", "procedureevents_mv"]
        for intindex in range(0, len(accepting_list)):
            tableinterest = accepting_list[intindex]
            selectedtable = thechart[tableinterest]
            for eachentry in selectedtable:
                if eachentry["itemid"] in tally_itemid:
                    tally_itemid[eachentry["itemid"]] += 1
                else:
                    tally_itemid.update({eachentry["itemid"]:1})
        if len(filepath) <= 0:
            return self.GetStrKeyIdDictionary(tally_itemid, "itemid", ["label"])
        else:
            afile = open(filepath, "x")
            contents = self.GetStrKeyIdDictionary(tally_itemid, "itemid", ["label"])
            afile.write(contents)
            afile.close()
            return contents

    def process2(self, thechart, filepath=""):
        tally_itemid = {}
        # chartevents, labevents, datetimeevents, procedureevents_mv
        accepting_list = ["chartevents", "labevents", "datetimeevents", "procedureevents_mv"]
        for intindex in range(0, len(accepting_list)):
            tableinterest = accepting_list[intindex]
            selectedtable = thechart[tableinterest]
            for eachentry in selectedtable:
                if eachentry["itemid"] in tally_itemid:
                    tally_itemid[eachentry["itemid"]] += 1
                else:
                    tally_itemid.update({eachentry["itemid"]: 1})
        if len(filepath) <= 0:
            return self.GetStrKeyIdDictionary(tally_itemid, "itemid", ["label"])
        else:
            afile = open(filepath, "x")
            contents = self.GetStrKeyIdDictionary(tally_itemid, "itemid", ["label"])
            afile.write(contents)
            afile.close()
            return contents
        # tally_cptcode = {}
        # # cptevents
        # return tally_cptcode

    def process3(self, thechart, filepath=""):
        tally_itemid = {}
        # chartevents, labevents, datetimeevents, procedureevents_mv
        accepting_list = ["chartevents", "labevents", "datetimeevents", "procedureevents_mv"]
        for intindex in range(0, len(accepting_list)):
            tableinterest = accepting_list[intindex]
            selectedtable = thechart[tableinterest]
            for eachentry in selectedtable:
                if eachentry["itemid"] in tally_itemid:
                    tally_itemid[eachentry["itemid"]] += 1
                else:
                    tally_itemid.update({eachentry["itemid"]: 1})
        if len(filepath) <= 0:
            return self.GetStrKeyIdDictionary(tally_itemid, "itemid", ["label"])
        else:
            afile = open(filepath, "x")
            contents = self.GetStrKeyIdDictionary(tally_itemid, "itemid", ["label"])
            afile.write(contents)
            afile.close()
            return contents
        # tally_icd9code = {}
        # # procedures_icd
        # return tally_icd9code




    def GetPatientChartByAdmissions(self, _subjectid):
        achart=self.GetPatientChart(_subjectid)
        bigchart = {}
        admidlist = self.admissions[self.admissions.subject_id==_subjectid]
        for eachadm_id in admidlist["hadm_id"]:
            newchart = {}
            for eachkey, eachrecarray in achart.items():
                newrecarray = eachrecarray[eachrecarray.hadm_id==eachadm_id]
                if eachkey not in newchart:
                    newchart.update({eachkey: newrecarray})#eachrecarray.name: newrecarray})
            if eachadm_id not in bigchart:
                bigchart.update({eachadm_id: newchart})
        return bigchart

        # admids = {}
        # for eachkey, eachthing in achart.items():
        #     print(eachthing.dtype.names)
        #     if "hadm_id" in eachthing.dtype.names:
        #         for eachentry in eachthing:
        #             common = str(eachentry["hadm_id"])
        #             if common not in admids.keys():
        #                 print(common)
        #                 admids.update({common: eachkey})
        #                 # admids.update({eachentry["hadm_id"]: eachkey})
        #                 #admids.update({eachentry["hadm_id"]})
        # return admids

    def GetPatientAdmissionsIds(self, _subjectid):
        at = self.admissions[self.admissions.subject_id==_subjectid]
        return at["hadm_id"]
        #print(self.mSpans.Data["admissions"]["subject_id"] == _subjectid)

        # for eachthing in self.mSpans.Data["admissions"]:
        #     if eachthing["subject_id"] == _subjectid:
        #         print(eachthing)
    #["subject_id"==_subjectid])#"#["subject_id"==_subjectid])#["subject_id"==str(_subjectid)])
        # for eachtable in self.mSpans.Data["admissions"]:
        #     print(eachtable["subject_id"==_subjectid])
            #print(eachtable["subject_id"==_subjectid])
            # admids.extend(eachtable[eachtable["subject_id"]=_subjectid])

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

    def GetStrKeyIdDictionary(self, tally, id_colname, id_label):
        astr = ""
        for eachkey, eachvalue in tally.items():
            aname = self.FindKeyLabel(id_colname, eachkey, id_label)
            astr += str(eachkey)
            astr += ","
            astr += aname
            astr += ","
            astr += str(eachvalue)
            astr += "\n"
        else:
            return astr
        return astr

    def FindKeyLabel(self, id_colname, id_value, id_label):
        for eachkey, eachtable in self.dictionary.items():
            if id_colname in eachtable.dtype.names:
                for eachnumber in range(0, len(eachtable)):
                    if id_value == eachtable[id_colname][eachnumber] or str(id_value) == eachtable[id_colname][eachnumber]:
                        for eachlabel in id_label:
                            if eachlabel in eachtable.dtype.names:
                                return eachtable[eachlabel][eachnumber]
                        #return eachtable[id_label][eachnumber]

    def GetItemName(self, itemid):
        # for eachkey, eachtable in self.dictionary.items():
        #     print(eachtable.dtype.names)
        for eachkey, eachtable in self.dictionary.items():
            if "itemid" in eachtable.dtype.names:
                for eachnumber in range(0,len(eachtable)):
                    if itemid == eachtable["itemid"][eachnumber]:
                        return eachtable["label"][eachnumber]

    def GetName(self, identifier_label, value_label, identifier_index):
        for eachkey, eachtable in self.dictionary.items():
            if identifier_label in eachtable.dtype.names:
                for eachnumber in range(0,len(eachtable)):
                    if identifier_index == eachtable[identifier_label][eachnumber]:
                        return eachtable[value_label][eachnumber]

    #def GetItemID(self, ):

                # for akey, avalue in eachtable["itemid"]:
                #     if itemid == avalue:
                #         return eachtable["label"][akey]
                # # if itemid in eachtable["itemid"]:
                # #     return eachtable["label"]
                # #return eachtable["itemid"][itemid]

    def ChartFiltered(self, _subjectid, thefunc):
        ptchart = self.GetPatientChart(_subjectid)
        return thefunc(ptchart)

    def TallyDictionary(self, outpath):
        adictionary = {}
        acounter = 0
        for eachpt in self.people["patients"]:
            acounter += 1
            print(acounter)
            ptchart = self.GetPatientChart(eachpt["subject_id"])
            for eachkey, eachtable in ptchart.items():
                if eachkey != "cptevents":
                    itemidd = eachtable["itemid"]
                    for eachid in itemidd:
                        if eachid in adictionary:
                            adictionary[eachid] += 1
                        else:
                            adictionary.update({eachid:1})
            # if acounter >= 5000:
            #     return adictionary
                        # for eacheachid in eachid:
                        #     if eacheachid in adictionary:
                        #         adictionary[eacheachid] += 1
                        #     else:
                        #         adictionary.update(eacheachid=0)
        return adictionary

    def GetPatientAdmissions(self, subjid):
        admids = {}




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


class DictionaryTally:
    def __init__(self, _dictofdicts=None, _thechart_dictofnump=None):
        self._backingfield = None

    @classmethod
    def TallyChart(cls, _thechart_dictofnump, _keycolumns={"itemid":type(int), "cpt_cd":type(str), "icd9_code":type(str)}): #, _specialkeycolumns={"cpt_cd":type(str)}): #, _specialkeycolumns={"cpt_cd": type(str)}):
        #{("itemid",type(int)), ("cpt_cd",type(str)), ("icd9_code",type(str))}):
        tallydictionary = {}
        # for eachkey, eachtable in _dictofdicts
        for colkey, valtype in _keycolumns.items():
            # if colkey not in _specialkeycolumns.keys():
            if str(colkey) not in tallydictionary.keys():
                thiscolumndictionary = {}
                tallydictionary.update({str(colkey): thiscolumndictionary})
            for eachkey, eachtable in _thechart_dictofnump.items():
                if str(colkey) in eachtable.dtype.names:
                    for eachentry in eachtable:
                        examinedvalue = eachentry[str(colkey)]
                        if examinedvalue in thiscolumndictionary.keys():
                            thiscolumndictionary[examinedvalue] += 1
                        else:
                            thiscolumndictionary.update({examinedvalue: 1})
            # implement below:
            # if colkey in _specialkeycolumns.keys():
            #     for eachkey, eachtable in _thechart_dictofnump.items():
            #         if str(colkey) in eachtable.dtype.names:
            #             for eachentry in eachtable:
            #                 examinedvalue = eachentry[str(colkey)]
            #                 if examinedvalue in thiscolumndictionary.keys


            # else:
            #     if colkey == "cpt_cd":
            #         if str(colkey) not in tallydictionary.keys():
            #             thiscolumndictionary = {}
            #             tallydictionary.update({str(colkey): thiscolumndictionary})
            #         for eachkey, eachtable in _thechart_dictofnump.items():
            #             # str(colkey) is "cpt_cd" which is NOT in the dictionary file. ranges are.
            #             if str(colkey) in eachtable.dtype.names:
            #                 for eachentry in eachtable:
            #                     examinedvalue = eachentry[str(colkey)] # <- note that this is a string value
            #                     if examinedvalue in thiscolumndictionary.keys():
            #                         thiscolumndictionary[examinedvalue] += 1
            #                     else:
            #                         thiscolumndictionary.update({examinedvalue: 1})

                                # this is where things get tricky.
                                # cpt_cd is actually a STRING literal of an integer.
                                # sometimes it can have a single character SUFFIX (either T or F, but regardless)
                                # cast to int and see if an error comes out. if it does, it has a suffix.

                                # try:
                                # ^ for different method.
        return tallydictionary
            #^ tally itemid, cpt_cd, and icd9_codes
    #
    # @classmethod
    # def TallyChartWithNames(cls, _thechart_dictofnump, _keycolumns={"itemid":type(int), "cpt_cd":type(str), "icd9_code":type(str)}):

    # def FinalTally(self, _dictofdicts, _thechart_dictofnump, _keycolumns={"itemid":type(int), "cpt_cd":type(str), "icd9_code":type(str)}, _specialkeycolumns={"cpt_cd": type(str)}):
    #
    #     tallied = self.TallyChart(_thechart_dictofnump, _keycolumns=_keycolumns, _specialkeycolumns=_specialkeycolumns)
    #     for eachkey, eachdict in tallied.items():
    #
    #     # structure of "tallied":
    #     # { ("itemid":
    #     # for eachkey, eachoccurencevalue in tallied.items():




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






