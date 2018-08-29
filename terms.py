#!/usr/bin/python

import cgitb;cgitb.enable()
import lib

mitname,mitemail = lib.GetUserCert()
if not mitname:
    print 'Content-type: text/html'
    print
    print lib.nocert
else:
    visits = lib.UpdateVisits(lib.tvisit,mitemail)
    print 'Content-type: text/html'
    print
    print \
"""
<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01//EN" "http://www.w3.org/TR/html4/strict.dtd">
<html>
 <head>
  <title>Westgate Playroom Policy</title>
  <link rel="stylesheet" href="%(css)s" type="text/css">
 </head>
 <body>
  <div id="main">
   <h3>
    Westgate Playroom Policy
    &#183; <a href="%(form)s">Playroom Application</a>
    &#183; <a href="%(main)s">Westgate Home</a>
   </h3>
   <hr>
   <p>
    Welcome to the Westgate playroom community! This community consists of
    resident parents, caretakers, and children who work together to provide
    a safe and fun place for our children to meet and play. We have created
    these guidelines to help ensure that the playroom remains a safe and fun
    place. Please set a good example and encourage other members of the
    community to follow the rules. Feel free to contact the Westgate Parent
    Resource Coordinators (PRCs) with any questions regarding playroom rules
    or membership policies.
   </p>
   <h4>Membership Eligibility</h4>
   Any resident of Westgate with children is eligible to be a member. We
   encourage you to get to know other members and build friendships and
   networks that will enhance your family's time at MIT. Members must also
   sign a liability release form. <strong>The current membership fee is
   $10.</strong>
<h4>Cleaning Policy</h4>
To keep the playroom clean and organized for all members and their children, we require that you agree to participate in one cleaning session during the year. Children are not allowed during the cleaning time, just one adult per family. Cleaning materials will be supplied. The schedules for the cleaning days are Saturdays from 9:00 am to 10:30 am. <strong> If you do not attend the session you previously agreed on, a $30 fine will be charged on your student account. </strong> After the Westgate PRCs receive your payment, you will be able to choose one date that works best for you. Time slots are assigned on "first-come-first-served" basis.   
   <h4>Rules and Guidelines</h4>
   If you are caught breaking the rules you will get a warning. If you are
   caught a second time you will be asked to forfeit your privileges
   temporarily and if you are caught a third time you will forfeit your use
   of the playroom for the remainder of the year without a refund of your
   money.
   <ol>
    <li>
     <strong>Always CLEAN UP after yourself and your child.</strong> Members
     are expected to assist in cleaning the playroom. Take good care of the
     toys and furniture. Please return toys to their place when you are done
     using the playroom. Memberes must not only clean up after each visit to
     the playroom, but are also expected to attend quarterly (every 3 months)
     deep cleanings.
    </li>
    <li>
     <strong>Children MUST be accompanied by an adult while in the
     playroom.</strong> Any child unsupervised by an adult will be asked to
     leave. Please watch your children carefully to avoid any injury or broken
     toys. Please do not sleep or be otherwise inattentive in the playroom. If
     your family has a caregiver who will be taking your children to the
     playroom you must inform the PRC of the caregiver's name so she/he can be
     added to the Playroom Community list. You, as the member, have full
     responsibility for the actions of the caregiver and any guests in the
     playroom. One adult may be responsible for no more than five children.
    </li>
    <li>
     <strong>Do not use the playroom when SICK.</strong> Remember that it is
     easy for infection to spread in a playroom where so many children play.
    </li>
    <li>
     <strong>No FOOD or DRINKS</strong> are allowed in the playroom except
     drinks in sippy cups.
    </li>
    <li>
     <strong>Remove your shoes</strong> and put them in the shoe compartment
     next to the door. We want to keep our carpets clean. If you bring a
     stroller, please park it outside the playroom or collapse it and store it
     out of the way of the play area.
    </li>
    <li>
     <strong>Please turn off the LIGHTS</strong> (and the air conditioner) if
     you are the last to leave.
    </li>
    <li>
     <strong>The playroom is a CO-OP.</strong> Please respect the concerns of
     other members: do not allow entry to people without ID access and always make
     sure the door is closed to prevent the use of the playroom by
     non-members.
    </li>
    <li>
     Each year members must <strong>renew their membership</strong>. If you move
     out earlier, we do not refund the membership fee. All of the ID cards providing 
     access are deleted at the start of the new school year and once the new application, fee and 
     clearning date is selected the membership is renewed. 
    </li>
   </ol>
   <hr>
   <div class="footer">
    Questions or comments? Bugs? Contact the Parents' Resource
    Coordinators at <a href="mailto:westgate-prc@mit.edu">westgate-prc@mit.edu</a>.
   </div>
  </div>
 </body>
</html>
""" % {'css':lib.css,'form':lib.form,'main':lib.main}
