import datetime
import pandas
import numpy

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


class LabEvent(MimicEvent,AutoRepr):
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


class DateTimeEvent(MimicEvent,AutoRepr):
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



# class Admission(EventSpan):
#     def __init__(self):



# adt = datetime.datetime.min
# print(adt)

# s = pandas.Series(numpy.random.randn(5), index=['a','b','c','d','e'])
# k = s[1:] + s[:-1]