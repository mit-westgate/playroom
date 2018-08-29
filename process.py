#!/usr/bin/python

import cgitb;cgitb.enable()
import lib,cgi,time,re

mitname,mitemail = lib.GetUserCert()
if not mitname:
    print 'Content-type: text/html'
    print
    print lib.nocert
else:
    form = cgi.FieldStorage()
    TryForm = lambda x:lib.TryForm(x,form,default='').strip()
    name = TryForm('name')
    email = TryForm('email')
    mid = TryForm('mid')
    spouse = TryForm('spouse')
    apt = TryForm('apt')
    phone = TryForm('phone')
    move = lib.ParseDate(TryForm('move'))
    child = [TryForm('child'+str(i)) for i in range(6)]
    birth = [lib.ParseDate(TryForm('birth'+str(i))) for i in range(6)]
    child = filter(lambda x:x[0],zip(child,birth))
    cares = [s.strip() for s in TryForm('cares').replace(',','\n').replace('\r','').split('\n')]
    cares = filter(None,cares)
    addemail = [s.strip() for s in TryForm('addemail').replace(',','\n').replace('\r','').split('\n')]
    addemail = filter(None,addemail)
    cern = TryForm('cern').replace('\n',' ').replace('\r','')
    agree = TryForm('agree') != ''
    liability = TryForm('liability') != ''
    errors = []
    if name == '':
        errors.append('You did not enter your name')
    if not lib.ValidEmail(email):
        errors.append('You entered an invalid e-mail address')
    if not re.compile('^9\d{8}$').match(mid):
        errors.append('You entered an invalid MIT ID number')
    if not all([lib.ValidEmail(e) for e in addemail]):
        errors.append('You entered an invalid additional e-mail address')
    if apt == '':
        errors.append('You did not enter your apartment number')
    if phone == '':
        errors.append('You did not enter your phone number')
    if move == '':
        errors.append('You either did not enter a move-out date or the '+ \
                      'date you entered was improperly formatted')
    if len(child) == 0:
        errors.append('You did not enter a child\'s name')
    if [c[1] for c in child].count('') > 0:
        errors.append('You did not include birthdates for every child or '+ \
                      'a birthdates was improperly formatted')
    if not lib.HasVisited(lib.tvisit,mitemail):
        errors.append('You did not visit and read the '+ \
                      '<a href="'+lib.terms+'">Westgate Playroom Policy</a>')
    elif not agree:
        errors.append('You did not indicate that you read and understood '+ \
                      'the Westgate Playroom Policy and you did not agree to '+ \
                      'comply to them')
    if not lib.HasVisited(lib.lvisit,mitemail):
        errors.append('You did not visit and read the '+ \
                      '<a href="'+lib.liability+'">Westgate Liability '+ \
                      'Release</a>')
    elif not liability:
        errors.append('You did not indicate that you read and understood '+ \
                      'the Westgate Liability Release')
    if len(errors) > 0:
        errors = '<ul>\n<li>'+'</li>\n<li>'.join(errors)+'</li>\n</ul>'
        print 'Content-type: text/html'
        print
        print \
"""
<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01//EN" "http://www.w3.org/TR/html4/strict.dtd">
<html>
 <head>
  <title>User Error</title>
  <link rel="stylesheet" href="%(css)s" type="text/css">
 </head>
 <body>
  <div id="main">
   <h3>
    User Error
    &#183; <a href="%(form)s">Playroom Application</a>
    &#183; <a href="%(main)s">Westgate Home</a>
   </h3>
   <hr>
   Your form submission generated the following errors and warnings.
   Please go back and try again.
   %(errors)s
   <hr>
   <div class="footer">
    Questions or comments? Bugs? Contact the Parents' Resource
    Coordinators at <a href="mailto:westgate-prc@mit.edu">westgate-prc@mit.edu</a>.
   </div>
  </div>
 </body>
</html>
""" % {'css':lib.css,'errors':errors,'main':lib.main,'form':lib.form}
    else:
        db = lib.File2Param(lib.playdb,'l')
        today = time.strftime('%Y-%m-%d')
        expire = lib.AddYear(today)
        entry = {'name_cert':mitname, \
                 'email_cert':mitemail, \
                 'name':name, \
                 'email':email, \
                 'addemail':addemail, \
                 'id':mid, \
                 'spouse':spouse, \
                 'apt':apt, \
                 'phone':phone, \
                 'move_date':move, \
                 'caregivers':cares, \
                 'children':child, \
                 'concerns':cern, \
                 'reg_date':today, \
                 'paid':False, \
                 'expire':expire, \
                 'keygive':False, \
                 'keyret':False, \
                 'agree':agree, \
                 'liability':liability}
        db.append(entry)
        lib.Param2File(db,lib.playdb)
        sender = '"Jason Walther" <jwalther@mit.edu>'
        proxy = '"Westgate PRC" <westgate-prc@mit.edu>'
        to = '"%(name)s" <%(email)s>' % {'name':name,'email':email}
        to = ', '.join([to]+addemail)
        bcc = proxy
        subject = 'Westgate Playroom Application'
        text = 'This is an automated message confirming that you '+ \
               'have successfully completed and submitted the '+ \
               'Westgate Playroom application. \n There are three more steps to complete the process. \n'+ \
               'Step 1. Pay $10 fee on adMIT One through (https://mit.universitytickets.com/w/event.aspx?id=858&p=1) under \'Westgate Playroom Annual Fee\'\n' + \
               'Step 2. Select a date to clean the playroom (https://docs.google.com/spreadsheets/d/1WQS2DQ6uVaqHk9a_hUtPNNgy38UJqUfvwxCXL--Jf34/edit#gid=0)\n' + \
               'Step 3.  Send email to Westgate Parent Coordinators (westgate-prc@gmail.com) that steps have been completed.\n' + \
               'At completion of steps within 3-5 business days; all MIT ID cards associated with your apt# will be activated for use of playroom.  A confirmation email will be sent to you. \n' + \
               'Thank you, \n WEC \n'

        e = lib.SendMail(sender=sender,proxy=proxy,to=to,bcc=bcc,subject=subject,text=text)
        print 'Content-type: text/html'
        print
        print \
"""
<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01//EN" "http://www.w3.org/TR/html4/strict.dtd">
<html>
 <head>
  <title>Playroom Application Submitted</title>
  <link rel="stylesheet" href="%(css)s" type="text/css">
 </head>
 <body>
  <div id="main">
   <h3>
    Playroom Application Submitted
    &#183; <a href="%(form)s">Playroom Application</a>
    &#183; <a href="%(main)s">Westgate Home</a>
   </h3>
   <hr>
   Your Westgate Playroom application has been successfully completed
   and submitted. Please bring $%(fee)s to %(name)s (the Parents' Resource
   Coordinators) in apartment %(apt)s and they will give you a key. You can
   contact them at %(phone)s or
   <a href="mailto:westgate-prc@mit.edu">westgate-prc@mit.edu</a>
   if you have additional questions.
   <hr>
   <div class="footer">
    Questions or comments? Bugs? Contact the Parents' Resource
    Coordinators at <a href="mailto:westgate-prc@mit.edu">westgate-prc@mit.edu</a>.
   </div>
  </div>
 </body>
</html>
""" % {'css':lib.css,'fee':lib.fee,'name':lib.prcname, \
       'apt':lib.prcapt,'phone':lib.prcphone,'form':lib.form, \
       'main':lib.main}
        
