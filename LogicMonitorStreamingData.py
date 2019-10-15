#!/bin/env python

import requests
import json
import hashlib
import base64
import time
import hmac



#Account Info
AccessId ='73L56U7cY64y6J72tdaP'
AccessKey ='V343B{SNZct{2mIz)w8k~EYf76[Z~}fVk8{R4DuT'
Company = 'seagen'
#Request Info
httpVerb ='GET'
resourcePath = '/device/devices/813/devicedatasources/49973/data'
queryParams = ''
data = ''

#Construct URL 
url = 'https://'+ Company +'.logicmonitor.com/santaba/rest' + resourcePath +queryParams

#Get current time in milliseconds
epoch =str(int(time.time() * 1000))

#Concatenate Request details
requestVars = httpVerb + epoch + data + resourcePath

#Construct signature
hmac = hmac.new(AccessKey.encode(),msg=requestVars.encode(),digestmod=hashlib.sha256).hexdigest()
signature = base64.b64encode(hmac.encode())

#Construct headers
auth = 'LMv1 ' + AccessId + ':' + signature.decode() + ':' + epoch
headers = {'Content-Type':'application/json','Authorization':auth}

#Make request
response = requests.get(url, data=data, headers=headers)

#Print status and body of response
print ('Response Status:',response.status_code)
print ('Response Body:',response.content)


json_data = json.loads(response.text)
#pd.io.json.json_normalize(response,

test = json_data['data']['instances']



percent_util = [i[1] for i in test['PureStorage_ArrayUtilization']['values']]
time_point = [i for i in test['PureStorage_ArrayUtilization']['time']]


print(json_data)