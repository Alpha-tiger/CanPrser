import os,subprocess
import pygal

class parser_summary:
    instance_filename = 'empty'

    #speed list to store speed and timestamp
    speed_timestamp = []
    speed_value = []


    pgn_list = set()

    spn_list = set()

    def __init__(self,filename):
        self.instance_filename = filename
        self.speed =[]
        self.pgn_list = set()
        self.spn_list = set()

    def add_speed (self,speed,timestamp):

        if(len(self.speed_timestamp)>0 and timestamp == self.speed_timestamp[-1]) :
            print('skipping timestamp same')
        else:
            self.speed_value.append(speed)
            self.speed_timestamp.append(timestamp)


    def plot_graph(self):
        print ("reached plot graph")
        print (self.speed_timestamp)
        print (self.speed_value)
        line_chart = pygal.Line()
        line_chart.title = "Generator - Speed vs Time"
        line_chart.x_labels = self.speed_timestamp
        line_chart.add('Speed',self.speed_value)
        line_chart.render_in_browser()

    def readfilename(self):
        return self.instance_filename


    def setpgnspn(self,pgn,spn):
        self.pgn_list = set(pgn)
        self.spn_list = set(spn)


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
         64976: "Inlet / Exhaust Conditions 2"
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
    print("Header(PGN) : {}".format(Header))
    print("Values(SPN) : {}".format(Values))
    print("Line Number : {}".format(Line))
    print("Time : {}".format(Timestamp))

    # separate the bytes
    b1 = Values[0:2]
    b2 = Values[2:4]
    b3 = Values[4:6]
    b4 = Values[6:8]
    b5 = Values[8:10]
    b6 = Values[10:12]
    b7 = Values[12:14]
    b8 = Values[14:16]

    # The value of certain fields are encoded in bytes , each data passed along a Can bus message has 8 bytes and depending on the SPN the values are in these 8 bytes
    # Data bytesthat are not available and are set to 0xFF. No raw parameter value (single byte) could have the value 0xFF.
    # When Data bytes have 2 bytes for value, The first byte is the least significant (Intel byte order). E.G.
    # Data bytes 4(DF) and 5(A1) form the parameter Engine speed. The first byte (4) with value DF is the least significant (Intel byte order). Therefore the raw value 0x1ADF = 6879 decimal.


    with open(ParsedFilesDir+"\\"+filename+"CANparsed.txt", "a") as text_file:

        # source address value
        SA = Header[6:]
        # PGN (Parameter Group Number) value
        PGN = Header[2:6]
        #print (PGN)
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
                    if (b4 != 'FF'):
                        t_Hexbyte = int(b4+b3, 16)
                        dtcspn = (bin(t_Hexbyte)[2:]).zfill(8)
                        t2_Hexbyte = int (b5,16)
                        dtcspn = dtcspn + (bin(t2_Hexbyte)[8:10])
                        print("SPN-1214,Fault Mode Identifier SPN:{}".format(int(dtcspn,2)), file=text_file)

                    print("Fault Code : {}".format(Values),file=text_file)
                elif int(PGN,16) == 65271:
                    if (b6 != 'FF'):
                        BatteryVoltage = int(b6+b5,16)* 0.05
                        print("SPN-168,Battery Potential/Input :{}".format(BatteryVoltage),file=text_file)
                    if (b8 != 'FF'):
                        KSBatteryVoltage = int(b8 + b7, 16) * 0.05
                        print("SPN-158,Key Switch Battery Potential :{}".format(KSBatteryVoltage), file=text_file)
                elif int(PGN,16) == 64914:
                    if (b1 != 'FF'):
                        t_Hexbyte = int(b1, 16)
                        EOpState = (bin(t_Hexbyte)[2:]).zfill(8)
                        print("SPN-3567,Engine Operating State :{}".format(checkenginestate(EOpState[4:8])),file=text_file)
                elif int(PGN,16) == 61444:
                    if (b5 != 'FF'):
                        EngineSpeed= int(b5+b4,16)* 0.125
                        print("SPN-190,Engine Speed :{}".format(EngineSpeed),file=text_file)
                        temp.add_speed(EngineSpeed,Timestamp)
                    if (b3 != 'FF'):
                        ActualEnginePT = int(b3,16) - 125
                        print("SPN-513,Actual Engine Percentage Torque :{}".format(ActualEnginePT),file=text_file)
                    if (b2 != 'FF'):
                        DriveDemandPT = int(b2,16)
                        print("SPN-512,Driver Demand Percentage Torque :{}".format(DriveDemandPT),file=text_file)
                    if (b8 != 'FF') :
                        EngineDemandPT = int(b8,16)
                        print("SPN-2432,Engine Demand Percentage Torque :{}".format(EngineDemandPT),file=text_file)
                elif int(PGN,16) == 61443:
                    if (b7 != 'FF'):
                        ActualMaxAvaialablePerTorque= int(b7,16)* 0.125
                        print("SPN-3357,Actual Maximum Available Engine - Percent Torque :{}".format(ActualMaxAvaialablePerTorque),file=text_file)
                    if (b3 != 'FF'):
                        EnginePercentLoadCurrentSpeed = int(b3,16) - 125
                        print("SPN-92,Engine % Load at current Speed :{}".format(EnginePercentLoadCurrentSpeed),file=text_file)
                    if (b2 != 'FF'):
                        AccelPedalpostion1 = int(b2, 16)
                        print("SPN-91,Accelerator Pedal Position 1 :{}".format(AccelPedalpostion1),file=text_file)
                    if (b5 != 'FF') :
                        AccelPedalpostion2 = int(b5,16)
                        print("SPN-29,Accelerator Pedal Position 2 :{}".format(AccelPedalpostion2),file=text_file)
                elif int(PGN,16) == 65262:
                    if (b1 != 'FF'):
                        EngCoolantTemp = int(b1, 16) - 40
                        print("SPN-110,Engine Coolant Temperature :{}".format(EngCoolantTemp),file=text_file)
                    if (b2 != 'FF'):
                        EngFuelTemp = int(b1, 16) - 40
                        print("SPN-174,Engine Fuel Temperature :{}".format(EngFuelTemp),file=text_file)
                    if (b4 != 'FF'):
                        EngOilTemp = (int((b4+b3), 16) *  0.03125)-273
                        print("SPN-175,Engine Oil Temperature :{}".format(EngOilTemp),file=text_file)
                elif int(PGN, 16) == 65030:
                    if (b6 != 'FF'):
                        GenAvgACFrequency = int(b6 + b5, 16) * 0.0078125
                        print("SPN-2436,Generator Average AC Frequency :{}".format(GenAvgACFrequency),file=text_file)
                    if (b2 != 'FF'):
                        GenAvgL2LV = int(b2+b1,16)
                        print("SPN-2440,Generator Average Line - Line AC RMS Voltage :{}".format(GenAvgL2LV),file=text_file)
                    if (b2 != 'FF'):
                        GenAvgL2NV = int(b4+b3,16)
                        print("SPN-2440,Generator Average Line - Neutral AC RMS Voltage :{}".format(GenAvgL2NV),file=text_file)
                elif int(PGN,16) == 65027:
                    if (b6 != 'FF'):
                        GenPhaseAFrequency = int(b6 + b5, 16) * 0.0078125
                        print("SPN-2437,Generator Phase AC Frequency :{}".format(GenPhaseAFrequency),file=text_file)
                    if (b2 != 'FF'):
                        GenPhaseAL2LV = int(b2+b1,16)
                        print("SPN-2441,Generator Phase A Line - Line AC RMS Voltage :{}".format(GenPhaseAL2LV),file=text_file)
                    if (b2 != 'FF'):
                        GenPhaseAL2NV = int(b4+b3,16)
                        print("SPN-2445,Generator Phase A Line - Neutral AC RMS Voltage :{}".format(GenPhaseAL2NV),file=text_file)
                    if (b8 != 'FF'):
                        GenPhaseACurrent = int(b8+b7,16)
                        print("SPN-2449,Generator Phase A AC RMS Current :{}".format(GenPhaseACurrent),file=text_file)
                elif int(PGN,16) == 65024:
                    #if (b6 != 'FF'):
                    #    GenPhaseBFrequency = int(b6 + b5, 16) * 0.0078125
                    #    print("SPN-2437 Generator Phase B Frequency :{}".format(GenPhaseBFrequency))
                    if (b2 != 'FF'):
                        GenPhaseBL2LV = int(b2+b1,16)
                        print("SPN-2442,Generator Phase B Line - Line AC RMS Voltage :{}".format(GenPhaseBL2LV),file=text_file)
                    if (b2 != 'FF'):
                        GenPhaseBL2NV = int(b4+b3,16)
                        print("SPN-2446,Generator Phase B Line - Neutral AC RMS Voltage :{}".format(GenPhaseBL2NV),file=text_file)
                    if (b8 != 'FF'):
                        GenPhaseBCurrent = int(b8+b7,16)
                        print("SPN-2450,Generator Phase B AC RMS Current :{}".format(GenPhaseBCurrent),file=text_file)
                elif int(PGN,16) == 65021:
                    # if (b6 != 'FF'):
                    #    GenPhaseBFrequency = int(b6 + b5, 16) * 0.0078125
                    #    print("SPN-2437 Generator Phase B Frequency :{}".format(GenPhaseBFrequency))
                    if (b2 != 'FF'):
                        GenPhaseCL2LV = int(b2 + b1, 16)
                        print("SPN-2443,Generator Phase C Line - Line AC RMS Voltage :{}".format(GenPhaseCL2LV),file=text_file)
                    if (b2 != 'FF'):
                        GenPhaseCL2NV = int(b4 + b3, 16)
                        print("SPN-2447,Generator Phase C Line - Neutral AC RMS Voltage :{}".format(GenPhaseCL2NV),file=text_file)
                    if (b8 != 'FF'):
                        GenPhaseCCurrent = int(b8 + b7, 16)
                        print("SPN-2451,Generator Phase C AC RMS Current :{}".format(GenPhaseCCurrent),file=text_file)
                elif int(PGN,16) == 65263:
                    if (b4 != 'FF'):
                        EngineOilPressure = int(b4,16)* 4
                        print("SPN-100,Engine Oil Pressure :{}".format(EngineOilPressure),file=text_file)
                elif int(PGN, 16) == 65282:
                    if (b5 != 'FF'):
                        EngineCoolantTemp = int(b5, 16)
                        print("SPN-110,EIC Coolant Temperature :{}".format(EngineCoolantTemp),file=text_file)
                    if (b5 != 'FF'):
                        EngineCoolantTemp = int(b7, 16) * 8
                        print("SPN-110,EIC Engine Oil Pressure :{}".format(EngineCoolantTemp),file=text_file)
                elif int(PGN, 16) == 64915:
                    if (b1 != 'FF'):
                        t_Hexbyte = int(b1, 16)
                        GenControl = ( bin(t_Hexbyte)[2:] ).zfill(8)
                        print("SPN-3567,EIC Generator Set to auto control :{}".format(GenControl[5:6]),file=text_file)
                    if (b2 != 'FF'):
                        AltEffeciency = int(b3+b2, 16)
                        print("SPN-4078,Alternator Effeciency :{}".format(AltEffeciency),file=text_file)
                elif int(PGN, 16) == 65270:
                    if (b1 != 'FF'):
                        EngPartInletPressure = int(b1, 16)
                        print("SPN-81,Engine Particulate Trap Inlet Pressure :{}".format(EngPartInletPressure),file=text_file)
                    if (b2 != 'FF'):
                        EngineIntakeManifoldPressure = int(b2, 16)
                        print("SPN-102,Engine Intake Manifold #1 Pressure :{}".format(EngineIntakeManifoldPressure),file=text_file)
                    if (b3 != 'FF'):
                        EngineIntakeManifoldTemperature = int(b3, 16)
                        print("SPN-105,Engine Intake Manifold #1 Temperature :{}".format(EngineIntakeManifoldTemperature),file=text_file)
                    if (b4 != 'FF'):
                        EngineAirInletPressure = int(b4, 16)
                        print("SPN-106,Engine Air Inlet Pressure :{}".format(EngineAirInletPressure),file=text_file)
                    if (b5 != 'FF'):
                        EngineAirInletDifferenetialPressure = int(b5, 16)
                        print("SPN-107,Engine Air Differential Pressure :{}".format(EngineAirInletDifferenetialPressure),file=text_file)
                    if (b7 != 'FF'):
                        EngineExhaustGasTemp = int(b7+b6, 16)
                        print("SPN-173,Engine Exhaust Gas Temperature :{}".format(EngineExhaustGasTemp),file=text_file)
                    if (b8 != 'FF'):
                        EngineCoolantDifferenetialPressure = int(b8, 16)
                        print("SPN-112,Engine Coolant Differential Pressure :{}".format(EngineCoolantDifferenetialPressure),file=text_file)
                elif int(PGN, 16) == 64934:
                    if (b1 != 'FF'):
                        GenExcitationFV = int(b2+b1, 16)
                        print("SPN-3380,Generator Excitation Field Voltage :{}".format(GenExcitationFV),file=text_file)
                    if (b3 != 'FF'):
                        GenExcitationFC = int(b4+b3, 16)
                        print("SPN-3381,Generator Excitation Field Current :{}".format(GenExcitationFC),file=text_file)
                    if (b5 != 'FF'):
                        GenOutputVbiasPercentage = (int(b6+b5, 16) * 0.1 ) - 3212.75
                        print("SPN-3382,Generator Output Voltage Bias Percentage :{}".format(GenOutputVbiasPercentage),file=text_file)
                elif int(PGN, 16) == 65266:
                    if (b7 != 'FF'):
                        EngThrottlePosition = int(b7, 16)
                        print("SPN-52,Engine Throttle Position :{}".format(EngThrottlePosition),file=text_file)
                    if (b1 != 'FF'):
                        EngFuelRate = int(b2+b1, 16)
                        print("SPN-183,Engine Fuel Rate :{}".format(EngFuelRate),file=text_file)
                    if (b3 != 'FF'):
                        EngInstantFE = int(b4+b3, 16)
                        print("SPN-184,Engine Instantaneous Fuel Economy :{}".format(EngInstantFE),file=text_file)
                    if (b5 != 'FF'):
                        EngAvgFE = int(b6+b5, 16)
                        print("SPN-185,Engine Avergae Fuel Economy :{}".format(EngAvgFE),file=text_file)
                    if (b8 != 'FF'):
                        EngThrottlePosition2 = int(b8, 16)
                        print("SPN-52,Engine Throttle Position 2 :{}".format(EngThrottlePosition2),file=text_file)
                elif int(PGN, 16) == 64976:
                    if (b1 != 'FF'):
                        EngineAirFilterDifferential2 = int(b1, 16)
                        print("SPN-2809,Engine Air Filter Differential 2 :{}".format(EngineAirFilterDifferential2),file=text_file)
                elif int(PGN, 16) == 65170:
                    if (b1 != 'FF'):
                        EnginePreFilterOilPressure = int(b1, 16)
                        print("SPN-1208,Engine Pre Filter Oil Pressure :{}".format(EnginePreFilterOilPressure),file=text_file)
                    if (b2 != 'FF'):
                        EngineExhaustGasPressure = int(b3+b2, 16)
                        print("SPN-1209,Engine Exhaust Gas Pressure :{}".format(EngineExhaustGasPressure),file=text_file)
                    if (b4 != 'FF'):
                        EngineFuelRackPosition = int(b4, 16)
                        print("SPN-1210,Engine Fuel Rack Position :{}".format(EngineFuelRackPosition),file=text_file)
                    if (b6 != 'FF'):
                        EngineGasMassFlowRate1 = int(b6+b5, 16)
                        print("SPN-1241,Engine Gas Mass Flow Rate 1 :{}".format(EngineGasMassFlowRate1),file=text_file)
                    if (b7 != 'FF'):
                        InstEstBrakePower = int(b8+b7, 16)
                        print("SPN-1242,Instantaneous Estimated Brake Power :{}".format(InstEstBrakePower),file=text_file)

                else:
                    if (int(PGN,16)):
                        print("PGN in hex is {0} in decimal {1}, not found".format(PGN,int(PGN,16)),file=text_file)
            else :
             if (int(PGN, 16)):
                print ("PGN {} Not found, values are ".format(int(Header[2:6],16)),Values,file=text_file)
    return;

