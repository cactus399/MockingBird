import MimicBrowsing
import MimicServer
import MimicObjects
import pandas
import numpy
import datetime


class DictionaryFrame:
    def __init__(self, _ip="127.0.0.1", _port="5432", _uid="postgres", _upw="postgres", _db="mimic", _sch="mimiciii", _tablesearchspace=["d_cpt", "d_icd_diagnoses", "d_icd_procedures", "d_items", "d_labitems"]):
        self._browser = MimicBrowsing.PlatformBrowser.ctor3(_db=_db, _sch=_sch, _ip=_ip, _tables=_tablesearchspace)
        self._df = self._browser.readallpandas()
        self._browser.cursor.close()
        self._browser.close()

    @classmethod
    def ctorItemIdDictionary(cls, _ip="127.0.0.1", _port="5432", _uid="postgres", _upw="postgres", _db="mimic", _sch="mimiciii", _tablesearchspace=["d_items", "d_labitems"]):
        thisguy = cls(_ip=_ip, _port=_port, _uid=_uid, _upw=_upw, _db=_db, _sch=_sch, _tablesearchspace=_tablesearchspace)
        return thisguy

    @classmethod
    def ctorCpt_CdDictionary(cls, _ip="127.0.0.1", _port="5432", _uid="postgres", _upw="postgres", _db="mimic", _sch="mimiciii", _tablesearchspace=["d_cpt"]):
        thisguy = cls(_ip=_ip, _port=_port, _uid=_uid, _upw=_upw, _db=_db, _sch=_sch, _tablesearchspace=_tablesearchspace)
        return thisguy

    @classmethod
    def ctorIcd9_CodeDictionary(cls, _ip="127.0.0.1", _port="5432", _uid="postgres", _upw="postgres", _db="mimic", _sch="mimiciii", _tablesearchspace=["d_icd_diagnoses", "d_icd_procedures"]):
        thisguy = cls(_ip=_ip, _port=_port, _uid=_uid, _upw=_upw, _db=_db, _sch=_sch, _tablesearchspace=_tablesearchspace)
        return thisguy

    @classmethod
    def ctorHospitalStays(cls, _ip="127.0.0.1", _port="5432", _uid="postgres", _upw="postgres", _db="mimic", _sch="mimiciii",
                          _tablesearchspace=["admissions", "icustays"]):
        thisguy = cls(_ip=_ip, _port=_port, _uid=_uid, _upw=_upw, _db=_db, _sch=_sch,
                      _tablesearchspace=_tablesearchspace)
        return thisguy

    @classmethod
    def ctorPeople(cls, _ip="127.0.0.1", _port="5432", _uid="postgres", _upw="postgres", _db="mimic", _sch="mimiciii",
                   _tablesearchspace=["patients", "caregivers"]):
        thisguy = cls(_ip=_ip, _port=_port, _uid=_uid, _upw=_upw, _db=_db, _sch=_sch,
                      _tablesearchspace=_tablesearchspace)
        return thisguy

    @classmethod
    def ctorDictionaries(cls, _ip="127.0.0.1", _port="5432", _uid="postgres", _upw="postgres", _db="mimic", _sch="mimiciii", _tablesearchspace=["d_cpt", "d_icd_diagnoses", "d_icd_procedures", "d_items", "d_labitems"]):
        thisguy = cls(_ip=_ip, _port=_port, _uid=_uid, _upw=_upw, _db=_db, _sch=_sch, _tablesearchspace=_tablesearchspace)
        return thisguy

    @classmethod
    def ctorFullDictionary(cls, _ip="127.0.0.1", _port="5432", _uid="postgres", _upw="postgres", _db="mimic", _sch="mimiciii",
                   _tablesearchspace=["patients", "caregivers", "admissions", "icustays", "d_cpt", "d_icd_diagnoses", "d_icd_procedures", "d_items", "d_labitems", ]):
        thisguy = cls(_ip=_ip, _port=_port, _uid=_uid, _upw=_upw, _db=_db, _sch=_sch,
                      _tablesearchspace=_tablesearchspace)
        return thisguy

    @property
    def Data(self):
        return self._df



    def __getitem__(self, item):
        counter = 0
        for eachentry in self.Data:
            if eachentry.name == item:
                return eachentry

        for eachentry in self.Data:
            if counter == item:
                return eachentry
            else:
                counter += 1

    def __iter__(self):
        return iter(self.Data)

    def __str__(self):
        return str(self.Data)

    def __repr__(self):
        return self.__str__()

        # [ patients, caregivers]
        # ["chartevents", "labevents", "cptevents", "datetimeevents"]
        # [ admissions, icustays ]

# class MimicObjectsFrame(DictionaryFrame):
#     def __init__(self, _ip="127.0.0.1", _port="5432", _uid="postgres", _upw="postgres", _db="mimic", _sch="mimiciii", _tablesearchspace=["d_cpt", "d_icd_diagnoses", "d_icd_procedures", "d_items", "d_labitems"]):
#         self._browser = MimicBrowsing.PlatformBrowser.ctor3(_db=_db, _sch=_sch, _ip=_ip, _tables=_tablesearchspace)
#         self._df = self._browser.readallpandas()
#
#     @property
#     def Data(self):
#         return self._df
#
#     def __getitem__(self, item):
#         counter = 0
#         for eachentry in self.Data:
#             if eachentry.name == item:
#                 return eachentry
#
#         for eachentry in self.Data:
#             if counter == item:
#                 return eachentry
#             else:
#                 counter += 1
#
#     def __iter__(self):
#         return iter(self.Data)
#
#     def __str__(self):
#         return str(self.Data)
#
#     def __repr__(self):
#         return self.__str__()
#
#
#         # [ patients, caregivers]
#         # ["chartevents", "labevents", "cptevents", "datetimeevents"]
#         # [ admissions, icustays ]
#
#
# class MimicDictionariesFrame:
#     def __init__(self, _ip="127.0.0.1", _port="5432", _uid="postgres", _upw="postgres", _db="mimic", _sch="mimiciii", _tablesearchspace=["d_cpt", "d_icd_diagnoses", "d_icd_procedures", "d_items", "d_labitems"]):
#         #self._platform = MimicServer.MimicServerPlatform.ctor1(_ip=_ip, _db=_db, _sch=_sch)
#         self._browser = MimicBrowsing.PlatformBrowser.ctor3(_db=_db, _sch=_sch, _ip=_ip, _tables=_tablesearchspace)
#         self._df = self._browser.readallpandas()
#
#     @property
#     def Data(self):
#         return self._df
#
#     def __getitem__(self, item):
#         counter = 0
#         for eachentry in self.Data:
#             if eachentry.name == item:
#                 return eachentry
#
#         for eachentry in self.Data:
#             if counter == item:
#                 return eachentry
#             else:
#                 counter += 1
#
#     def __iter__(self):
#         return iter(self.Data)
#
#     def __str__(self):
#         return str(self.Data)
#
#     def __repr__(self):
#         return self.__str__()




# class MimicDictionariesFrame(MimicBrowsing.PlatformBrowser):
#     def __init__(self, _db="mimic", _sch="mimiciii", _tablesearchspace=["d_cpt", "d_icd_diagnoses", "d_icd_procedures", "d_items", "d_labitems"]):
#         super().__init__()
#
#     @classmethod
#     def ctor0(cls):
#         return cls()
#
#     @classmethod
#     def ctor1(cls, _db="mimic", _sch="mimiciii", _tablesearchspace=["d_cpt", "d_icd_diagnoses", "d_icd_procedures", "d_items", "d_labitems"]):
#         thisguy = MimicDictionariesFrame.ctor0()
#         thisguy.__dict__.update(MimicServer.MimicServerPlatform.ctor0(_db=_db, _sch=_sch).__dict__)
#         thisguy.__dict__.update(
#             MimicBrowsing.PlatformBrowser.ctor3(_filters=_filters, _tablesearchspace=_tablesearchspace).__dict__)
#         thisguy
#
#
#     def GetSeries(self, index):
#         for eachthing in self._df:
#             if(eachthing.name == index):
#                 return eachthing
#
#         counter = 0
#         for eachthing in self._df:



# ["d_cpt", "d_icd_diagnoses", "d_icd_procedures", "d_items", "d_labitems"]