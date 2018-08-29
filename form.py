#!/usr/bin/python

import cgitb;cgitb.enable()
import lib

mitname,mitemail = lib.GetUserCert()

if not mitname:
    print 'Content-type: text/html'
    print
    print lib.nocert
else:
    print 'Content-type: text/html'
    print
    print \
"""
<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01//EN" "http://www.w3.org/TR/html4/strict.dtd">
<html>
 <head>
  <title>Playroom Application</title>
  <link rel="stylesheet" href="%(css)s" type="text/css">
  <script language="javascript" type="text/javascript">
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
    var e = document.getElementById('form');
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
    var e = document.getElementById('form');
    for (var i=0;i<e.length;i++) if (/ inactive/.test(e[i].className)) e[i].value = '';
   }
  </script>
 </head>
 <body onload="initialfields()">
  <div id="main">
   <h3>
    <p class="left">
     Playroom Application &#183; <a href="%(main)s">Westgate Home</a>
    </p>
    <p class="right"><a href="%(table)s">Admin</a></p>
    <div class="clear"></div>
   </h3>
   <hr>
   <form action="%(process)s" method="post" onsubmit="clearfields()" id="form">
    <table id="formtable">
     <tr>
      <td class="head">Name</td>
      <td><input type="text" name="name" value="%(name)s" class="w314"></td>
     </tr>
     <tr>
      <td class="head">E-mail</td>
      <td><input type="text" name="email" value="%(email)s" class="w314"></td>
     </tr>
     <tr>
      <td class="head">MIT ID #</td>
      <td><input type="text" name="mid" class="w314"></td>
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
      <td><textarea name="addemail" class="h3 w314 inactive" id="addemail" ghost="If applicable; separate multiple addresses by line breaks or commas" onfocus="entertext(this.id)" onblur="exittext(this.id)"></textarea></td>
     </tr>
     <tr>
      <td class="head">Apartment #</td>
      <td><input type="text" name="apt" class="w314"></td>
     </tr>
     <tr>
      <td class="head">Phone #</td>
      <td><input type="text" name="phone" class="w314"></td>
     </tr>
     <tr>
      <td class="head">Anticipated move-out date</td>
      <td><input type="text" name="move" id="move" class="w314 inactive" ghost="mm/dd/yyyy" onfocus="entertext(this.id)" onblur="exittext(this.id)"></td>
     </tr>
     <tr>
      <td class="head">Child's name</td>
      <td>
       <input type="text" name="child0" class="w180" id="child0">
       <span class="head">Birthdate</span>
       <input type="text" name="birth0" class="w77 inactive" id="birth0" ghost="mm/dd/yyyy" onfocus="entertext(this.id)" onblur="exittext(this.id)">
      </td>
     </tr>
     <tr style="display:none">
      <td class="head">Child's name</td>
      <td>
       <input type="text" name="child1" class="w180" id="child1">
       <span class="head">Birthdate</span>
       <input type="text" name="birth1" class="w77 inactive" id="birth1" ghost="mm/dd/yyyy" onfocus="entertext(this.id)" onblur="exittext(this.id)">
      </td>
     </tr>
     <tr style="display:none">
      <td class="head">Child's name</td>
      <td>
       <input type="text" name="child2" class="w180" id="child2">
       <span class="head">Birthdate</span>
       <input type="text" name="birth2" class="w77 inactive" id="birth2" ghost="mm/dd/yyyy" onfocus="entertext(this.id)" onblur="exittext(this.id)">
      </td>
     </tr>
     <tr style="display:none">
      <td class="head">Child's name</td>
      <td>
       <input type="text" name="child3" class="w180" id="child3">
       <span class="head">Birthdate</span>
       <input type="text" name="birth3" class="w77 inactive" id="birth3" ghost="mm/dd/yyyy" onfocus="entertext(this.id)" onblur="exittext(this.id)">
      </td>
     </tr>
     <tr style="display:none">
      <td class="head">Child's name</td>
      <td>
       <input type="text" name="child4" class="w180" id="child4">
       <span class="head">Birthdate</span>
       <input type="text" name="birth4" class="w77 inactive" id="birth4" ghost="mm/dd/yyyy" onfocus="entertext(this.id)" onblur="exittext(this.id)">
      </td>
     </tr>
     <tr style="display:none">
      <td class="head">Child's name</td>
      <td>
       <input type="text" name="child5" class="w180" id="child5">
       <span class="head">Birthdate</span>
       <input type="text" name="birth5" class="w77 inactive" id="birth5" ghost="mm/dd/yyyy" onfocus="entertext(this.id)" onblur="exittext(this.id)">
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
      <td><textarea name="cern" class="w314 h3"></textarea></td>
     </tr>
     <tr>
      <td class="head"><input type="checkbox" name="agree" value="True"></td>
      <td>
       <div class="w320">
        I have read the <a href="%(terms)s">Westgate Playroom Policy</a>
        and I agree to it on behalf of myself, my family, caretakers, and
        guests with full responsibility. This includes agreeing to cleaning the playroom for one session during the year under penalty of a $30 fine on my student account.
       </div>
      </td>
     </tr>
     <tr>
      <td class="head"><input type="checkbox" name="liability" value="True"></td>
      <td>
       <div class="w320">
        I have read the <a href="%(liability)s">Westgate Playroom
        Liability Release</a> and I agree to be legally bound by it.
       </div>
      </td>
     </tr>
     <tr>
      <td></td>
      <td>
       <div class="submit">
        <input type="submit" value="Submit">
       </div>
      </td>
     </tr>
    </table>
   </form>
   <hr>
   <div class="footer">
    Questions or comments? Bugs? Contact the Parents' Resource
    Coordinators at <a href="mailto:westgate-prc@mit.edu">westgate-prc@mit.edu</a>.
   </div>
  </div>
 </body>
</html>
""" % {'css':lib.css,'name':mitname,'email':mitemail.lower(), \
       'process':lib.process,'terms':lib.terms,'liability':lib.liability, \
       'table':lib.table,'main':lib.main}
