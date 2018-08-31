import psycopg2
import datetime
import os
import pandas
import MimicObjects


class MimicConnectionConfiguration:
    def __init__(self, _ip="127.0.0.1", _port="5432", _db="mimic", _schema="mimiciii", _uid="postgres", _pw="postgres"):
        self._ipaddress=_ip
        self._port=_port
        self._userid=_uid
        self._password=_pw
        self._database=_db
        self._schema=_schema
        # self._ipaddress = ""
        # self._port = ""
        # self._userid=""
        # self._password=""
        # self._database=""
        # self._schema=""

    @classmethod
    def ctor0(cls):
        cwd = os.getcwd()
        try:
            defaultconnectionconfigfile = open(cwd + "\\DefaultConnectionConfiguration") #"C:\Users\LittleRed\OneDrive\BangPython\MimicServer\DefaultConnectionConfiguration.txt")
            thestr = defaultconnectionconfigfile.readline()
            if len(thestr) >= 0:
                alist = thestr.split(',')
                constructed = cls()
                constructed._ipaddress = alist[0]
                constructed._port = alist[1]
                constructed._userid = alist[2]
                constructed._password = alist[3]
                constructed._database = alist[4]
                constructed._schema = alist[5]
                return constructed
            else:
                constructed = cls()
                constructed._ipaddress = "127.0.0.1"
                constructed._port = "5432"
                constructed._userid = "postgres"
                constructed._password = "postgres"
                constructed._database = "mimic"
                constructed._schema = "mimiciii"
                return constructed

        except FileNotFoundError:
            constructed = cls()
            constructed._ipaddress = "127.0.0.1"
            constructed._port = "5432"
            constructed._userid = "postgres"
            constructed._password = "postgres"
            constructed._database = "mimic"
            constructed._schema = "mimiciii"
            return constructed


    @classmethod
    def ctor1(cls, _db, _sch):
        constructed = MimicConnectionConfiguration.ctor0()
        constructed._database = _db
        constructed._schema = _sch
        return constructed

    @classmethod
    def ctor2(cls, _ip, _db, _sch):
        constructed = MimicConnectionConfiguration.ctor1(_db, _sch)
        constructed._ipaddress = _ip
        return constructed

    @classmethod
    def ctor3(cls, _ip, _po, _uid, _pw, _db, _sch):
        constructed = MimicConnectionConfiguration.ctor0()
        constructed._ipaddress = _ip
        constructed._port = _po
        constructed._userid = _uid
        constructed._password = _pw
        constructed._database = _db
        constructed._schema = _sch
        return constructed

    @classmethod
    def ctor4(cls, _csvConnStr):
        constructed = MimicConnectionConfiguration.ctor0()
        splitstr = _csvConnStr.split(',')
        constructed = MimicConnectionConfiguration.ctor3(splitstr[0], splitstr[1], splitstr[2], splitstr[3], splitstr[4], splitstr[5])
        return constructed

    @property
    def ipaddress(self):
        return self._ipaddress

    @ipaddress.setter
    def ipaddress(self, _ipaddress):
        self._ipaddress = _ipaddress

    @property
    def port(self):
        return self._port

    @port.setter
    def port(self, _port):
        self._port = _port

    @property
    def userid(self):
        return self._userid

    @userid.setter
    def userid(self, _userid):
        self._userid = _userid

    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, _password):
        self._password = _password

    @property
    def database(self):
        return self._database

    @database.setter
    def database(self, _database):
        self._database = _database

    @property
    def schema(self):
        return self._schema

    @schema.setter
    def schema(self, _schema):
        self._schema = _schema

    @property
    def connectionstring(self):
        thestr = ""
        thestr += "host="
        thestr += self.ipaddress
        thestr += " port=" + self.port + " user=" + self.userid + " password=" + self.password
        thestr += " dbname=" + self.database
        return thestr

    def __repr__(self):
        thestr = self.connectionstring
        thestr += " schema=" + self.schema
        return thestr


