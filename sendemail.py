#!/usr/bin/python

import cgitb;cgitb.enable()
import lib,cgi

if not lib.Auth():
    print 'Content-type: text/html'
    print
    print lib.noauth
else:
    form = cgi.FieldStorage()
    TryForm = lambda x:lib.TryForm(x,form,default='').strip()
    sender = '"Michael Churchill" <rmchurch@mit.edu>'
    mitname,mitemail = lib.GetUserCert()
    proxy = '"'+mitname+'" <'+mitemail+'>'
    to = TryForm('to')
    cc = TryForm('cc')
    bcc = TryForm('bcc')
    subject = TryForm('subject')
    text = TryForm('text')
    errors = []
    if to == '':
        errors.append('The "To" field was left empty')
    if subject == '':
        errors.append('The "Subject" field was left empty')
    if text == '':
        errors.append('The "Text" field was left empty')
    if len(errors) > 0:
        errors = '<ul>\n<li>'+'</li>\n<li>'.join(errors)+'</li>\n</ul>'
        print 'Content-type: text/html'
        print
        print \
"""
<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01//EN" "http://www.w3.org/TR/html4/strict.dtd">
<html>
 <head>
  <title>E-mail Error</title>
  <link rel="stylesheet" href="%(css)s" type="text/css">
 </head>
 <body>
  <div id="main">
   <h3>
    <p class="left">
     E-mail Error
     &#183; <a href="%(form)s">Playroom Application</a>
     &#183; <a href="%(main)s">Westgate Home</a>
    </p>
    <p class="right"><a href="%(table)s">Admin</a></p>
    <div class="clear"></div>
   </h3>
   <hr>
   Your e-mail submission generated the following errors and warnings.
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
        e = lib.SendMail(sender=sender,proxy=proxy,to=to,cc=cc,bcc=bcc,subject=subject,text=text)
        if e == None:
            msg = 'Your Westgate Playroom e-mail was successfully submitted.'
        else:
            msg = 'Your Westgate Playroom e-mail submission was unsuccessful. '+ \
                  'Contact the Westgate Graduate Coordinators at '+ \
                  '<a href="mailto:westgate-gc@mit.edu>westgate-gc@mit.edu</a> '+ \
                  'for assistance.'
        print 'Content-type: text/html'
        print
        print \
"""
<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01//EN" "http://www.w3.org/TR/html4/strict.dtd">
<html>
 <head>
  <title>E-mail Submitted</title>
  <link rel="stylesheet" href="%(css)s" type="text/css">
 </head>
 <body>
  <div id="main">
   <h3>
    <p class="left">
     E-Mail Submitted
     &#183; <a href="%(form)s">Playroom Application</a>
     &#183; <a href="%(main)s">Westgate Home</a>
    </p>
    <p class="right"><a href="%(table)s">Admin</a></p>
    <div class="clear"></div>
   </h3>
   <hr>
   %(msg)s
   <hr>
   <div class="footer">
    Questions or comments? Bugs? Contact the Parents' Resource
    Coordinators at <a href="mailto:westgate-prc@mit.edu">westgate-prc@mit.edu</a>.
   </div>
  </div>
 </body>
</html>
""" % {'css':lib.css,'msg':msg,'form':lib.form,'main':lib.main, \
       'table':lib.table}