def log2file(text):

    with open("CanParserValues.txt", "w") as text_file:
        text_file.write("Purchase Amount: {0}".format(text))

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

#create a parsed Dir to place the file in
if not os.path.exists(ParsedFilesDir):
    os.makedirs(ParsedFilesDir)


# iterate through all the files

for filename in os.listdir(LogFilesDir):
    #try:

        file = open(LogFilesDir+"\\"+filename, 'r', errors='replace')
        #lno is used to keep the line numbers
        newfile_flag=1
        print('New file')
        temp = parser_summary('trial')
        lno=0
        for line in file:
            if lno>0 :
                spaceremovedline =line.replace(" ","")
                splitline = spaceremovedline.split("\t")
                if (len(splitline)>2) and splitline[0].isdigit():
                    #print (splitline)
                    with open(ParsedFilesDir+"\\"+filename+"Raw.txt", "a") as text_file:
                        data = splitline[0]+","+splitline[2]+","+splitline[7]+","+splitline[10]+splitline[11]+splitline[12]+splitline[13]+splitline[14]+splitline[15]+splitline[16]+splitline[17]
                        print(data, file=text_file)
                        #newfile = 1 Indicates a new canlog file has been opened for parsing.
                        parseJ1939(data,filename,newfile_flag,temp)
            lno = lno+1
            newfile_flag=0
        temp.plot_graph()
    #except  Exception:
    #   print (filename +" could not be parsed")