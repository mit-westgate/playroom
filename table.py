#!/usr/bin/python

import cgitb;cgitb.enable()
import lib

freq = 10
header = \
"""
<tr>
 <td class="%(lead)s"><input type="checkbox" onclick="selectall(this.checked)" name="allcheck%(icheck)s"></td>
 <td class="%(lead)sname1"><a href="javascript:toggle('name')">Name</a>
  <input type="hidden" name="visible-name" id="visible-name" value="False">
 </td>
 <td class="%(lead)sname2" style="display:none"><a href="javascript:toggle('name')">Name</a></td>
 <td class="%(lead)semail1"><a href="javascript:toggle('email')">E-mail</a>
  <input type="hidden" name="visible-email" id="visible-email" value="False">
 </td>
 <td class="%(lead)semail2" style="display:none"><a href="javascript:toggle('email')">E-mail</a></td>
 <td class="%(lead)sid1"><a href="javascript:toggle('id')">ID</a>
  <input type="hidden" name="visible-id" id="visible-id" value="False">
 </td>
 <td class="%(lead)sid2" style="display:none"><a href="javascript:toggle('id')">ID</a></td>
 <td class="%(lead)sspouse1"><a href="javascript:toggle('spouse')">Spouse</a>
  <input type="hidden" name="visible-spouse" id="visible-spouse" value="False">
 </td>
 <td class="%(lead)sspouse2" style="display:none"><a href="javascript:toggle('spouse')">Spouse</a></td>
 <td class="%(lead)scares1"><a href="javascript:toggle('cares')">Caregivers</a>
  <input type="hidden" name="visible-cares" id="visible-cares" value="False">
 </td>
 <td class="%(lead)scares2" style="display:none"><a href="javascript:toggle('cares')">Caregivers</a></td>
 <td class="%(lead)saddemail1"><a href="javascript:toggle('addemail')">E-mails</a>
  <input type="hidden" name="visible-addemail" id="visible-addemail" value="False">
 </td>
 <td class="%(lead)saddemail2" style="display:none"><a href="javascript:toggle('addemail')">E-mails</a></td>
 <td class="%(lead)sapt1"><a href="javascript:toggle('apt')">Apt</a>
  <input type="hidden" name="visible-apt" id="visible-apt" value="False">
 </td>
 <td class="%(lead)sapt2" style="display:none"><a href="javascript:toggle('apt')">Apt</a></td>
 <td class="%(lead)sphone1"><a href="javascript:toggle('phone')">Phone</a>
  <input type="hidden" name="visible-phone" id="visible-phone" value="False">
 </td>
 <td class="%(lead)sphone2" style="display:none"><a href="javascript:toggle('phone')">Phone</a></td>
 <td class="%(lead)smove1"><a href="javascript:toggle('move')">Depart</a>
  <input type="hidden" name="visible-move" id="visible-move" value="False">
 </td>
 <td class="%(lead)smove2" style="display:none"><a href="javascript:toggle('move')">Depart</a></td>
 <td class="%(lead)schild1"><a href="javascript:toggle('child')">Children</a>
  <input type="hidden" name="visible-child" id="visible-child" value="False">
 </td>
 <td class="%(lead)schild2" style="display:none"><a href="javascript:toggle('child')">Children</a></td>
 <td class="%(lead)sbirth1"><a href="javascript:toggle('birth')">Birthdates</a>
  <input type="hidden" name="visible-birth" id="visible-birth" value="False">
 </td>
 <td class="%(lead)sbirth2" style="display:none"><a href="javascript:toggle('birth')">Birthdates</a></td>
 <td class="%(lead)scern1"><a href="javascript:toggle('cern')">Concerns</a>
  <input type="hidden" name="visible-cern" id="visible-cern" value="False">
 </td>
 <td class="%(lead)scern2" style="display:none"><a href="javascript:toggle('cern')">Concerns</a></td>
 <td class="%(lead)sreg1"><a href="javascript:toggle('reg')">Registered</a>
  <input type="hidden" name="visible-reg" id="visible-reg" value="False">
 </td>
 <td class="%(lead)sreg2" style="display:none"><a href="javascript:toggle('reg')">Registered</a></td>
 <td class="%(lead)sexpire1"><a href="javascript:toggle('expire')">Expires</a>
  <input type="hidden" name="visible-expire" id="visible-expire" value="False">
 </td>
 <td class="%(lead)sexpire2" style="display:none"><a href="javascript:toggle('expire')">Expires</a></td>
 <td class="%(lead)spaid1"><a href="javascript:toggle('paid')">Paid</a>
  <input type="hidden" name="visible-paid" id="visible-paid" value="False">
 </td>
 <td class="%(lead)spaid2" style="display:none"><a href="javascript:toggle('paid')">Paid</a></td>
 <td class="%(lead)skeygive1"><a href="javascript:toggle('keygive')">Key Given</a>
  <input type="hidden" name="visible-keygive" id="visible-keygive" value="False">
 </td>
 <td class="%(lead)skeygive2" style="display:none"><a href="javascript:toggle('keygive')">Key Given</a></td>
 <td class="%(lead)skeyret1"><a href="javascript:toggle('keyret')">Key Returned</a>
  <input type="hidden" name="visible-keyret" id="visible-keyret" value="False">
 </td>
 <td class="%(lead)skeyret2" style="display:none"><a href="javascript:toggle('keyret')">Key Returned</a></td>
 <td class="%(lead)smitname1"><a href="javascript:toggle('mitname')">MIT Name</a>
  <input type="hidden" name="visible-mitname" id="visible-mitname" value="False">
 </td>
 <td class="%(lead)smitname2" style="display:none"><a href="javascript:toggle('mitname')">MIT Name</a></td>
 <td class="%(lead)smitemail1"><a href="javascript:toggle('mitemail')">MIT E-mail</a>
  <input type="hidden" name="visible-mitemail" id="visible-mitemail" value="False">
 </td>
 <td class="%(lead)smitemail2" style="display:none"><a href="javascript:toggle('mitemail')">MIT E-mail</a></td>
 <td class="%(lead)sagree1"><a href="javascript:toggle('agree')">Terms</a>
  <input type="hidden" name="visible-agree" id="visible-agree" value="False">
 </td>
 <td class="%(lead)sagree2" style="display:none"><a href="javascript:toggle('agree')">Terms</a></td>
 <td class="%(lead)sliability1"><a href="javascript:toggle('liability')">Liability</a>
  <input type="hidden" name="visible-liability" id="visible-liability" value="False">
 </td>
 <td class="%(lead)sliability2" style="display:none"><a href="javascript:toggle('liability')">Liability</a></td>
</tr>
"""