class MimicTablesConfiguration:
    def __init__(self):
        basepath = os.getcwd()
        datatablenamesfile = open(basepath + "\\DataTableNames")
        contents = datatablenamesfile.readline()
        if len(contents) >= 0:
            splitstr = contents.split(',')
            self._tablenames = splitstr
        else:
            self._tablenames = ["admissions","callout","caregivers","chartevents","chartevents_1","chartevents_2","chartevents_3","chartevents_4","chartevents_5","chartevents_6","chartevents_7","chartevents_8","chartevents_9","chartevents_10","chartevents_11","chartevents_12","chartevents_13","chartevents_14","chartevents_15","chartevents_16","chartevents_17","cptevents,datetimeevents","diagnoses_icd","drgcodes","d_cpt","d_icd_diagnoses","d_icd_procedures","d_items","d_labitems","icustays","inputevents_cv","inputevents_mv","labevents","microbiologyevents","noteevents","outputevents,patients","prescriptions","procedureevents_mv","procedures_icd","services","transfers"]

    @property
    def tablenames(self):
        return self._tablenames


class PgsqlInterface:
    def __init__(self):
        self._connectionconfig = MimicConnectionConfiguration.ctor0()
        self._connection = None

    @classmethod
    def ctor0(cls, _db, _sch):
        thisguy = cls()
        thisguy._connectionconfig = MimicConnectionConfiguration.ctor1(_db, _sch)
        return thisguy

    @classmethod
    def ctor1(cls, _ip, _db, _sch):
        thisguy = cls()
        thisguy._connectionconfig = MimicConnectionConfiguration.ctor2(_ip, _db, _sch)
        return thisguy

    @classmethod
    def ctor2(cls, _mcc):
        thisguy = cls()
        thisguy._connectionconfig = _mcc
        return thisguy

    @classmethod
    def ctor3(cls, _connstr):
        thisguy = cls()
        thisguy._connectionconfig = MimicConnectionConfiguration.ctor4(_connstr)
        return thisguy

    # ^ order is ip, port, user, pw, database, schema.
    # _____________________ ^ Constructors ______________________

    @property
    def connectionconfiguration(self):
        return self._connectionconfig

    @connectionconfiguration.setter
    def connectionconfiguration(self, _mcc):
        self._connectionconfig = _mcc

    @property
    def connection(self):
        if self._connection is None:
            self._connection = psycopg2.connect(self.connectionconfiguration.connectionstring)
            return self._connection
        else:
            return self._connection

    @property
    def connectionstring(self):
        return self.connectionconfiguration.connectionstring

    @property
    def tablenames(self):
        return self.tablesconfiguration.tablenames

    # ______________________ ^ PROPERTIES ________________________

    def connect(self, _newconnstr=""): # slightly redundant, but allows for method-mediated connection to DB using connectionconfiguration
        if len(_newconnstr) == 0:
            self.connection
            if self.connection.closed != 0: # closed attr = 0 means that the connection is open (psycopg2)
                self._connection = psycopg2.connect(self.connectionconfiguration.connectionstring)
        else:
            mirrored = PgsqlInterface.ctor2(_newconnstr)
            self = mirrored

    # ________________________^ METHODS ______________________________


class MimicServerPlatform(PgsqlInterface):
    def __init__(self, _ip="127.0.0.1", _port="5432", _db="mimic", _schema="mimiciii", _uid="postgres", _pw="postgres"):
        super().__init__()
        self._tablesconfig = MimicTablesConfiguration()

    @classmethod
    def ctor0(cls, _db, _sch):
        thisguy = PgsqlInterface.ctor0(_db, _sch)
        thisguy._tablesconfig = MimicTablesConfiguration()
        return thisguy

    @classmethod
    def ctor1(cls, _ip, _db, _sch):
        thisguy = PgsqlInterface.ctor1(_ip, _db, _sch)
        thisguy._connectionconfig = MimicConnectionConfiguration.ctor2(_ip, _db, _sch)
        return thisguy

    @classmethod
    def ctor2(cls, _mcc, _mtc):
        thisguy = PgsqlInterface()
        thisguy._connectionconfig = _mcc
        thisguy._tablesconfig = _mtc
        return thisguy

