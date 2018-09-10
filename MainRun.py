import datetime
import pandas
import numpy
import time
import MockingWrapper
import MimicObjects
import Context
import string
import SlidingWindow

################################### INTUBATED PHENOTYPING #########################################
ventcondition1 = SlidingWindow.PhenotypeDynamicItem(50812, "str", conditionlist=[("==","INTUBATED",1)])
ventcondition2 = SlidingWindow.PhenotypeDynamicItem(535, "number", conditionlist=[(">",0,1)])
ventcondition3 = SlidingWindow.PhenotypeDynamicItem(578, "number", conditionlist=[(">",0,1)])
ventcondition4 = SlidingWindow.PhenotypeDynamicItem(506, "number", conditionlist=[(">",0,1)])
ventcondition5 = SlidingWindow.PhenotypeDynamicItem(543, "number", conditionlist=[(">",0,1)])
ventcondition6 = SlidingWindow.PhenotypeDynamicItem(450, "number", conditionlist=[(">",0,1)])
ventcondition7 = SlidingWindow.PhenotypeDynamicItem(648, "str", conditionlist=[("==","Intubated/trach",1)])
ventcondition8 = SlidingWindow.PhenotypeDynamicItem(651, "number", conditionlist=[(">",0,1)])
ventcondition9 = SlidingWindow.PhenotypeDynamicItem(652, "number", conditionlist=[(">",0,1)])
ventcondition10 = SlidingWindow.PhenotypeDynamicItem(682, "number", conditionlist=[(">",0,1)])
ventcondition11 = SlidingWindow.PhenotypeDynamicItem(683, "number", conditionlist=[(">",0,1)])
ventcondition12 = SlidingWindow.PhenotypeDynamicItem(684, "number", conditionlist=[(">",0,1)])
# ventcondition13 = SlidingWindow.PhenotypeDynamicItem(50819, "number", conditionlist=[(">",0,1)])
ventcondition14 = SlidingWindow.PhenotypeDynamicItem(50828, "number", conditionlist=[(">",0,1)])
ventcondition15 = SlidingWindow.PhenotypeDynamicItem(50826, "number", conditionlist=[(">",0,1)])
ventcondition16 = SlidingWindow.PhenotypeDynamicItem(684, "number", conditionlist=[(">",0,1)])
ventcondition17 = SlidingWindow.PhenotypeDynamicItem(157, "str", conditionlist=[("!=","None",1)])
ventcondition18 = SlidingWindow.PhenotypeDynamicItem(640, "str", conditionlist=[("==","Intubated",1)])
# ventcondition19 = SlidingWindow.PhenotypeDynamicItem(50819, "number", conditionlist=[(">",0,1)])
# ventcondition20 = SlidingWindow.PhenotypeDynamicItem(50826, "number", conditionlist=[(">",0,1)])
ventcondition21 = SlidingWindow.PhenotypeDynamicItem(50, "number", conditionlist=[(">",0,1)])
ventcondition22 = SlidingWindow.PhenotypeDynamicItem(444, "number", conditionlist=[(">",0,1)])
ventcondition23 = SlidingWindow.PhenotypeDynamicItem(619, "number", conditionlist=[(">",0,1)])
ventcondition24 = SlidingWindow.PhenotypeDynamicItem(449, "number", conditionlist=[(">",0,1)])
ventcondition25 = SlidingWindow.PhenotypeDynamicItem(224684, "number", conditionlist=[(">",0,1)])
ventcondition26 = SlidingWindow.PhenotypeDynamicItem(224685, "number", conditionlist=[(">",0,1)])
ventcondition27 = SlidingWindow.PhenotypeDynamicItem(224686, "number", conditionlist=[(">",0,1)])
ventcondition28 = SlidingWindow.PhenotypeDynamicItem(224421, "number", conditionlist=[(">",0,1)])
ventcondition29 = SlidingWindow.PhenotypeDynamicItem(220339, "number", conditionlist=[(">",0,1)])
ventcondition30 = SlidingWindow.PhenotypeDynamicItem(224688, "number", conditionlist=[(">",0,1)])
ventcondition31 = SlidingWindow.PhenotypeDynamicItem(224689, "number", conditionlist=[(">",0,1)])
ventcondition32 = SlidingWindow.PhenotypeDynamicItem(224690, "number", conditionlist=[(">",0,1)])
# ventcondition33 = SlidingWindow.PhenotypeDynamicItem(220210, "number", conditionlist=[(">",0,1)])
ventcondition34 = SlidingWindow.PhenotypeDynamicItem(224422, "number", conditionlist=[(">",0,1)])
ventcondition35 = SlidingWindow.PhenotypeDynamicItem(224687, "number", conditionlist=[(">",0,1)])
ventcondition36 = SlidingWindow.PhenotypeDynamicItem(224696, "number", conditionlist=[(">",0,1)])
ventcondition37 = SlidingWindow.PhenotypeDynamicItem(223900, "str", conditionlist=[("==","No Response-ETT",1)])
ventcondition38 = SlidingWindow.PhenotypeDynamicItem(223902, "str", conditionlist=[("==","Intubated/trached",1)])
ventcondition39 = SlidingWindow.PhenotypeDynamicItem(226732, "str", conditionlist=[("==","Endotracheal tube",1)])
ventcondition40 = SlidingWindow.PhenotypeDynamicItem(224832, "str", conditionlist=[("==","Standard",1)])
ventcondition41 = SlidingWindow.PhenotypeDynamicItem(223838, "str", conditionlist=[("==","Oral-L",0), ("==","Oral-R",0)])
ventcondition42 = SlidingWindow.PhenotypeDynamicItem(224415, "str", conditionlist=[("!=","Not Applicable",0), ("!=","None",0)])
ventcondition43 = SlidingWindow.PhenotypeDynamicItem(224385, "number", conditionlist=[(">",0,1)])
ventcondition44 = SlidingWindow.PhenotypeDynamicItem(223837, "str", conditionlist=[("!=","Not applicable",0), ("!=","None",0)])
ventcondition45 = SlidingWindow.PhenotypeDynamicItem(224700, "number", conditionlist=[(">",0,1)])
ventcondition46 = SlidingWindow.PhenotypeDynamicItem(223848, "str", conditionlist=[("!=","Not applicable",0), ("!=","None",0)])
ventcondition47 = SlidingWindow.PhenotypeDynamicItem(227810, "number", conditionlist=[(">",0,1)])
ventcondition48 = SlidingWindow.PhenotypeDynamicItem(1483, "str", conditionlist=[("!=","Not applicable",0), ("!=","None",0), ("!=","Exempt per order",0), ("!=","Exempt per MD",0), ("!=","CMO",0)])
ventcondition49 = SlidingWindow.PhenotypeDynamicItem(224740, "str", conditionlist=[("!=","Not applicable",0), ("!=","None",0), ("!=","Exempt per order",0), ("!=","Exempt per MD",0), ("!=","CMO",0)])
# ventcondition43 = SlidingWindow.PhenotypeDynamicItem(227810, "number", conditionlist=[(">",0,1)])



