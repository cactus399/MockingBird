import MimicServer
import MimicObjects
import MimicBrowsing
import datetime
import pandas
import numpy

# pb = MimicBrowsing.PlatformBrowser.ctor2("postgres", "public", _subject_id="500")
# afilter = MimicBrowsing.ConditionCollection(MimicBrowsing.ConditionBundle(MimicBrowsing.ConditionUnit("patient_id,=,500")))
afilter = MimicBrowsing.ConditionCollection(_filterstring="subject_id=500;")
print(afilter)
_filters=[afilter]*4
print(_filters)
pb = MimicBrowsing.PlatformBrowser.ctor3(_filters=[afilter]*4, _db="postgres", _sch="public")
    #, afilter, afilter, afilter])
print("hello")
print(pb.sqlcommandstring)
whole = pb.readallpandas()
for eachthing in whole:
    print(eachthing['subject_id'])
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
