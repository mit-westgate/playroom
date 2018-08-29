#!/usr/bin/python

import cgitb;cgitb.enable()
import os,re,time,ldap,smtplib
from datetime import datetime

quote1 = '&#39;'
quote2 = '&quot;'

pres = 'palomagr'
crc = 'alevec'
prc = 'eldante'
sc = 'scotttan'
itc = 'yasushis'
rfro = 'csauer'
csc = 'yyn'
gc = 'amiya'
tr = 'hannahac'
rla = 'naomic'
pcc = 'bichoy'
wm = 'roys'

officer = {'WG Presidents':pres,'WG Couples Resource Coordinators':crc,'WG Parents Resource Coordinators':prc,'WG Social Chairs':sc,'WG Recycling & Floor Rep Organizers':rfro,'WG Graduate Coordinators':gc,'WG Secretary/Treasurers':tr,'Residential Life Associate':rla,'WG Webmaster':wm, 'WG Information and Technology Coordinators': itc,'WG Community and Sustainability Coordinators':csc}
emails = {'WG Presidents':'westgate-gc@mit.edu','WG Couples Resource Coordinators':'westgate-crc@mit.edu','WG Parents Resource Coordinators':'westgate-prc@mit.edu','WG Social Chairs':'westgate-sc@mit.edu','WG Recycling & Floor Rep Organizers':'westgate-rfro@mit.edu','WG Graduate Coordinators':'westgate-gc@mit.edu','WG Secretary/Treasurers':'westgate-sec-treas@mit.edu','Residential Life Associate':'westgate-rla@mit.edu','WG Webmaster':'westgate-wm@mit.edu', 'WG Information and Technology Coordinators':'westgate-ipc@mit.edu','WG Community and Sustainability Coordinators':'westgate-csc@mit.edu'}

#superusers = ['kdk323','jwalther','awalther','jrmac']
superusers = ['jpwhit05','otanovic','yasushis']

main = 'http://westgate.mit.edu'
root = 'http://westgate.mit.edu/scripts/playroom/'
# sroot = 'https://scripts-cert.mit.edu/~westgate/scripts/playroom/'
sroot = 'https://westgate.scripts.mit.edu:444/scripts/playroom/'
css = root+'style.css'
form = sroot+'form.py'
process = sroot+'process.py'
terms = sroot+'terms.py'
liability = sroot+'liability.py'
csv = sroot+'getcsv.py'
update = sroot+'update.py'
table = sroot+'table.py'
add = sroot+'add.py'
email = sroot+'sendemail.py'
importcsv = sroot+'importcsv.py'
playcsv = sroot+'db/playroom.csv'

db = os.curdir+os.sep+'db'+os.sep
playdb = db+'playroom.txt'
csvdb = db+'playroom.csv'
tvisit = db+'termvisits.txt'
lvisit = db+'liabilityvisits.txt'

fee = 10
prcname = 'Tonya Smith'
prcapt = 'F4'
prcphone = ''
visitcutoff = 30

noauth = \
"""
<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01//EN" "http://www.w3.org/TR/html4/strict.dtd">
<html>
 <head>
  <title>Westgate Family Housing</title>
  <link rel="stylesheet" href="%(css)s" type="text/css">
 </head>
 <body>
  <div id="main">
   This page is only accessible to certain members of the Westgate
   Executive Committee and the Westgate House Team with MIT
   certificates.
  </div>
 </body>
</html>
""" % {'css':css }

nocert = \
"""
<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01//EN" "http://www.w3.org/TR/html4/strict.dtd">
<html>
 <head>
  <title>Westgate Family Housing</title>
  <link rel="stylesheet" href="%(css)s" type="text/css">
 </head>
 <body>
  <div id="main">
   This page is only accessible to MIT affiliates with the appropriate
   certificates installed on their computers. For more information about
   certificates, visit MIT IST's page on
   <a href="http://web.mit.edu/ist/topics/certificates/">Certificates at MIT</a>.
  </div>
 </body>
</html>
""" % {'css':css}

#----------------------------------------------------------------------------------
def File2Param(fn,t):
    try:
        f = open(fn,'r')
        p = eval(f.read())
        f.close()
        if t=='l':
            return list(p)
        elif t=='d':
            return dict(p)
        else:
            return str(p)
    except:
        if t=='l':
            return []
        elif t=='d':
            return {}
        else:
            return ''

#----------------------------------------------------------------------------------
def Param2File(p,fn):
    f = open(fn,'w')
    f.write(str(p))
    f.close()

