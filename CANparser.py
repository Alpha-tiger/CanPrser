import os,subprocess
import pygal


totalpgnbytelist = []

class parser_summary:
    instance_filename = 'empty'

    #speed list to store speed and timestamp


    def __init__(self,filename):
        self.instance_filename = filename
        self.pgn_list = []
        self.spn_list = []
        self.speed_timestamp = []
        self.speed_value = []
        self.boostpressure_value = []
        self.boostpressure_timestamp = []
        self.engoilpressure_value = []
        self.engoilpressure_timestamp = []
        self.engcoolanttemp_value = []
        self.engcoolanttemp_timestamp = []
        self.engmanifoldtemperature_value = []
        self.engmanifoldtemperature_timestamp = []
        self.engmanifoldpressure_value = []
        self.engmanifoldpressure_timestamp = []
        self.fulerate_value = []
        self.fulerate_timestamp = []
        self.pgn_byte_list = []
        self.pgn_list = []
        self.spn_list = []
        self.set_pgnlist = []
        self.GenAvgL2LV = []
        self.GenAvgL2NV = []
        self.GenAvgACFrequency = []
        self.GenAvgACRMS = []
        self.GenAvgTimestamp = []
        self.GenPhaseAFrequency = []
        self.GenPhaseAL2LV = []
        self.GenPhaseAL2NV = []
        self.GenPhaseACurrent = []
        self.GenPhaseATimestamp = []
        self.GenPhaseBFrequency = []
        self.GenPhaseBL2LV = []
        self.GenPhaseBL2NV = []
        self.GenPhaseBCurrent = []
        self.GenPhaseBTimestamp = []
        self.GenPhaseCFrequency = []
        self.GenPhaseCL2LV = []
        self.GenPhaseCL2NV = []
        self.GenPhaseCCurrent = []
        self.GenPhaseCTimestamp = []

    def add_speed (self,speed,timestamp):

        if  len(self.speed_timestamp)>0 and timestamp == self.speed_timestamp[-1] :
            pass
        else:
            self.speed_value.append(speed)
            self.speed_timestamp.append(timestamp)

    def add_engoilpressure (self,value,timestamp):

        if len(self.engoilpressure_value) > 0 and timestamp == self.engoilpressure_timestamp[-1]:
            pass
        else:
            self.engoilpressure_value.append(value)
            self.engoilpressure_timestamp.append(timestamp)

    def add_boostpressure (self,value,timestamp):

        if len(self.boostpressure_value) > 0 and timestamp == self.boostpressure_timestamp[-1]:
            pass
        else:
            self.boostpressure_value.append(value)
            self.boostpressure_timestamp.append(timestamp)

    def add_engcoolanttemp (self,value,timestamp):

        if len(self.engcoolanttemp_value) > 0 and timestamp == self.engcoolanttemp_timestamp[-1]:
            pass
        else:
            self.engcoolanttemp_value.append(value)
            self.engcoolanttemp_timestamp.append(timestamp)

    def add_engmanifoldpressure (self,value,timestamp):

        if len(self.engmanifoldpressure_value) > 0 and timestamp == self.engmanifoldpressure_timestamp[-1]:
            pass
        else:
            self.engmanifoldpressure_value.append(value)
            self.engmanifoldpressure_timestamp.append(timestamp)

    def add_engmanifoldtemperature (self,value,timestamp):

        if len(self.engmanifoldtemperature_value) > 0 and timestamp == self.engmanifoldtemperature_timestamp[-1]:
            pass
        else:
            self.engmanifoldtemperature_value.append(value)
            self.engmanifoldtemperature_timestamp.append(timestamp)

    def add_fulerate(self,value,timestamp):

        if len(self.fulerate_value) > 0 and timestamp == self.fulerate_timestamp[-1]:
            pass
        else:
            self.fulerate_value.append(value)
            self.fulerate_timestamp.append(timestamp)

    def add_GenAvg (self,current,frequency,l2l,l2n,timestamp):

        if len(self.GenAvgTimestamp) > 0 and timestamp == self.GenAvgTimestamp[-1]:
            pass
        else:
            self.GenAvgACFrequency.append(frequency)
            self.GenAvgACRMS.append(current)
            self.GenAvgL2LV.append(l2l)
            self.GenAvgL2NV.append(l2n)
            self.GenAvgTimestamp.append(timestamp)

    def add_GenAvg (self,current,frequency,l2l,l2n,timestamp):

        if len(self.GenAvgTimestamp) > 0 and timestamp == self.GenAvgTimestamp[-1]:
            pass
        else:
            self.GenAvgACFrequency.append(frequency)
            self.GenAvgACRMS.append(current)
            self.GenAvgL2LV.append(l2l)
            self.GenAvgL2NV.append(l2n)
            self.GenAvgTimestamp.append(timestamp)

    def add_PhaseA (self,current,frequency,l2l,l2n,timestamp):

        if len(self.GenPhaseATimestamp) > 0 and timestamp == self.GenPhaseATimestamp[-1]:
            pass
        else:
            self.GenPhaseAFrequency.append(frequency)
            self.GenPhaseACurrent.append(current)
            self.GenPhaseAL2LV.append(l2l)
            self.GenPhaseAL2NV.append(l2n)
            self.GenPhaseATimestamp.append(timestamp)

    def add_PhaseB (self,current,frequency,l2l,l2n,timestamp):

        if len(self.GenPhaseBTimestamp) > 0 and timestamp == self.GenPhaseBTimestamp[-1]:
            pass
        else:
            self.GenPhaseBFrequency.append(frequency)
            self.GenPhaseBCurrent.append(current)
            self.GenPhaseBL2LV.append(l2l)
            self.GenPhaseBL2NV.append(l2n)
            self.GenPhaseBTimestamp.append(timestamp)

    def add_PhaseC (self,current,frequency,l2l,l2n,timestamp):

        if len(self.GenPhaseCTimestamp) > 0 and timestamp == self.GenPhaseCTimestamp[-1]:
            pass
        else:
            self.GenPhaseCFrequency.append(frequency)
            self.GenPhaseCCurrent.append(current)
            self.GenPhaseCL2LV.append(l2l)
            self.GenPhaseCL2NV.append(l2n)
            self.GenPhaseCTimestamp.append(timestamp)

    def plot_graph(self):

        arrangedspeed_value = []
        arrangedfulerate_value = []
        arrangedengmanifoldpressure_value = []
        arrangedengoilpressure_value = []
        arrangedboostpressure_value = []
        arrangedengcoolanttemp_value = []
        arrangedGenAvgL2LV = []
        arrangedGenAvgL2NV = []
        arrangedGenAvgACFrequency = []
        arrangedGenAvgACRMS = []
        arrangedGenPhaseAFrequency = []
        arrangedGenPhaseAL2LV = []
        arrangedGenPhaseAL2NV = []
        arrangedGenPhaseACurrent = []
        arrangedGenPhaseBFrequency = []
        arrangedGenPhaseBL2LV = []
        arrangedGenPhaseBL2NV = []
        arrangedGenPhaseBCurrent = []
        arrangedGenPhaseCFrequency = []
        arrangedGenPhaseCL2LV = []
        arrangedGenPhaseCL2NV = []
        arrangedGenPhaseCCurrent = []





        print ("reached plot graph")
        currentWorkingDir = os.getcwd()

        timestamp = set(self.speed_timestamp+self.engcoolanttemp_timestamp+self.engoilpressure_timestamp+self.engmanifoldpressure_timestamp+self.fulerate_timestamp+self.GenAvgTimestamp+self.GenPhaseATimestamp+self.GenPhaseBTimestamp+self.GenPhaseCTimestamp)

        sortedtimestamp = sorted(timestamp)

        cursor=0

        for i in sortedtimestamp:
            if i in self.speed_timestamp:
                cursor=self.speed_timestamp.index(i)
                arrangedspeed_value.append(self.speed_value[cursor])
            else :
                arrangedspeed_value.append(None)

            if i in self.boostpressure_timestamp:
                cursor=self.boostpressure_timestamp.index(i)
                arrangedboostpressure_value.append(self.boostpressure_value[cursor])
            else :
                arrangedspeed_value.append(None)

            if i in self.engcoolanttemp_timestamp:
                cursor=self.engcoolanttemp_timestamp.index(i)
                arrangedengcoolanttemp_value.append(self.engcoolanttemp_value[cursor])
            else :
                arrangedengcoolanttemp_value.append(None)

            if i in self.engoilpressure_timestamp:
                cursor=self.engoilpressure_timestamp.index(i)
                arrangedengoilpressure_value.append(self.engoilpressure_value[cursor])
            else :
                arrangedengoilpressure_value.append(None)

            if i in self.engmanifoldpressure_timestamp:
                cursor=self.engmanifoldpressure_timestamp.index(i)
                arrangedengmanifoldpressure_value.append(self.engmanifoldpressure_value[cursor])
            else :
                arrangedengmanifoldpressure_value.append(None)

            if i in self.fulerate_timestamp:
                cursor=self.fulerate_timestamp.index(i)
                arrangedfulerate_value.append(self.fulerate_value[cursor])
            else :
                arrangedfulerate_value.append(None)

            if i in self.GenAvgTimestamp:
                cursor=self.GenAvgTimestamp.index(i)
                arrangedGenAvgACFrequency.append(self.GenAvgACFrequency[cursor])
                arrangedGenAvgACRMS.append(self.GenAvgACRMS[cursor])
                arrangedGenAvgL2NV.append(self.GenAvgL2NV[cursor])
                arrangedGenAvgL2LV.append(self.GenAvgL2LV[cursor])
            else:
                arrangedGenAvgACFrequency.append(None)
                arrangedGenAvgACRMS.append(None)
                arrangedGenAvgL2NV.append(None)
                arrangedGenAvgL2LV.append(None)

            if i in self.GenPhaseATimestamp:
                cursor=self.GenPhaseATimestamp.index(i)
                arrangedGenPhaseAFrequency.append(self.GenPhaseAFrequency[cursor])
                arrangedGenPhaseACurrent.append(self.GenPhaseACurrent[cursor])
                arrangedGenPhaseAL2LV.append(self.GenPhaseAL2LV[cursor])
                arrangedGenPhaseAL2NV.append(self.GenPhaseAL2NV[cursor])
            else:
                arrangedGenPhaseAFrequency.append(None)
                arrangedGenPhaseACurrent.append(None)
                arrangedGenPhaseAL2LV.append(None)
                arrangedGenPhaseAL2NV.append(None)

            if i in self.GenPhaseBTimestamp:
                cursor=self.GenPhaseBTimestamp.index(i)
                arrangedGenPhaseBFrequency.append(self.GenPhaseBFrequency[cursor])
                arrangedGenPhaseBCurrent.append(self.GenPhaseBCurrent[cursor])
                arrangedGenPhaseBL2LV.append(self.GenPhaseBL2LV[cursor])
                arrangedGenPhaseBL2NV.append(self.GenPhaseBL2NV[cursor])
            else:
                arrangedGenPhaseBFrequency.append(None)
                arrangedGenPhaseBCurrent.append(None)
                arrangedGenPhaseBL2LV.append(None)
                arrangedGenPhaseBL2NV.append(None)

            if i in self.GenPhaseCTimestamp:
                cursor=self.GenPhaseCTimestamp.index(i)
                arrangedGenPhaseCFrequency.append(self.GenPhaseCFrequency[cursor])
                arrangedGenPhaseCCurrent.append(self.GenPhaseCCurrent[cursor])
                arrangedGenPhaseCL2LV.append(self.GenPhaseCL2LV[cursor])
                arrangedGenPhaseCL2NV.append(self.GenPhaseCL2NV[cursor])
            else:
                arrangedGenPhaseCFrequency.append(None)
                arrangedGenPhaseCCurrent.append(None)
                arrangedGenPhaseCL2LV.append(None)
                arrangedGenPhaseCL2NV.append(None)





        print("data vs time")
        print (arrangedspeed_value)
        print (arrangedengcoolanttemp_value)
        print (arrangedengoilpressure_value)
        print (arrangedengmanifoldpressure_value)
        print (arrangedboostpressure_value)
        print (arrangedfulerate_value)
        print (len(sortedtimestamp))
        line_chart = pygal.Line()
        line_chart.title = "Generator - Data vs Time"
        line_chart.x_labels = sortedtimestamp
        line_chart.add('Speed',arrangedspeed_value)
        line_chart.add('Eng coolant temp',arrangedengcoolanttemp_value)
        line_chart.add('Eng Oil Pressure',arrangedengoilpressure_value)
        line_chart.add('Manifold Pressure',arrangedengmanifoldpressure_value)
        line_chart.add('Boost Pressure',arrangedboostpressure_value)
        line_chart.add('Fuel Rate',arrangedfulerate_value)

        line_chart.render_to_file(currentWorkingDir+'/ChartFiles/'+self.instance_filename+'Combined.svg')

        line_chart2 = pygal.Line()
        line_chart2.title = "Generator - Power Data vs Time"
        line_chart2.x_labels = sortedtimestamp
        line_chart2.add('Average Frequency', arrangedGenAvgACFrequency)
        line_chart2.add('Average Current', arrangedGenAvgACRMS)
        line_chart2.add('Average Line to Line', arrangedGenAvgL2LV)
        line_chart2.add('Average Line to Neutral', arrangedGenAvgL2NV)
        line_chart2.add('Phase A Frequency', arrangedGenPhaseAFrequency)
        line_chart2.add('Phase A Current', arrangedGenPhaseACurrent)
        line_chart2.add('Phase A Line to Line', arrangedGenPhaseAL2LV)
        line_chart2.add('Phase A Line to Neutral', arrangedGenPhaseAL2NV)
        line_chart2.add('Phase B Frequency', arrangedGenPhaseBFrequency)
        line_chart2.add('Phase B Current', arrangedGenPhaseBCurrent)
        line_chart2.add('Phase B Line to Line', arrangedGenPhaseBL2LV)
        line_chart2.add('Phase B Line to Neutral', arrangedGenPhaseBL2NV)
        line_chart2.add('Phase C Frequency', arrangedGenPhaseCFrequency)
        line_chart2.add('Phase C Current', arrangedGenPhaseCCurrent)
        line_chart2.add('Phase C Line to Line', arrangedGenPhaseCL2LV)
        line_chart2.add('Phase C Line to Neutral', arrangedGenPhaseCL2NV)

        line_chart2.render_to_file(currentWorkingDir + '/ChartFiles/' + self.instance_filename + 'Power.svg')



        with open(ParsedFilesDir + "\\" + filename[0] + "Analysed.txt", "a") as text_file:

            self.set_pgnlist = set(self.pgn_list)
            print("PGN List : {}".format(self.set_pgnlist),file=text_file)
            for i in self.set_pgnlist:
                print ("{} occurs {} times".format(i,self.pgn_list.count(i)),file=text_file)

            print("PGN and associated byte changes {}".format(set(self.pgn_byte_list)),file=text_file)

            print(" SPN List : {}".format(set(self.spn_list)),file=text_file)
            print("{},{}".format(filename[0] ,set(self.spn_list)))

            for i in self.pgn_byte_list:
                totalpgnbytelist.append(i)

    def readfilename(self):
        return self.instance_filename


    def setpgnspn(self,pgn,spn):

        self.pgn_list.append(pgn)

        self.spn_list.append(spn)

    def pgndataidentifier (self,PGN,b1,b2,b3,b4,b5,b6,b7,b8):

        hb1 = '0'
        hb2 = '0'
        hb3 = '0'
        hb4 = '0'
        hb5 = '0'
        hb6 = '0'
        hb7 = '0'
        hb8 = '0'
        pgn = str(PGN)

        if b1 != 'FF':
            hb1 = '1'

        if b2 != 'FF':
            hb2 = '1'

        if b3 != 'FF':
            hb3 = '1'

        if b4 != 'FF':
            hb4 = '1'

        if b5 != 'FF':
            hb5 = '1'

        if b6 != 'FF':
            hb6 = '1'

        if b7 != 'FF':
            hb7 = '1'

        if b8 != 'FF':
            hb8 = '1'

        self.pgn_byte_list.append("PGN-{},{}{}{}{}{}{}{}{}".format(pgn,hb1,hb2,hb3,hb4,hb5,hb6,hb7,hb8))