intubatedstatephenotypeitemlist = [ventcondition1, ventcondition2, ventcondition3,ventcondition4,ventcondition5,ventcondition6,ventcondition7,ventcondition8,ventcondition9,ventcondition10,ventcondition11,ventcondition12,ventcondition14,ventcondition15,ventcondition16,ventcondition17,ventcondition18,ventcondition21,ventcondition22,ventcondition23,ventcondition24,ventcondition25,ventcondition26,ventcondition27,ventcondition28,ventcondition29,ventcondition30,ventcondition31,ventcondition32,ventcondition34,ventcondition35,ventcondition36,ventcondition37,ventcondition38,ventcondition39,ventcondition40,ventcondition41,ventcondition42,ventcondition43,ventcondition44,ventcondition45,ventcondition46,ventcondition47,ventcondition48,ventcondition49]

intubatedphenotype = SlidingWindow.PhenotypeDynamic("intubated", _phenotypeitemlist=intubatedstatephenotypeitemlist)
##########################################################################################

######################## Non-invasive airway PHENOTYPING
# notubecondition1a = SlidingWindow.PhenotypeDynamicItem(640, "str", conditionlist=[("==","Extubated",1)])
# notubecondition2a = SlidingWindow.PhenotypeDynamicItem(50812, "str", conditionlist=[("==","NOT INTUBATED",0), ("!=","INTUBATED",0)])
# notubecondition3a = SlidingWindow.PhenotypeDynamicItem(467, "str", conditionlist=[("!=","Other/Remarks",0), ("!=","None",0)])
# notubecondition4a = SlidingWindow.PhenotypeDynamicItem(468, "str", conditionlist=[("!=","Other/Remarks",0), ("!=","None",0)])
# #notubecondition5a = SlidingWindow.PhenotypeDynamicItem(723, "str", conditionlist=[("==","5 Oriented",1)])
# notubecondition6a = SlidingWindow.PhenotypeDynamicItem(1087, "str", conditionlist=[("==","Pt Verbalized",1)])
# notubecondition7a = SlidingWindow.PhenotypeDynamicItem(63, "number", conditionlist=[(">",0,1)])
# notubecondition8a = SlidingWindow.PhenotypeDynamicItem(64, "number", conditionlist=[(">",0,1)])
# notubecondition9a = SlidingWindow.PhenotypeDynamicItem(66, "number", conditionlist=[(">",0,1)])
# notubecondition10a = SlidingWindow.PhenotypeDynamicItem(68, "str", conditionlist=[("!=","None",1)])
#
# NIairway_phenotypeitemlist = [notubecondition1a, notubecondition2a, notubecondition3a, notubecondition4a, notubecondition6a, notubecondition7a, notubecondition8a, notubecondition9a, notubecondition10a]
#
# NIairway_phenotype = SlidingWindow.PhenotypeDynamic("extub_event", _phenotypeitemlist=NIairway_phenotypeitemlist)
#########################################################

