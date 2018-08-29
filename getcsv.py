#!/usr/bin/python

import cgitb;cgitb.enable()
import lib,csv

if not lib.Auth():
    print 'Content-type: text/html'
    print
    print lib.noauth
else:
    db = lib.File2Param(lib.playdb,'l')
    caremax = max([len(e['caregivers']) for e in db])
    carehead = ['Caregiver '+str(i) for i in range(1,caremax+1)]
    addemailmax = max([len(e['addemail']) for e in db])
    addemailhead = ['Other E-mails '+str(i) for i in range(1,addemailmax+1)]
    childmax = max([len(e['children']) for e in db])
    childhead = ['Child '+str(i) for i in range(1,childmax+1)]
    birthhead = ['Birthdate '+str(i) for i in range(1,childmax+1)]
    f = open(lib.csvdb,'w')
    writer = csv.writer(f)
    header = ['Name','E-mail','ID','Spouse']+carehead+addemailhead+['Apt', \
              'Phone','Depart']+childhead+birthhead+['Concerns', \
              'Registered','Expires','Paid','Key Given','Key Returned', \
              'MIT Name','MIT E-mail','Terms','Liability']
    writer.writerow(header)

    for e in db:
        carefull = e['caregivers']+['']*(caremax-len(e['caregivers']))
        addemailfull = e['addemail']+['']*(addemailmax-len(e['addemail']))
        child = [c[0] for c in e['children']]
        supp = ['']*(childmax-len(child))
        childfull = child+supp
        birthfull = [c[1] for c in e['children']]+supp
        row = [e['name'],e['email'],e['id'],e['spouse']]+carefull \
              +addemailfull+[e['apt'],e['phone'],e['move_date']]+ \
               childfull+birthfull+[e['concerns'],e['reg_date'], \
               e['expire'],str(e['paid']),str(e['keygive']), \
               str(e['keyret']),e['name_cert'],e['email_cert'], \
               str(e['agree']),str(e['liability'])]
        writer.writerow(row)

    f.close()

    lib.Redirect(lib.playcsv)
