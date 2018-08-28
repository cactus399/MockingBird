# import pandas
# import psycopg2
# import MimicServer
#
# # NOTE:
# # the events ("shit that happened") are timestamped.
# # the events should be browsed in temporal order
# # REGARDLESS of which table it belongs to.
# # DbBrowser - have multiple cursors associated with a single connection
# # Megacursor will wrap all event cursors - Megacursor will have a method "fetchone()"
# # just like cursor. "fetchone()" will actually not advance any of the cursors
#
# class SubCursor:
#     def __init__(self, _mimicserverplatform=None, _sqlcommand=""):
#         self._mimicserverplatform = _mimicserverplatform
#         self._sqlcommand = _sqlcommand
#
#     @property
#     def sqlcommand(self):
#         return self._sqlcommand
#
#
# class DbBrowser(MimicServer.MimicServerPlatform):
#     def __init__(self):
#         super().__init__()
#         self._cursorcollection = None
#         self._stagingarray = None
#
# class DbBrowserSchema: # describes the variable across which DbBrowser will traverse the database
#     def __init__(self):
#         pass
#
# class
#
#
# # class DbBrowser(MimicServer.MimicServerPlatform):
# #     def __init__(self):
# #         super().__init__()

import pandas
import psycopg2
import MimicServer


class Logical:
    def __init__(self, _intvalue=-1):
        self._intvalue = _intvalue

    def __str__(self):
        if self._intvalue == 0:
            return "AND"
        if self._intvalue == 1:
            return "OR"
        if self._intvalue == 2:
            return "NOT"
        else:
            return ""

    def __repr__(self):
        return self.__str__()

    @property
    def operator(self):
        return self.__str__()

    @operator.setter
    def operator(self, _operatorvalue):
        _tolower = _operatorvalue.lower()
        if _tolower == "and":
            self._intvalue = 0
        if _tolower == "or":
            self._intvalue = 1
        if _tolower == "not":
            self._intvalue = 2
        else:
            self._intvalue = -1


class ConditionUnit:
    def __init__(self, _totalstr):
        if len(_totalstr) > 0:
            abool = ',' in _totalstr
            if abool == True:
                split = _totalstr.split(',')
                self._comparison = split[1]
                self._left = split[0]
                self._right = split[2]
            else:
                self._comparison = ""
                self._left = ""
                self._right = ""
        else:
            self._comparison = ""
            self._left = ""
            self._right = ""

    @classmethod
    def ctor0(cls):
        return cls()

    def __str__(self):
        thestr = ""
        thestr += self._left + self._comparison + self._right
        return thestr

    def __repr__(self):
        return self.__str__()

    def __iter__(self):
        return iter(self.__str__())

    def __len__(self):
        return len(self.__str__())


class ConditionBundle:
    def __init__(self, _conditionunits=[], _logicals=[]):
        if _conditionunits != None:
            numunits = len(_conditionunits)
            if numunits > 0:
                self._logicals = [Logical(1)]*(numunits - 1)
            else:
                self._logicals = _logicals
        self._conditionunits = _conditionunits

    def __str__(self):
        thestr = ""
        thestr += "("
        counter = 0
        unitslength = len(self._conditionunits)
        for acondition in self._conditionunits:
            if counter > 0:
                thestr += " "
            thestr += str(acondition)
            if counter < unitslength - 1:
                thestr += " "
                thestr += str(self._logicals[counter])
            counter += 1
        thestr += ")"
        return thestr

    def __repr__(self):
        return self.__str__()

    def __iter__(self):
        return iter(self._conditionunits)

    def __len__(self):
        return len(self._conditionunits)

    def __getitem__(self, item):
        return self._conditionunits[item]