def FormatEntry(entry,i,last):
    global header,freq
    e = entry.copy()
    h = (i % freq == 9)*(header % {'lead':'','icheck':int(round(float(i)/freq))})
    e['last'] = (i % freq == 9 or last)*' last'
    e['cares1'] = ', '.join(e['caregivers'])
    e['cares2'] = '\n'.join(e['caregivers'])
    e['addemail1'] = ', '.join(e['addemail'])
    e['addemail2'] = '\n'.join(e['addemail'])
    e['child1'] = ', '.join([c[0] for c in e['children']])
    e['child2'] = '\n'.join([c[0] for c in e['children']])
    e['birth1'] = ', '.join([str(c[1]) for c in e['children']])
    e['birth2'] = '\n'.join([str(c[1]) for c in e['children']])
    e['ispaid'] = e['paid']*' checked'
    e['iskeygive'] = e['keygive']*' checked'
    e['iskeyret'] = e['keyret']*' checked'
    e['isagree'] = e['agree']*' checked'
    e['isliability'] = e['liability']*' checked'
    e['i'] = i
    e['r'] = i%2
    return \
"""
<tr>
 <input type="hidden" name="delete%(i)s" id="delete%(i)s" value="False">
 <td class="d%(r)s left%(last)s"><input type="checkbox" name="check%(i)s" id="check%(i)s" value="True"></td>
 <td class="d%(r)s name1 left%(last)s" id="cell-name%(i)s">%(name)s</td>
 <td class="d%(r)s name2%(last)s" style="display:none"><input type="text" name="name%(i)s" value="%(name)s" id="input-name%(i)s" class="w140"></td>
 <td class="d%(r)s email1%(last)s" id="cell-email%(i)s">%(email)s</td>
 <td class="d%(r)s email2%(last)s" style="display:none"><input type="text" name="email%(i)s" value="%(email)s" id="input-email%(i)s" class="w140"></td>
 <td class="d%(r)s id1%(last)s" id="cell-id%(i)s">%(id)s</td>
 <td class="d%(r)s id2%(last)s" style="display:none"><input type="text" name="id%(i)s" value="%(id)s" id="input-id%(i)s" class="w140"></td>
 <td class="d%(r)s spouse1%(last)s" id="cell-spouse%(i)s">%(spouse)s</td>
 <td class="d%(r)s spouse2%(last)s" style="display:none"><input type="text" name="spouse%(i)s" value="%(spouse)s" id="input-spouse%(i)s" class="w140"></td>
 <td class="d%(r)s cares1%(last)s" id="cell-cares%(i)s">%(cares1)s</td>
 <td class="d%(r)s cares2%(last)s" style="display:none"><textarea name="cares%(i)s" id="input-cares%(i)s" class="h2 w140">%(cares2)s</textarea></td>
 <td class="d%(r)s addemail1%(last)s" id="cell-addemail%(i)s">%(addemail1)s</td>
 <td class="d%(r)s addemail2%(last)s" style="display:none"><textarea name="addemail%(i)s" id="input-addemail%(i)s" class="h2 w140">%(addemail2)s</textarea></td>
 <td class="d%(r)s apt1%(last)s" id="cell-apt%(i)s">%(apt)s</td>
 <td class="d%(r)s apt2%(last)s" style="display:none"><input type="text" name="apt%(i)s" value="%(apt)s" id="input-apt%(i)s" class="w140"></td>
 <td class="d%(r)s phone1%(last)s" id="cell-phone%(i)s">%(phone)s</td>
 <td class="d%(r)s phone2%(last)s" style="display:none"><input type="text" name="phone%(i)s" value="%(phone)s" id="input-phone%(i)s" class="w140"></td>
 <td class="d%(r)s move1%(last)s" id="cell-move%(i)s">%(move_date)s</td>
 <td class="d%(r)s move2%(last)s" style="display:none"><input type="text" name="move%(i)s" value="%(move_date)s" id="input-move%(i)s" class="w140"></td>
 <td class="d%(r)s child1%(last)s" id="cell-child%(i)s">%(child1)s</td>
 <td class="d%(r)s child2%(last)s" style="display:none"><textarea name="child%(i)s" id="input-child%(i)s" class="h2 w140">%(child2)s</textarea></td>
 <td class="d%(r)s birth1%(last)s" id="cell-birth%(i)s">%(birth1)s</td>
 <td class="d%(r)s birth2%(last)s" style="display:none"><textarea name="birth%(i)s" id="input-birth%(i)s" class="h2 w140">%(birth2)s</textarea></td>
 <td class="d%(r)s cern1%(last)s" id="cell-cern%(i)s">%(concerns)s</td>
 <td class="d%(r)s cern2%(last)s" style="display:none"><textarea name="cern%(i)s" id="input-cern%(i)s" class="h2 w140">%(concerns)s</textarea></td>
 <td class="d%(r)s reg1%(last)s" id="cell-reg%(i)s">%(reg_date)s</td>
 <td class="d%(r)s reg2%(last)s" style="display:none"><input type="text" name="reg%(i)s" value="%(reg_date)s" id="input-reg%(i)s" class="w140"></td>
 <td class="d%(r)s expire1%(last)s" id="cell-expire%(i)s">%(expire)s</td>
 <td class="d%(r)s expire2%(last)s" style="display:none"><input type="text" name="expire%(i)s" value="%(expire)s" id="input-expire%(i)s" class="w140"></td>
 <td class="d%(r)s paid1%(last)s" id="cell-paid%(i)s"><input type="checkbox" disabled%(ispaid)s></td>
 <td class="d%(r)s paid2%(last)s" style="display:none"><input type="checkbox" name="paid%(i)s" value="True"%(ispaid)s id="input-paid%(i)s"></td>
 <td class="d%(r)s keygive1%(last)s" id="cell-keygive%(i)s"><input type="checkbox" disabled%(iskeygive)s></td>
 <td class="d%(r)s keygive2%(last)s" style="display:none"><input type="checkbox" name="keygive%(i)s" value="True"%(iskeygive)s id="input-keygive%(i)s"></td>
 <td class="d%(r)s keyret1%(last)s" id="cell-keyret%(i)s"><input type="checkbox" disabled%(iskeyret)s></td>
 <td class="d%(r)s keyret2%(last)s" style="display:none"><input type="checkbox" name="keyret%(i)s" value="True"%(iskeyret)s id="input-keyret%(i)s"></td>
 <td class="d%(r)s mitname1%(last)s" id="cell-mitname%(i)s">%(name_cert)s</td>
 <td class="d%(r)s mitname2%(last)s" style="display:none"><input type="text" name="mitname%(i)s" value="%(name_cert)s" id="input-mitname%(i)s" class="w140"></td>
 <td class="d%(r)s mitemail1%(last)s" id="cell-mitemail%(i)s">%(email_cert)s</td>
 <td class="d%(r)s mitemail2%(last)s" style="display:none"><input type="text" name="mitemail%(i)s" value="%(email_cert)s" id="input-mitemail%(i)s" class="w140"></td>
 <td class="d%(r)s agree1%(last)s" id="cell-agree%(i)s"><input type="checkbox" disabled%(isagree)s></td>
 <td class="d%(r)s agree2%(last)s" style="display:none"><input type="checkbox" name="agree%(i)s" value="True"%(isagree)s id="input-agree%(i)s"></td>
 <td class="d%(r)s liability1%(last)s right" id="cell-liability%(i)s"><input type="checkbox" disabled%(isliability)s></td>
 <td class="d%(r)s liability2%(last)s right" style="display:none"><input type="checkbox" name="liability%(i)s" value="True"%(isliability)s id="input-liability%(i)s"></td>
</tr>
""" % e +h

