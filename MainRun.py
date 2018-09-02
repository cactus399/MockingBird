import datetime
import pandas
import numpy
import time
import MockingWrapper
import MimicObjects
import Context
import string


# in Tucson 8/27/2018
#
# astr = "6005F"
# anint = int(astr)


# print(anint)
#
mock = MockingWrapper.MockingBird(_db="postgres", _sch="public") # general platform
mock.ScanAdmissionsRecords(_writetofile=True)
# arecord = mock.GetChartRecord(_filter="subject_id=23 AND hadm_id=152223")
# arecord.WriteToDisk("C:\\MMd\\experimental\\hello.csv")



# print(type(arecord.Chart[0]))

# mock.ScanAdmissions(_writetofile=True)
# mock.ScanAdmissions(_tostring_func=mock.process_csv)
# print(mock.GetDictionaryItem_Branch("cpt_cd", 94003))
# achart = mock.GetChartRaw(_keyvaluepair=("subject_id", 249))#("subjectid=249")
#achart = mock.GetChartSorted(_keyvaluepair=("subject_id",249))
#sortedchart = achart.DataSorted

# for eachkey, eachthing in sortedchart.items():
#     for eachrow in eachthing:
#         print(eachrow)
#         print("*($#)*(#@)*$#()@*$#()@")
#         print("*($#)*(#@)*$#()@*$#()@")
#         print("*($#)*(#@)*$#()@*$#()@")

# tallyachart = mock.TallyChart(achart)
# tallyobj = MimicObjects.Tally(tallyachart)
# chartobj = MimicObjects.Chart(achart)
# sortedchart = chartobj.SortChart()
# unsortedstr = chartobj.DisplayStr

# print(numpy.dtype("datetime64[ns]"))



# print(unsortedstr)
# for eachthing in c
# hartobj.DataRaw["cptevents"]:
#     print(str(eachthing["chartdate"]))
    # if eachthing["chartdate"] == "NaT" or eachthing["chartdate"] == None:
        # print(eachthing)
# print(chartobj.DataRaw["cptevents"]["chartdate"])
# unsortedstr = chartobj.DisplayStr
# print(unsortedstr)
print("______________________\n")
print("______________________\n")
print("______________________\n")
print("______________________\n")
# print(chartobj.DataRaw)
# sortedstr = chartobj.DisplaySortedStr
# print(sortedstr)

# print(chartobj.DisplayTypesStr)
# print(chartobj.DisplayStr)
#print(tallyobj.DisplayStr)



# print(tallyachart)
# adict = mock.TallyChart(_chart=achart)
# print(adict)
# print(achart)
# atally = mock
# .TallyChart(achart)
# MimicObjects.Chart.DisplayDoD(atally)
# anotherchart = MimicObjects.Chart(achart, atally)
# anotherchart.DIsplayDoD(atally)



# for eachkey, eachitem in achart.items():
#     print(str(eachkey))
#     for eachentry in eachitem:


# # anitem = mock.GetDictionaryItem2("cpt_cd", "3300F")
# # print(anitem)
# thechart = mock.GetChart(_keyvaluepair=("subject_id", 249))
# tally = mock.TallyChart(thechart)
# print(tally)
# print(mock.GetDictionaryItem("itemid", 50818))
# one = mock.GetDictionaryItem("cpt_cd", "97002")

# anum = "5000"
# print(anum[len(anum)-1])

# astr = "500F"
# delchars = ''.join(set(string.printable) - set(string.digits))
# astr.translate()
# print(astr)
# # print(mock.dictionary)

# print(tally)
##atally = Context.DictionaryTally.TallyChart(_thechart_dictofnump=thechart) #mock.dictionary, _thechart_dictofnump=thechart)
#atally - dict. it is a dictionary of 3 entries
#   {
#       "itemid" : { 211: 14, 84: 17, etc...} - another example: { itemid1: occurences_int_of_itemid1_inchart, itemid2: occurences_int_of_itemid2_inchart, ...}
#       "cpt_cd" : { "99233": 10, "99232": 9, ...} - another example: { cpt_cd1: occurences_int_of_cpt_cd1_inchart, cpt_cd2: occurences_int_of_cpt_cd2_inchart, ...}
#       "icd9_code" : { "49322": 1, "51882": 1, ...} - another example: { icd9_code1: occurences_int_of_icd9_code1_inchart, icd9_code2: occurences_int_of_icd9_code2_inchart, ...}
#   }