class ConditionCollection:
    def __init__(self, _unitsbundles=[], _logicals=[], _filterstring=""):
        self._unitsbundles = _unitsbundles
        self._logicals = _logicals
        self._plainstr = _filterstring

    def __str__(self):
        if len(self._plainstr) <= 0:
            thestr = ""
            counter = 0
            unitslength = len(self._unitsbundles)
            for acondition in self._unitsbundles:
                if counter > 0:
                    thestr += " "
                thestr += str(acondition)
                if counter < unitslength - 1:
                    thestr += " "
                    thestr += str(self._logicals[counter])
                counter += 1
            return thestr
        else:
            return self._plainstr

    def __repr__(self):
        return self.__str__()

    def __len__(self):
        if len(self._plainstr) > 0:
            return 1
        else:
            return len(self._unitsbundles)

    def __iter__(self):
        return iter(self._unitsbundles)

    def __getitem__(self, item):
        return self._unitsbundles[item]

    @property
    def filters(self):
        return self._unitsbundles

    @property
    def logicals(self):
        return self._logicals

    @property
    def filtercount(self):
        if self._unitsbundles != None:
            return len(self._unitsbundles)
        else:
            return 0

    @property
    def logicalcount(self):
        return len(self._logicals)


class Filter:
    def __init__(self,filterstring=None,conditionslist=None, logicals=None):
        self._filterstring = filterstring
        self._conditionslist=conditionslist
        self._logicals = logicals

    def __str__(self):
        if self._filterstring != None:
            return self._filterstring
        else:
            thestr = ""
            loglength = len(self._logicals)
            conlength = len(self._conditionslist)
            if loglength < conlength - 1:
                for ea in range(conlength - 1 - loglength):
                    self._logicals.extend(0)
            counter = 0
            for eachcondition in self._conditionslist:
                if counter > 0:
                    thestr += ""
                thestr += eachcondition
                if counter < conlength - 1:
                    thestr += " "
                    thestr += self._logicals[counter]

    def __repr__(self):
        return self.__str__()

    def __len__(self):
        if self._conditionslist != None:
            if len(self._conditionslist) > 0:
                return len(self._conditionslist)
        else:
            if self._filterstring != None:
                if len(self._filterstring) > 0:
                    return len(self._filterstring)
            else:
                return 0

    def __iter__(self):
        return iter([self])

#__________________________^ conditions: condition UNIT, BUNDLEs, COLLECTIONs.______________


class SqlCommandType:
    def __init__(self, _intvalue=-1):
        self._intvalue = _intvalue

    def __str__(self):
        if self._intvalue == 0:
            return "SELECT"
        # if self._intvalue == 1:
        #     return "UPDATE"
        # if self._intvalue == 2:
        #     return "DELETE"
        else:
            return ""

    def __repr__(self):
        return self.__str__()

    @property
    def operator(self):
        return self.__str__()

    @operator.setter
    def operator(self, _operatorvalue):
        _tolower = _operatorvalue.lower()
        if _tolower == "select":
            self._intvalue = 0
        # if _tolower == "or":
        #     self._intvalue = 1
        # if _tolower == "not":
        #     self._intvalue = 2
        else:
            self._intvalue = -1


class SqlColumnCollection:
    def __init__(self, _columns=['*']):
        self._columns = _columns

    def __str__(self):
        thestr = ""
        counter = 0
        capped = len(self._columns)
        if capped > 0:
            for eachcol in self._columns:
                thestr += eachcol
                if counter < capped - 1:
                    thestr += ', '
        return thestr

    def __repr__(self):
        return self.__str__()