if not lib.Auth():
    print 'Content-type: text/html'
    print
    print lib.noauth
else:
    
    db = lib.File2Param(lib.playdb,'l')
    body = ''.join([FormatEntry(e,i,i+1==len(db)) for e,i in zip(db,range(len(db)))])
    mitname,mitemail = lib.GetUserCert()
    print 'Content-type: text/html'
    print
    print \
"""
<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01//EN" "http://www.w3.org/TR/html4/strict.dtd">
<html class="white">
 <head>
  <title>Playroom Membership</title>
  <link rel="stylesheet" href="%(css)s" type="text/css">
  <script language="javascript" type="text/javascript">
   function deleteselected() {
    var tbl = document.getElementById('dbtable');
    for (var i=0;i<%(number)s;i++) {
     if (eval('document.table.check'+i).checked == true) {
      tbl.rows[i+1+parseInt(i/%(freq)s)].style.display = 'none';
      document.getElementById('delete'+i).value = 'True';
     }
    }
   }
   function add() {
    var tbl = document.getElementById('formtable');
    tbl.rows[ndisp+10].style.display = '';
    ndisp += 1;
    if (ndisp == 5) {
     document.getElementById('add').style.display = 'none';
    } else if (ndisp == 1) {
     document.getElementById('remove').style.display = '';
    }
   }
   function remove() {
    var tbl = document.getElementById('formtable');
    tbl.rows[ndisp+9].style.display = 'none';
    document.getElementById('child'+(ndisp)).value = '';
    document.getElementById('birth'+(ndisp)).value = 'mm/dd/yyyy';
    ndisp -= 1;
    if (ndisp == 0) {
     document.getElementById('remove').style.display = 'none';
    } else if (ndisp == 4) {
     document.getElementById('add').style.display = '';
    }
   }
   function entertext(id) {
    var e = document.getElementById(id);
    es = e.className;
    if (/ inactive/.test(es)) {
     e.className = es.replace(/ inactive/g,' active');
     e.value = '';
    }
   }
   function exittext(id) {
    var e = document.getElementById(id);
    var val = e.value;
    if (/^(\s*)$/.test(val)) {
     e.className = e.className.replace(/ active/g,' inactive');
     e.value = e.getAttribute('ghost');
    }
   }
   function initialfields() {
    var e = document.getElementById('entry');
    for (var i=0;i<e.length;i++) {
     if (e[i].id) {
      var val = e[i].value;
      es = e[i].className;
      if ((/^(\s*)$/.test(val) || val == e[i].getAttribute('ghost')) && !/child/.test(e[i].id)) {
       e[i].className = es.replace(/ active/g,' inactive');
       e[i].value = e[i].getAttribute('ghost');
      } else
       e[i].className = es.replace(/ inactive/g,' active')
     }
    }
    var tbl = document.getElementById('formtable');
    for (ndisp=5;ndisp>0;ndisp--) {
     var c = document.getElementById('child'+ndisp);
     var d = document.getElementById('birth'+ndisp);
     if (!(/^(\s*)$/.test(c.value) && d.value == d.getAttribute('ghost'))) {
      for (j=ndisp;j>0;j--)
       tbl.rows[j+9].style.display = '';
      break;
     }
    }
    if (ndisp == 5)
     document.getElementById('add').style.display = 'none';
    else if (ndisp > 0)
     document.getElementById('remove').style.display = '';
    else if (ndisp == 0)
     document.getElementById('remove').style.display = 'none';
    else if (ndisp < 5)
     document.getElementById('add').style.display = '';
   }
   function clearfields() {
    var e = document.getElementById('entry');
    for (var i=0;i<e.length;i++) if (/ inactive/.test(e[i].className)) e[i].value = '';
   }
   function toggle(str) {
    toggleCol(str+'1');
    toggleCol(str+'2');
    e = document.getElementById('visible-'+str);
    if (e.value == 'True') {
     e.value = 'False';
     for (var i=0;i<%(number)s;i++) {
      td = document.getElementById('cell-'+str+i);
      inp = document.getElementById('input-'+str+i);
      if (inp.type == 'checkbox') {
       if (inp.checked) var ischecked = ' checked';
       else var ischecked = '';
       td.innerHTML = '<input type="checkbox" disabled'+ischecked+'>';
      } else if (str == 'cern')
       td.innerHTML = inp.value.replace(/^\s+|\s+$/g,'');
      else td.innerHTML = inp.value.replace(/^\s+|\s+$/g,'').replace(/\\n/g,', ').replace(/\\r/g,'');
     }
    }
    else e.value = 'True';
   }
   function toggleCol(strCol) {
    var tds = document.getElementsByTagName("td");
    for (var idx in tds) {
     if (new RegExp(' '+strCol,'').test(tds[idx].className))
      if (tds[idx].style.display == "none")
       tds[idx].style.display = "";
     else
      tds[idx].style.display = "none";
    }
   }
   function addentry() {
    document.getElementById('entrydiv').style.display = '';
    document.getElementById('tablediv').style.display = 'none';
   }
   function sendemail() {
    document.getElementById('emaildiv').style.display = '';
    document.getElementById('tablediv').style.display = 'none';
    var to = document.email.to;
    var cc = document.email.cc;
    var bcc = document.email.bcc;
    to.value = '"%(mitname)s" <%(mitemail)s>';
    cc.value = '';
    bcc.value = '';
    for (var i=0;i<%(number)s;i++) {
     if (eval('document.table.check'+i).checked) {
      bcc.value += eval('document.table.email'+i).value+', ';
      var addemail = eval('document.table.addemail'+i).value.replace(/^\s+|\s+$/g,'');
      if (addemail != '')
       bcc.value += addemail.replace(/\\n/g,', ')+', ';
     }
    }
   }
   function importcsv() {
    document.getElementById('importdiv').style.display = '';
    document.getElementById('tablediv').style.display = 'none';
   }
   function showtable() {
    document.getElementById('entrydiv').style.display = 'none';
    document.getElementById('emaildiv').style.display = 'none';
    document.getElementById('importdiv').style.display = 'none';
    document.getElementById('tablediv').style.display = '';
   }
   function selectall(checked) {
    for (var i=0;i<%(number)s;i++)
     eval('document.table.check'+i).checked = checked;
    for (var j=0;j<%(cnumber)s;j++)
     eval('document.table.allcheck'+j).checked = checked;
   }
  </script>
 </head>
 <body class="white" onload="initialfields()">
  <h3>
   Playroom Membership
   &#183; <a href="%(form)s">Playroom Application</a>
   &#183; <a href="%(main)s">Westgate Home</a>
  </h3>
  <div id="entrydiv" style="display:none">
   <a href="javascript:showtable()">Return to Table</a>
   <form method="post" action="%(add)s" id="entry" name="entry" onsubmit="clearfields()">
    <table class="wide" id="formtable">
     <tr>
      <td class="head top">Name</td>
      <td class="top"><input type="text" name="name" value="" ghost="" class="w314"></td>
     </tr>
     <tr>
      <td class="head">E-mail</td>
      <td><input type="text" name="email" value="" ghost="" class="w314"></td>
     </tr>
     <tr>
      <td class="head">MIT ID #</td>
      <td><input type="text" name="mid" ghost="" class="w314"></td>
     </tr>
     <tr>
      <td class="head">Spouse's name</td>
      <td><input type="text" name="spouse" id="spouse" class="w314 inactive" ghost="If applicable" onfocus="entertext(this.id)" onblur="exittext(this.id)"></td>
     </tr>
     <tr>
      <td class="head">Names of other caregivers</td>
      <td><textarea name="cares" class="w314 h3 inactive" id="cares" ghost="If applicable; separate multiple names by line breaks or commas" onfocus="entertext(this.id)" onblur="exittext(this.id)"></textarea></td>
     </tr>
     <tr>
      <td class="head">Additional e-mails</td>
      <td><textarea name="addemail" class="w314 h3 inactive" id="addemail" ghost="If applicable; separate multiple addresses by line breaks or commas" onfocus="entertext(this.id)" onblur="exittext(this.id)"></textarea></td>
     </tr>
     <tr>
      <td class="head">Apartment #</td>
      <td><input type="text" name="apt" ghost="" class="w314"></td>
     </tr>
     <tr>
      <td class="head">Phone #</td>
      <td><input type="text" name="phone" ghost="" class="w314"></td>
     </tr>
     <tr>
      <td class="head">Anticipated move-out date</td>
      <td><input type="text" name="move" id="move" class="w314 inactive" ghost="mm/dd/yyyy" onfocus="entertext(this.id)" onblur="exittext(this.id)"></td>
     </tr>
     <tr>
      <td class="head">Child's name</td>
      <td>
       <input type="text" name="fchild0" class="w180" ghost="" id="child0">
       <span class="head">Birthdate</span>
       <input type="text" name="fbirth0" class="w77 inactive" id="birth0" ghost="mm/dd/yyyy" onfocus="entertext(this.id)" onblur="exittext(this.id)">
      </td>
     </tr>
     <tr style="display:none">
      <td class="head">Child's name</td>
      <td>
       <input type="text" name="fchild1" class="w180" ghost="" id="child1">
       <span class="head">Birthdate</span>
       <input type="text" name="fbirth1" class="w77 inactive" id="birth1" ghost="mm/dd/yyyy" onfocus="entertext(this.id)" onblur="exittext(this.id)">
      </td>
     </tr>
     <tr style="display:none">
      <td class="head">Child's name</td>
      <td>
       <input type="text" name="fchild2" class="w180" ghost="" id="child2">
       <span class="head">Birthdate</span>
       <input type="text" name="fbirth2" class="w77 inactive" id="birth2" ghost="mm/dd/yyyy" onfocus="entertext(this.id)" onblur="exittext(this.id)" class="inactive">
      </td>
     </tr>
     <tr style="display:none">
      <td class="head">Child's name</td>
      <td>
       <input type="text" name="fchild3" class="w180" ghost="" id="child3">
       <span class="head">Birthdate</span>
       <input type="text" name="fbirth3" class="w77 inactive" id="birth3" ghost="mm/dd/yyyy" onfocus="entertext(this.id)" onblur="exittext(this.id)">
      </td>
     </tr>
     <tr style="display:none">
      <td class="head">Child's name</td>
      <td>
       <input type="text" name="fchild4" class="w180" ghost="" id="child4">
       <span class="head">Birthdate</span>
       <input type="text" name="fbirth4" class="w77 inactive" id="birth4" ghost="mm/dd/yyyy" onfocus="entertext(this.id)" onblur="exittext(this.id)">
      </td>
     </tr>
     <tr style="display:none">
      <td class="head">Child's name</td>
      <td>
       <input type="text" name="fchild5" class="w180" ghost="" id="child5">
       <span class="head">Birthdate</span>
       <input type="text" name="fbirth5" class="w77 inactive" id="birth5" ghost="mm/dd/yyyy" onfocus="entertext(this.id)" onblur="exittext(this.id)">
      </td>
     </tr>
     <tr>
      <td></td>
      <td>
       <span id="add"><a href="javascript:add();">Add Child</a></span>
       <span id="remove"><a href="javascript:remove();">Remove Child</a></span>
      </td>
     </tr>
     <tr>
      <td class="head">Special concerns</td>
      <td><textarea name="cern" ghost="" class="h3 w314"></textarea></td>
     </tr>
     <tr>
      <td class="head">Registration Date</td>
      <td><input type="text" name="reg" id="reg" class="w314 inactive" ghost="mm/dd/yyyy" onfocus="entertext(this.id)" onblur="exittext(this.id)"></td>
     </tr>
     <tr>
      <td class="head">Expiration Date</td>
      <td><input type="text" name="expire" id="expire" class="w314 inactive" ghost="mm/dd/yyyy" onfocus="entertext(this.id)" onblur="exittext(this.id)"></td>
     </tr>
     <tr>
      <td class="head">Paid</td>
      <td><input type="checkbox" name="paid" value="True"></td>
     </tr>
     <tr>
      <td class="head">Key Given</td>
      <td><input type="checkbox" name="keygive" value="True"></td>
     </tr>
     <tr>
      <td class="head">Key Returned</td>
      <td><input type="checkbox" name="keyret" value="True"></td>
     </tr>
     <tr>
      <td class="head">MIT Name</td>
      <td><input type="text" name="mitname" value="" ghost="" class="w314"></td>
     </tr>
     <tr>
      <td class="head">MIT E-mail</td>
      <td><input type="text" name="mitemail" value="" ghost="" class="w314"></td>
     </tr>
     <tr>
      <td class="head">Terms and conditions</td>
      <td><input type="checkbox" name="agree" value="True"></td>
     </tr>
     <tr>
      <td class="head">Liability waiver</td>
      <td><input type="checkbox" name="liability" value="True"></td>
     </tr>
     <tr>
      <td class="bottom"></td>
      <td class="bottom">
       <div class="submit">
        <input type="submit" value="Submit">
       </div>
      </td>
     </tr>
    </table>
   </form>
  </div>
  <div id="tablediv">
   <a href="javascript:addentry()">Add Entry</a>
   <a href="javascript:sendemail()">E-mail Selected</a>
   <a href="javascript:deleteselected()">Delete Selected</a>
   <a href="javascript:importcsv()">Import CSV</a>
   <a href="%(csv)s">Export CSV</a>
   <form method="post" action="%(update)s" id="table" name="table">
    <table class="db wide" id="dbtable">
%(header)s
%(body)s
     <tr>
      <td class="bottom" colspan="44">
       <div class="submit">
        <input type="hidden" name="number" value="%(number)s">
        <input type="submit" value="Finalize Changes" ghost="">
       </div>
      </td>
    </table>
   </form>
  </div>
  <div id="emaildiv" style="display:none">
   <a href="javascript:showtable()">Return to Table</a>
   <form method="post" action="%(email)s" name="email">
    <table class="wide">
     <tr>
       <td class="head lead">From</td>
       <td class="lead">"%(mitname)s" &#60;%(mitemail)s&#62;</td>
     </tr>
     <tr>
      <td class="head">To</td>
      <td><textarea name="to" class="h3 w510"></textarea></td>
     </tr>
     <tr>
      <td class="head">Cc</td>
      <td><textarea name="cc" class="h3 w510"></textarea></td>
     </tr>
     <tr>
      <td class="head">Bcc</td>
      <td><textarea name="bcc" class="h3 w510"></textarea></td>
     </tr>
     <tr>
      <td class="head">Subject</td>
      <td><input type="text" name="subject" class="w510"></td>
     <tr>
      <td class="head">Text</td>
      <td><textarea name="text" class="h12 w510"></textarea></td>
     </tr>
     <tr>
      <td class="bottom"></td>
      <td class="bottom">
       <div class="submit">
        <input type="submit" value="Submit">
       </div>
      </td>
     </tr>
    </table>
   </form>
  </div>
  <div id="importdiv" style="display:none">
   <a href="javascript:showtable()">Return to Table</a>
   <form action="%(import)s" method="post">
    <table class="wide">
     <tr>
      <td class="head lead">Import CSV</td>
      <td class="lead"><textarea name="import" class="h12 w510"></textarea></td>
     </tr>
     <tr>
      <td></td>
      <td>
       <div class="submit">
        <input type="submit" value="Submit">
       </div>
      </td>
     </tr>
     <tr>
      <td class="bottom"></td>
      <td class="bottom">
       <p class="w510">
        Paste your CSV file above. The first row must be a header row in the form
       </p>
       <p class="w510">
        "Name, E-mail, ID, Spouse, Caregiver 1, Caregiver 2,...Caregiver
        <em>M</em>, Other E-mails 1, Other E-mails 2,...Other E-mails
        <em>N</em>, Apt, Phone, Depart, Child 1, Child 2,...Child <em>P</em>,
        Birthdate 1, Birthdate 2,...Birthdate <em>P</em>, Concerns, Registered,
        Expires, Paid, Key Given, Key Returned, MIT Name, MIT E-mail, Terms,
        Liability"
       </p>
       <p class="w510">
        where <em>M</em> is the maximum number of caregivers in any single
        entry across those you importing, <em>N</em> similarly is the maximum
        number of additional e-mails, and <em>P</em> is the maximum number of
        children (and birthdates).
       </p>
      </td>
     </tr>
    </table>
   </form>
  </div>
  <div class="footerwide">
   Questions or comments? Bugs? Contact the Parents' Resource
   Coordinators at <a href="mailto:westgate-prc@mit.edu">westgate-prc@mit.edu</a>.
  </div>
 </body>
</html>
""" % {'css':lib.css,'header':header % {'lead':'lead ','icheck':'0'}, \
       'body':body,'csv':lib.csv, 'update':lib.update,'add':lib.add, \
       'number':len(db),'email':lib.email,'import':lib.importcsv, \
       'mitname':mitname,'mitemail':mitemail,'cnumber':len(db)/freq+1, \
       'freq':freq,'main':lib.main,'form':lib.form,'table':lib.table}
