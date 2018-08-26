import MimicServer
import MimicObjects
import MimicBrowsing
import MimicDictionaries
import Context
import datetime
import pandas
import numpy
import time

start = time.time()

athing = Context.CohortBrowser.ctor1(_db="postgres", _sch="public")
df = athing.GetPatientChart(249)

for eachthing in df:
    print(eachthing)

df = athing.GetPatientChart(300)

for eachthing in df:
    print(eachthing)
#df = athing.readallpandas() #athing.GetPatientChart(249)

#print(df)


end = time.time()
print(end - start)

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