class SqlCommand:
    def __init__(self, _sqlcommandtype=SqlCommandType(0), _columns=SqlColumnCollection(), _tablename="", _filtercoll=[]):
        self._sqlcommandtype = _sqlcommandtype
        self._tablename = _tablename
        self._columns = _columns
        # acoll = list()
        # acoll.extend(_filtercoll)
        self._filtercollection = _filtercoll

        ## - SELECT (* // col1, col2) FROM (tablename) WHERE (str(filtercollection))

    def __str__(self):
        thestr = ""
        thestr += str(self._sqlcommandtype)
        ##thestr += " "
        # Part 1 : ^ "SELECT "

        thestr += " "
        thestr += str(self._columns)
        # acounter = 0
        # acap = len(self._columns)
        # # if columncount is greater than 1,must add them according to following nomenclature:
        # # SELECT col1, col2, col3... WHERE (filtercollection str);
        # for eachcol in self._columns:
        #     thestr += eachcol
        #     if acounter < acap - 1:
        #         thestr += ', '


        # Part 2 : ^ "*" or "colname1, colname2..."

        thestr += " FROM "
        thestr += self._tablename
        # Part 2a: ^ " FROM tablename

        acounter = 0
        if self._filtercollection != None:
            acap = len(self._filtercollection)
            if acap > 0:
                thestr += ' WHERE '
                thestr += str(self._filtercollection)
                # for eachfilter in self._filtercollection.filters:
            #     thestr += str(eachfilter)
            #     if acounter < acap - 1:
            #         thestr += ', '
            #     acounter += 1
            #     #--
        # Part 3 : ^ " WHERE str(filtercollection)

        thestr += ";"
        # Part 4 : ^ ";"

        return thestr
    ## ^ returns something like "SELECT * FROM table WHERE a=1 AND b=2 AND (c<3 OR d>4)"

    def __repr__(self):
        return self.__str__()

    @property
    def tablename(self):
        return self._tablename

    @tablename.setter
    def tablename(self, _tablenamevalue):
        self._tablename = _tablenamevalue

    @property
    def columns(self):
        return self._columns

    @columns.setter
    def columns(self, _columnsvalue):
        self._columns = _columnsvalue

    @property
    def filtercollection(self):
        return self._filtercollection

    @filtercollection.setter
    def filtercollection(self, _filtercollectionvalue):
        self._filtercollection = _filtercollectionvalue
# ____________________^ SqlColumnCollection, SqlCommand, SqlCommandType ___________