#_____________________ ^ Constructors ______________________

    @property
    def connectionconfiguration(self):
        return self._connectionconfig

    @connectionconfiguration.setter
    def connectionconfiguration(self, _mcc):
        self._connectionconfig = _mcc

    @property
    def tablesconfiguration(self):
        return self._tablesconfig

    @tablesconfiguration.setter
    def tablesconfiguration(self, _mtc):
        self._tablesconfig = _mtc

    @property
    def connection(self):
        if self._connection is None:
            self._connection = psycopg2.connect(self.connectionconfiguration.connectionstring)
            return self._connection
        else:
            return self._connection

    @property
    def connectionstring(self):
        return self.connectionconfiguration.connectionstring

    @property
    def tablenames(self):
        return self.tablesconfiguration.tablenames
# ______________________ ^ PROPERTIES ________________________

    def connect(self, _newconnstr=""): # slightly redundant, but allows for method-mediated connection to DB using connectionconfiguration
        if len(_newconnstr) == 0:
            self.connection
            if self.connection.closed != 0: # closed attr = 0 means that the connection is open (psycopg2)
                self._connection = psycopg2.connect(self.connectionconfiguration.connectionstring)
        else:
            mirrored = MimicServerPlatform.ctor2(_newconnstr, self.tablesconfiguration)
            self = mirrored





# all events (including cpt_events)
# chartevents, cpt_events,
# labevents, datetimeevents,
# microbiologyevents
# noteevents
#

# ________________________^ METHODS ______________________________


# class MimicBrowser(MimicServerPlatform):
#     def __init__(self):
#         super().__init__()
#         self._cursor = None
#
#     @classmethod
#     def ctor0(cls):
#         return cls()
#
#     # @property
#     # def cursor(self):
#     #     if self._cursor == None:
#     #         self._cursor = self.connection.cursor()
#
# #msp = MimicServerPlatform.ctor1("127.0.0.1", "postgres", "public")


# #msp = MimicServerPlatform.ctor0("postgres", "public")
# msp = MimicServerPlatform.ctor0("postgres", "public") #("192.168.0.13", "postgres", "public")
# msp.connect()
# sqlstr = "SELECT * FROM chartevents;"
# cur = msp.connection.cursor()
# cur.execute(sqlstr)
# arow = cur.fetchone()
# print(arow)

#cur.execute("SELECT * FROM patients;")

# df = pandas.read_sql(sqlstr, msp.connection)
#
# acounter = 0
# for each in df.iterrows():
#     #thepatient = MimicObjects.Admission.ctor1(each[1])
#     #print(thepatient)
#
#     anobject = MimicObjects.Patient.ctor1(each[1])
#     #print(each[1]['subject_id'])
#     acounter+=1
#     if acounter > 5:
#         break

# acounter = 0
# for each in range(dflength):
#     print(df[each])
#     acounter += 1
#     if acounter > 10:
#         break


#df1 = pandas.read_sql_table('patients', msp.connection)
# acounter = 0
# for arow in df.iteritems():
#     print(arow['subject_id'])
#     acounter += 1
#     if acounter > 10:
#         break

# for arow in df.loc:
# #    print(arow)
#     aperson = MimicObjects.Patient.ctor1(arow)
#     print(aperson)
#     acounter += 1
#     if acounter > 10:
#         break



#class MimicServerAgent(MimicServerPlatform):
#aplatform = MimicServerPlatform.ctor0("postgres", "public")
# print(aplatform.connection.closed)
# aplatform.connection.close()
# print(aplatform.connection.closed)
# aplatform.connect()
# print(aplatform.connection.closed)
# aplatform.connection.close()
# print(aplatform.connection.closed)

# print(aplatform._connection)
# ac = aplatform.connection
# print(ac)
#
# print(aplatform.connectionconfiguration)
# print(aplatform.connection.closed)
# aplatform.connection.close()
# print(aplatform.connection.closed)
# #cur = aplatform.connection.cursor()
# sqlstr = "SELECT * FROM patients;"
# #cur.execute("SELECT * FROM patients;")
# df = pandas.read_sql(sqlstr, aplatform.connection)
# print(df)


# amimic = MimicConnectionConfiguration.ctor1("postgres", "public")
# amimictb = MimicTablesConfiguration()
# print(amimictb.tablenames)
# print(amimic.connectionstring)
# conn = psycopg2.connect(amimic.connectionstring)
# cur=conn.cursor()
# cur.execute("SELECT * FROM patients;")
# print(cur.fetchone())



