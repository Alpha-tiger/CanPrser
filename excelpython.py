import openpyxl
import win32com
import imaplib
import smtplib
import time
import email


#reading email

ORG_EMAIL = '@gmail.com'
FROM_EMAIL = 'talk2tpc' + ORG_EMAIL
FROM_PWD = 'tom@track24'
SMTP_SERVER = 'imap.gmail.com'
SMTP_PORT = 993

def read_email_from_gmail():
    #try:
        mail = imaplib.IMAP4_SSL(SMTP_SERVER)
        mail.login(FROM_EMAIL,FROM_PWD)
        mail.select('inbox')

        type, data = mail.search(None, 'ALL')
        mail_ids = data[0]
        print (data)

        id_list = mail_ids.split()
        first_email_id = int(id_list[0])
        latest_email_id = int(id_list[-1])

        for i in range(latest_email_id,first_email_id, -1):
            typ, data = mail.fetch(i, '(RFC822)' )

            for response_part in data:
                if isinstance(response_part, tuple):
                    msg = mail.message_from_string(response_part[1])
                    email_subject = msg['subject']
                    email_from = msg['from']
                    print ('From : ' + email_from + '\n')
                    print ('Subject : ' + email_subject + '\n')

    #except :
    #    print (Exception)


def read_excel_file():
    excel_document = openpyxl.load_workbook('DeliveryOrderTEST.xlsx')

    SheetNameList=excel_document.get_sheet_names()
    print(SheetNameList[0])

    sheet = excel_document.get_sheet_by_name(SheetNameList[0])


    multiple_cells = sheet['A1':'AP30']
    for row in multiple_cells:
        for cell in row:
            if cell.value == None :
                pass
            else :
                print (cell.value)
                if cell.value == '$DeliveryOrderNumber':
                    cell.value == ''
                if cell.value == '$RoamworksOrderNumber':
                        cell.value == ''
                if cell.value == '$Date':
                    cell.value == ''
                if cell.value == '$Time':
                        cell.value == ''


read_email_from_gmail()