# #print(atally.keys())
# for eachkey, eachvalue in atally.items():
#     # for eachkey1, eachvalue1 in eachvalue.items():
#     # # keyname = mock.GetDictionaryItem()
#     for eachkey1, eachvalue1 in eachvalue.items():
#         # print(str(eachkey)+ ", " + str(eachkey1)+ ", " + str(eachvalue)+ ", " + str(eachvalue1))
#         keyentry = mock.GetDictionaryItem(eachkey, eachkey1) #eachkey1, eachvalue1)
#         print(str(eachkey) +","+str(eachkey1))
#         print(str(keyentry))
#         # print(str(eachkey1) + ", " + str(eachvalue1) + ", ")
#         # print(keyentry)


# for eachtable in thechart.items():
#     print(eachtable)
#
# thechart = mock.GetChart(_keyvaluepair=("subject_id", 500))
# for eachtable in thechart.items():
#     print(eachtable)



# print(mock.GetDictionaryItem("subject_id", 249))

# print(mock._browserplatform.sqlcommandstring)


###############################

# #theb = Context.CohortBrowser.ctor1(_db="postgres", _sch="public")
#
# theb = Context.CohortBrowser.ctor1(_db="mimic", _sch="mimiciii")
#
# # print(theb._schema)
#
# astr = theb.FindKeyLabel("icd9_code", 146, ["long_title"])
# print(astr)
#
# # bc = theb.GetPatientChartByAdmissions(249)
# # print(bc)
#
# #  SCRIPT FOR FILING EACH PATIENT-ADMISSION (BELOW)
# # ultstring = "C:\\MMd"
# #
# # for eachpt in theb.patients:
# #     theb.OrganizePatient(eachpt["subject_id"], ultstring)
# #  SCRIPT FOR FILING EACH PATIENT-ADMISSION ^
#     #print(eachpt["subject_id"])

#theb.OrganizePatient(249, "C:\\MMd")

# print(theb.GetPatientAdmissionsIds(249))

#bigchart = theb.GetPatientChartByAdmissions(249)

# print(bigchart)

# athing = theb.GetPatientChart(249)
# print(theb.mSpans.Data)
#print(type(theb.mSpans.Data["admissions"][theb.mSpans.Data["admissions"].subject_id==249]))

# adict = {}
#
# for eachrc in athing:
#     df1 = pandas.DataFrame(eachrc, eachrc)
#     adict.update({df1.name: df1})
#
# print(adict)

# tally = theb.process1(athing, "C:\\MMd\\pt249.csv")
# print(tally)

# for eachkey, eachvalue in tally.items():
#     aname = theb.FindKeyLabel("itemid", eachkey, ["label"])
#     astr = ""
#     astr += str(eachkey)
#     astr += ", "
#     astr += aname
#     astr += ", "
#     astr += str(eachvalue)
#     print(astr)

#
# #print(athing["chartevents"]["itemid"])
# sniper = theb.GetPatientChart(249)
# for eachentry in sniper["chartevents"].iterrows():
#     print(eachentry)

# athing = theb.GetPatientAdmissionChart(249)
# print(athing)
# theb.GetPatientAdmissionsIds(249)

# astr = theb.GetItemName(50818)
# print(astr)
# # print(type(theb.people))
# # print(type(theb.people["patients"]))
# #
# contents = theb.TallyDictionary("")
#
# afile = open("C:\\MMd\\talliedN.txt", "x")
#
# for eachkey, eachvalue in contents.items():
#     afile.write(str(eachkey))
#     afile.write(",")
#     afile.write(str(eachvalue))
#     afile.write(",")
#     afile.write(theb.GetItemName(eachkey))
#     afile.write("\n")
#
# afile.close()

# print(theb.people["patients"].to_records()["subject_id"])


# for eachthing in theb.people["patients"]:
#     print(eachthing)
# print(theb.people["patients"])
#athing = theb.GetPatientChart(249)
#thisguy = athing[0]
# print(thisguy[thisguy["itemid"]==211])
# print(thisguy.loc[thisguy.itemid==211])

