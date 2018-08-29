#!/usr/bin/python

import cgitb;cgitb.enable()
import lib,cgi,time,re

if not lib.Auth():
    print 'Content-type: text/html'
    print
    print lib.noauth
else:
    TryForm = lambda x:lib.TryForm(x,form,default='').strip()
    form = cgi.FieldStorage()
    name = TryForm('name')
    email = TryForm('email')
    mid = TryForm('mid')
    spouse = TryForm('spouse')
    apt = TryForm('apt')
    phone = TryForm('phone')
    move = lib.ParseDate(TryForm('move'))
    child = [TryForm('fchild'+str(i)) for i in range(6)]
    birth = [lib.ParseDate(TryForm('fbirth'+str(i))) for i in range(6)]
    child = filter(lambda x:x[0],zip(child,birth))
    cares = [s.strip() for s in TryForm('cares').replace(',','\n').split('\n')]
    cares = filter(None,cares)
    addemail = [s.strip() for s in TryForm('addemail').replace(',','\n').split('\n')]
    addemail = filter(None,addemail)
    cern = TryForm('cern').replace('\n',' ').replace('\r','')
    reg = lib.ParseDate(TryForm('reg'))
    expire = lib.ParseDate(TryForm('expire'))
    paid = TryForm('paid') != ''
    keygive = TryForm('keygive') != ''
    keyret = TryForm('keyret') != ''
    mitname = TryForm('mitname')
    mitemail = TryForm('mitemail')
    agree = TryForm('agree') != ''
    liability = TryForm('liability') != ''
    errors = []
    if not lib.ValidEmail(email):
        errors.append('You entered an invalid e-mail address')
    if not all([lib.ValidEmail(e) for e in addemail]):
        errors.append('You entered an invalid additional e-mail address')
    if move == False:
        errors.append('The move-out date is improperly formatted')
    if [c[1] for c in child].count(False) > 0:
        errors.append('A birthdate is improperly formatted')
    if reg == False:
        errors.append('The registration date is improperly formatted')
    if expire == False:
        errors.append('The expiration date is improperly formatted')
    if not lib.ValidEmail(mitemail):
        errors.append('You entered an invalid Athena e-mail address')
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
""" % {'css':lib.css,'errors':errors,'form':lib.form,'main':lib.main}
    else:
        db = lib.File2Param(lib.playdb,'l')
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
                 'reg_date':reg, \
                 'paid':paid, \
                 'expire':expire, \
                 'keygive':keygive, \
                 'keyret':keyret, \
                 'agree':agree, \
                 'liability':liability}
        db.append(entry)
        lib.Param2File(db,lib.playdb)
        lib.Redirect(lib.table)
