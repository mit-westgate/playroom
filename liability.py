#!/usr/bin/python

import cgitb;cgitb.enable()
import lib

mitname,mitemail = lib.GetUserCert()
if not mitname:
    print 'Content-type: text/html'
    print
    print lib.nocert
else:
    visits = lib.UpdateVisits(lib.lvisit,mitemail)
    print 'Content-type: text/html'
    print
    print \
"""
<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01//EN" "http://www.w3.org/TR/html4/strict.dtd">
<html>
 <head>
  <title>Westgate Playroom Liability Release</title>
  <link rel="stylesheet" href="%(css)s" type="text/css">
 </head>
 <body>
  <div id="main">
   <h3>
    Westgate Playroom Liability Release
    &#183; <a href="%(form)s">Playroom Application</a>
    &#183; <a href="%(main)s">Westgate Home</a>
   </h3>
   <hr>
   <h3>Liability Release, Waiver, Discharge and Covenant Not to Sue</h3>
   <p>
    This is a legally binding Release, Waiver, Discharge and Covenant Not
    to Sue (collectively, "Release"), made voluntarily by me, the undersigned
    Releasor, on my own behalf, and on behalf of my heirs, executors,
    administrators, legal representatives and assigns (hereinafter collectively,
    "Releasor," "I" or "me", which terms shall also include Releasor's parents
    or guardian, if Releasor is under 18 years of age) to the Massachusetts
    Institute of Technology ("MIT").
   </p>
   <p>
    As the undersigned Releasor, I fully recognize that there are dangers and
    risks to which I may be exposed by participating in the Westgate Playroom
    Program (the "Activity"). As the undersigned Releasor, I understand
    that MIT does not require me to participate in this Activity, but I want to
    do so despite the possible dangers and risks and despite this Release. With
    informed consent, and for valuable consideration received, including
    assistance provided by MIT, as the undersigned Releasor, I agree to assume
    and take on myself all of the risks and responsibilities in any way arising
    from or associated with this Activity, and I release MIT and all of its
    affiliates, divisions, departments and other units, committees and groups,
    and its and their respective governing boards, officers, directors,
    principals, trustees, legal representatives, members, owners, employees,
    agents, administrators, assigns, and contractors (collectively "Releasees"),
    from any and all claims, demands, suits, judgments, damages, actions and
    liabilities of every name and nature whatsoever, whenever occurring, whether
    known or unknown, contingent or fixed, at law or in equity, that I may
    suffer at any time arising from or in connection with the Activity,
    including any injury or harm to me, my death, or damage to my property
    (collectively "Liabilities"), and I agree to defend, indemnify, and save
    Releasees harmless from and against any and all Liabilities.
   </p>
   <p>
    As the undersigned Releasor, I recognize that this Release means I am giving
    up, among other things, all rights to sue Releasees for injuries, damages
    or losses I may incur. I also understand that this Release binds my heirs,
    executors, administrators, legal representatives and assigns, as well as
    myself. I also affirm that I have adequate medical or health insurance to
    cover any medical assistance I may require.
   </p>
   <p>
    I agree that this Release shall be governed for all purposes by Massachusetts
    law, without regard to such law on choice of law.
   </p>
   <p>
    <strong>I have read this entire Release. I fully understand the entire
    Release and acknowledge that I have had the opportunity to review this
    Release with an attorney of my choosing if I so desire, and I agree to be
    legally bound by the Release.</strong>
   </p>
   <p>
    <strong>THIS IS A RELEASE OF YOUR RIGHTS, READ CAREFULLY AND UNDERSTAND
    BEFORE SIGNING.</strong>
   </p>
   <hr>
   <div class="footer">
    Questions or comments? Bugs? Contact the Parents' Resource
    Coordinators at <a href="mailto:westgate-prc@mit.edu">westgate-prc@mit.edu</a>.
   </div>
  </div>
 </body>
</html>
""" % {'css':lib.css,'form':lib.form,'main':lib.main}
