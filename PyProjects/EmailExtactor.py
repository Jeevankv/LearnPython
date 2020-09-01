import re
txt='''JSSAJDTCNBAERP LOGINJSSATEB IRINSMOODLEJSSATEB VIDEOALUMNIJSS MAHAVIDYAPEETHASUTTUR KSHETRACONTACT US
JSSATE Bengaluru
Your Keyword...


Admissions open for 2020-2021 for B.E. and MBA. For further details Contact : Off: 080 - 2861 2565, 2861 1702, Principal: +91 96866 77259, Administrative officer: +91 99009 28583
AboutAdmissionAcademicsResearchCampus LifeJSSATEB STEPOnline Fee
CONTACT US
JSS Academy of Technical Education > Contact Us
jssate-bengaluru
JSSATE-B Campus,
Uttarahalli-Kengeri Road,
Bengaluru – 560 060

Ph: 080 – 2861 2565, 28612565,  2861 1702
Fax: 080 – 2861 2706 / 2861 2646
E-Mail: info@jssateb.ac.in
Website: www.jssateb.ac.in


Introduction
Departments
Placements
Committee
Mandatory Disclosure
DOWNLOADS
JSS ATE Forms, Stationaries,
Brochures, etc...

PLACEMENTS
Placement Statistics. Placed Students
& Companies..,

PHOTO GALLERY
View JSS ATE event photos
and galleries...

ABOUT JSSATE
Organization
About JSSATE
Governing Council
Principal’s Desk
Dean Research
Dean Student Welfare
Centre of Excellence
QUICK LINKS
Faculty List Of All Dept
JSSATE Service Rules
NIRF Details
Audit Reports
Library
Events
EDC
Facility
NSS
Short Video on JSSATEB
Committee
VERVE
Constitution Day Celebration 2019
PLACEMENTS
Placements
Campus Placement
Additional Placements
INSIGHTS
Admission
All Departments
Research
Centre of Excellence
Green Campus
CONTACT US
JSS Academy of Technical Education, Bengaluru
JSSATE-B Campus,
Uttarahalli-Kengeri Road, Bengaluru – 560 060
Ph: 080 - 2861 2565, 2861 1702
Fax: 080-2861 2706/2861 2646
E-Mail: info@jssateb.ac.in
Website: www.jssateb.ac.in

ABOUT BANGALORE
South India's most alive city, there are no outsiders in Bangalore. A melting point of ethnic and cultural backgrounds, the hoi polloi of Bangalore is charmingly mixed.

READ MORESTAY CONNECTED : 
Copyright©2020 JSSATE Bengaluru, All Rights Reserved. Powered by Dept. of CSE/ISE, Site Last Updated on 03/03/2020Back To Top
Hey!How can I Help?
'''
if __name__ == '__main__':

    regex = re.compile(r"\w+[@][.]?\w+[.]?\w+")
    match = regex.findall(txt)
    print(set(match))

    with open("email.txt","a") as f:
        for index,value in enumerate(set(match),1):
            f.write(f"email {index} : {value}\n")