#creating a library to store all PGN numbers
J1939 = dict()
J1939.keys()
J1939 = {64914: "Engine Operating Information",
         65262: "Engine Temperature 1",
         65226: "Fault Code",
         65271: "Vehicle Electrical Power 1",
         65276: "Engine Fuel Level",
         61444: "Electronic Engine Controller 1",
         61443: "Electronic Engine Controller 2",
         65253: "Engine Hours, Revolutions",
         65190: "Boost Pressure",
         65030: "Average Phase Information",
         65027: "Phase A Information",
         65024: "Phase B Information",
         65021: "Phase C Information",
         65252: "Shutdown",
         65263: "Engine Fluid Level/Pressure",
         65282: "Coolant Info",
         64915: "Generator Control",
         59904: "Request Group",
         65223: "Electronic Transmission",
         65270: "Inlet / Exhaust Conditions",
         64934: "Voltage Regulator Excitation Status",
         65266: "Fuel Economy",
         65247: "Electronic Engine Controller 3",
         65170: "Engine Information",
         64976: "Inlet / Exhaust Conditions 2",
         59904: "Request"
         }


def parseJ1939(rawdata,filename,newfile_flag,temp):



    # function to parse the raw data
    # function expects data to be <PGN(0-8),(9)b1(10-11)b2(12-13)b3(14-15)b4(16-17)b5(18-19)b6(20-21)b7(22-23)b8(24-25)> format
    data = ''.join(rawdata.split())
    # first 8 characters are the header containing PGN
    # 9th character is the comma
    # 10th character onwards containg the SPN data
    rawcontent=data.split(',')
    #print(rawcontent)
    Line = rawcontent [0]
    Timestamp = rawcontent[1]
    Header = rawcontent[2]
    Values = rawcontent[3]
    #print("Header(PGN) : {}".format(Header))
    #print("Values(SPN) : {}".format(Values))
    #print("Line Number : {}".format(Line))
    #print("Time : {}".format(Timestamp))

    # separate the bytes
    b1 = Values[0:2]
    b2 = Values[2:4]
    b3 = Values[4:6]
    b4 = Values[6:8]
    b5 = Values[8:10]
    b6 = Values[10:12]
    b7 = Values[12:14]
    b8 = Values[14:16]

    # source address value
    SA = Header[6:]
    # PGN (Parameter Group Number) value
    PGN = Header[3:7]

    temp.pgndataidentifier(int(PGN,16),b1,b2,b3,b4,b5,b6,b7,b8)


    # The value of certain fields are encoded in bytes , each data passed along a Can bus message has 8 bytes and depending on the SPN the values are in these 8 bytes
    # Data bytesthat are not available and are set to 0xFF. No raw parameter value (single byte) could have the value 0xFF.
    # When Data bytes have 2 bytes for value, The first byte is the least significant (Intel byte order). E.G.
    # Data bytes 4(DF) and 5(A1) form the parameter Engine speed. The first byte (4) with value DF is the least significant (Intel byte order). Therefore the raw value 0x1ADF = 6879 decimal.


    with open(ParsedFilesDir+"\\"+filename+"CANparsed.txt", "a") as text_file:


        # check to verify the data is passed along correct
        if PGN.isalnum():
            # checks if the PGN parsed as int is available in the library
            if int(PGN,16) in J1939.keys():
                print("PGN {} Found, values are {} ".format(int(PGN, 16), Values),file=text_file)
                if int(PGN,16) == 65226:
                    if (b1 != 'FF'):
                        t_Hexbyte = int(b1, 16)
                        DTCLamp = ( bin(t_Hexbyte)[2:]).zfill(8)
                        print("SPN-987,Protect Lamp :{}".format(checkstate(DTCLamp[0:2])),file=text_file)
                        print("SPN-987,Amber Warning Lamp :{}".format(checkstate(DTCLamp[2:4])), file=text_file)
                        print("SPN-987,Red Stop Lamp :{}".format(checkstate(DTCLamp[4:6])), file=text_file)
                        print("SPN-987,Malfunction Indicator Lamp :{}".format(checkstate(DTCLamp[6:8])), file=text_file)
                        temp.setpgnspn(65226,987)
                    if (b2 != 'FF'):
                        t_Hexbyte = int(b2, 16)
                        DTCFlashLamp = ( bin(t_Hexbyte)[2:]).zfill(8)
                        print("SPN-987,Protect Flash Lamp :{}".format(checkstate(DTCFlashLamp[0:2])),file=text_file)
                        print("SPN-987,Amber Warning Flash Lamp :{}".format(checkstate(DTCFlashLamp[2:4])), file=text_file)
                        print("SPN-987,Red Stop Flash Lamp :{}".format(checkstate(DTCFlashLamp[4:6])), file=text_file)
                        print("SPN-987,Malfunction Indicator Flash Lamp :{}".format((DTCFlashLamp[6:8])), file=text_file)
                    if (b5 != 'FF'):
                        t_Hexbyte = int(b5, 16)
                        FMI = (bin(t_Hexbyte)[2:]).zfill(8)
                        print("SPN-1215,Fault Mode Identifier :{}".format(FMI[0:5].zfill(8)), file=text_file)
                        temp.setpgnspn(65226, 1215)
                    if (b4 != 'FF'):
                        t_Hexbyte = int(b4+b3, 16)
                        dtcspn = (bin(t_Hexbyte)[2:]).zfill(8)
                        t2_Hexbyte = int (b5,16)
                        dtcspn = dtcspn + (bin(t2_Hexbyte)[8:10])
                        print("SPN-1214,Fault Mode Identifier SPN:{}".format(int(dtcspn,2)), file=text_file)
                        temp.setpgnspn(65226, 1214)


                    print("Fault Code : {}".format(Values),file=text_file)
                elif int(PGN,16) == 65271:
                    if (b6 != 'FF'):
                        BatteryVoltage = int(b6+b5,16)* 0.05
                        print("SPN-168,Battery Potential/Input :{}".format(BatteryVoltage),file=text_file)
                        temp.setpgnspn(65271, 168)
                    if (b8 != 'FF'):
                        KSBatteryVoltage = int(b8 + b7, 16) * 0.05
                        print("SPN-158,Key Switch Battery Potential :{}".format(KSBatteryVoltage), file=text_file)
                        temp.setpgnspn(65271, 158)
                elif int(PGN,16) == 64914:
                    if (b1 != 'FF'):
                        t_Hexbyte = int(b1, 16)
                        EOpState = (bin(t_Hexbyte)[2:]).zfill(8)
                        print("SPN-3567,Engine Operating State :{}".format(checkenginestate(EOpState[4:8])),file=text_file)
                        temp.setpgnspn(64914, 3567)
                elif int(PGN,16) == 61444:
                    if (b5 != 'FF'):
                        EngineSpeed= int(b5+b4,16)* 0.125
                        print("SPN-190,Engine Speed :{}".format(EngineSpeed),file=text_file)
                        temp.add_speed(EngineSpeed,Timestamp)
                        temp.setpgnspn(61444, 190)
                    if (b3 != 'FF'):
                        ActualEnginePT = int(b3,16) - 125
                        print("SPN-513,Actual Engine Percentage Torque :{}".format(ActualEnginePT),file=text_file)
                        temp.setpgnspn(61444, 513)
                    if (b2 != 'FF'):
                        DriveDemandPT = int(b2,16)
                        print("SPN-512,Driver Demand Percentage Torque :{}".format(DriveDemandPT),file=text_file)
                        temp.setpgnspn(61444, 512)
                    if (b8 != 'FF') :
                        EngineDemandPT = int(b8,16)
                        print("SPN-2432,Engine Demand Percentage Torque :{}".format(EngineDemandPT),file=text_file)
                        temp.setpgnspn(61444, 2432)
                elif int(PGN,16) == 61443:
                    if (b7 != 'FF'):
                        ActualMaxAvaialablePerTorque= int(b7,16)* 0.125
                        print("SPN-3357,Actual Maximum Available Engine - Percent Torque :{}".format(ActualMaxAvaialablePerTorque),file=text_file)
                        temp.setpgnspn(61443, 3357)
                    if (b3 != 'FF'):
                        EnginePercentLoadCurrentSpeed = int(b3,16) - 125
                        print("SPN-92,Engine % Load at current Speed :{}".format(EnginePercentLoadCurrentSpeed),file=text_file)
                        temp.setpgnspn(61443, 92)
                    if (b2 != 'FF'):
                        AccelPedalpostion1 = int(b2, 16)
                        print("SPN-91,Accelerator Pedal Position 1 :{}".format(AccelPedalpostion1),file=text_file)
                        temp.setpgnspn(61443, 91)
                    if (b5 != 'FF') :
                        AccelPedalpostion2 = int(b5,16)
                        print("SPN-29,Accelerator Pedal Position 2 :{}".format(AccelPedalpostion2),file=text_file)
                        temp.setpgnspn(61443, 29)
                elif int(PGN,16) == 65262:
                    if (b1 != 'FF'):
                        EngCoolantTemp = int(b1, 16) - 40
                        if EngCoolantTemp == 214 :
                            EngCoolantTemp = 0
                        print("SPN-110,Engine Coolant Temperature :{}".format(EngCoolantTemp),file=text_file)
                        temp.add_engcoolanttemp(EngCoolantTemp, Timestamp)
                        temp.setpgnspn(61443, 110)
                    if (b2 != 'FF'):
                        EngFuelTemp = int(b1, 16) - 40
                        print("SPN-174,Engine Fuel Temperature :{}".format(EngFuelTemp),file=text_file)
                        temp.setpgnspn(61443, 174)
                    if (b4 != 'FF'):
                        EngOilTemp = (int((b4+b3), 16) *  0.03125)-273
                        print("SPN-176,Engine Oil Temperature :{}".format(EngOilTemp),file=text_file)
                        temp.setpgnspn(61443, 175)
                elif int(PGN, 16) == 65030:
                    if (b6 != 'FF'):
                        GenAvgACFrequency = int(b6 + b5, 16) * 0.0078125
                        print("SPN-2436,Generator Average AC Frequency :{}".format(GenAvgACFrequency),file=text_file)
                        temp.setpgnspn(65030, 2436)
                    else:
                        GenAvgACFrequency=None
                    if (b2 != 'FF'):
                        GenAvgL2LV = int(b2+b1,16)
                        print("SPN-2440,Generator Average Line - Line AC RMS Voltage :{}".format(GenAvgL2LV),file=text_file)
                        temp.setpgnspn(65030, 2440)
                    if (b2 != 'FF'):
                        GenAvgL2NV = int(b4+b3,16)
                        print("SPN-2440,Generator Average Line - Neutral AC RMS Voltage :{}".format(GenAvgL2NV),file=text_file)
                        temp.setpgnspn(65030, 2440)
                    if (b8 != 'FF'):
                        GenAvgACRMS = int(b8 + b7, 16)
                        print("SPN-2448,Generator Average AC RMS Current :{}".format(GenAvgACRMS),file=text_file)
                        temp.setpgnspn(65030, 2448)

                        temp.add_GenAvg(GenAvgACRMS,GenAvgACFrequency,GenAvgL2LV,GenAvgL2NV,Timestamp)

                elif int(PGN,16) == 65027:
                    if (b6 != 'FF'):
                        GenPhaseAFrequency = int(b6 + b5, 16) * 0.0078125
                        print("SPN-2437,Generator Phase AC Frequency :{}".format(GenPhaseAFrequency),file=text_file)
                    else:
                        GenPhaseAFrequency=None
                        temp.setpgnspn(65027, 2437)
                    if (b2 != 'FF'):
                        GenPhaseAL2LV = int(b2+b1,16)
                        print("SPN-2441,Generator Phase A Line - Line AC RMS Voltage :{}".format(GenPhaseAL2LV),file=text_file)
                        temp.setpgnspn(65027, 2441)
                    if (b2 != 'FF'):
                        GenPhaseAL2NV = int(b4+b3,16)
                        print("SPN-2445,Generator Phase A Line - Neutral AC RMS Voltage :{}".format(GenPhaseAL2NV),file=text_file)
                        temp.setpgnspn(65027, 2445)
                    if (b8 != 'FF'):
                        GenPhaseACurrent = int(b8+b7,16)
                        print("SPN-2449,Generator Phase A AC RMS Current :{}".format(GenPhaseACurrent),file=text_file)
                        temp.setpgnspn(65027, 2449)
                        temp.add_PhaseA(GenPhaseACurrent,GenPhaseAFrequency,GenPhaseAL2LV,GenPhaseAL2NV,Timestamp)

                elif int(PGN,16) == 65024:
                    if (b6 != 'FF'):
                        GenPhaseBFrequency = int(b6 + b5, 16) * 0.0078125
                        print("SPN-2437 Generator Phase B Frequency :{}".format(GenPhaseBFrequency))
                    else:
                        GenPhaseBFrequency=None
                    if (b2 != 'FF'):
                        GenPhaseBL2LV = int(b2+b1,16)
                        print("SPN-2442,Generator Phase B Line - Line AC RMS Voltage :{}".format(GenPhaseBL2LV),file=text_file)
                        temp.setpgnspn(65024, 2442)
                    if (b2 != 'FF'):
                        GenPhaseBL2NV = int(b4+b3,16)
                        print("SPN-2446,Generator Phase B Line - Neutral AC RMS Voltage :{}".format(GenPhaseBL2NV),file=text_file)
                        temp.setpgnspn(65024, 2446)
                    if (b8 != 'FF'):
                        GenPhaseBCurrent = int(b8+b7,16)
                        print("SPN-2450,Generator Phase B AC RMS Current :{}".format(GenPhaseBCurrent),file=text_file)
                        temp.setpgnspn(65024, 2450)

                        temp.add_PhaseB(GenPhaseBCurrent, GenPhaseBFrequency, GenPhaseBL2LV, GenPhaseBL2NV, Timestamp)


                elif int(PGN,16) == 65021:
                     if (b6 != 'FF'):
                        GenPhaseCFrequency = int(b6 + b5, 16) * 0.0078125
                        print("SPN-2437 Generator Phase B Frequency :{}".format(GenPhaseCFrequency))
                     else:
                         GenPhaseCFrequency = None
                     if (b2 != 'FF'):
                        GenPhaseCL2LV = int(b2 + b1, 16)
                        print("SPN-2443,Generator Phase C Line - Line AC RMS Voltage :{}".format(GenPhaseCL2LV),file=text_file)
                        temp.setpgnspn(65021, 2443)
                     if (b2 != 'FF'):
                        GenPhaseCL2NV = int(b4 + b3, 16)
                        print("SPN-2447,Generator Phase C Line - Neutral AC RMS Voltage :{}".format(GenPhaseCL2NV),file=text_file)
                        temp.setpgnspn(65021, 2447)
                     if (b8 != 'FF'):
                        GenPhaseCCurrent = int(b8 + b7, 16)
                        print("SPN-2451,Generator Phase C AC RMS Current :{}".format(GenPhaseCCurrent),file=text_file)
                        temp.setpgnspn(65021, 2451)

                        temp.add_PhaseC(GenPhaseCCurrent, GenPhaseCFrequency, GenPhaseCL2LV, GenPhaseCL2NV, Timestamp)


                elif int(PGN,16) == 65263:
                     if (b4 != 'FF'):
                        EngineOilPressure = int(b4,16)* 4
                        if EngineOilPressure == 1016:
                            EngineOilPressure = 0
                        print("SPN-100,Engine Oil Pressure :{}".format(EngineOilPressure),file=text_file)
                        temp.add_engoilpressure(EngineOilPressure,Timestamp)
                        temp.setpgnspn(65263, 100)
                #check spn as this is proprietary
                elif int(PGN, 16) == 65282:
                     if (b5 != 'FF'):
                        EngineCoolantTemp = int(b5, 16)
                        print("SPN-110,EIC Coolant Temperature :{}".format(EngineCoolantTemp),file=text_file)
                        temp.setpgnspn(65282, 110)
                     if (b5 != 'FF'):
                        EngineCoolantTemp = int(b7, 16) * 8
                        print("SPN-110,EIC Engine Oil Pressure :{}".format(EngineCoolantTemp),file=text_file)
                        temp.setpgnspn(65282, 110)
                elif int(PGN, 16) == 64915:
                    if (b1 != 'FF'):
                        t_Hexbyte = int(b1, 16)
                        GenControl = ( bin(t_Hexbyte)[2:] ).zfill(8)
                        print("SPN-3567,EIC Generator Set to auto control :{}".format(GenControl[5:6]),file=text_file)
                        temp.setpgnspn(64915, 3567)
                    if (b2 != 'FF'):
                        AltEffeciency = int(b3+b2, 16) *0.0025
                        print("SPN-4078,Alternator Effeciency :{}".format(AltEffeciency),file=text_file)
                        temp.setpgnspn(64915, 4078)
                elif int(PGN, 16) == 65270:
                    if (b1 != 'FF'):
                        EngPartInletPressure = int(b1, 16) *0.5
                        print("SPN-81,Engine Particulate Trap Inlet Pressure :{}".format(EngPartInletPressure),file=text_file)
                        temp.setpgnspn(65270, 81)
                    if (b2 != 'FF'):
                        EngineIntakeManifoldPressure = int(b2, 16) * 2
                        if EngineIntakeManifoldPressure > 500:
                            EngineIntakeManifoldPressure=0
                        print("SPN-102,Engine Intake Manifold #1 Pressure :{}".format(EngineIntakeManifoldPressure),file=text_file)
                        temp.add_engmanifoldpressure(EngineIntakeManifoldPressure,Timestamp)
                        temp.setpgnspn(65270, 102)
                    if (b3 != 'FF'):
                        EngineIntakeManifoldTemperature = int(b3, 16) - 40
                        if EngineIntakeManifoldTemperature > 210:
                            EngineIntakeManifoldTemperature=0
                        print("SPN-105,Engine Intake Manifold #1 Temperature :{}".format(EngineIntakeManifoldTemperature),file=text_file)
                        temp.add_engmanifoldtemperature(EngineIntakeManifoldTemperature,Timestamp)
                        temp.setpgnspn(65270, 105)
                    if (b4 != 'FF'):
                        EngineAirInletPressure = int(b4, 16) * 2
                        print("SPN-106,Engine Air Inlet Pressure :{}".format(EngineAirInletPressure),file=text_file)
                        temp.setpgnspn(65270, 106)
                    if (b5 != 'FF'):
                        EngineAirInletDifferenetialPressure = int(b5, 16) * 2
                        print("SPN-107,Engine Air Differential Pressure :{}".format(EngineAirInletDifferenetialPressure),file=text_file)
                        temp.setpgnspn(65270, 107)
                    if (b7 != 'FF'):
                        EngineExhaustGasTemp = (int(b7+b6, 16) * 0.03125) - 273
                        print("SPN-173,Engine Exhaust Gas Temperature :{}".format(EngineExhaustGasTemp),file=text_file)
                        temp.setpgnspn(65270, 173)
                    if (b8 != 'FF'):
                        EngineCoolantDifferenetialPressure = int(b8, 16) * 0.5
                        print("SPN-112,Engine Coolant Differential Pressure :{}".format(EngineCoolantDifferenetialPressure),file=text_file)
                        temp.setpgnspn(65270, 112)
                elif int(PGN, 16) == 64934:
                    if (b1 != 'FF'):
                        GenExcitationFV = (int(b2+b1, 16)*0.05) - 1606
                        print("SPN-3380,Generator Excitation Field Voltage :{}".format(GenExcitationFV),file=text_file)
                        temp.setpgnspn(64934, 3380)
                    if (b3 != 'FF'):
                        GenExcitationFC = int(b4+b3, 16) * 0.05
                        print("SPN-3381,Generator Excitation Field Current :{}".format(GenExcitationFC),file=text_file)
                        temp.setpgnspn(64934, 3381)
                    if (b5 != 'FF'):
                        GenOutputVbiasPercentage = (int(b6+b5, 16) * 0.1 )
                        print("SPN-3382,Generator Output Voltage Bias Percentage :{}".format(GenOutputVbiasPercentage),file=text_file)
                        temp.setpgnspn(64934, 3382)
                elif int(PGN, 16) == 65266:
                    if (b7 != 'FF'):
                        EngThrottlePosition = int(b7, 16)
                        print("SPN-52,Engine Throttle Position :{}".format(EngThrottlePosition),file=text_file)
                        temp.setpgnspn(65266, 52)
                    if (b1 != 'FF'):
                        t = int(b2+b1, 16)
                        EngFuelRate = (t * 0.05)
                        print("SPN-183,Engine Fuel Rate :{} L/hr".format(EngFuelRate),file=text_file)
                        temp.add_fulerate(EngFuelRate,Timestamp)
                        temp.setpgnspn(65266, 183)

                    if (b3 != 'FF'):
                        EngInstantFE = int(b4+b3, 16)
                        print("SPN-184,Engine Instantaneous Fuel Economy :{}".format(EngInstantFE),file=text_file)
                        temp.setpgnspn(65266, 184)
                    if (b5 != 'FF'):
                        EngAvgFE = int(b6+b5, 16)
                        print("SPN-185,Engine Avergae Fuel Economy :{}".format(EngAvgFE),file=text_file)
                        temp.setpgnspn(65266, 185)
                    if (b8 != 'FF'):
                        EngThrottlePosition2 = int(b8, 16)
                        print("SPN-52,Engine Throttle Position 2 :{}".format(EngThrottlePosition2),file=text_file)
                        temp.setpgnspn(65266, 52)
                elif int(PGN, 16) == 64976:
                    if (b1 != 'FF'):
                        EngineAirFilterDifferential2 = int(b1, 16)
                        print("SPN-2809,Engine Air Filter Differential 2 :{}".format(EngineAirFilterDifferential2),file=text_file)
                        temp.setpgnspn(64976, 2809)
                elif int(PGN, 16) == 65170:
                    if (b1 != 'FF'):
                        EnginePreFilterOilPressure = int(b1, 16)
                        print("SPN-1208,Engine Pre Filter Oil Pressure :{}".format(EnginePreFilterOilPressure),file=text_file)
                        temp.setpgnspn(65170, 1208)
                    if (b2 != 'FF'):
                        EngineExhaustGasPressure = int(b3+b2, 16)
                        print("SPN-1209,Engine Exhaust Gas Pressure :{}".format(EngineExhaustGasPressure),file=text_file)
                        temp.setpgnspn(65170, 1209)
                    if (b4 != 'FF'):
                        EngineFuelRackPosition = int(b4, 16)
                        print("SPN-1210,Engine Fuel Rack Position :{}".format(EngineFuelRackPosition),file=text_file)
                        temp.setpgnspn(65170, 1210)
                    if (b6 != 'FF'):
                        EngineGasMassFlowRate1 = int(b6+b5, 16)
                        print("SPN-1241,Engine Gas Mass Flow Rate 1 :{}".format(EngineGasMassFlowRate1),file=text_file)
                        temp.setpgnspn(65170, 1241)
                    if (b7 != 'FF'):
                        InstEstBrakePower = int(b8+b7, 16)
                        print("SPN-1242,Instantaneous Estimated Brake Power :{}".format(InstEstBrakePower),file=text_file)
                        temp.setpgnspn(65170, 1242)

                elif int(PGN, 16) == 65253:
                    if (b1 != 'FF'):
                        EngineHours = int(b4+b3+b2+b1, 16) * 0.05
                        print("SPN-247,Engine Hours :{}".format(EngineHours),file=text_file)
                        temp.setpgnspn(65253, 247)

                elif int(PGN, 16) == 65190:
                    if (b1 != 'FF'):
                        BoostPressure = int(b2+b1, 16) * 0.05
                        print("SPN- 1127 Boost Pressure:{}".format(BoostPressure),file=text_file)
                        temp.add_boostpressure(BoostPressure, Timestamp)
                        temp.setpgnspn(65190, 1127)

                else:
                    if (int(PGN,16)):
                        print("PGN in hex is {0} in decimal {1}, not found".format(PGN,int(PGN,16)),file=text_file)
            else :
             if (int(PGN, 16)):
                print ("PGN {} Not found, values are ".format(int(Header[2:6],16)),Values,file=text_file)
    return;