######################################### EXTUBATED PHENOTYPING ####################################
# notubecondition1 = SlidingWindow.PhenotypeDynamicItem(50812, "str", conditionlist=[("==","NOT INTUBATED",0), ("!=","INTUBATED",0)])
# notubecondition2 = SlidingWindow.PhenotypeDynamicItem(535, "str", conditionlist=[("==","None",0), ("==","Not Applicable",0)])
# notubecondition3 = SlidingWindow.PhenotypeDynamicItem(578, "str", conditionlist=[("==","None",0), ("==","Not Applicable",0)])
# notubecondition4 = SlidingWindow.PhenotypeDynamicItem(506, "str", conditionlist=[("==","None",0), ("==","Not Applicable",0)])
# notubecondition5 = SlidingWindow.PhenotypeDynamicItem(543, "str", conditionlist=[("==","None",0), ("==","Not Applicable",0)])
# notubecondition6 = SlidingWindow.PhenotypeDynamicItem(450, "str", conditionlist=[("==","None",0), ("==","Not Applicable",0)])
# notubecondition7 = SlidingWindow.PhenotypeDynamicItem(648, "str", conditionlist=[("!=","Intubated/trach",1)])
# notubecondition8 = SlidingWindow.PhenotypeDynamicItem(651, "str", conditionlist=[("==","None",0), ("==","Not Applicable",0)])
# notubecondition9 = SlidingWindow.PhenotypeDynamicItem(652, "str", conditionlist=[("==","None",0), ("==","Not Applicable",0)])
# notubecondition10 = SlidingWindow.PhenotypeDynamicItem(682, "str", conditionlist=[("==","None",0), ("==","Not Applicable",0)])
# notubecondition11 = SlidingWindow.PhenotypeDynamicItem(683, "str", conditionlist=[("==","None",0), ("==","Not Applicable",0)])
# notubecondition12 = SlidingWindow.PhenotypeDynamicItem(684, "str", conditionlist=[("==","None",0), ("==","Not Applicable",0)])
# notubecondition13 = SlidingWindow.PhenotypeDynamicItem(50819, "str", conditionlist=[("==","None",0), ("==","Not Applicable",0)])
# notubecondition14 = SlidingWindow.PhenotypeDynamicItem(50828, "str", conditionlist=[("==","None",0), ("==","Not Applicable",0)])
# notubecondition15 = SlidingWindow.PhenotypeDynamicItem(50826, "str", conditionlist=[("==","None",0), ("==","Not Applicable",0)])
# notubecondition16 = SlidingWindow.PhenotypeDynamicItem(684, "str", conditionlist=[("==","None",0), ("==","Not Applicable",0)])
# notubecondition17 = SlidingWindow.PhenotypeDynamicItem(157, "str", conditionlist=[("==","None",1)])
# notubecondition18 = SlidingWindow.PhenotypeDynamicItem(640, "str", conditionlist=[("==","Extubated",1)])
# notubecondition19 = SlidingWindow.PhenotypeDynamicItem(50819, "str", conditionlist=[("==","None",0), ("==","Not Applicable",0)])
# notubecondition20 = SlidingWindow.PhenotypeDynamicItem(50826, "str", conditionlist=[("==","None",0), ("==","Not Applicable",0)])
# notubecondition21 = SlidingWindow.PhenotypeDynamicItem(50, "str", conditionlist=[("==","None",0), ("==","Not Applicable",0)])
# notubecondition22 = SlidingWindow.PhenotypeDynamicItem(444, "str", conditionlist=[("==","None",0), ("==","Not Applicable",0)])
# notubecondition23 = SlidingWindow.PhenotypeDynamicItem(619, "str", conditionlist=[("==","None",0), ("==","Not Applicable",0)])
# notubecondition24 = SlidingWindow.PhenotypeDynamicItem(449, "str", conditionlist=[("==","None",0), ("==","Not Applicable",0)])
#
# extubatedstatephenotypeitemlist = [notubecondition1, notubecondition2, notubecondition3,notubecondition4,notubecondition5,notubecondition6,notubecondition7,notubecondition8,notubecondition9,notubecondition10,notubecondition11,notubecondition12,notubecondition13,notubecondition14,notubecondition15,notubecondition16,notubecondition17,notubecondition18,notubecondition19,notubecondition20,notubecondition21,notubecondition22,notubecondition23,notubecondition24]
#
# extubatedphenotype = SlidingWindow.PhenotypeDynamic("intub_stat", _phenotypeitemlist=extubatedstatephenotypeitemlist)
####################################################################################################