#----------------------------------------------------------------------------------
def ReplaceQuotes(s):
    s = re.compile("'").sub(quote1,s)
    s = re.compile('"').sub(quote2,s)
    return s

#----------------------------------------------------------------------------------
def ReturnQuotes(s):
    s = re.compile(quote1).sub("'",s)
    s = re.compile(quote2).sub('"',s)
    return s

#----------------------------------------------------------------------------------
# This function takes a year and returns true if it is a leap year, false if not.

def IsLeap(y):
        if not y%400:
                return True
        elif not y%100:
                return False
        elif not y%4:
                return True
        else:
                return False

#----------------------------------------------------------------------------------
# This function takes a year, month, and day of the month and returns true if this
# is a valid day of the year, false if not.

def TrueDates(y,m,d):
        dmax = [31,29,31,30,31,30,31,31,30,31,30,31]
        if dmax[m-1] < d:
                return False
        if m == 2 and d == 29 and not IsLeap(y):
                return False
        return True

#----------------------------------------------------------------------------------
# This function parses a string representing a date and returns a string formatted
# "yyyy-mm-dd". The input date string needs to be written month-date-year. The year
# can be written with 4 digits or just the last 2. Single-digit months and days do
# not necessarily need to be padded with a zero. If the year is ommitted, the
# current year is assumed. Slashes, hyphens, or white space can be used to separate
# the different numbers. If the string cannot be parsed or the date is not
# possible, the function returns a null string.

def ParseDate(s):

        if s == '':
            return ''

        # Set regular expression and attempt to match to input string
        expr = re.compile('(?:\s*(?P<month1>(?:1[0-2])|(?:0?[1-9]))\s*[-/\s]\s*(?P<day1>[0-3]?\d)\s*(?:[-/\s]\s*(?P<year1>(?:\d\d)?\d\d?))?\s*)|'+
                          '(?:\s*(?P<year2>\d{4})\s*[-/\s]\s*(?P<month2>(?:1[0-2])|(?:0?[1-9]))\s*[-/\s]\s*(?P<day2>[0-3]?\d)\s*)')
        match = expr.match(s)

        # No success if match could not be made or if there are trailing unmatched characters
        if not match or match.end() < len(s):
                return False
        if match.group('year2') == None:
            y,m,d = match.group('year1'),match.group('month1'),match.group('day1')
        else:
            y,m,d = match.group('year2'),match.group('month2'),match.group('day2')

        # If no year was entered, default to current year
        if not y:
                y = str(datetime.now().year)

        # If only two digits of year were entered, assume that first two digits are "20"^M
        if len(y) == 2:
                y = str(int(y)+2000)

        # If the parsed date does not occur in calendar, return false
        if not TrueDates(int(y),int(m),int(d)):
                return False

        # Pad month and day with zeroes if necessary and return formatted string
        if len(m) == 1:
                m = '0'+m
        if len(d) == 1:
                d = '0'+d
        return y+'-'+m+'-'+d

#----------------------------------------------------------------------------------
def AddYear(s):
    y0 = int(s[0:4])
    m0 = int(s[5:7])
    d0 = int(s[8:])
    y = y0+1
    if m0 == 2 and d0 == 29 and not isLeap(y):
        m = 3
        d = 1
    else:
        m = m0
        d = d0
    return '%04d-%02d-%02d' % (y,m,d)

#----------------------------------------------------------------------------------
def GetDate():
    n = datetime.now()
    return '%04d-%02d-%02d' % (n.year,n.month,n.day)

#----------------------------------------------------------------------------------
def IsPastBy(s,days):
    s = ParseDate(s)
    if not s:
        return False
    d0 = datetime(int(s[:4]),int(s[5:7]),int(s[8:10]))
    return (datetime.now()-d0).days > days

#----------------------------------------------------------------------------------
def UpdateVisits(visitdb,email):
    global visitcutoff
    visits = File2Param(visitdb,'l')
    visits = [v for v in visits if not IsPastBy(v['date'],visitcutoff)]
    emails = [v for v in visits if v['email']==email]
    if len(emails) == 0:
        visits.append({'date':GetDate(),'email':email})
    else:
        emails[0]['date'] = GetDate()
        for e in emails[1:]:
            e = {}
    visits = filter(None,visits)
    visits.sort(cmp=lambda x,y:cmp(x['date'],y['date']))
    Param2File(visits,visitdb)