# def FilterChartHR(DFlist):
#     newlist = []
#     for eachdf in DFlist:
#         if eachdf.columns.contains("itemid"):
#             print(True)
#             newdf = eachdf[eachdf["itemid"]==211]
#             newlist.append(newdf)
#         else:
#             print(False)
#             newlist.append(pandas.DataFrame([], columns=eachdf.columns))
#     return newlist
#
# bestthing = theb.ChartFiltered(500, FilterChartHR)
#
# for eachthing in bestthing:
#     print(len(eachthing))

# adude = thisguy.where(thisguy.itemid==211)
# print(adude)

# print(athing[0][athing[0].itemid==211])
#athing = theb.GetPatientChartFiltered2(249, ["itemid==211", "itemid==211", "itemid==211", ""])

# ptchart = theb.GetPatientChart(249)
# print(theb.dictionary)
#
# # print(theb["labevents"][theb["labevents"].charttime > "2262-1-1"])
# print(theb.Dictionary(0).name)
# print(theb.Dictionary(0))

# print(str(theb["labevents"].charttime.min()) + ", " + str(theb["labevents"].charttime.max()))


# for eachdf in aptchart:
#     print(eachdf)


#print(aptchart[0][(aptchart.i)])#[0].loc["charttime>2065-10-10", "charttime<2066-10-10"])

# def SqlConditionsBuilder(_colname, _operator, _val):
#     return _colname + _operator + _val
#
# def argstest(*args):
#     for eachthing in args:
#         print(eachthing)
#
# argstest(10,11,12)

#print(SqlConditionsBuilder("itemid","=","50800"))

#start = time.time()


# def afunc(_left, _right):
#     return _left == _right
#
#
# def afuncLAMBDA(func, *args):
#     return func(*args)

#print(afuncLAMBDA(lambda x,y: x+y, 1,5))


# # athing2 = map(afunc, [250, 200])
#
# athing2 = list(map(lambda x: (float(5)/9)*(x-32), [90]))
#
# print(athing2)
#
# athing = map(lambda _left,_right: _left == _right, [250,1],[250,1])
# #print(astr)
# print(list(athing))
# athing = Context.CohortBrowser.ctor1(_db="postgres", _sch="public")
# avar = athing.GetPatientChart(249)
# print(avar)
#athing.GetPatientChartsAll("C:\\MMd\\")a

# df = athing.GetPatientChart(249)
#
# for eachthing in df:
#     print(eachthing)
#
# df = athing.GetPatientChart(300)
#
# for eachthing in df:
#     print(eachthing)


#df = athing.readallpandas() #athing.GetPatientChart(249)

#print(df)


#end = time.time()
#print(end - start)

# dictionary = MimicDictionaries.MimicDictionariesFrame(_db="postgres", _sch="public")
# people = MimicDictionaries.MimicDictionariesFrame(_db="postgres", _sch="public", _tablesearchspace=["patients", "caregivers"])



# dictionary = MimicDictionaries.DictionaryFrame.ctorDictionaries(_db="postgres", _sch="public")
# df = dictionary["d_labitems"]
# # print(df.name)
# counter = 0
# allcount = len(df.values)



# for eachrow in df.itemid:
#     print(eachrow)
#     counter += 1
#     # print(df[df.row_id==counter])



# print(df)
# count = len(df.values)
# for acounter in range(0,count):
#     print(df[acounter:acounter+1])

# for acounter in range(0,count):
#     # print(df.iloc[acounter])
#     print(df)
#     #apt = MimicObjects.Patient.ctor1(df.ix[acounter])
#     print(acounter)

#    print(apt)
# #print dictionary._browser.cursor.description
# aguide = [entry.name for entry in dictionary._browser.cursor.description]
# print(aguide)
# for eachentry in dictionary._browser.cursor.description:
#     print(eachentry.name)

# patientdf = dictionary["patients"]
# print(patientdf)
#
# print(patientdf.ix[0])
# for eachguy in patientdf.values:
#     apt = MimicObjects.Patient.ctor2(eachguy)
#     print(apt)
#
# print("hi")