def checkstate(value):

    if value == '11':

        return (" Not available");

    elif value == '00':

        return (" Lamp Off");

    elif value == '01':

        return (" Lamp On");

    else :

        return (" Reserved");


def checkenginestate(value):

    if value == '0000':

        return ("Engine Stopped");

    elif value == '0001':

        return ("Pre Start");

    elif value == '0010':

        return ("Starting");

    elif value == '0011':

        return ("Warm-Up");

    elif value == '0100':

        return ("Running");

    elif value == '0101':

        return ("CoolDown");

    elif value == '0110':

        return ("Engine Stopping");

    elif value == '0111':

        return ("Post Run");

    elif value == '1110':

        return ("Reserved");

    else :

        return ("Not Avialable");



    print ("Initialized dictionary",file=text_file)
    print("There is a total of {} entries on the PGN dictionary".format(len(J1939)),file=text_file)


#C:\\Users\\thomas\\Documents\\Workspace Tom\\HEMS\\OLY-GEP-165K-2011.csv

currentWorkingDir = os.getcwd()

# location of the Canlog files
LogFilesDir = currentWorkingDir + "\\CanLogFiles"

# location to where the parsed files should be placed
ParsedFilesDir = currentWorkingDir + "\\Parsed"



# location to where the parsed files should be placed
ChartFilesDir = currentWorkingDir + "\\ChartFiles"