######################################## EXTUBATION EVENT PHENOTYPING ##########

notubecondition1a = SlidingWindow.PhenotypeDynamicItem(640, "str", conditionlist=[("==","Extubated",1)])
notubecondition2a = SlidingWindow.PhenotypeDynamicItem(50812, "str", conditionlist=[("==","NOT INTUBATED",0), ("!=","INTUBATED",0)])
notubecondition3a = SlidingWindow.PhenotypeDynamicItem(467, "str", conditionlist=[("!=","Other/Remarks",0), ("!=","None",0), ("!=","Not applicable",0)])
notubecondition4a = SlidingWindow.PhenotypeDynamicItem(468, "str", conditionlist=[("!=","Other/Remarks",0), ("!=","None",0), ("!=","Not applicable",0)])
#notubecondition5a = SlidingWindow.PhenotypeDynamicItem(723, "str", conditionlist=[("==","5 Oriented",1)])
# notubecondition6a = SlidingWindow.PhenotypeDynamicItem(1087, "str", conditionlist=[("!=","Other/Remarks",0), ("!=","None",0), ("!=","Not applicable",0)])
notubecondition7a = SlidingWindow.PhenotypeDynamicItem(63, "number", conditionlist=[(">",0,1)])
notubecondition8a = SlidingWindow.PhenotypeDynamicItem(64, "number", conditionlist=[(">",0,1)])
notubecondition9a = SlidingWindow.PhenotypeDynamicItem(66, "number", conditionlist=[(">",0,1)])
notubecondition10a = SlidingWindow.PhenotypeDynamicItem(68, "str", conditionlist=[("!=","Other/Remarks",0), ("!=","None",0), ("!=","Not applicable",0)])
notubecondition11a = SlidingWindow.PhenotypeDynamicItem(67, "number", conditionlist=[(">",0,1)])
notubecondition12a = SlidingWindow.PhenotypeDynamicItem(223903, "str", conditionlist=[("==","Verbal",1)])
notubecondition13a = SlidingWindow.PhenotypeDynamicItem(227582, "number", conditionlist=[(">",0,1)])
notubecondition14a = SlidingWindow.PhenotypeDynamicItem(227580, "number", conditionlist=[(">",0,1)])
notubecondition15a = SlidingWindow.PhenotypeDynamicItem(227579, "number", conditionlist=[(">",0,1)])
notubecondition16a = SlidingWindow.PhenotypeDynamicItem(227577, "str", conditionlist=[("!=","Other/Remarks",0), ("!=","None",0), ("!=","Not applicable",0)])
notubecondition17a = SlidingWindow.PhenotypeDynamicItem(227578, "str", conditionlist=[("!=","Other/Remarks",0), ("!=","None",0), ("!=","Not applicable",0)])
notubecondition18a = SlidingWindow.PhenotypeDynamicItem(228414, "str", conditionlist=[("==","Normal",1)])


