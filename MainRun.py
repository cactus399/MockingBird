import MimicServer
import MimicObjects
import MimicBrowsing
import datetime
import pandas
import numpy

msp = MimicServer.MimicServerPlatform.ctor0("postgres", "public")
msp.connect()
thecurse = msp.connection.cursor("curse")
thestr = "SELECT * FROM patients;"
thecurse.execute(thestr)
avar = thecurse.fetchall()

for athing in avar:
    print(athing)