#create a parsed Dir to place the file in
if not os.path.exists(ParsedFilesDir):
    os.makedirs(ParsedFilesDir)

#create a chart Dir to place images of parsed data
if not os.path.exists(ChartFilesDir):
    os.makedirs(ChartFilesDir)


# iterate through all the files

for filename in os.listdir(LogFilesDir):
    try:

        file = open(LogFilesDir+"\\"+filename, 'r', errors='replace')
        #lno is used to keep the line numbers
        newfile_flag=1

        filename=filename.split('.')
        temp = parser_summary(filename[0])
        print('Parsing {}'.format(filename[0]))
        lno=0
        for line in file:
            if lno>0 :
                spaceremovedline =line.replace(" ","")
                splitline = spaceremovedline.split("\t")
                if (len(splitline)>2) and splitline[0].isdigit():
                    #print (splitline)
                    with open(ParsedFilesDir+"\\"+filename[0]+"Raw.txt", "a") as text_file:
                        data = splitline[0]+","+splitline[2]+","+splitline[7]+","+splitline[10]+splitline[11]+splitline[12]+splitline[13]+splitline[14]+splitline[15]+splitline[16]+splitline[17]
                        print(data, file=text_file)
                        #print(data)
                        #newfile = 1 Indicates a new canlog file has been opened for parsing.
                        parseJ1939(data,filename[0],newfile_flag,temp)
            lno = lno+1
            newfile_flag=0
        # temp.plot_graph()
    except  Exception:
       print (filename[0] +" could not be parsed")
print(set(totalpgnbytelist))