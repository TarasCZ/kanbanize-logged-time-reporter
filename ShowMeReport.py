import requests, json, webbrowser, os
import xml.etree.ElementTree as ET

with open('./config.json') as json_data_file:
    data = json.load(json_data_file)
    date = data['date']

apiUrl = "https://{0}.kanbanize.com/index.php/api/kanbanize/get_log_time_activities".format(data['domain'])
apiData = {"fromdate": date['from'], "todate": date['to'], "author": data['username']}
apiHeaders = {"apikey": data['api-key'], "Content-Type": "application/json"}
response = requests.post(apiUrl, data=json.dumps(apiData), headers=apiHeaders)

root = ET.fromstring(response.text)

logRecords = []
for child in root:
    logRecord = {}
    for subchild in child:
        if subchild.tag == "date":
            logRecord['date'] = subchild.text[0:10]
        if subchild.tag == "cardid":
            logRecord['cardId'] = subchild.text
        if subchild.tag == "cardtitle":
            logRecord['cardTitle'] = subchild.text
        if subchild.tag == "loggedtime":
            logRecord['loggedTime'] = subchild.text
    
    logRecords.append(logRecord)

with open('logRecords.js', 'w') as outputFile:
    outputFile.write('reportData = ' + json.dumps(logRecords))

webbrowser.open('file://' + os.path.realpath('index.html'));
