import pandas
import numpy
import MimicBrowsing
import MimicDictionaries
import MimicObjects
import Context
import MimicServer
import datetime
import string

class MockingBird:
    def __init__(self, _ip="127.0.0.1", _port="5432", _uid="postgres", _pw="postgres", _db="mimic", _sch="mimiciii", _columnselection = ["*"], _tablesearchspace=["chartevents", "labevents", "cptevents", "datetimeevents", "diagnoses_icd", "procedures_icd", "procedureevents_mv", "noteevents"]): #, "noteevents"]):
        # 9/1/2018 - added "noteevents" to the _tablesearchspace default search string list. if bugs, remove noteevents.
        # 9/1/2018 - ^ this bugs out due to MimicObjects.Chart.MergeChartsByTime_branch1 not having the right default parameter for keylabels
        ##################################### WRAPPED PLATFORM#################
        self._browserplatform = MimicBrowsing.PlatformBrowser.ctor4(_ip=_ip, _port=_port, _uid=_uid, _pw=_pw, _db=_db, _sch=_sch, _columnselection=_columnselection, _tables=_tablesearchspace)
        self._browserplatform.connect()
        # MimicBrowsing.PlatformBrowser - inherits MimicServerPlatform + MimicCursor
        # MimicServer.MimicServerPlatform -
            # connectionconfiguration: provides ip, port, id, pw, db, schema
            # ?tables configuration?? necessary?
            # connection attribute - psycopg2 connection
            # connection string
            # ?tablenames?? necessary?
            # (method) connect()
        # MimicBrowsing.MimicCursor -
            # ?tableindex (shows current position in "tables of interest" list), like a cursor??? is this necessary?
            #
        # MimicBrowsing.PlatformBrowser - (derives from MimicBrowsing.MimicCursor [and also from MimicServer.MimicServerPlatform])
            # cursor attribute - psycopg2 cursor (derived from connection ^)
            # table searchspace -> needed to know which tables to derive patient data from

        ######################################## DICTIONARIES
        # self.mDictionaries = MimicDictionaries.DictionaryFrame.ctorDictionaries(_ip=_ip, _port=_port, _uid=_uid,
        #                                                                         _upw=_upw, _db=_db, _sch=_sch)
        # self.mObjects = MimicDictionaries.DictionaryFrame.ctorPeople(_ip=_ip, _port=_port, _uid=_uid, _upw=_upw,
        #                                                              _db=_db, _sch=_sch)
        # self.mSpans = MimicDictionaries.DictionaryFrame.ctorSpans(_ip=_ip, _port=_port, _uid=_uid, _upw=_upw, _db=_db,
        #                                                           _sch=_sch)
        # ctorItemIdDictionary
        # ctorCpt_CdDictionary
        # ctorIcd9_CodeDictionary
        # ctorSpans
        # ctorPeople
        # need dictionaries of 3 types - ItemId, CptCode, Icd9Code at baseline (see
        # 1a MimicDictionaries.DictionaryFrame.ctorDictionaries (d_items, d_labitems) - ItemIds
        # 1b NEW - """" ctorCPT (d_cpt) - CPT codes
        # 1c NEW - """" ctorICD (d_icd_procedures, d_icd_diagnoses) - ICD9
        # 2  """" ctorObjects (patients, caregivers)
        # 3  """" ctorSpans (admissions, icustays)

        # self.mDictionaryItemId = MimicDictionaries.DictionaryFrame.ctorItemIdDictionary(_ip=_ip, _port=_port, _uid=_uid, _upw=_pw, _db=_db, _sch=_sch)
        # self.mDictionaryCpt_Cd = MimicDictionaries.DictionaryFrame.ctorCpt_CdDictionary(_ip=_ip, _port=_port, _uid=_uid, _upw=_pw, _db=_db, _sch=_sch)
        # self.mDictionaryIcd9_Code = MimicDictionaries.DictionaryFrame.ctorCpt_CdDictionary(_ip=_ip, _port=_port, _uid=_uid, _upw=_pw, _db=_db, _sch=_sch)
        # self.mDictionaryHospitalStays = MimicDictionaries.DictionaryFrame.ctorHospitalStays(_ip=_ip, _port=_port, _uid=_uid, _upw=_pw, _db=_db, _sch=_sch)
        # self.mDictionaryPeople = MimicDictionaries.DictionaryFrame.ctorPeople(_ip=_ip, _port=_port, _uid=_uid, _upw=_pw, _db=_db, _sch=_sch)
        self._mDictionary = MimicDictionaries.DictionaryFrame.ctorFullDictionary(_ip=_ip, _port=_port, _uid=_uid, _upw=_pw, _db=_db, _sch=_sch)

    @property
    def connection(self):
        return self._browserplatform.connection

    @property
    def cursor(self):
        return self._browserplatform.cursor

    @cursor.setter
    def cursor(self, _cursorvalue):
        self._browserplatform.cursor=_cursorvalue

    @property
    def dictionary(self):
        return self._mDictionary.Data

    def Readall_numpy(self):
        return self._browserplatform.readallpandas()

    def Connect(self, newstr=""):
        self._browserplatform.connect(newstr)

    def Close(self):
        self._browserplatform.close()

    def _getchartraw(self, _filter="", _mimicEntry=None, _mimicObject=None, _keyvaluepair=()):

        # plan 1: _filter is a pure SQL string
        # plan 2: _filter is a sql_conditioncollection
        # plan 3: _filter is untouched and _mimicEntry is given (a numpy NDarray from recarray)
        # plan 4: _mimicObject instance provided (patient, caregiver... etc)
        # plan 5: _keyvaluepair (column_name, value_to_match) e.g. ("subject_id", 249)
        if len(_filter) > 0:
            self._browserplatform.Filters = [_filter]
            return self.Readall_numpy()

        if _mimicEntry != None: # <-- will be very important later on.
            # mimicEntry is considered to be single ROW from any Mimic table
            # this depends entirely on the TYPE of entry given - the unique identifier will depend on which type
            # e.g. if Patient Entry, then subject_id.
            # if Admission entry, then hadm_id.
            # if ChartEvent entry, then itemid, et cetera
            return None

        if _mimicObject != None:
            # implement later - for when mimic is entirely objectified.
            return None

        # if len(_filterdictionary) > 0:
        #     for eachkey, eachvalue in _filterdictionary:
        if len(_keyvaluepair) == 2:
            strwithin = str(_keyvaluepair[0])
            strwithin += "="
            strwithin += str(_keyvaluepair[1])
            self._browserplatform.Filters = [strwithin]
            # implement later
            return self.Readall_numpy()

        # ultimately we get a dictionary of the N "cardinal" chart tables filtered per the above.
        return None


    def _getchartsorted(self, _filter="", _mimicEntry=None, _mimicObject=None, _keyvaluepair=(), _outputfilepath="", _writetofile=False):
        achart = self._getchartraw(_filter=_filter, _mimicEntry=_mimicEntry, _mimicObject=_mimicObject, _keyvaluepair=_keyvaluepair)
        chartobj = MimicObjects.Chart(achart, self)
        if len(_outputfilepath) > 0:
            if _writetofile == True:
                chartobj.WriteToDisk(_outputfilepath)
        else:
            pathstring = ""
            pathstring += "C:\\MMd\\"
            pathstring += _filter
            pathstring += ".csv"
            if _writetofile == True:
                chartobj.WriteToDisk(pathstring)
        return chartobj.DataSorted
        # return MimicObjects.Chart(achart, self)


    def GetChartRecord(self, _filter="", _mimicEntry=None, _mimicObject=None, _keyvaluepair=(), _outputfilepath="", _writetofile=False):
        achart = self._getchartraw(_filter=_filter, _mimicEntry=_mimicEntry, _mimicObject=_mimicObject,
                                   _keyvaluepair=_keyvaluepair)
        chartobj = MimicObjects.Record(achart, self)
        if len(_outputfilepath) > 0:
            if _writetofile == True:
                chartobj.WriteToDisk(_outputfilepath)
        else:
            pathstring = ""
            pathstring += "C:\\MMd\\"
            pathstring += _filter
            pathstring += ".csv"
            if _writetofile == True:
                chartobj.WriteToDisk(pathstring)
        return chartobj


    def GetDictionaryItem(self, _keyname, _keyvalue):#_Filter="", _mimicEntry=None, _mimicObject=None):
        # _keyname = "itemid", _keyvalue = 50818
        for eachkey, eachtable in self.dictionary.items():
            eachtablecolumns = eachtable.dtype.names
            if _keyname in eachtablecolumns or str(_keyname) in eachtablecolumns:
                target = self.dictionary[eachkey][self.dictionary[eachkey][_keyname] == eachtable[_keyname][eachtable[_keyname] == _keyvalue]]
                #                                                           what did i do here? ^
                #                                        eachtable[_keyname] gives the entire list of values across all rows of that column
                #                                        eachtable[_keyname][eachtable[_keyname] == _keyvalue] -> value of a cell where keyname = keyvalue
                #                                 self.dictionary[eachkey][_keyname] gives list too (actually equal to eachtable[_keyname])
                if len(target) > 0:
                    return target
            else: # exceptions to this rule: (cpt_cd -> exists as a min, max value range [inclusive both ends] in d_cpt)
                if str(_keyname) == "cpt_cd":
                    cpt_dictionary = self.dictionary["d_cpt"]
                    for eachentry in cpt_dictionary:
                        if eachentry["codesuffix"] == None: # this means "T" or "F" is not part of the cpt_cd
                            _keyvalue = int(_keyvalue)
                            target = cpt_dictionary[numpy.logical_and(cpt_dictionary["mincodeinsubsection"] <= _keyvalue, cpt_dictionary["maxcodeinsubsection"] >= _keyvalue)]
                            if len(target) > 0:
                                return target
                        else: # this means that codesuffix is either T or F, meaning that cpt_cd's value (_keyvalue) is something like "0007F"
                            _keyvalue = str(_keyvalue)
                            laststr = _keyvalue[len(_keyvalue)-1]
                            firststr = ""
                            for eachcharacter in _keyvalue:
                                if eachcharacter.isdigit() == True:
                                    firststr += eachcharacter
                            _keyvalue_intvalue = int(firststr)
                            target = cpt_dictionary[numpy.logical_and(cpt_dictionary["mincodeinsubsection"] <= _keyvalue_intvalue, cpt_dictionary["maxcodeinsubsection"] >= _keyvalue_intvalue, cpt_dictionary["codesuffix"] == laststr)]
                            if len(target) > 0:
                                return target
        return None

    def TallyChart(self, _chart, _keycolumns={"itemid": type(int), "cpt_cd": type(str), "icd9_code": type(str)}, _specialkeycolumns={"cpt_cd":type(str)}):
        tallydictionary = {}
        for colkey, valtype in _keycolumns.items(): # cycle through default "dictionary key" names (3 of them)
            # if colkey not in _specialkeycolumns.keys():
            if str(colkey) not in tallydictionary.keys():
                thiscolumndictionary = {}
                tallydictionary.update({str(colkey): thiscolumndictionary})
            for eachkey, eachtable in _chart.items():
                # if str(colkey) in eachtable.dtype.names:
                if str(colkey) in eachtable.dtype.names:
                    for eachentry in eachtable:
                        # print(str(colkey))
                        examinedvalue = eachentry[str(colkey)]#str(colkey)]
                        examinedentry = self.GetDictionaryItem(str(colkey), examinedvalue) # exception is when colkey = d_cpt - take care of this in the GetDictionaryItem instance method itself
                        if examinedvalue in thiscolumndictionary.keys():
                            thiscolumndictionary[examinedvalue]["count"] += 1
                        else:
                            if str(colkey) not in _specialkeycolumns.keys():
                                thiscolumndictionary.update({examinedvalue: {"count": 1, "chart_entry": eachentry, "dictionary_entry": examinedentry}})
                            else:
                                if str(colkey) == "cpt_cd":
                                    thiscolumndictionary.update({examinedvalue: {"count": 1, "chart_entry": eachentry, "dictionary_entry": examinedentry}})


            # # for eachkey, eachtable in _dictofdicts
            # for colkey, valtype in _keycolumns.items():
            #     # if colkey not in _specialkeycolumns.keys():
            #     if str(colkey) not in tallydictionary.keys():
            #         thiscolumndictionary = {}
            #         tallydictionary.update({str(colkey): thiscolumndictionary})
            #     for eachkey, eachtable in _thechart_dictofnump.items():
            #         if str(colkey) in eachtable.dtype.names:
            #             for eachentry in eachtable:
            #                 examinedvalue = eachentry[str(colkey)]
            #                 if examinedvalue in thiscolumndictionary.keys():
            #                     thiscolumndictionary[examinedvalue] += 1
            #                 else:
            #                     thiscolumndictionary.update({examinedvalue: 1})
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


    def ProcessChart(self, _chart=None, _tally=None, _tostring_func=None, _outfilepath=""):
        if _tally == None:
            tally = self.TallyChart(_chart)
        else:
            tally = _tally
        # do other stuff like output to file, serialize, etc.
        if len(_outfilepath) > 0:
            astrr = _tostring_func(_chart, tally)
            # afile = open(_outfilepath, "x")
            # if _tostring_func == None:
            #     afile.write(str(tally))
            #     afile.write("\n__________________\n")
            #     afile.write(str(_chart))
            #     afile.close()
            # else:
            #     thestr = _tostring_func(_chart, tally)
            #     afile.write(thestr)
            #     afile.close()


    def _scanadmissions(self, _tostring_func=None, _rootdir="C:\\MMd\\", _writetofile=True):
        for eachentry in self.dictionary["admissions"]:
            filterstr = ""
            filterstr += "hadm_id="
            # print(type(eachentry["hadm_id"]))
            filterstr += str(eachentry["hadm_id"])
            filterstr += " AND "
            filterstr += "subject_id="
            filterstr += str(eachentry["subject_id"])
            #thisadmissionchart = self.GetChartRaw(_filter=filterstr)
            #thisadmissiontally = self.TallyChart(thisadmissionchart)
            thisadmissionfilepath = _rootdir
            thisadmissionfilepath += filterstr
            thisadmissionfilepath += ".csv"
            self._getchartsorted(_filter=filterstr, _outputfilepath=thisadmissionfilepath, _writetofile=_writetofile)
            # self.GetChartSorted()
            #self.ProcessChart(_chart=thisadmissionchart, _tally=thisadmissiontally, _tostring_func= _tostring_func, _outfilepath=thisadmissionfilepath) #_tostring_func(thisadmissionchart, thisadmissiontally), _outfilepath=thisadmissionfilepath)


    def ScanAdmissionsRecords(self, _tostring_func=None, _rootdir="C:\\MMd\\", _writetofile=True):
        for eachentry in self.dictionary["admissions"]:
            filterstr = ""
            filterstr += "hadm_id="
            # print(type(eachentry["hadm_id"]))
            filterstr += str(eachentry["hadm_id"])
            filterstr += " AND "
            filterstr += "subject_id="
            filterstr += str(eachentry["subject_id"])
            #thisadmissionchart = self.GetChartRaw(_filter=filterstr)
            #thisadmissiontally = self.TallyChart(thisadmissionchart)
            thisadmissionfilepath = _rootdir
            thisadmissionfilepath += filterstr
            thisadmissionfilepath += ".csv"
            self.GetChartRecord(_filter=filterstr, _outputfilepath=thisadmissionfilepath, _writetofile=_writetofile)


    #################### TRASH/DEPRECATED BELOW####################################################
    def GetDictionaryItem_Branch(self, _keyname, _keyvalue):#_Filter="", _mimicEntry=None, _mimicObject=None):
        # _keyname = "itemid", _keyvalue = 50818
        for eachkey, eachtable in self.dictionary.items():
            eachtablecolumns = eachtable.dtype.names
            if _keyname in eachtablecolumns or str(_keyname) in eachtablecolumns:
                target = self.dictionary[eachkey][self.dictionary[eachkey][_keyname] == eachtable[_keyname][eachtable[_keyname] == _keyvalue]]
                #                                                           what did i do here? ^
                #                                        eachtable[_keyname] gives the entire list of values across all rows of that column
                #                                        eachtable[_keyname][eachtable[_keyname] == _keyvalue] -> value of a cell where keyname = keyvalue
                #                                 self.dictionary[eachkey][_keyname] gives list too (actually equal to eachtable[_keyname])
                if len(target) > 0:
                    return target
            else: # exceptions to this rule: (cpt_cd -> exists as a min, max value range [inclusive both ends] in d_cpt)
                if str(_keyname) == "cpt_cd":
                    cpt_dictionary = self.dictionary["d_cpt"]
                    if _keyvalue.isnumeric() == True: # this means "T" or "F" is not part of the cpt_cd
                        _keyvalue = int(_keyvalue)
                        target = cpt_dictionary[numpy.logical_and(cpt_dictionary["mincodeinsubsection"] <= _keyvalue, cpt_dictionary["maxcodeinsubsection"] >= _keyvalue)]
                        if len(target) > 0:
                            return target
                    else: # this means that codesuffix is either T or F, meaning that cpt_cd's value (_keyvalue) is something like "0007F"
                        _keyvalue = str(_keyvalue)
                        laststr = _keyvalue[len(_keyvalue)-1]
                        firststr = ""
                        for eachcharacter in _keyvalue:
                            if eachcharacter.isdigit() == True:
                                firststr += eachcharacter
                        _keyvalue_intvalue = int(firststr)
                        target = cpt_dictionary[numpy.logical_and(cpt_dictionary["mincodeinsubsection"] <= _keyvalue_intvalue, cpt_dictionary["maxcodeinsubsection"] >= _keyvalue_intvalue, cpt_dictionary["codesuffix"] == laststr)]
                        # target = cpt_dictionary[
                        #          (cpt_dictionary["mincodeinsubsection"] <= _keyvalue_intvalue and cpt_dictionary[
                        #         "maxcodeinsubsection"] >= _keyvalue_intvalue and cpt_dictionary[
                        #         "codesuffix"] == laststr)]
                        if len(target) > 0:
                            return target

                            # codelow = eachentry["mincodeinsubsection"]
                            # codehi = eachentry["maxcodeinsubsection"]
                            # if _keyvalue >= codelow and _keyvalue <= codehi:
                            #     target = eachentry

                        # if eachentry["codesuffix"] == None:
                        #     print(eachentry)
            # #     TO BE IMPLEMENTED - difficulty in range 0001F - 0015F... let's say cpt_cd is 0007F (solution is to give F and T their own values... but there is some overlap if that happens. to be continued... 0 and 1? may not work due to overlap. might have to be 1000 and 2000, for example
        return None
    # def process_csv_debugged(self, chart, tally):
    #     bigstr = ""
    #     for eachkey, eachentity in tally.items():
    #         bigstr += str(eachkey) + ": \n"
    #         for
    #         # print(str(eachkey) + " ----- " + str(eachentity))
    #         for eachid, eachdict in eachentity.items():
    #             if eachid == "count":
    #                 bigstr += str(eachid) + " = "
    #                 bigstr += eachdict
    #                 bigstr += "\n"
    #             if eachid == "chart_entry":
    #                 bigstr += str(eachid) + " = "
    #                 for finalkey, finalentry in eachdict.items():
    #                     bigstr += str(finalkey)
    #                     bigstr += " = "
    #                     bigstr += finalentry
    #                     bigstr += ", "
    #                     bigstr += "\n"
    #             if eachid == "dictionary_entry":
    #                 bigstr += str(eachid) + " = "
    #                 for finalkey, finalentry in eachdict.items():
    #                     bigstr += str(finalkey)
    #                     bigstr += " = "
    #                     bigstr += finalentry
    #                     bigstr += ", "
    #                     bigstr += "\n"
    #     bigstr += "\n"
    #     bigstr += "-------------------------------------"
    #     bigstr += "\n"
    #     for eachkey, eachval in chart.items():
    #         bigstr += str(eachkey)
    #         bigstr += " = "
    #         bigstr += "\n"
    #
    #     return bigstr

    def process_csv(self, chart, tally):
        bigstr = ""
        for eachkey, eachentity in tally.items():
            bigstr += str(eachkey) + ": \n"
            print(str(eachkey) + " ----- " + str(eachentity))
            for eachid, eachdict in eachentity.items():
                if eachid == "count":
                    bigstr += str(eachid) + " = "
                    bigstr += eachdict
                    bigstr += "\n"
                if eachid == "chart_entry":
                    bigstr += str(eachid) + " = "
                    for finalkey, finalentry in eachdict.items():
                        bigstr += str(finalkey)
                        bigstr += " = "
                        bigstr += finalentry
                        bigstr += ", "
                        bigstr += "\n"
                if eachid == "dictionary_entry":
                    bigstr += str(eachid) + " = "
                    for finalkey, finalentry in eachdict.items():
                        bigstr += str(finalkey)
                        bigstr += " = "
                        bigstr += finalentry
                        bigstr += ", "
                        bigstr += "\n"
        bigstr += "\n"
        bigstr += "-------------------------------------"
        bigstr += "\n"
        for eachkey, eachval in chart.items():
            bigstr += str(eachkey)
            bigstr += " = "
            bigstr += "\n"

        return bigstr




# chartevents - charttime
# cptevents - chartDATE
# datetimeevents - charttime
# labevents - charttime
# procedureevents_mv - starttime, endtime
#
# procedures_icd - no timestamp
# diagnoses_icd - no timestamp
#


class MockingBirdPlus(MockingBird):
    def __init__(self, _ip="127.0.0.1", _port="5432", _uid="postgres", _pw="postgres", _db="mimic", _sch="mimiciii", _columnselection = ["*"], _tablesearchspace=["chartevents", "labevents", "cptevents", "datetimeevents"]):
        super().__init__(_ip=_ip, _port=_port, _uid=_uid, _pw=_pw, _db=_db, _sch=_sch, _columnselection=_columnselection, _tablesearchspace=_tablesearchspace)

    # two levels of dictionary-searching
    # 1) simply getting the dictionary entry
    # 2) getting the cpt_cd range entry - you know what i mean

            # def OrganizeChart(self, _chartdata):
            #    for eachkey, eachtable in _chartdata:
