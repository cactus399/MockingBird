import datetime
import pandas
import numpy
import MockingWrapper
import os

class AutoRepr(object):
    def __repr__(self):
        return str(self.__dict__)
    # def __repr__(self):
    #      items = ("%s = %r" % (k, v) for k, v in self.__dict__.items())
    #      return "<%s: {%s}>" % (self.__class__.__name__, ', '.join(items))


class Person(AutoRepr):
    def __init__(self):
        self._id = -1

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, _idvalue):
        self._id = _idvalue


class Patient(Person):
    def __init__(self):
        super().__init__()
        self._gender = ""
        self._dob = datetime.datetime.min
        self._dod = datetime.datetime.min
        self._dod_hosp = datetime.datetime.min
        self._dod_ssn = datetime.datetime.min
        self._expire_flag = ""

    @classmethod
    def ctor0(cls):
        return cls()

    @classmethod
    def ctor1(cls, _datarow):
        thisguy = cls()
        thisguy._id = _datarow['subject_id'] # note - this will be different for the other derived Person type (Caregiver)
        thisguy._gender = _datarow['gender']
        thisguy._dob = _datarow['dob']
        thisguy._dod = _datarow['dod']
        thisguy._dod_hosp = _datarow['dod_hosp']
        thisguy._dod_ssn = _datarow['dod_ssn']
        thisguy._expire_flag = _datarow['expire_flag']
        return thisguy

    # @classmethod
    # def ctor2(cls, _datarow):
    #     thisguy = cls()
    #     thisguy._id = _datarow[1]  # note - this will be different for the other derived Person type (Caregiver)
    #     thisguy._gender = _datarow[2]
    #     thisguy._dob = _datarow[3]
    #     thisguy._dod = _datarow[4]
    #     thisguy._dod_hosp = _datarow[5]
    #     thisguy._dod_ssn = _datarow[6]
    #     thisguy._expire_flag = _datarow[7]
    #     return thisguy

    @property
    def gender(self):
        return self._gender

    @gender.setter
    def gender(self, _gendervalue):
        self._gender = _gendervalue

    @property
    def dob(self):
        return self._dob

    @dob.setter
    def dob(self, _dobvalue):
        self._dob = _dobvalue

    @property
    def dod(self):
        return self._dod

    @dod.setter
    def dod(self, _dodvalue):
        self._dod = _dodvalue

    @property
    def dod_hosp(self):
        return self._dod_hosp

    @dod_hosp.setter
    def dod_hosp(self, _dod_hospvalue):
        self._dod_hosp = _dod_hospvalue

    @property
    def dod_ssn(self):
        return self._dod_ssn

    @dod_ssn.setter
    def dod_ssn(self, _dod_ssnvalue):
        self._dod_ssn = _dod_ssnvalue

    @property
    def expire_flag(self):
        return self._expire_flag

    @expire_flag.setter
    def expire_flag(self, _expire_flagvalue):
        self._expire_flag = _expire_flagvalue

    # def __repr__(self):
    #     items = ("%s = %r" % (k, v) for k, v in self.__dict__.items())
    #     return "<%s: {%s}>" % (self.__class__.__name__, ', '.join(items))


class CareGiver(Person):
    def __init__(self):
        super().__init__()
        self._label = ""
        self._description = ""

    @classmethod
    def ctor0(cls):
        return cls()

    @classmethod
    def ctor1(cls, _datarow):
        thisguy = cls()
        thisguy._id = _datarow['cgid']
        thisguy._label = _datarow['label']
        thisguy._description = _datarow['description']
        return thisguy

    # @classmethod
    # def ctor2(cls, _datarow):
    #     thisguy = cls()
    #     thisguy._id = _datarow[1]
    #     thisguy._label = _datarow[2]
    #     thisguy._description = _datarow[3]
    #     return thisguy

    @property
    def label(self):
        return self._label

    @label.setter
    def label(self, _labelvalue):
        self._label = _labelvalue

    @property
    def description(self):
        return self._description

    @description.setter
    def description(self, _descriptionvalue):
        self._description = _descriptionvalue


#______________________^ PERSON, PATIENT, CAREGIVER ^ ____________________


class Event(AutoRepr):
    def __init__(self):
        self._timestamp = datetime.datetime.min

    @classmethod
    def ctor0(cls):
        thisguy = cls()
        return thisguy

    @classmethod
    def ctor1(cls, _timestamp_param):
        thisguy = Event.ctor0()
        thisguy._timestamp = _timestamp_param
        return thisguy

    @property
    def timestamp(self):
        return self._timestamp

    @timestamp.setter
    def timestamp(self, _timestampvalue):
        self._timestamp = _timestampvalue


class MimicEvent(Event):
    def __init__(self):
        super().__init__()
        self._subject_id = -1
        self._hadm_id = -1

    @classmethod
    def ctor0(cls):
        return cls()

    @classmethod
    def ctor1(cls, _datarow):
        thisguy = Event.ctor1(_datarow) # MimicEvent.ctor0()
        thisguy._subject_id = _datarow['subject_id']
        thisguy._hadm_id = _datarow['hadm_id']
        return thisguy

    @property
    def subject_id(self):
        return self._subject_id

    @subject_id.setter
    def subject_id(self, _subject_idvalue):
        self._subject_id = _subject_idvalue

    @property
    def hadm_id(self):
        return self._hadm_id

    @hadm_id.setter
    def hadm_id(self, _hadm_idvalue):
        self._hadm_id = _hadm_idvalue


class MimicValue(AutoRepr):
    def __init__(self):
        self._value = ""
        self._valueuom = ""

    @classmethod
    def ctor0(cls):
        return cls()

    @classmethod
    def ctor1(cls, _datarow):
        thisguy = MimicValue.ctor0()
        thisguy._value = _datarow['value']
        thisguy._valueuom = _datarow['valueuom']
        return thisguy

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, _valuevalue):
        self._value = _valuevalue

    @property
    def valueuom(self):
        return self._valueuom

    @valueuom.setter
    def valueuom(self, _valueuomvalue):
        self._valueuom = _valueuomvalue


class MimicValueNumeric(MimicValue):
    def __init__(self):
        super().__init__()
        self._valuenum = -1.0

    @classmethod
    def ctor0(cls):
        return cls()

    @classmethod
    def ctor1(cls, _datarow):
        thisguy = MimicValue.ctor1(_datarow) # MimicValueNumeric.ctor0()
        thisguy._valuenum = _datarow['valuenum']
        return thisguy

    @property
    def valuenum(self):
        return self._valuenum

    @valuenum.setter
    def valuenum(self, _valuenumvalue):
        self._valuenum = _valuenumvalue


class ChartEvent(MimicEvent):
    def __init__(self):
        super().__init__()
        self._icustay_id = -1
        self._itemid = -1
        #self._charttime --> this is replaced by timestamp property of the base class Event
        self._storetime = datetime.datetime.min
        self._cgid = -1
        self._mimicvaluenumeric = MimicValueNumeric()
        # self._value = ""          - replaced by property MimicValueNumeric
        # self._valuenum = -1.0     - replaced by property MimicValueNumeric
        # self._valueuom = ""       - replaced by property MimicValueNumeric

        self._warning = -1
        self._error = -1
        # ^ metavision-specific

        self._resultstatus = ""
        self._stopped = ""
        # ^ carevue-specific

    @classmethod
    def ctor0(cls):
        return cls()

    @classmethod
    def ctor1(cls, _datarow):
        thisguy = MimicEvent.ctor1(_datarow) # ChartEvent.ctor0()

        # - note:
        # Event -> MimicEvent -> ChartEvent.
        # Event properties: timestamp
        # MimicEvent properties: subject_id, hadm_id

        # thisguy._subject_id = _datarow['subject_id'] # - already set by MimicEvent.ctor1(_datarow) above
        # thisguy._hadm_id = _datarow['hadm_id']       # - already set by MimicEvent.ctor1(_datarow) above
        thisguy._icustay_id = _datarow['icustay_id']
        thisguy._itemid = _datarow['itemid']
        # thisguy.timestamp =  #_datarow['charttime']  # - already set by MimicEvent.ctor1(_datarow) above
        thisguy._storetime = _datarow['storetime']
        thisguy._cgid = _datarow['cgid']
        thisguy._mimicvaluenumeric = MimicValueNumeric.ctor1(_datarow)
        # thisguy._value = _datarow['value']        - replaced by property MimicValueNumeric
        # thisguy._valuenum = _datarow['valuenum']  - replaced by property MimicValueNumeric
        # thisguy._valueuom = _datarow['valueuom']  - replaced by property MimicValueNumeric
        thisguy._warning = _datarow['warning']
        thisguy._error = _datarow['error']
        thisguy._resultstatus = _datarow['resultstatus']
        thisguy._stopped = _datarow['stopped']

    # @classmethod
    # def ctor2(cls, _datarow):
    #     thisguy = MimicEvent.ctor2(_datarow)  # ChartEvent.ctor0()
    #
    #     # - note:
    #     # Event -> MimicEvent -> ChartEvent.
    #     # Event properties: timestamp
    #     # MimicEvent properties: subject_id, hadm_id
    #
    #     # thisguy._subject_id = _datarow['subject_id'] # - already set by MimicEvent.ctor1(_datarow) above
    #     # thisguy._hadm_id = _datarow['hadm_id']       # - already set by MimicEvent.ctor1(_datarow) above
    #     thisguy._icustay_id = _datarow[3]
    #     thisguy._itemid = _datarow[4]
    #     # thisguy.timestamp =  #_datarow['charttime']  # - already set by MimicEvent.ctor1(_datarow) above
    #     thisguy._storetime = _datarow[6]
    #     thisguy._cgid = _datarow[7]
    #     thisguy._mimicvaluenumeric = MimicValueNumeric.ctor2(_datarow)
    #     # thisguy._value = _datarow['value']        - replaced by property MimicValueNumeric
    #     # thisguy._valuenum = _datarow['valuenum']  - replaced by property MimicValueNumeric
    #     # thisguy._valueuom = _datarow['valueuom']  - replaced by property MimicValueNumeric
    #     thisguy._warning = _datarow[11]
    #     thisguy._error = _datarow[12]
    #     thisguy._resultstatus = _datarow[13]
    #     thisguy._stopped = _datarow[14]

    @property
    def icustay_id(self):
        return self._icustay_id

    @icustay_id.setter
    def icustay_id(self, _icustay_idvalue):
        self._icustay_id = _icustay_idvalue

    @property
    def itemid(self):
        return self._itemid

    @itemid.setter
    def itemid(self, _itemidvalue):
        self._itemid = _itemidvalue

    @property
    def storetime(self):
        return self._storetime

    @storetime.setter
    def storetime(self, _storetimevalue):
        self._storetime = _storetimevalue

    @property
    def cgid(self):
        return self._cgid

    @cgid.setter
    def cgid(self, _cgidvalue):
        self._cgid = _cgidvalue

    @property
    def value(self):
        return self._mimicvaluenumeric.value

    @value.setter
    def value(self, _valuevalue):
        self._mimicvaluenumeric.value = _valuevalue

    @property
    def valuenum(self):
        return self._mimicvaluenumeric.valuenum

    @valuenum.setter
    def valuenum(self, _valuenumvalue):
        self._mimicvaluenumeric.valunum = _valuenumvalue

    @property
    def valueuom(self):
        return self._mimicvaluenumeric.valueuom

    @valueuom.setter
    def valueuom(self, _valueuomvalue):
        self._mimicvaluenumeric.valueuom = _valueuomvalue

    @property
    def warning(self):
        return self._warning

    @warning.setter
    def warning(self, _warningvalue):
        self._warning = _warningvalue

    @property
    def error(self):
        return self._error

    @error.setter
    def error(self, _errorvalue):
        self._error = _errorvalue

    @property
    def resultstatus(self):
        return self._resultstatus

    @resultstatus.setter
    def resultstatus(self, _resultstatusvalue):
        self._resultstatus = _resultstatusvalue

    @property
    def stopped(self):
        return self.stopped

    @stopped.setter
    def stopped(self, _stoppedvalue):
        self._stopped = _stoppedvalue


class LabEvent(MimicEvent, AutoRepr):
    def __init__(self):
        super().__init__()
        self._itemid = -1
        self._mimicvaluenumeric = MimicValueNumeric()
        self._flag = ""

    @classmethod
    def ctor0(cls):
        return cls()

    @classmethod
    def ctor1(cls, _datarow):
        thisguy = MimicEvent.ctor1(_datarow)
        thisguy._itemid = _datarow['itemid']
        thisguy._mimicvaluenumeric = MimicValueNumeric.ctor1(_datarow)
        thisguy._flag = _datarow['flag']

    @property
    def itemid(self):
        return self._itemid

    @itemid.setter
    def itemid(self, _itemidvalue):
        self._itemid = _itemidvalue

    @property
    def flag(self):
        return self._flag

    @flag.setter
    def flag(self, _flagvalue):
        self._flag = _flagvalue

    @property
    def value(self):
        return self._mimicvaluenumeric.value

    @value.setter
    def value(self, _valuevalue):
        self._mimicvaluenumeric.value = _valuevalue

    @property
    def valuenum(self):
        return self._mimicvaluenumeric.valuenum

    @valuenum.setter
    def valuenum(self, _valuenumvalue):
        self._mimicvaluenumeric.valunum = _valuenumvalue

    @property
    def valueuom(self):
        return self._mimicvaluenumeric.valueuom

    @valueuom.setter
    def valueuom(self, _valueuomvalue):
        self._mimicvaluenumeric.valueuom = _valueuomvalue


class DateTimeEvent(MimicEvent, AutoRepr):
    def __init__(self):
        super().__init__()
        self._icustay_id = -1
        self._itemid = -1
        #self._charttime --> this is replaced by timestamp property of the base class Event
        self._storetime = datetime.datetime.min
        self._cgid = -1
        self._mimicvalue = MimicValue()
        # self._value = ""          - replaced by property MimicValueNumeric
        # self._valuenum = -1.0     - replaced by property MimicValueNumeric
        # self._valueuom = ""       - replaced by property MimicValueNumeric

        self._warning = -1
        self._error = -1
        # ^ metavision-specific

        self._resultstatus = ""
        self._stopped = ""
        # ^ carevue-specific

    @classmethod
    def ctor0(cls):
        return cls()

    @classmethod
    def ctor1(cls, _datarow):
        thisguy = MimicEvent.ctor1(_datarow) # ChartEvent.ctor0()

        # - note:
        # Event -> MimicEvent -> ChartEvent.
        # Event properties: timestamp
        # MimicEvent properties: subject_id, hadm_id

        # thisguy._subject_id = _datarow['subject_id'] # - already set by MimicEvent.ctor1(_datarow) above
        # thisguy._hadm_id = _datarow['hadm_id']       # - already set by MimicEvent.ctor1(_datarow) above
        thisguy._icustay_id = _datarow['icustay_id']
        thisguy._itemid = _datarow['itemid']
        # thisguy.timestamp =  #_datarow['charttime']  # - already set by MimicEvent.ctor1(_datarow) above
        thisguy._storetime = _datarow['storetime']
        thisguy._cgid = _datarow['cgid']
        thisguy._mimicvalue = MimicValue.ctor1(_datarow)
        # thisguy._value = _datarow['value']        - replaced by property MimicValueNumeric
        # thisguy._valuenum = _datarow['valuenum']  - replaced by property MimicValueNumeric
        # thisguy._valueuom = _datarow['valueuom']  - replaced by property MimicValueNumeric
        thisguy._warning = _datarow['warning']
        thisguy._error = _datarow['error']
        thisguy._resultstatus = _datarow['resultstatus']
        thisguy._stopped = _datarow['stopped']

    @property
    def icustay_id(self):
        return self._icustay_id

    @icustay_id.setter
    def icustay_id(self, _icustay_idvalue):
        self._icustay_id = _icustay_idvalue

    @property
    def itemid(self):
        return self._itemid

    @itemid.setter
    def itemid(self, _itemidvalue):
        self._itemid = _itemidvalue

    @property
    def storetime(self):
        return self._storetime

    @storetime.setter
    def storetime(self, _storetimevalue):
        self._storetime = _storetimevalue

    @property
    def cgid(self):
        return self._cgid

    @cgid.setter
    def cgid(self, _cgidvalue):
        self._cgid = _cgidvalue

    @property
    def value(self):
        return self._mimicvalue.value

    @value.setter
    def value(self, _valuevalue):
        self._mimicvalue.value = _valuevalue

    @property
    def valueuom(self):
        return self._mimicvalue.valueuom

    @valueuom.setter
    def valueuom(self, _valueuomvalue):
        self._mimicvalue.valueuom = _valueuomvalue

    @property
    def warning(self):
        return self._warning

    @warning.setter
    def warning(self, _warningvalue):
        self._warning = _warningvalue

    @property
    def error(self):
        return self._error

    @error.setter
    def error(self, _errorvalue):
        self._error = _errorvalue

    @property
    def resultstatus(self):
        return self._resultstatus

    @resultstatus.setter
    def resultstatus(self, _resultstatusvalue):
        self._resultstatus = _resultstatusvalue

    @property
    def stopped(self):
        return self.stopped

    @stopped.setter
    def stopped(self, _stoppedvalue):
        self._stopped = _stoppedvalue


#
# class Chart:
#     def __init__(self, _chartdata={}, _tally={}):
#         self._chartdata = _chartdata # - dictionary of recarrays
#         self._tally = _tally         # - dictionary of dictionaries of dictionaries (e.g.:
#          itemid, cpt_cd, icd9_codes

#         # {"icd9_code":
# #         #   { "49322":
# #         #       { "count": 1, "chart_entry": (tuple or ndarray), "dictionary_entry": (recarray of a single ndarray for a dictionary entry) }
# #         #   }
# #         # }
#
#     @property
#     def ChartData(self):
#         return self._chartdata
#
#     @property
#     def TallyData(self):
#         return self._tally
#
#     def DisplayStr(self):
#         astr = Chart.DisplayDD(self.ChartData)
#         astr += "\n ----------------- \n"
#         astr += Chart.DisplayDD(self.TallyData)
#         return astr
#
#     # @classmethod
#     # def DisplayDD(cls, _dd):
#     #
#
#     # @classmethod
#     # def DisplayDoD(cls, dod):
#     #     concatstring = ""
#     #     for eachkey, eachitem in dod.items():
#     #         concatstring += str(eachkey)
#     #         concatstring += "\n"
#     #         for eachkey1, eachentry in eachitem.items():
#     #             for eachkey2, eachentry2 in eachentry.items():
#     #                 concatstring += eachkey2 +": "
#     #                 concatstring += str(eachentry2)
#     #                 concatstring += ", "
#     #                 concatstring += "\n"
#     #     print(concatstring)
#                 # for eachentry1 in eachentry.items():
#     # def DisplayStr(self):
#     #     astr = ""
#     #     for eachkey, eachset in self.Data.itmes():
#     #         str +=
#     # note - this is a dictionary of recarrays.


    # chart events has -
    # { chartevents, labevents, cptevents, procedureevents_mv,
    # datetimeevents}



## IMPLEMENT LATER #### (BELOW)
# class CptEvent(MimicEvent,AutoRepr):
#     def __init__(self):
#         super().__init__()
#         self._costcenter = ""
#         self._cpt_cd = ""
#         self._cpt_number = -1
#         self._cpt_suffix = ""
#         self._ticket_id_seq = -1
#         self._sectionheader = ""
#         self._subsectionheader = ""
#         self._description = ""
#
#     @classmethod
#     def ctor0(cls):
#         return cls()
#
#     @classmethod
#     def ctor1(cls, _datarow):
#         thisguy = MimicEvent.ctor1(_datarow)
#         thisguy._costcenter = _datarow['costcenter']
#         thisguy._cpt_cd = _datarow['cpt_cd']
#         thisguy._cpt_number = _datarow['cpt_number']
#         thisguy._cpt_suffix = _datarow['cpt_suffix']
#         thisguy._ticket_id_seq = _datarow['ticket_id_seq']
#         thisguy._sectionheader = _datarow['sectionheader']
#         thisguy._subsectionheader = _datarow['subsectionheader']
#         thisguy._description = _datarow['description']
#
#     @property
#     def costcenter(self):



#______________________^ events, eventspans ^____________________________________________________
#______________________^ chartevent, labevent, microbiologyevent, datetimeevent, noteevent_______`


class EventSpan:
    def __init__(self):
        self._startevent = Event()
        self._endevent = Event()

    @classmethod
    def ctor0(cls):
        thisguy = cls()
        return thisguy

    @classmethod
    def ctor1(cls, _datarow):
        thisguy = EventSpan.ctor0(_datarow)
        thisguy._startevent = _datarow['admittime']
        thisguy._endevent = _datarow['dischtime']

    @classmethod
    def ctor2(cls, _startevent_param, _endevent_param):
        thisguy = EventSpan.ctor0()
        thisguy._startevent = _startevent_param
        thisguy._endevent = _endevent_param
        return thisguy

    @classmethod
    def ctor3(cls, _startevent_datetime, _endevent_datetime):
        thisguy = EventSpan.ctor0()
        thisguy._startevent = Event.ctor1(_startevent_datetime)
        thisguy._endevent = Event.ctor1(_endevent_datetime)
        return thisguy

    @property
    def startevent(self):
        return self._startevent

    @startevent.setter
    def startevent(self, _starteventvalue):
        self._startevent = _starteventvalue

    @property
    def starttimestamp(self):
        return self.startevent.timestamp

    @property
    def endevent(self):
        return self._endevent

    @endevent.setter
    def endevent(self, _endeventvalue):
        self._endevent = _endeventvalue

    @property
    def endtimestamp(self):
        return self.endevent.timestamp


class MimicEventSpan(EventSpan):
    def __init__(self):
        super().__init__()
        self._subject_id = -1
        self._hadm_id = -1

    @classmethod
    def ctor0(cls):
        return cls()

    @classmethod
    def ctor1(cls, _datarow):
        thisguy = Event.ctor1(_datarow) # MimicEvent.ctor0()
        thisguy._startevent = _datarow['admittime']
        thisguy._endevent = _datarow['dischtime']
        thisguy._subject_id = _datarow['subject_id']
        thisguy._hadm_id = _datarow['hadm_id']
        return thisguy

    @property
    def subject_id(self):
        return self._subject_id

    @subject_id.setter
    def subject_id(self, _subject_idvalue):
        self._subject_id = _subject_idvalue

    @property
    def hadm_id(self):
        return self._hadm_id

    @hadm_id.setter
    def hadm_id(self, _hadm_idvalue):
        self._hadm_id = _hadm_idvalue


class Admission(MimicEventSpan):
    def __init__(self):
        super().__init__()
        self._deathtime = datetime.datetime.min
        self._admission_type = ""
        self._admission_location = ""
        self._discharge_location = ""
        self._insurance = ""
        self._language = ""
        self._religion = ""
        self._marital_status = ""
        self._ethnicity = ""
        self._edregtime = datetime.datetime.min
        self._edouttime = datetime.datetime.min
        self._diagnosis = ""
        self._hospital_expire_flag = -1
        self._has_chartevents_data = -1

    @classmethod
    def ctor0(cls):
        return cls()

    @classmethod
    def ctor1(cls, _datarow):
        thisguy = MimicEventSpan.ctor1(_datarow)
        thisguy._deathtime = Event.ctor1(_datarow['deathtime'])
        thisguy._admission_type = _datarow['admission_type']
        thisguy._admission_location = _datarow['admission_location']
        thisguy._discharge_location = _datarow['discharge_location']
        thisguy._insurance = _datarow['insurance']
        thisguy._language = _datarow['language']
        thisguy._religion = _datarow['religion']
        thisguy._marital_status = _datarow['marital_status']
        thisguy._ethnicity = _datarow['ethnicity']
        thisguy._edregtime = Event.ctor1(_datarow['edregtime'])
        thisguy._edouttime = Event.ctor1(_datarow['edouttime'])
        thisguy._diagnosis = _datarow['diagnosis']
        thisguy._hospital_expire_flag = _datarow['hospital_expire_flag']
        thisguy._has_chartevents_data = _datarow['has_chartevents_data']
        return thisguy

    @property
    def admittime(self):
        return self.startevent.timestamp

    @admittime.setter
    def admittime(self, _admittimevalue):
        self.startevent = Event.ctor1(_admittimevalue)

    @property
    def dischtime(self):
        return self.dischtime.timestamp

    @dischtime.setter
    def dischtime(self, _dischtimevalue):
        self.endevent = Event.ctor1(_dischtimevalue)

    @property
    def deathtime(self):
        return self._deathtime

    @deathtime.setter
    def deathtime(self, _deathtimevalue):
        self._deathtime = _deathtimevalue

    @property
    def admission_type(self):
        return self._admission_type

    @admission_type.setter
    def admission_type(self, _admission_typevalue):
        self._admission_type = _admission_typevalue

    @property
    def admission_location(self):
        return self._admission_location

    @admission_location.setter
    def admission_location(self, _admission_locationvalue):
        self._admission_location = _admission_locationvalue

    @property
    def discharge_location(self):
        return self._discharge_location

    @discharge_location.setter
    def discharge_location(self, _discharge_locationvalue):
        self._discharge_location = _discharge_locationvalue

    @property
    def insurance(self):
        return self._insurance

    @insurance.setter
    def insurance(self, _insurancevalue):
        self._insurance = _insurancevalue

    @property
    def language(self):
        return self._language

    @language.setter
    def language(self, _languagevalue):
        self._language = _languagevalue

    @property
    def religion(self):
        return self._religion

    @religion.setter
    def religion(self, _religionvalue):
        self._religion = _religionvalue

    @property
    def marital_status(self):
        return self._marital_status

    @marital_status.setter
    def marital_status(self, _marital_statusvalue):
        self._marital_status = _marital_statusvalue

    @property
    def ethnicity(self):
        return self._ethnicity

    @ethnicity.setter
    def ethnicity(self, _ethnicityvalue):
        self._ethnicity = _ethnicityvalue

    @property
    def edregtime(self):
        return self._edregtime

    @edregtime.setter
    def edregtime(self, _edregtimevalue):
        self._edregtime = _edregtimevalue

    @property
    def edouttime(self):
        return self._edouttime

    @edouttime.setter
    def edouttime(self, _edouttimevalue):
        self._edouttime = _edouttimevalue

    @property
    def diagnosis(self):
        return self._diagnosis

    @diagnosis.setter
    def diagnosis(self, _diagnosisvalue):
        self._diagnosis = _diagnosisvalue

    @property
    def hospital_expire_flag(self):
        return self._hospital_expire_flag

    @hospital_expire_flag.setter
    def hospital_expire_flag(self, _hospital_expire_flagvalue):
        self._hospital_expire_flag = _hospital_expire_flagvalue

    @property
    def has_chartevents_data(self):
        return self._has_chartevents_data

    @has_chartevents_data.setter
    def has_chartevents_data(self, _has_chartevents_datavalue):
        self._has_chartevents_data = _has_chartevents_datavalue


class IcuStay(MimicEventSpan):
    def __init__(self):
        super().__init__()
        self._icustay_id = -1
        self._dbsource = ""
        self._first_careunit = ""
        self._last_careunit = ""
        self._first_wardid = -1
        self._last_wardid = -1
        self._los = -1.0

    @classmethod
    def ctor0(cls):
        return cls()

    @classmethod
    def ctor1(cls, _datarow):
        thisguy = MimicEventSpan.ctor1(_datarow)
        thisguy.startevent = _datarow['intime']
        thisguy.endevent = _datarow['outtime']
        thisguy._icustay_id = _datarow('icustay_id')
        thisguy._dbsource = _datarow('dbsource')
        thisguy._first_careunit = _datarow('first_careunit')
        thisguy._last_careunit = _datarow('last_careunit')
        thisguy._first_wardid = _datarow('first_wardid')
        thisguy._last_wardid = _datarow('last_wardid')
        thisguy._los = _datarow('los')
        return thisguy

    @property
    def intime(self):
        return self.startevent.timestamp

    @intime.setter
    def intime(self, _intimevalue):
        self.startevent = Event.ctor1(_intimevalue)

    @property
    def outtime(self):
        return self.endevent.timestamp

    @outtime.setter
    def outtime(self, _outtimevalue):
        self.endevent = Event.ctor1(_outtimevalue)

    @property
    def icustay_id(self):
        return self._icustay_id

    @icustay_id.setter
    def icustay_id(self, _icustay_idvalue):
        self._icustay_id = _icustay_idvalue

    @property
    def dbsource(self):
        return self._dbsource

    @dbsource.setter
    def dbsource(self, _dbsourcevalue):
        self._dbsource = _dbsourcevalue

    # self._first_careunit = ""
    # self._last_careunit = ""
    # self._first_wardid = -1
    # self._last_wardid = -1
    # self._los = -1.0

    @property
    def first_careunit(self):
        return self._first_careunit

    @first_careunit.setter
    def first_careunit(self, _first_careunitvalue):
        self._first_careunit = _first_careunitvalue

    @property
    def last_careunit(self):
        return self._last_careunit

    @last_careunit.setter
    def last_careunit(self, _lastcareunitvalue):
        self._last_careunit = _lastcareunitvalue

    @property
    def first_wardid(self):
        return self._first_wardid

    @first_wardid.setter
    def first_wardid(self, _first_wardidvalue):
        self._first_wardid = _first_wardidvalue

    @property
    def last_wardid(self):
        return self._last_wardid

    @last_wardid.setter
    def last_wardid(self, _last_wardidvalue):
        self._last_wardid = _last_wardidvalue

    @property
    def los(self):
        return self._los;

    @los.setter
    def los(self, _losvalue):
        self._los = _losvalue


#####################################^^^ BASE CLASSES prior to 8/28 ^^###############################################
class Tally:
    def __init__(self, _ddd):
        self._ddd = _ddd

    @property
    def Data(self):
        return self._ddd

    @property
    def DisplayStr(self):
        astr = ""
        for eachkey1, eachdict1 in self.Data.items():
            astr += str(eachkey1) + ": \n" # "icd9_code: "
            for eachkey2, eachdict2 in eachdict1.items():
                astr += str(eachkey2) + "   : \n" # thecode itself - "49993" for example
                for eachkey3, eachdict3 in eachdict2.items():
                    astr += str(eachkey3) # eachkey3 - count, chart_entry, dictionary_entry
                    astr += "       : "
                    astr += str(eachdict3) + ", "
                    astr += "\n"
                astr += "\n"
        return astr
                # "count", "chart_entry", "dictionary_entry"


class Chart:
    # EXPOSED - constructor arguments: _chartdata is the raw chart data dictionary. _platform is to be passed as a MockingWrapper.MockingBird class instance.
    ################################################################################################
    def __init__(self, _chartdata, _platform):
        self._chartdata = _chartdata
        self._platform = _platform
        self._chartdatasorted = {}

    # EXPOSED - 1) simply returns the raw _chartdata.################################################
    @property
    def _dataraw(self):
        return self._chartdata

    # EXPOSED - 2) returns the sorted raw data ################################################
    @property
    def DataSorted(self):
        if len(self._chartdatasorted) <= 0:
            self._chartdatasorted = self.SortChart()
        return self._chartdatasorted

    # (hidden) - datastring of the sorted data, to be used in disk I/O by WriteToDisk method
    # modify this to control what gets written to HD
    @property
    def DataString(self):
        fullstr = ""
        thedata = self.DataSorted
        for eachkey, eachthing in thedata.items():
            for eachitem in eachthing:
                fullstr += str(eachitem)
                fullstr += "\n"
            fullstr += "_______________________________\n"
        return fullstr

    # EXPOSED - m1) writes the string provided by self.DataString to file.############################################
    ################################################
    def WriteToDisk(self, filepathway=""):
        if len(filepathway) > 0:
            if os.path.isfile(filepathway) == False:
                afile = open(filepathway, "x")
                afile.write(self.DataString)
                afile.close()

    # EXPOSED - m2) actual sorting instance method to be used. ################################################
    # does no disk I/O - that's for WriteToDisk method.################################################
    def SortChart(self):
        timestamped_numpyrecords = []
        nostamped_numpyrecords = []
        timestamped_silo_keys = {}
        nostamped_silo_keys = {}
        for eachkey, eachrecarray in self._dataraw.items():
            datetimetypehere = False
            for eachcolname, eachcoltypetuple in eachrecarray.dtype.fields.items():
                if numpy.dtype("datetime64[ns]") == eachcoltypetuple[0] or eachcolname == "charttime" or eachcolname == "chartdate" or eachcolname == "starttime":
                    if str(eachkey) != "noteevents":
                        datetimetypehere = True
                        if str(eachkey) not in timestamped_silo_keys.keys():
                            timestamped_silo_keys.update({str(eachkey): str(eachcolname)})
            if datetimetypehere == False:
                nostamped_numpyrecords.append(eachrecarray)
        timestamped_numpyrecords = self.MergeChartsByTime(self._dataraw, timestamped_silo_keys)
        self._chartdatasorted.update({"chart": timestamped_numpyrecords})
        self._chartdatasorted.update({"other": nostamped_numpyrecords})
        return self._chartdatasorted

    # (hidden) - used by SortChart method.
    # this is the most complicated method in this class.
    # _rawdata is the chart dictionary (raw), _silo_keys is automatically obtained by iterating through each table in the rawchart.
    # _silo_keys is passed by the calling method SortChart method. typically should be like the following:
    # { "chartevents": "charttime", "labevents": "charttime", "cptevents": "
    def MergeChartsByTime(self, _rawdata, _silo_keys,
                          _dictionarylabels={'chartevents': "label", 'labevents': "label",
                                                     'cptevents': "subsectionheader", 'datetimeevents': "label",
                                                     'procedureevents_mv': "label", 'procedures_icd': "long_title",
                                                     'diagnoses_icd': "long_title"},  #'noteevents': "text"},
                          _dictionarylabelslist={"itemid": 0, "cpt_cd": 0, "icd9_code": 0}):
        # --> this was the right way of thinking of silo_keys. _silo_keys - {'chartevents': 'charttime', 'labevents': 'charttime', 'cptevents': 'chartdate', 'datetimeevents': 'charttime', 'procedureevents_mv': 'starttime'}
        # problem was that some (actually most) of the dtypes in each recarray was returning type('O') instead of type('datetime64[ns]') for some reason
        # e.g. dtype.items gives the iterable that looks like this: ( ( type('<i8'), 'rowid'), (type('<M8[something]'), 'charttime')
        # the problem is that tuple[0] was giving type('O') (python object type) for some charttimes, chartdates, and starttimes, thus bypassing the condition put into method SortChart
        timeseries = []
        statusindexer = {}  # - index pointer to track the position within each chart (for "megacursor"-type iteration)
        indexmaxima = {}  # - gives maximum sizes of the entire rawchart so that the loop knows when to stop and return the value.
        currentstate = {}  # - "staging area" where the pointed row in each table is held before being "shuffled off". all entries will be None when the task is completed (sorting)
        for eachkey, eachaxiscolumn in _silo_keys.items():
            if str(eachkey) not in statusindexer.keys():
                statusindexer.update({str(eachkey): 0})
            if str(eachkey) not in indexmaxima.keys():
                themaxindex = _rawdata[str(eachkey)].size - 1
                indexmaxima.update({str(eachkey): themaxindex})
            if str(eachkey) not in currentstate.keys():
                currentstate.update({str(eachkey): None})

        endit = False
        while endit == False:
            winner = numpy.datetime64(pandas.Timestamp.max)
            winningkey = ""
            for eachkey, eachindex in statusindexer.items():  # populates the current state
                focusedvalue = None
                if statusindexer[str(eachkey)] <= indexmaxima[str(eachkey)]:
                    focusedvalue = _rawdata[str(eachkey)][statusindexer[str(eachkey)]][_silo_keys[str(eachkey)]]
                currentstate[str(eachkey)] = focusedvalue

            # judge which is most recent (save to winner)
            for eachkey, eachvalue in currentstate.items():
                if eachvalue is not None:
                    if eachvalue <= winner:
                        winner = eachvalue
                        winningkey = eachkey
            if len(winningkey) > 0:
                numpyentry = _rawdata[winningkey][statusindexer[winningkey]]
                dictionaryentry = self.GetDictItem(numpyentry, _dictionarylabelslist)
                # if winningkey in _dictionarylabels.keys():
                actuallabel = dictionaryentry[_dictionarylabels[winningkey]]
                # print("rawdat entry type:")
                # print(type(_rawdata[winningkey][statusindexer[winningkey]]))
                # print("label entry type:")
                # print(type(actuallabel))
                timeseries.append((_rawdata[winningkey][statusindexer[winningkey]], actuallabel))
                statusindexer[winningkey] += 1

            else:
                endit = True
        return timeseries

    def ___oldMergeChartsByTime(self, _rawdata,
                                _silo_keys):  # _silo_keys - {'chartevents': 'charttime', 'labevents': 'charttime', 'cptevents': 'chartdate', 'datetimeevents': 'charttime', 'procedureevents_mv': 'starttime'}
        timeseries = []
        statusindexer = {}
        indexmaxima = {}
        currentstate = {}
        for eachkey, eachaxiscolumn in _silo_keys.items():
            if str(eachkey) not in statusindexer.keys():
                statusindexer.update({str(eachkey): 0})
            if str(eachkey) not in indexmaxima.keys():
                themaxindex = _rawdata[str(eachkey)].size - 1
                indexmaxima.update({str(eachkey): themaxindex})
            if str(eachkey) not in currentstate.keys():
                currentstate.update({str(eachkey): None})

        endit = False
        # winner = numpy.datetime64(pandas.Timestamp.max)
        # print(winner)
        # print(type(winner))
        while endit == False:
            winner = numpy.datetime64(pandas.Timestamp.max)
            winningkey = ""
            for eachkey, eachindex in statusindexer.items():  # populates the current state
                focusedvalue = None
                if statusindexer[str(eachkey)] <= indexmaxima[str(eachkey)]:
                    focusedvalue = _rawdata[str(eachkey)][statusindexer[str(eachkey)]][_silo_keys[str(eachkey)]]
                currentstate[str(eachkey)] = focusedvalue

            # judge which is most recent (save to winner)
            for eachkey, eachvalue in currentstate.items():
                # print(eachvalue)
                # print(type(eachvalue))
                # print("__@_#_$#_$_#_$#_")
                if eachvalue is not None:
                    if eachvalue <= winner:
                        winner = eachvalue
                        winningkey = eachkey
            if len(winningkey) > 0:
                timeseries.append(_rawdata[winningkey][statusindexer[winningkey]])
                statusindexer[winningkey] += 1
            else:
                endit = True
        return timeseries

        # # break if all values of currentstate = None
        # breakit = True
        # for each1, each2 in currentstate.items():
        #     if each2 is not None:
        #         breakit = False
        #         break
        # if breakit == True:
        #     endit = True

        # if str(eachkey) not in currentstate.keys():
        #     if statusindexer[str(eachkey)] <= indexmaxima[str(eachkey)]:
        #         currentstate.update({str(eachkey): _rawdata[str(eachkey)][statusindexer[str(eachkey)]][_silo_keys[str(eachkey)]]})
        # else:

    def GetDictItem(self, numpyentry, _dictionarylabelslist):
        for eachkey, eachvalue in _dictionarylabelslist.items():
            if str(eachkey) in numpyentry.dtype.names:
                thevalue = numpyentry[str(eachkey)]
                dictentry = self._platform.GetDictionaryItem(str(eachkey), thevalue)
                return dictentry
        return None

    # def GetCurrentState(self, _rawdata, _statusindexer):

    @property
    def DisplayStr(self):
        astr = ""
        for eachkey1, eachentry1 in self._dataraw.items():
            astr += str(eachkey1) + ": \n"
            for eachentryN in eachentry1:
                astr += str(type(eachentryN))
                astr += " -- "
                astr += str(eachentryN) + "\n"
        return astr

    # @property
    # def DisplaySortedStr(self):
    #     # first, sort all of the tables independently
    #     # then, use a cursor-like method to consolidate them into a single list (or ndarray???)
    #     for eachkey1, eachentry1 in self.DataRaw.items():
    #         if "charttime" in eachentry1.dtype.names:
    #             eachentry1.sort(axis=0, order="charttime")
    #             #for eachrow in eachentry1:
    #                 #if str(eachrow["charttime"]) == "NaT" or str(eachrow["charttime"]) == "None" or type(eachrow["charttime"]).isinstance(type(None)):
    #                     #eachrow["charttime"] = datetime.datetime.max
    #
    #         if "chartdate" in eachentry1.dtype.names:
    #             eachentry1.sort(axis=0, order="chartdate")
    #             # for eachrow in eachentry1:
    #             #     #if str(eachrow["chartdate"]) == "NaT" or str(eachrow["chartdate"]) == "None" or type(eachrow["chartdate"]).isinstance(type(None)):
    #             #         eachrow["chartdate"] = datetime.datetime.max
    #             #         print(datetime.datetime.max)
    #             #         print(eachrow["chartdate"])
    #
    #     return self.DisplayStr

    @property
    def DisplayTypesStr(self):
        astr = ""
        for eachkey1, eachentry1 in self.Data.items():
            astr += str(eachkey1) + ": \n"
            for eachentryN in eachentry1:
                astr += str(eachentryN.dtype["row_id"]) + ","
                # for eachitem in eachentryN.dtype
                # astr += str(eachentryN.dtype[]) + ", "
                # astr += str(eachentryN.dtype) + "\n"

                # for eachthing in eachentryN.dtype.names:
                #     astr += str(eachthing) + "\n"
        return astr

# ^ components of _chartdata by default
# chartevents - charttime
# cptevents - chartDATE
# datetimeevents - charttime
# labevents - charttime
# procedureevents_mv - starttime, endtime
#
# procedures_icd - no timestamp
# diagnoses_icd - no timestamp


# class PatientAdmission:
#     def __init__(self):



# class ChartEntry:
#     def __init__(self):
#         # (_rawdata[winningkey][statusindexer[winningkey]], actuallabel)
#         # ^ above will be the input. (t1, t2). t1 is a numpy array, t2 is also a numpy array?


#################################

# class Lex:
#     def __init__(self, _strintlist = None):
#         self._strintlist = _strintlist

class Lexicon: # the set of pre-determined item ids that we are looking for.
    def __init__(self, _itemidlist=None):
        self._itemidlist = _itemidlist

    @property
    def ItemIdList(self):
        return self._itemidlist


    # the following take parameters as EITHER a TimeBucket OR a RecordEntry.
    # as long as there is a property called RecordEntries being an iterable list of RecordEntry instances
    def SatisfiedBoolean(self, _recordentriesinstance):
        thebool = False
        for eachlexiconitem in self.ItemIdList:
            for eachitem in _recordentriesinstance.RecordEntries:
                if str(eachitem.ConceptId) == str(eachlexiconitem):
                    thebool = True
                    break
            if thebool == True:
                break
        return thebool

    def SatisfiedCount(self, _recordentriesinstance):
        thecount = 0
        for eachlexiconitem in self.ItemIdList:
            for eachitem in _recordentriesinstance.RecordEntries:
                if str(eachitem.ConceptId) == str(eachlexiconitem):
                    thecount += 1
        return thecount

    def SatisfiedFraction(self, _recordentriesinstance):
        thecount = self.SatisfiedCount(_recordentriesinstance)
        thetotalcount = len(_recordentriesinstance.RecordEntries)
        return float(thecount) / float(thetotalcount)

class TimeSpan:
    def __init__(self, mintime=None, maxtime=None):
        self._mintime = mintime
        self._maxtime = maxtime

    @property
    def StartTimeStamp(self):
        return self._mintime

    @property
    def EndTimeStamp(self):
        return self._maxtime

    @property
    def Duration(self):
        td = self.EndTimeStamp - self.StartTimeStamp
        return td

class RecordPackage:
    def __init__(self, _recordentries):
        self._recordentries = _recordentries

    @property
    def Count(self):
        return len(self.RecordEntries)

    @property
    def Length(self):
        return self.Count

    @property
    def ItemIdList(self):
        iil = []
        for eachitem in self._recordentries:
            iil.extend(eachitem.ConceptId)
        return iil

    @property
    def LabelList(self):
        ll = []
        for eachitem in self._recordentries:
            ll.extend(eachitem.Label)
        return ll

    @property
    def ConceptLabelList(self):
        cll = []
        for eachitem in self._recordentries:
            cll.append(eachitem.ConceptLabel)
        return cll

    @property
    def TimeStamp(self):
        if self._recordentries is not None:
            if len(self._recordentries) > 0:
                return self._recordentries[0].TimeStamp
        return None

    @property
    def RecordEntries(self):
        return self._recordentries

    def AddRecordEntry(self, _recentry):
        self._recordentries.append(_recentry)


class RecordEntry:
    def __init__(self, _rowtuple):
        self._rowtuple = _rowtuple

    @property
    def Label(self):
        return self._rowtuple[1]

    @property
    def Value(self):
        for eachitem in self._columnnames:
            if str(eachitem) == "value" or str(eachitem) == "description":
                return self._row[eachitem]
        return None

    @property
    def ConceptId(self): # returns the itemid number or cpt code number or icd9 code number
        for eachitem in self._columnnames:
            if str(eachitem) == "itemid" or str(eachitem) == "cpt_cd" or str(eachitem) == "icd9_code":
                return self._row[eachitem]

    @property
    def ConceptLabel(self): # "itemid" or "cpt_cd" or "icd9_code" is returned
        for eachitem in self._columnnames:
            if str(eachitem) == "itemid" or str(eachitem) == "cpt_cd" or str(eachitem) == "icd9_code":
                return str(eachitem)

    @property
    def _row(self):
        return self._rowtuple[0]

    @property
    def TimeStamp(self):
        for eachitem in self._columnnames:
            if str(eachitem) == "charttime" or str(eachitem) == "starttime" or str(eachitem) == "chartdate":
                return self._row[eachitem]

    @property
    def _columnnames(self):
        return self._rowtuple[0].dtype.names

    def ToString(self):
        astr = ""
        astr += str(self._row)
        astr += ", "
        astr += str(self.Label)
        return astr

class Record:
    def __init__(self, _chart, _platform):
        self._baseplatform = _platform
        self._tally = self._baseplatform.TallyChart(_chart)
        _sortedchart = Chart(_chart, self._baseplatform)
        self._sortedrecordentries = []
        for eachitem in _sortedchart.DataSorted["chart"]:
            self._sortedrecordentries.append(RecordEntry(eachitem))
        self._notes = _sortedchart.DataSorted["other"][2]
        self._icd9procedures = _sortedchart.DataSorted["other"][1]
        self._icd9diagnoses = _sortedchart.DataSorted["other"][0]
        # self._chart = _chart  # rawdata
        # self._baseplatform = _platform  # MockingWrapper.MockingBird(_db=_db, _sch=_sch)
        # self._tally = self._baseplatform.TallyChart(self._chart)  # raw data
        # self._sortedchart = Chart(self._chart, self._baseplatform)
        # self._sortedrecordentries = None
        ##self._timebucketlist = None
        self._recordpackagelist = []

    @property
    def Tally(self):
        return self._tally

    @property
    def RecordEntries(self):
        return self._sortedrecordentries

    @property
    def Notes(self):
        return self._notes #self._sortedchart.DataSorted["other"][2]

    @property
    def Icd9Procedures(self):
        return self._icd9procedures #self._sortedchart.DataSorted["other"][1]

    @property
    def Icd9Diagnoses(self):
        return self._icd9diagnoses #self._sortedchart.DataSorted["other"][0]

    @property
    def RecordPackageList(self):
        if self._recordpackagelist is None or len(self._recordpackagelist) <= 0:
            self._recordpackagelist = self._getrecordpackagelist()
        return self._recordpackagelist

    def _getrecordpackagelist(self):
        timecursor = numpy.datetime64(datetime.datetime.min)
        stagingarea = []
        currentrecordpackage = RecordPackage([])
        _recordpackagelist = [] # <-- object to return. list of RecordPackages
        iteratorcount = 0
        iteratormax = len(self.RecordEntries)
        for eachitem in self.RecordEntries:
            currenttimestamp = eachitem.TimeStamp #datetime.datetime(eachitem.TimeStamp)
            if currenttimestamp <= timecursor: # current timestamp is equal to the overallprogress of the loop
                currentrecordpackage.AddRecordEntry(eachitem)
            else: # (else if currenttimestamp > timecursor, meaning the chart "moved on" in form of currenttimestamp
                if currentrecordpackage.Count > 0:
                    _recordpackagelist.append(currentrecordpackage)
                timecursor = currenttimestamp
                currentrecordpackage = RecordPackage([])
                currentrecordpackage.AddRecordEntry(eachitem)
            iteratorcount += 1
            # now check if we're at the end of RecordEntries
            if iteratorcount >= iteratormax: # we hit the end of RecordEntries
                if len(currentrecordpackage.RecordEntries) > 0:
                    _recordpackagelist.append(currentrecordpackage)
        return _recordpackagelist


    def WriteToDiskOrganized(self, filepathway=""):
        if len(filepathway) > 0:
            if os.path.isfile(filepathway) == False:
                fullstr = ""
                afile = open(filepathway, "x")
                for eachitem in self.RecordEntries:
                    fullstr += str(eachitem.TimeStamp) + ", "
                    fullstr += str(eachitem.Label) + ", "
                    fullstr += str(eachitem.Value) + ", "
                    fullstr += str(eachitem.ConceptLabel) + ", "
                    fullstr += str(eachitem.ConceptId) + "\n"
                fullstr += "\n"
                fullstr += "___________________NOTES:___________________"
                fullstr += "\n"

                for eachthing in self.Notes:
                    fullstr += str(eachthing) + "\n"

                fullstr += "\n"
                fullstr += "___________________ICD9_PROCEDURES:___________________"
                fullstr += "\n"

                for eachthing in self.Icd9Procedures:
                    fullstr += str(eachthing) + "\n"

                fullstr += "\n"
                fullstr += "___________________ICD9_DIAGNOSES:___________________"
                fullstr += "\n"

                for eachthing in self.Icd9Diagnoses:
                    fullstr += str(eachthing) + "\n"

                afile.write(fullstr)
                afile.close()

    def WriteToDisk(self, filepathway=""):
        if len(filepathway) > 0:
            if os.path.isfile(filepathway) == False:
                afile = open(filepathway, "x")
                afile.write(self.DataString)
                afile.close()
        #self._wrappedchart_instance.WriteToDisk(_filepathway)

    # (hidden) - datastring of the sorted data, to be used in disk I/O by WriteToDisk method
    # modify this to control what gets written to HD
    @property
    def DataString(self):
        fullstr = ""
        fullstr += "___________________ENTRIES:_________________"
        for eachthing in self.RecordEntries:
            fullstr += eachthing.ToString() + "\n"

        fullstr += "\n"
        fullstr += "___________________NOTES:___________________"
        fullstr += "\n"

        for eachthing in self.Notes:
            fullstr += str(eachthing) + "\n"

        fullstr += "\n"
        fullstr += "___________________ICD9_PROCEDURES:___________________"
        fullstr += "\n"

        for eachthing in self.Icd9Procedures:
            fullstr += str(eachthing) + "\n"

        fullstr += "\n"
        fullstr += "___________________ICD9_DIAGNOSES:___________________"
        fullstr += "\n"

        for eachthing in self.Icd9Diagnoses:
            fullstr += str(eachthing) + "\n"
        return fullstr

    # EXPOSED - m1) writes the string provided by self.DataString to file.############################################
    ################################################


# class Record:
#     def __init__(self, _chart, _platform):
#         self._chart = _chart # rawdata
#         self._baseplatform = _platform #MockingWrapper.MockingBird(_db=_db, _sch=_sch)
#         self._tally = self._baseplatform.TallyChart(self._chart) # raw data
#         self._sortedchart = Chart(self._chart, self._baseplatform)
#         self._sortedrecordentries = None
#
#     @property
#     def _rawdata_unordered(self): # raw data
#         return self._chart
#
#     @property
#     def Tally(self):
#         return self._tally
#
#     @property
#     def _wrappedchart_instance(self): # type is of Chart (see above in this file)
#         if self._sortedchart is None:
#             self._sortchart()
#         if self._sortedrecordentries is None:
#             self._sortedrecordentries = []
#             for eachitem in self.Chart:
#                 arecentry = RecordEntry(eachitem)
#                 self._sortedrecordentries.append(arecentry)
#         return self._sortedrecordentries
#         # return self._sortedchart
#
#     @property
#     def Chart(self):
#         return self._sortedchart.DataSorted["chart"]
#
#     @property
#     def Notes(self):
#         return self._sortedchart.DataSorted["other"][2]
#
#     @property
#     def Icd9Procedures(self):
#         return self._sortedchart.DataSorted["other"][1]
#
#     @property
#     def Icd9Diagnoses(self):
#         return self._sortedchart.DataSorted["other"][0]
#
#     def _sortchart(self):
#         if self._sortedchart is None:
#             self._sortedchart = Chart(self._chart, self._baseplatform)
#
#     def WriteToDisk(self, _filepathway=""):
#         self._wrappedchart_instance.WriteToDisk(_filepathway)


##########################################################


    # def SortChart(self):

















# # DEPRECATED - previous version of current SortChart method##############################
    # # will rename to something else later on################################################
    # def SortChart2(self):
    #     timestamped_numpyrecords = []
    #     nostamped_numpyrecords = []
    #
    #     timestamped_silo_keys = {}
    #     nostamped_silo_keys = {}
    #
    #     for eachkey, eachrecarray in self.DataRaw.items():
    #         datetimetypehere = False
    #         for eachcolname, eachcoltypetuple in eachrecarray.dtype.fields.items():
    #             # print(eachcoltypetuple[0])
    #             # print("RUIEOWPURE(*#*(@$*##@")
    #             if numpy.dtype("datetime64[ns]") == eachcoltypetuple[0]:
    #                 if str(eachkey) not in timestamped_silo_keys.keys():
    #                     datetimetypehere = True
    #                     timestamped_silo_keys.update({str(eachkey): str(eachcolname)})
    #                     # print("there's a datetime")
    #             #     break
    #             # else:
    #             #     # print("no datetimehere")
    #             #     # # print(eachkey)
    #             #     # nostamped_numpyrecords.append(eachrecarray)
    #         if datetimetypehere == True:
    #             #timestamped_silo_keys.update({str(eachkey): str(eachcolname)})
    #             print(eachkey)
    #             print("_____")
    #             print("datetime exists")
    #         else:
    #             nostamped_numpyrecords.append(eachrecarray)
    #             print(eachkey)
    #             print("_____")
    #             print("NO DATETIME!")
    #
    #     print(timestamped_silo_keys)
    #
    #     timestamped_numpyrecords = self.MergeChartsByTime_branch1(self.DataRaw, timestamped_silo_keys)
    #     self._chartdatasorted.update({"chart": timestamped_numpyrecords})
    #     self._chartdatasorted.update({"icd": nostamped_numpyrecords})
    #     # afile = open("C:\\MMd\\merged3.csv", "x")
    #     # for eachthing in timestamped_numpyrecords:
    #     #     afile.write(str(eachthing))
    #     #     afile.write("\n")
    #     # afile.close()
    #
    #         #         hasdt = True
    #         #         break
    #         # if hasdt == True:
    #         #     if str(eachkey) not in timestamped_silo_keys.keys():
    #         #         timestamped_silo_keys
    #         # # if hasdt == True:
    #         # #     timestamped_silo_keys.extend(str(eachkey))
    #         # # else:
    #         # #     nostamped_silo_keys.extend(str(eachkey))
    #     return self._chartdatasorted

    # class TimeBucket:
    #     def __init__(self, _recordentries):
    #         self._recordentries = _recordentries
    #         self._ts = None
    #         self._setTimeSpanField()
    #
    #     @property
    #     def ItemIdList(self):
    #         iil = []
    #         for eachitem in self._recordentries:
    #             iil.extend(eachitem.ConceptId)
    #         return iil
    #
    #     @property
    #     def LabelList(self):
    #         ll = []
    #         for eachitem in self._recordentries:
    #             ll.extend(eachitem.Label)
    #         return ll
    #
    #     @property
    #     def ConceptLabelList(self):
    #         cll = []
    #         for eachitem in self._recordentries:
    #             cll.extend(eachitem.ConceptLabel)
    #         return cll
    #
    #     @property
    #     def StartTimeStamp(self):
    #         # self._setTimeSpanField()
    #         return self._ts.StartTimeStamp
    #
    #     @property
    #     def EndTimeStamp(self):
    #         # self._setTimeSpanField(self)
    #         return self._ts.EndTimeStamp
    #
    #     @property
    #     def Duration(self):
    #         # self._setTimeSpanField()
    #         return self._ts.Duration
    #
    #     @property
    #     def RecordEntries(self):
    #         return self._recordentries
    #
    #     def _setTimeSpanField(self):
    #         mintime = datetime.datetime.max
    #         maxtime = datetime.datettime.min
    #         for eachitem in self._recordentries:
    #             if mintime >= eachitem.TimeStamp:
    #                 mintime = eachitem.TimeStamp
    #             if maxtime <= eachitem.TimeStamp:
    #                 maxtime = eachitem.TimeStamp
    #         self._ts = TimeSpan(mintime, maxtime)
    #
    # # class RecordPackage:
    # #     def __init__(self, _recordentrylist):
    # #         self._recordentrylist = _recordentrylist
    # #
    # #     @property
    # #     def