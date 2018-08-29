#!/usr/bin/python

import cgitb;cgitb.enable()
import lib,cgi,csv,os

def UpdateDict(h,r,e):
    if h == 'Name':
        e['name'] = r
    elif h == 'Spouse':
        e['spouse'] = r
    elif h[:9] == 'Caregiver' and r != '':
        e['caregivers'].append(r)
    elif h == 'E-mail':
        e['email'] = r
    elif h == 'Apt':
        e['apt'] = r
    elif h == 'Phone':
        e['phone'] = r
    elif h == 'ID':
        e['id'] = r
    elif h == 'Depart':
        e['move_date'] = r
    elif h[:5] == 'Child' and r != '':
        e['children'].append(r)
    elif h[:9] == 'Birthdate' and r != '':
        e['birthdate'].append(r)
    elif h == 'Concerns':
        e['concerns'] = r
    elif h == 'Registered':
        e['reg_date'] = r
    elif h == 'MIT Name':
        e['name_cert'] = r
    elif h == 'MIT E-mail':
        e['email_cert'] = r
    elif h[:13] == 'Other E-mails' and r != '':
        e['addemail'].append(r)
    elif h == 'Paid':
        e['paid'] = r=='True'
    elif h == 'Key Given':
        e['keygive'] = r=='True'
    elif h == 'Key Returned':
        e['keyret'] = r=='True'
    elif h == 'Expires':
        e['expire'] = r
    elif h == 'Terms':
        e['agree'] = r=='True'
    elif h == 'Liability':
        e['liability'] = r=='True'
    return e

if not lib.Auth():
    print 'Content-type: text/html'
    print
    print lib.noauth
else:
    form = cgi.FieldStorage()
    imp = lib.TryForm('import',form,default='').strip()
    reader = csv.reader(imp.split('\n'))
    db = lib.File2Param(lib.playdb,'l')
    for row in reader:
        header = row
        break
    for row in reader:
        e = {'caregivers':[],'children':[],'birthdate':[],'addemail':[]}
        for h,r in zip(header,row):
            e = UpdateDict(h,r,e)
        e['children'] = zip(e['children'],e['birthdate'])
        del e['birthdate']
        db.append(e)
    lib.Param2File(db,lib.playdb)
    lib.Redirect(lib.table)
