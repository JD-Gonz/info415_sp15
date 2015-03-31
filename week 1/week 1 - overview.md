```
 _       __          __      ___
| |     / /__  ___  / /__   <  /
| | /| / / _ \/ _ \/ //_/   / / 
| |/ |/ /  __/  __/ ,<     / /  
|__/|__/\___/\___/_/|_|   /_/   
```                             

## Week 1
### Tuesday
- who I am and what I do
	- Andrew McKenna
	- iSchool 2012 graduate; also have a degree in political science
	- worked at Boeing for a year as a developer; did some security work (mobile and web)
	- work at Security Innovation (just over two years now)
		- web applicaiton security
		- thick client reversing
		- attach simulations
		- research: locks, nfc, more to come
	- no on knows everything, even me
	- I will be working full time during this quarter
- teaching methodology
	- here to teach and share knowlege
	- was in college a few years ago, I remember how it is
	- if you have a ton of projects or stuff all lining up, let me know
	- everyone gets 4 late days to use
	- late penalty: 10% daily, stops at 50% deduction
	- grading
		- midterm: 25%
		- final: 15%
		- hw: 60%
	- ask me aboust unrelated security topics
- class overview
	- go over weekly schedule
- github
	- we will use github for class materials
	- file issues, enhancements, question
	- use github to build and display your work
	- catalyst to turn in work
- where web application security fits into information security
	- malware analysis
	- network & infrastructure
	- application security
	- physical security
	- policy & compliance
	- exploit development
	- forensics
- online resources for security in general
	- slides and demo
- bug bounties
	- bugcrowd.com
	- hackerone.com
	- bonus points if you find/writeup bug bounty
- responsible disclosure
	- no full disclosure
	- legal implications of finding vulns
	- be careful for what you look for and how
- general tips and tricks
	- stay away from automated tools
	- keep your eyes open
	- send bad input
	- come up with favorite testing payloads
	- develop an "eye" for it
- books
	- Web Application Hacker's Handbook
	- Browser Hacker's Handbook
	- Tangled Web
	- A Bug Hunter's Diary
	- Hacking: The Art of Exploitation
- anatomy of a web application
	- frontend
		- content delivered to client
		- html, javascript, css
		- ajax
	- middle layer
		- PHP, Python, RoR, Node, ASP.NET
		- pages are dynamically generated
		- requests parameters are parsed 
	- database
		- MySQL, MSSQL, postgresql, sqlite
		- direct queries or through ORM
	- cookies
		- session management
		- sent with every request
		- essentially an ID badge
		- demo a session hijack w/ student
- lay of the web application land
	- web 2.0 hotness
		- way more happening clientside 
		- lots of ajax
		- lots of moving parts
		- interfacing with host system more
		- increase reliance on 3rd party code
	- MVC
		- sites are moving to this style framework
	- HTML5
		- codifying things that were being hacked together now
		- more vulnerabilities (somewhat)
		- the web is taking over the desktop
		- this is the future
- threat modeling (pdf)
	- get example document
	- read docs, figure out how app works
	- watch how data moves
	- define user roles
	- define assets
	- define components
	- access matrix
	- component diagram
	- threat tree
- typical pentest
	- walk through 2 week pentest schedule
	- 2 days for overview, threat model, initial poke around
	- build test plan
	- go through test cases, explore app and functionality
	- document as you find things!
	- 2 days for documentation

### Wednesday
- tools setup
	- interception proxies
		- tamper data
		- burp
		- fiddler
		- MITM and Certs
		- watching reqeusts
	- packet capture
		- tcpdump
		- wireshark
- capturing traffic
	- how to look at traffic
	- how to edit traffic
	- replaying requests

### Thursday
- how the internet works (slides)
	- OSI & TCP/IP models
	- DNS
	- DHCP
	- routing
	- SSL/TLS
	- HTTP
	- CAs
	- 2FA
- how HTTP works
- how a browser works
- puzzle

### Homework
- required: 
	- none
- recommended:
	- read WAHH chapter 12
	- read WAHH chapter 3