class MimicCursor:
    # def __init__(self, _tablesearchspace=[], _tableindex=-1, _sqlcmd=SqlCommand()):
    #     self._tablesearchspace = _tablesearchspace
    #     self._tableindex = _tableindex
    #     self._sqlcmd = _sqlcmd

    # def __init__(self, _tablesearchspace=[], _tableindex=-1, _filterset=[], _columnselection=[]):
    #     #_filterset=ConditionCollection(), _columnselection=SqlColumnCollection()):
    #     self._tablesearchspace = _tablesearchspace
    #     self._tableindex = _tableindex
    #     self._columnselection = _columnselection
    #     self._filterset = _filterset
    def __init__(self, _tablesearchspace=["chartevents", "labevents", "cptevents", "datetimeevents"], _tableindex=0, _columnselection=["*"], _filterset=[]): #, _subject_id="103"):
        # cu = ConditionUnit("subject_id,=," + _subject_id)
        # cb = ConditionBundle(_conditionunits=[cu])
        # cc = ConditionCollection(_unitsbundles=[cb])
        # _filters = [cc] * len(_tablesearchspace)
        columnselectionlength = len(_columnselection)
        filterselectionlength = len(_filterset)
        _searchspacelength = len(_tablesearchspace)
        columnselectionDelta = _searchspacelength - columnselectionlength
        filterselectionDelta = _searchspacelength - filterselectionlength
        if columnselectionlength < _searchspacelength:
            for each in range(columnselectionDelta):
                _columnselection.extend(["*"])

        if filterselectionlength > 0:
            if filterselectionlength < _searchspacelength:
                for each in range(filterselectionDelta):
                    _filterset.extend(_filterset[-1])

        # for each in range(len(_tablesearchspace)):
        #     self._columnselection.extend(_columnselection)
        self._filterset = _filterset # * len(_tablesearchspace)
        self._columnselection = _columnselection
        self._tablesearchspace = _tablesearchspace
        self._tableindex = _tableindex
        #self._columnselection = _columnselection
        #if len(_filterset) > 0:
        #self._filterset = _filters

    @classmethod
    def ctor0(cls):
        return cls()

    @classmethod
    def ctor1(cls, _tablesearchspace=["patients","caregivers"], _tableindex=0, _columnselection=["*"]):
        #, "labevents", "cptevents", "datetimeevents"], _tableindex=0, _columnselection=["*"]):
        _columnselection = ["*"]*len(_tablesearchspace)
        thisguy = cls(_tablesearchspace=_tablesearchspace, _tableindex=_tableindex, _columnselection=_columnselection)
        #thisguy._columnselection = thisguy._columnselection * len(_tablesearchspace)
        return thisguy

    @classmethod
    def ctor2(cls, _tablesearchspace=["chartevents", "labevents", "cptevents", "datetimeevents"], _tableindex=0, _columnselection=["*"], _subject_id="103"):
        cu = ConditionUnit("subject_id,=,"+_subject_id)
        cb = ConditionBundle(_conditionunits=[cu])
        cc = ConditionCollection(_unitsbundles=[cb])
        _filters = [cc] * len(_tablesearchspace)
        _columnselection = ["*"] * len(_tablesearchspace)
        thisguy = cls(_tablesearchspace=_tablesearchspace, _tableindex=_tableindex, _columnselection=_columnselection, _filterset=_filters, _subject_id=_subject_id)
        # thisguy._columnselection = thisguy._columnselection * len(_tablesearchspace)
        return thisguy

    @classmethod
    def ctor3(cls, _tablesearchspace=["chartevents", "labevents", "cptevents", "datetimeevents"], _tableindex=0, _columnselection=["*"], _filters=[Filter("patient=501")]):
        thisguy = cls(_tablesearchspace=_tablesearchspace, _tableindex=_tableindex, _columnselection=_columnselection, _filterset=_filters)
        return thisguy

    @property
    def ___hide___columns(self):
        return self._columnselection[self.focusedtableindex]

    @property
    def ___hide___filters(self):
        if len(self._filterset) > 0:
            return self._filterset[self.focusedtableindex]
        else:
            return None
        # if self._filterset != None:
        #     if self.focusedtableindex < len(self._filterset):
        #         return self._filterset[self.focusedtableindex]
        # else:
        #     return ""

    @property
    def sqlcommandstring(self):
        aguy = SqlCommand(_columns=self.___hide___columns, _filtercoll=self.___hide___filters, _tablename=self.focusedtablename)
        # hello = ConditionCollection(_filterstring=self.___hide___filters)
        return str(aguy)


    @property
    def tablesearchspace(self):
        return self._tablesearchspace

    @tablesearchspace.setter
    def tablesearchspace(self, _value):
        self._tablesearchspace = _value

    @property
    def tablesearchspaceLength(self):
        return len(self.tablesearchspace)

    @property
    def focusedtableindex(self):
        return self._tableindex

    @focusedtableindex.setter
    def focusedtableindex(self, _tableindexvalue):
        self._tableindex = _tableindexvalue
        # if _tableindexvalue < self.tablesearchspaceLength:
        #     self._tableindex = _tableindexvalue
        # else:
        #     self._tableindex = self.tablesearchspaceLength - 1

    @property
    def focusedtablename(self):
        if self.tablesearchspaceLength > 0:
            return self.tablesearchspace[self.focusedtableindex]
        else:
            return ""

    @focusedtablename.setter
    def focusedtablename(self, _value):
        lowervalue = _value.lower()
        counter = 0
        for eachstr in self.tablesearchspace:
            if lowervalue == eachstr:
                self._tableindex = counter
                break
            else:
                counter += 1

    @property
    def Filters(self):
        return self._filterset

    @Filters.setter
    def Filters(self, _fvalues):
        self._filterset = _fvalues