extubationeventphenotypeitemlist = [notubecondition1a, notubecondition2a, notubecondition3a, notubecondition4a, notubecondition7a, notubecondition8a, notubecondition9a, notubecondition10a, notubecondition11a, notubecondition12a, notubecondition13a, notubecondition14a, notubecondition15a, notubecondition16a, notubecondition17a, notubecondition18a]

extubeventphenotype = SlidingWindow.PhenotypeDynamic("extubated", _phenotypeitemlist=extubationeventphenotypeitemlist)
#################################################

##### noninvasive phenotyping ######
# noninvasive1 =

##### tracheo phenotyping ######
trcondition1 = SlidingWindow.PhenotypeDynamicItem(224829, "str", conditionlist=[("!=", "None", 0), ("!=", "Not Applicable", 0)])
trcondition2 = SlidingWindow.PhenotypeDynamicItem(223847, "str", conditionlist=[("!=", "None", 0), ("!=", "Not Applicable", 0), ("!=", "No", 0)])
trcondition3 = SlidingWindow.PhenotypeDynamicItem(224830, "str", conditionlist=[("!=", "None", 0), ("!=", "Not Applicable", 0), ("!=", "No", 0)])
trcondition4 = SlidingWindow.PhenotypeDynamicItem(224831, "str", conditionlist=[("!=", "None", 0), ("!=", "Not Applicable", 0), ("!=", "No", 0)])
trcondition5 = SlidingWindow.PhenotypeDynamicItem(225448, "number", conditionlist=[(">",0,1)])
trcondition6 = SlidingWindow.PhenotypeDynamicItem(224417, "number", conditionlist=[(">",0,1)])
trcondition7 = SlidingWindow.PhenotypeDynamicItem(687, "str", conditionlist=[("!=", "None", 0), ("!=", "Not Applicable", 0), ("!=", "Other", 0)])
trcondition8 = SlidingWindow.PhenotypeDynamicItem(7286, "str", conditionlist=[("==", "Done", 1)])
trcondition9 = SlidingWindow.PhenotypeDynamicItem(688, "str", conditionlist=[("!=", "None", 0), ("!=", "Not Applicable", 0)])
trcondition10 = SlidingWindow.PhenotypeDynamicItem(690, "str", conditionlist=[("!=", "None", 0), ("!=", "Not Applicable", 0)])
trcondition11 = SlidingWindow.PhenotypeDynamicItem(691, "str", conditionlist=[("!=", "None", 0), ("!=", "Not Applicable", 0)])
trcondition12 = SlidingWindow.PhenotypeDynamicItem(692, "str", conditionlist=[("!=", "None", 0), ("!=", "Not Applicable", 0)])
# ventcondition1 = SlidingWindow.PhenotypeDynamicItem(50812, "str", conditionlist=[("==","INTUBATED",1)])
# ventcondition2 = SlidingWindow.PhenotypeDynamicItem(535, "number", conditionlist=[(">",0,1)])

trachphenotypeitemlist = [trcondition1, trcondition2, trcondition3, trcondition4, trcondition5, trcondition6, trcondition7, trcondition8, trcondition9, trcondition10, trcondition11, trcondition12]

trachphenotype = SlidingWindow.PhenotypeDynamic("trached", _phenotypeitemlist=trachphenotypeitemlist)

################ SBT capturing phenotyping ########################
sbtcondition1 = SlidingWindow.PhenotypeDynamicItem(595, "number", conditionlist=[(">",0,1)])
sbtcondition2 = SlidingWindow.PhenotypeDynamicItem(1397, "number", conditionlist=[(">",0,1)])
sbtcondition3 = SlidingWindow.PhenotypeDynamicItem(614, "number", conditionlist=[(">",0,1)])
sbtcondition4 = SlidingWindow.PhenotypeDynamicItem(651, "number", conditionlist=[(">",0,1)])
sbtcondition5 = SlidingWindow.PhenotypeDynamicItem(652, "number", conditionlist=[(">",0,1)])
sbtcondition6 = SlidingWindow.PhenotypeDynamicItem(684, "number", conditionlist=[(">",0,1)])
sbtcondition7 = SlidingWindow.PhenotypeDynamicItem(224686, "number", conditionlist=[(">",0,1)])
sbtcondition8 = SlidingWindow.PhenotypeDynamicItem(224421, "number", conditionlist=[(">",0,1)])
sbtcondition9 = SlidingWindow.PhenotypeDynamicItem(224689, "number", conditionlist=[(">",0,1)])
sbtcondition10 = SlidingWindow.PhenotypeDynamicItem(224422, "number", conditionlist=[(">",0,1)])

sbtconditionitemlist = [sbtcondition1,sbtcondition2,sbtcondition3,sbtcondition4,sbtcondition5,sbtcondition6,sbtcondition7,sbtcondition8,sbtcondition9,sbtcondition10]

sbtphenotype = SlidingWindow.PhenotypeDynamic("SBT", _phenotypeitemlist=sbtconditionitemlist)
############################ BRAINSTORMING... #########################

#

#######################################################

fullphenotype = [intubatedphenotype, extubeventphenotype, trachphenotype, sbtphenotype]

### BUG: record[0] gets out of range at times. specifically patient #57 ~ #59...
### it was 59. C:\MMd\hadm_id=186474 AND subject_id=67_compositecursors3.csv this is the patient.
## jesus. hadm_id 186474 has NO data.

#hadm_id=174486 AND subject_id=357 - perfect patient candidate - never trached
### BUG: patient 94 (C:\MMd\hadm_id=174162 AND subject_id=107_compositecursors3.csv) has a numpy.float64 object has no attr 'replace' error.

# BUG - ValueError: invalid literal for int() with base 10: 'G0272'
# this is C:\MMd\hadm_id=169339 AND subject_id=345_compositecursors4.csv's chart. Patient # 238
####################9-4-2018#############

# candidates for era testing:
# hadm_id=114585 AND subject_id=115
# hadm_id=174486 AND subject_id=357
# hadm_id=197569 AND subject_id=330
# hadm_id=168847 AND subject_id=156 - ERROR AT EXTUBATION...
# hadm_id=199488 AND subject_id=148
# hadm_id=198161 AND subject_id=145
####

mock = MockingWrapper.MockingBird(_db="postgres", _sch="public")
therecord = mock.GetChartRecord(_filter="hadm_id=168847 AND subject_id=156") #hadm_id=145674 AND subject_id=357")
wide = SlidingWindow.CompositeCursor(therecord, fullphenotype, _durationwidth=numpy.timedelta64(360, 'm'), _advancementduration=numpy.timedelta64(30, 'm'))
narr = SlidingWindow.CompositeCursor(therecord, fullphenotype, _durationwidth=numpy.timedelta64(10, 'm'), _advancementduration=numpy.timedelta64(5, 'm'))
wide.GetAllCaptureArrays()
narr.GetAllCaptureArrays()

anerawide = SlidingWindow.EventDetection(wide, _fullcapture=True)
aneranarr = SlidingWindow.EventDetection(narr)

# dumpywide = anerawide.OrderEventsByTime()
# dumpynarr = aneranarr.OrderEventsByTime()

for eachitem in anerawide.TimeOrderedEvents: #dumpywide:
    print(eachitem)
print("__________")
for eachitem in aneranarr.TimeOrderedEvents: #dumpynarr:
    print(eachitem)
#
# dumpy.sort(key= lambda timestamp: timestamp[0])
#
# print("___________")
# print(dumpy)
#
# dumpy2 = numpy.sort(dumpy, axis=0, dtype=[("timestamp", 'M'), ("index", 'i'), ("state",'S')], order="timestamp")
# print(dumpy2)
# look = anera.EraListDates
# print(anera.EraListDates)

# eralist = SlidingWindow.EventDetection.FindErasAll(wide)

# eras = SlidingWindow.EventDetection.FindEras(wide, "intub")
#
# print(eras)
# short = SlidingWindow.CompositeCursor(therecord, fullphenotype, _durationwidth=numpy.timedelta64(180, 'm'), _advancementduration=numpy.timedelta64(90, 'm'))
# ws = [wide, short]
# bigman = SlidingWindow.CompositeCursorStack(ws)
# print(str(bigman.CurrentTimeSpanCapturesArrayVertical("intub")), str(bigman.CurrentTimeSpanCapturesArrayVertical("extub")), str(bigman.CurrentTimeSpanCapturesArrayVertical("trach")), str(bigman.CurrentTimeSpanCapturesArrayVertical("sbt")))
# bigman.Advance()
# print(str(bigman.CurrentTimeSpanCapturesArrayVertical("intub")), str(bigman.CurrentTimeSpanCapturesArrayVertical("extub")), str(bigman.CurrentTimeSpanCapturesArrayVertical("trach")), str(bigman.CurrentTimeSpanCapturesArrayVertical("sbt")))
# bigman.Advance()
# print(str(bigman.CurrentTimeSpanCapturesArrayVertical("intub")), str(bigman.CurrentTimeSpanCapturesArrayVertical("extub")), str(bigman.CurrentTimeSpanCapturesArrayVertical("trach")), str(bigman.CurrentTimeSpanCapturesArrayVertical("sbt")))
# mock.GetChartRecord(_filter="hadm_id=110777 AND subject_id=335", _outputfilepath="C:\\MMd\\hadm_id=110777 AND subject_id=335.csv",_writetofile=True)
# print("done")
# mock.ScanAdmissionsRecords(_patientcount=230, _writetofile=True)
#mock.ScanAdmissionsRecords_CompositeCursors(fullphenotype, _patientcount=230, _durationwidth=numpy.timedelta64(10, 'm'), _advancementduration=numpy.timedelta64(5, 'm'))

# #hadm_id=174486 AND subject_id=357") #hadm_id=140037 AND subject_id=94") #hadm_id=198161 AND subject_id=145")
#

# thedata = fullspectrum.GetAllCaptureArrays()

#SlidingWindow.CompositeCursor.DisplayConsole(thedata)


# thestr = ""
# for eachkey, eachitem in thedata.items():
#     thisline = ""
#     thisline += str(eachkey) + ", "
#     for eachkey2, eachitem2 in eachitem.items():
#         thisline += str(eachitem2.Value) + ", "
#     print(thisline)
#     thestr += thisline
#     thestr += "\n"


# windowIntubated = SlidingWindow.SlidingCursorDynamic(therecord, intubatedphenotype, _durationwidth=numpy.timedelta64(360, 'm'), _advancementduration=numpy.timedelta64(120, 'm'))
# windowIntubated.CaptureAll0906()
# for eachitem in windowIntubated.Captured:
#     print(str(eachitem.LeftBound) + ", " + str(eachitem.Value))

# windowExtubated = SlidingWindow.SlidingCursorDynamic(therecord, extubeventphenotype, _durationwidth=numpy.timedelta64(360, 'm'), _advancementduration=numpy.timedelta64(120, 'm'))
# windowExtubated.CaptureAll0906()
# for eachitem in windowExtubated.Captured:
#     print(str(eachitem.LeftBound) + ", " + str(eachitem.Value))


# windowIntubated.CaptureAll0906()
# for eachitem in windowIntubated.Captured:
#     print(eachitem.Value)

# # windowintubated = SlidingWindow.SlidingCursorDynamic(therecord, intubatedphenotype, _durationwidth=numpy.timedelta64(360, 'm'), _advancementduration=numpy.timedelta64(120, 'm'))
# for eachkey, eachitem in intubatedphenotype._phenotypes.items():
#     print(eachkey)
#     for eachitem2 in eachitem._conditionlist:
#         print(str(eachitem.Type) + ", " + str(eachitem2))


#mock.ScanAdmissionsRecords(_writetofile=True, _patientcount=200)



######################################
# mock.ScanAdmissionsRecords_AdvancedTally(_patientcount=200, _writetofile=False)
# afile = open("C:\\MMd\\TALLY200a.txt", "x")
# afile.write(mock.AdvancedTally_String)
# afile.close()
#######################################

