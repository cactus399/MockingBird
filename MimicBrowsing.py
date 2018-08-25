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


class ConditionBundle:
    def __init__(self, _conditionunits=None, _logicals=None):
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


class ConditionCollection:
    def __init__(self, _unitsbundles=[], _logicals=[]):
        self._unitsbundles = _unitsbundles
        self._logicals = _logicals

    def __str__(self):
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

    def __repr__(self):
        return self.__str__()

    @property
    def filters(self):
        return self._unitsbundles

    @property
    def logicals(self):
        return self._logicals

    @property
    def filtercount(self):
        return len(self._unitsbundles)

    @property
    def logicalcount(self):
        return len(self._logicals)
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
    def __init__(self, _sqlcommandtype=SqlCommandType(0), _columns=SqlColumnCollection(), _tablename="", _filtercoll=ConditionCollection()):
        self._sqlcommandtype = _sqlcommandtype
        self._tablename = _tablename
        self._columns = _columns
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
        acap = self._filtercollection.filtercount
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

    def __init__(self, _tablesearchspace=[], _tableindex=-1):
        self._tablesearchspace = _tablesearchspace
        self._tableindex = _tableindex

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
        if _tableindexvalue < self.tablesearchspaceLength:
            self._tableindex = _tableindexvalue
        else:
            self._tableindex = self.tablesearchspaceLength - 1

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

class PlatformBrowser(MimicServer.MimicServerPlatform, MimicCursor):
    def __init__(self):
        super().__init__()









cu1 = ConditionUnit('subject_id,=,3015')
cu2 = ConditionUnit('charttime,=,2017-10-28')
cu3 = ConditionUnit('hadm_id,=,100')
cb1 = ConditionBundle([cu1,cu2,cu3])
cu4 = ConditionUnit('dischtime,<,2017-10-30')
cc1 = ConditionCollection([cu4,cb1],['AND'])

# # thing = SqlColumnCollection()
# # print(str(thing))
#
# sqlrequest = SqlCommand(_filtercoll=cc1, _tablename='patients')
# print(str(sqlrequest))
# #print(cc1)