class PlatformBrowser(MimicServer.MimicServerPlatform, MimicCursor):
    def __init__(self):
        super().__init__()
        self._psycocursor = None

    @classmethod
    def ctor0(cls):
        return cls()

    @classmethod
    def ctor1(cls, _db, _sch):
        thisguy = PlatformBrowser.ctor0()
        thisguy.__dict__.update(MimicServer.MimicServerPlatform.ctor0(_db=_db, _sch=_sch).__dict__)
        thisguy.__dict__.update(MimicCursor.ctor1().__dict__)
        thisguy.connect()
        thisguy._psycocursor = thisguy.connection.cursor()#(name="psycocursor")
        #thisguy._psycocursor.execute(thisguy.sqlcommandstring)
        return thisguy

    @classmethod
    def ctor2(cls, _db, _sch, _subject_id="103"):
        thisguy = PlatformBrowser.ctor0()#(_db, _sch, _subject_id=_subject_id)
        thisguy.__dict__.update(MimicServer.MimicServerPlatform.ctor0(_db=_db, _sch=_sch).__dict__)
        thisguy.__dict__.update(MimicCursor.ctor2(_subject_id=_subject_id).__dict__)
        thisguy.connect()
        thisguy._psycocursor = thisguy.connection.cursor()#(name="psycocursor")
        #thisguy._psycocursor.execute(thisguy.sqlcommandstring)
        return thisguy

    @classmethod
    def ctor3(cls, _db, _sch, _ip="127.0.0.1", _filters=[], _columnselection=["*"], _tables=["chartevents", "labevents", "cptevents", "datetimeevents"]):
        thisguy = PlatformBrowser.ctor0()
        thisguy.__dict__.update(MimicServer.MimicServerPlatform.ctor1(_ip=_ip, _db=_db, _sch=_sch).__dict__)
        thisguy.__dict__.update(MimicCursor.ctor3(_filters=_filters, _columnselection=_columnselection, _tablesearchspace=_tables).__dict__)
        # print(thisguy._filterset)
        # print(thisguy.connectionstring)
        # print(thisguy.sqlcommandstring)
        thisguy.connect()
        thisguy._psycocursor = thisguy.connection.cursor()  # (name="psycocursor")
        #thisguy._psycocursor.execute(thisguy.sqlcommandstring)
        return thisguy

    @classmethod
    def ctorDictionaries(cls, _db, _sch, _ip="127.0.0.1", _filters=[], _columnselection=["*"], _tables=["d_cpt", "d_icd_diagnoses", "d_icd_procedures", "d_items", "d_labitems"]):
        thisguy = PlatformBrowser.ctor0()
        thisguy.__dict__.update(MimicServer.MimicServerPlatform.ctor0(_db=_db, _sch=_sch).__dict__)
        thisguy.__dict__.update(MimicCursor.ctor3(_filters=_filters, _columnselection=_columnselection, _tablesearchspace=_tables).__dict__)
        thisguy.connect()
        thisguy._psycocursor = thisguy.connection.cursor()  # (name="psycocursor")
        thisguy._psycocursor.execute(thisguy.sqlcommandstring)
        return thisguy


    @property
    def cursor(self):
        return self._psycocursor

    @cursor.setter
    def cursor(self, _cursorvalue):
        self._psycocursor = _cursorvalue

    def readone(self):
        # check if cursor is closed or not
        if self.cursor.closed == True: # means it is closed
            self.cursor = self.connection.cursor()
            astr = self.sqlcommandstring
            self.cursor.execute(astr)
        athingthing = self.cursor.fetchone()
        if athingthing == None:
            self.cursor.close()
            self.advance()
            if self.focusedtableindex >= self.tablesearchspaceLength:
                return None
            else:
                return self.readone()
                #self.cursor.execute(self.sqlcommandstring)
        return athingthing
        #return self.cursor.fetchone()

    def readall(self):
        alldat = []
        while self.canadvance() == True:
            if self.cursor.closed == True:
                self.cursor = self.connection.cursor()
                self.cursor.execute(self.sqlcommandstring)
            onetable = self.cursor.fetchall()
            alldat.extend(onetable)
            self.cursor.close()
            self.advance()
        return alldat

        # alldat = []
        # while self.canadvance() == True:
        #     if self.cursor.closed == True:
        # #        print("check1")
        #         self.advance()
        #         self.cursor.execute(self.sqlcommandstring)
        #     athing = self.cursor.fetchall()
        # #    print("check2")
        #     if athing != None:
        #         alldat.append(athing)
        #         self.cursor.close()
        # #        print("check3")
        #     self.advance()
        # #     print("check4")
        # #     print(self.focusedtableindex)
        # # print(self.canadvance())
        # return alldat

        # alldat = []
        # while True:
        #     athing = self.readone()
        #     if athing == None:
        #             return alldat
        #     else:
        #         alldat.append(athing)
        # return None

    def readallpandas(self):
        dfarray = {}
        while self.canadvance() == True:
            # print(self.cursor.closed)
            # print("cursorstate ^")
            #print(self.sqlcommandstring)
            if self.cursor.closed == False:
                self.cursor.execute(self.sqlcommandstring)
            colnames = [entry.name for entry in self.cursor.description]
            onetable = pandas.read_sql(self.sqlcommandstring, self.connection, columns=colnames, index_col="row_id")#, index_col="row_id")#, index_col=self.cursor.description) #, self.cursor.description)
            onetable.name = self.focusedtablename
            # we need to identify each onetable by the tablename in order to know which MimicObject to construct.
            # dataframe name is not an attribute. Maybe we need to make an extension method.
            # temprec = onetable.to_records()
            # temprec.dtype.names = onetab
            dfarray.update({onetable.name:onetable.to_records()})
            #dfarray.append(onetable)
            self.advance()
        self.focusedtableindex = 0
        return dfarray

    def readallpandas_csv(self):
        csvarray = []
        while self.canadvance() == True:
            onetable = pandas.read_sql(self.sqlcommandstring, self.connection)
            # we need to identify each onetable by the tablename in order to know which MimicObject to construct.
            # dataframe name is not an attribute. Maybe we need to make an extension method.
            csvarray.append(onetable)
            self.advance()
        return csvarray


    def advance(self):
        self.focusedtableindex += 1

    def canadvance(self):
        if self.focusedtableindex < self.tablesearchspaceLength:
            return True
        else:
            return False

    def close(self):
        self._psycocursor.close()
        self.connection.close()

    def OutputDictionary(self, _filename, _filemode):
        afile = open(_filename, _filemode)
        thestr = self.readallpandas()
        for eachitem in thestr:
            for anotheritem in eachitem.get_values():
                afile.write(str(anotheritem))
                afile.write("\n")
        afile.close()

    # def Output(self, _filename, _filemode):
    #     afile = open(_filename, _filemode)
    #     for eachitem in thestr:
    #         for anotheritem in eachitem.get_values():
    #             afile.write(str(anotheritem))
    #             afile.write("\n")
    #     afile.close()


    # @classmethod
    # def ctor1(cls, _targettables, _mc):
    #     thisguy = cls()
    #     thisguy.tablesearchspace = _targettables
    #     thisguy.focusedtableindex = 0
    #     return thisguy






# cu1 = ConditionUnit('subject_id,=,3015')
# cu2 = ConditionUnit('charttime,=,2017-10-28')
# cu3 = ConditionUnit('hadm_id,=,100')
# cb1 = ConditionBundle([cu1,cu2,cu3])
# cu4 = ConditionUnit('dischtime,<,2017-10-30')
# cc1 = ConditionCollection([cu4,cb1],['AND'])

# # thing = SqlColumnCollection()
# # print(str(thing))
#
# sqlrequest = SqlCommand(_filtercoll=cc1, _tablename='patients')
# print(str(sqlrequest))
# #print(cc1)