#
# counter = 0
#
# #print(patientdf)
# max = len(patientdf)
# while counter < max:
#     thisguy = patientdf.ix[counter] #patientdf.loc[counter]
#     print(thisguy)
#     #apt = MimicObjects.Patient.ctor1(thisguy)
#     counter += 1
#
# print("done")

# demdf = patientdf.iloc[0, 1]
# print(demdf)
    #apt = MimicObjects.Patient.ctor1(eachthing)
    #print(apt)

#     apatient = MimicObjects.Patient.ctor1(eachrow)
#     listofpatients.extend(apatient)
#
# for eachpt in listofpatients:
#     print(eachpt)


# pb = MimicBrowsing.PlatformBrowser.ctor3(_db="postgres", _sch="public", _tables=["patients"])#, _filters=[MimicBrowsing.Filter("subject_id=600")])
#
# df = pb.readallpandas()
# # for eachframe in df:
# #     if eachframe.name == "labevents":
# #         print(eachframe)
#
# print(df)

#
# file = open("C:\\MMd\\thefile.txt", "x")
# file.write(str(df))

#for eachthing in df:
#    print(eachthin)

#pb = MimicBrowsing.PlatformBrowser.ctorDictionaries(_db="postgres", _sch="public")

#dicts = pb.readallpandas()

##pb.OutputDictionary("C:\\MMd\\pt600.txt", "x")

# AND charttime>'2165-11-05 19:00:00'
# pb.OutputDictionary("C:\\MMd\\pt1.txt", "x")

# print(pb.sqlcommandstring)
# whole = pb.readallpandas()
# print(whole)

# pb = MimicBrowsing.PlatformBrowser.ctor2("postgres", "public", _subject_id="500")
# afilter = MimicBrowsing.ConditionCollection(MimicBrowsing.ConditionBundle(MimicBrowsing.ConditionUnit("patient_id,=,500")))
# afilter = MimicBrowsing.ConditionCollection(_filterstring="subject_id=500;")
# print(afilter)
# _filters=[afilter]*4
# print(_filters)
# pb = MimicBrowsing.PlatformBrowser.ctor3(_filters=[afilter]*4, _db="postgres", _sch="public")
#     #, afilter, afilter, afilter])
# print("hello")
# print(pb.sqlcommandstring)
# whole = pb.readallpandas()
# for eachthing in whole:
#     print(eachthing['subject_id'])
#whole = pb.readone()

# for eachthing in whole:
#     print(eachthing)
# while True:
#     athing = pb.readone()
#     print(athing)
#     if athing == None:
#         break

# print(pb.sqlcommandstring)
## whole = pb.readall()
## print(len(whole))
# anum = len(whole)
#print(anum)
# for eachline in whole:
#     print(len(eachline))

# sample = ["lol", "lol2"]
# alist = ["1"]
# twolist = alist * len(sample)
# print(twolist)


    # for eachthing in eachline:
    #     print(eachthing)

# athing = pb.readone()

# print(athing)
# athing = pb.readone()
# print(athing)

# msp = MimicServer.MimicServerPlatform.ctor0("postgres", "public")
# msp.connect()
# thecurse = msp.connection.cursor("curse")
# thestr = "SELECT * FROM patients;"
# thecurse.execute(thestr)
# avar = thecurse.fetchone()
# print(thecurse.description[0][0])
#
# for athing in avar:
#     print(athing)

# # class A:
# #     def __init__(self):
# #         self._val1 = 1
# #         self._val2 = 2
# #
# # class B:
# #     def __init__(self):
# #         self._val3 = 3
# #         self._val4 = 4
# #
# # class C(A, B):
# #     def __init__(self):
# #         super().__init__()
# #
# #     @classmethod
# #     def ctor0(cls):
# #         return cls()
# #
# #     @classmethod
# #     def ctor1(cls, _a, _b):
# #         thisguy = cls()
# #         thisguy.__dict__.update(_a.__dict__)
# #         thisguy.__dict__.update(_b.__dict__)
# #         #thisguy.__dict__.update(_a)
# #         #thisguy.__dict__.update(_b)
# #         return thisguy
# #
# #
# # a = A()
# # b = B()
# # c = C.ctor1(a, b)
# # print(c._val1)
# # print(c._val4)
# -