#----------------------------------------------------------------------------------
def HasVisited(visitdb,email):
    global visitcutoff
    visits = File2Param(visitdb,'l')
    visits = [v for v in visits if not IsPastBy(v['date'],visitcutoff)]
    for v in visits:
        if v['email'] == email:
            return True
    return False

#----------------------------------------------------------------------------------
def SortRank(entries,ranks):
    r = zip(ranks,entries)
    ri = zip(r,range(len(r)))
    ri.sort()
    return map(lambda x:x[0][1],ri)

#----------------------------------------------------------------------------------
def TryForm(variable,form,default=None):
    try:
        return form.getlist(variable)[0]
    except:
        return default

#----------------------------------------------------------------------------------
# Based on http://en.wikipedia.org/wiki/E-mail_address#Limitations
def ValidEmail(email):
    lc = "[-\w!#$%*/?|^{}`~&'+=]"
    lcd = "[-\w!#$%*/?|^{}`~&'+=.]"
    dm = '[-a-zA-Z0-9]'
    expr = re.compile("""((?:%s+%s?)*%s@(?:%s+\.)*%s+)""" % (lc,lcd,lc,dm,dm))
    m = expr.match(email)
    return bool(m) and m.end() == len(email)

#----------------------------------------------------------------------------------
def Redirect(url):
    print 'Content-type: text/html'
    print
    print \
"""
<html>
 <head>
  <meta http-equiv="refresh" content="0; url=%s">
 </head>
 <body>
 </body>
</html>
""" % url

#----------------------------------------------------------------------------------
def OfficerList():
    global officer
    return ','.join(officer.values()).split(',')

#----------------------------------------------------------------------------------
# eduPersonPrimaryAffiliation   Primary affiliation status
# cn                            Full name
# uidNumber
# eduPersonScopedAffiliation
# street                        Street address
# eduPersonPrincipalName
# uid                           Athena user ID
# postalCode                    Postal code
# mail                          E-mail address
# loginShell
# gidNumber
# homePhone                     Home phone number
# apple-user-homeDirectory      Apple home directory
# l                             City
# o
# st                            State
# eduPersonAffiliation          Affiliation status
# sn                            Last name
# homeDirectory                 Athena home directory
# ou                            Department
# givenName                     First name

def GetAttributes(attr):
#    try:
        keys = os.environ.keys()
        keys.sort()
        searchid = os.environ['SSL_CLIENT_S_DN_Email'].split('@')
        l = ldap.open("ldap.mit.edu")
        l.protocol_version = ldap.VERSION3
        baseDN = "dc=mit,dc=edu"
        searchScope = ldap.SCOPE_SUBTREE
        searchFilter = "uid="+searchid[0]
        retrieveAttributes = None
        ldap_result_id = l.search(baseDN,searchScope,searchFilter,retrieveAttributes)
        result_type,result_data = l.result(ldap_result_id,0)
        return result_data[0][1][attr][0]
#    except:
#        return False

#----------------------------------------------------------------------------------
def Auth():
    global superusers
    uidauth = GetAttributes('uid')
    return bool(superusers.count(uidauth))

#----------------------------------------------------------------------------------
def GetOfficer():
    global officer
    uidauth = GetAttributes('uid')
    for pos,uid in officer.items():
        if uid.split(',').count(uidauth):
            return pos
    return 'Anonymous Super Hacker'

#----------------------------------------------------------------------------------
def GetUserCert():
    return GetAttributes('cn'),GetAttributes('mail')

#----------------------------------------------------------------------------------
# Multiple addresses in one argument must be separated by commas
def SendMail(sender='',proxy=None,to='',cc='',bcc='',subject='',text=''):
    if proxy == None:
        proxy = sender
    message = 'From: %s\nTo: %s\nCc: %s\nBcc: %s\nSubject: %s\n\n%s' % (proxy,to,cc,bcc,subject,text)
    recipients = (',').join([to,cc,bcc]).split(',')
    server = smtplib.SMTP('outgoing.mit.edu')
    try:
        server.sendmail(sender,recipients,message)
    except smtplib.SMTPRecipientsRefused:
        e = 'SMTPRecipientsRefused'
    except smtplib.SMTPHeloError:
        e = 'SMTPHeloError'
    except smtplib.SMTPSenderRefused:
        e = 'SMTPSenderRefused'
    except smtplib.SMTPDataError:
        e = 'SMTPDataError'
    except:
        e = 'Unexpected Error'
    else:
        e = None
    server.quit()
    return e