# arec = mock.GetChartRecord(_filter="hadm_id=198161 AND subject_id=145")
# print(arec.PatientInfo.Age)
# print(arec.PatientInfo.dob)
# thephenotype = SlidingWindow.PhenotypeDynamic([640, 506, 578, 722, 720, 682, 683, 684, 732, 157, 543, 631, 40, 50826, 50819, 50827, 50828, 221, 619, 8382, 50, 535, 218])
# # dictphen = {}
# # for eachitem in thephenotype:
# #     if eachitem not in dictphen:
# #         dictphen.update({eachitem: {}})
# uvalues = arec.GetUniqueConceptIds(searchdictionary=thephenotype._phenotypes)
#
# for eachkey, eachvalue in uvalues.items():
#     print(str(eachkey) + ", " + str(eachvalue))

# awindow = SlidingWindow.SlidingCursorDynamic(arec, thephenotype, _durationwidth=numpy.timedelta64(360, 'm'), _advancementduration=numpy.timedelta64(120, 'm'))
# awindow.CaptureAll()
# for eachitem in awindow.Captured:
#     print(str(eachitem.LeftBound) + "," + str(eachitem.Value))
# acap = awindow.Capture()
# awindow.Advance()
# print(acap.LeftBound)
# print(acap.RightBound)
# print(acap.Value)
# acap = awindow.Capture()
# awindow.Advance()
# print(acap.LeftBound)
# print(acap.RightBound)
# print(acap.Value)
# awindow.CaptureAll()
# for eachitem in awindow.Captured:
#     if eachitem.Value >= 0:
#         print(str(eachitem.LeftBound) + ", " + str(eachitem.Value) + ", " + str(eachitem.RightBound))

# snaps = []
# asnap1 = awindow.Capture()
# snaps.append(asnap1)
# print(awindow.Advance())
# asnap2 = awindow.Capture()
# snaps.append(asnap2)
# print(awindow.Advance())
# asnap3 = awindow.Capture()
# snaps.append(asnap3)
# print(awindow.Advance())
# asnap4 = awindow.Capture()
# snaps.append(asnap4)
# print(awindow.Advance())
#
# for eachitem in snaps:
#     print(str(eachitem.LeftBound) + ", " + str(eachitem.RightBound))
################################################################



# aphen = SlidingWindow.PhenotypeDynamic([640, 506, 578, 722, 720, 682, 683, 684, 732, 157, 543, 631, 40, 50826, 50819, 50827, 50828, 221, 619, 8382, 50, 535, 218])
#
#

#


#awindow = SlidingWindow.SlidingCursorSimple(arec, _cursorwidth=10, _capturephenotype=thephenotype)
#awindow.TraverseRecord()

# for eachitem in awindow.SnapFrameList:
#     print(str(eachitem.Value) + ", " + str(eachitem.LeftDate) + ", " + str(eachitem.RightDate))

# class BangIterable:
#     def __init__(self, default = []):
#         self._array = default
#         self._index = 0
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         if self._index < len(self._array) - 1:
#             self._index += 1
#         else:
#             raise StopIteration
#         return self._index
#
#     def __getitem__(self, _index):
#         return self._array[_index]
#
# obj = BangIterable([1,2,3,4,5,6])
#
# for eachitem in obj:
#     print(eachitem)


# for eachitem in awindow.SelectedItems:
#     print(str(eachitem.TimeStamp))
#     print(str(eachitem.LabelList))
#     print(str(eachitem.ConceptLabelList))
#     print("________________________")
#
# awindow.AdvanceWindowByItem()
# print("________________________")
# print("________________________")
# print("________________________")
# print("________________________")
#
# for eachitem in awindow.SelectedItems:
#     print(str(eachitem.TimeStamp))
#     print(str(eachitem.LabelList))
#     print(str(eachitem.ConceptLabelList))
#     print("________________________")

# for eachitem in arec.RecordPackageList:
#     print(str(eachitem.TimeStamp))
#     print(str(eachitem.LabelList))
#     print(str(eachitem.ConceptLabelList))
#     print("________________________")

# arecord = mock.GetChartRecord(_filter="subject_id=23 AND hadm_id=152223")
# arecord.WriteToDisk("C:\\MMd\\experimental\\hello.csv")

#vhghjghjghj

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
# print("______________________\n")
# print("______________________\n")
# print("______________________\n")
# print("______________________\n")
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
