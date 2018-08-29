#!/usr/bin/python

import cgitb;cgitb.enable()
import lib,cgi,os

if not lib.Auth():
    print 'Content-type: text/html'
    print
    print lib.noauth
else:
    form = cgi.FieldStorage()
    TryForm = lambda x:lib.TryForm(x,form,default='').strip()
    errors = []
    dbnew = []
    n = int(lib.TryForm('number',form,default=0))
    for i in range(n):
        si = str(i)
        delete = TryForm('delete'+si)=='True'
        if not delete:
            name = TryForm('name'+si)
            email = TryForm('email'+si)
            mid = TryForm('id'+si)
            spouse = TryForm('spouse'+si)
            apt = TryForm('apt'+si)
            phone = TryForm('phone'+si)
            move = lib.ParseDate(TryForm('move'+si))
            child = [c.strip() for c in TryForm('child'+si).split('\n')]
            birth = [lib.ParseDate(b.strip()) for b in TryForm('birth'+si).split('\n')]
            child = filter(lambda x:x[0] and x[1],zip(child,birth))
            cares = [s.strip() for s in TryForm('cares'+si).replace(',','\n').split('\n')]
            cares = filter(None,cares)
            addemail = [s.strip() for s in TryForm('addemail'+si).replace(',','\n').split('\n')]
            addemail = filter(None,addemail)
            cern = TryForm('cern'+si).replace('\n',' ').replace('\r','')
            reg = lib.ParseDate(TryForm('reg'+si))
            expire = lib.ParseDate(TryForm('expire'+si))
            paid = TryForm('paid'+si)=='True'
            keygive = TryForm('keygive'+si)=='True'
            keyret = TryForm('keyret'+si)=='True'
            mitname = TryForm('mitname'+si)
            mitemail = TryForm('mitemail'+si)
            agree = TryForm('agree'+si)=='True'
            liability = TryForm('liability'+si)=='True'
            eref = 'Entry #'+str(i+1)+': '
            if not lib.ValidEmail(email):
                errors.append(eref+'You entered an invalid e-mail address')
            if not all([lib.ValidEmail(e) for e in addemail]):
                errors.append(eref+'You entered an invalid additional e-mail address')
            if move == False:
                errors.append(eref+'The move-out date is impropely formatted')
            if [c[1] for c in child].count(False) > 0:
                errors.append(eref+'A birthdate is improperly formatted')
            if reg == False:
                errors.append(eref+'The registration date is improperly formatted')
            if expire == False:
                errors.append(eref+'The expiration date is improperly formatted')
            if not lib.ValidEmail(mitemail):
                errors.append(eref+'You entered an invalid Athena e-mail address')
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
            dbnew.append(entry)
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
    <p class="left">
     User Error
     &#183; <a href="%(form)s">Playroom Application</a>
     &#183; <a href="%(main)s">Westgate Home</a>
    </p>
    <p class="right"><a href="%(table)s">Admin</a></p>
    <div class="clear"></div>
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
""" % {'css':lib.css,'errors':errors,'main':lib.main,'form':lib.form, \
       'table':lib.table}
    else:
        lib.Param2File(dbnew,lib.playdb)
        lib.Redirect(lib.table)
