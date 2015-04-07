```
    _____   ____________     __ __ _________
   /  _/ | / / ____/ __ \   / // /<  / ____/
   / //  |/ / /_  / / / /  / // /_/ /___ \  
 _/ // /|  / __/ / /_/ /  /__  __/ /___/ /  
/___/_/ |_/_/    \____/     /_/ /_/_____/  
    --- Web Application Security ---       

``` 

# Description
This course will cover the ins and outs of web application security from the perspectives of the developer, administrator, and attacker. We will cover attacks from the all too common Cross-Site Scripting (XSS) attack through Cross-Site Request Forgery (CSRF), SQL Injection (SQLi), all the way to more advanced topics such as hash length extension attacks, cookie tossing, deserialization, and specialized vulnerabilities against common web frameworks.
 
The goals of this course center around familiarizing students with how to recognize a possible vulnerability, write a proof-of-concept, and provide helpful remediation so that a developer can properly mitigate the issue. The emphasis will be on hands-on learning and the students will be expected to think creatively as they face common defenses and work with unfamiliar frameworks and languages.

# Grading
Grade breakdown:
- midterm: 25%
- final: 15%
- hw: 60%

Late penalty: 
- 10% daily (24hrs from time due)
- stops at 50% deduction
- 4 late days to use				

# Resources
- Bitsync key: BVJ3RLXHMCWW5AFAVNMB4RRVOLWW72UD7  
- Suggested reading: Web Application Hacker's Handbook                                          

# Weekly Schedule

## Week 1 - Foundations (March 30 to April 3)
### Tuesday
- introduction
- class overview
- threat modeling

### Wednesday
- tools setup
- capturing traffic

### Thursday
- how the internet works
- client to server communications
- browser basics

### Homework
- required
	- none
- recommended
	- read WAHH chapter 12
	- read WAHH chapter 3


## Week 2 - XSS (April 6 to 10)
### Tuesday
- cross-site scripting (XSS)
	- how it works
	- why it's so common
	- why it's bad
	- how to find it
	- how to mitigate
- reflective XSS
- stored XSS
- DOM XSS
- XSS demos

### Wednesday
- character encoding
- unicode security
- punycode domains

### Thursday
- filter bypass techniques
	- no spaces (encoding and slashes)
	- no script tag
	- XSS via images
	- encoding galore
	- other weirdness
- do stuff
	- filter bypassing

### Homework
- required
	- XSS challenges
	- pentest report
	- due next thursday


## Week 3 - XSS (April 13 to 17)
### Tuesday
- advanced payloads
	- exfiltrating cookies
	- inducing user action
	- fake login forms

### Wednesday
- regular expressions

### Thursday
- go over homework
- BeEF framework
- client-side exploits

### Homework
- required
	- special XSS payloads
- recommended
	- reading on CSRF and Clickjacking
		- WAHH Chapter 13 section on "Inducing User Action" (501-515)
		- http://www.troyhunt.com/2013/05/clickjack-attack-hidden-threat-right-in.html


## Week 4 - CSRF & Clickjacking (April 20 to 24)
### Tuesday
- CSRF
	- how it works
	- why it's bad
	- how to find it
	- how to mitigate
- CSRF examples
	- demo CSRF

### Wednesday
- how Tor works

### Thursday
- go over homework
- Clickjacking
	- how it works
	- why it's bad
	- how to mitigate
	- special tactics

### Homework
- required
	- CSRF challenges
	- clickjacking challenges
	- pentest report
	- due next thursday
- recommended
	- read WAHH chapter 9


## Week 5 - SQLi (April 27 to May 2)
### Tuesday
- SQL injection
	- how it works
	- why it's bad
	- how to find it
	- how to mitigate
	- how to pull data
	- special tactics
- SQLi demos

### Wednesday
- buffer overflows

### Thursday
- SQL practice

### Homework
- required
	- SQL injection challenges
	- pentest report
	- due next thursday


## Week 6 - SQLi (May 4 to 8)
### Tuesday
- Advanced SQL injection techniques

### Wednesday
- lockpicking
	- slides
	- https://www.youtube.com/watch?v=ChbyaXBKNY8

### Thursday
- Hibernation attacks

### Homework
- required
	- advanced SQL challenges
	- pentest report
	- due next thursday
- recommended
	- read WAHH chapter 6
	- read WAHH chapter 7


## Week 7 - Authentication (May 11 to 15)
### Tuesday
- session fixation
- session invalidation issues

### Wednesday
- metasploit

### Thursday
- authentication 2.0
	- 2 factor auth
	- single signon
	- cookie tossing

### Homework
required
	- midterm
	- due next tuesday


## Week 8 - Crypto (May 18 to 22)
### Tuesday
- cryptography
	- public/private key
	- forward secrecy
	- hashes
	- stream vs block cipher
	- algorithm modes: ECB, CBC, others

### Wednesday
- keyloggers

### Thursday
- authentication
	- walk through typical auth scheme
	- password hashing
	- set cookie
	- attacks
- info leakage
- cookie entropy
- cookie settings
- ssl scan

### Homework
required
	- crypto challenges
	- pentest report
	- due next thursday
recommended
	- read WAHH Chapter 10 section "Manipulating File Paths"
	- read WAHH Chapter 11 section "Example 12: Racing Against the Login"

## Week 9 - Advanced (May 25 to 29)
### Tuesday
- remote file inclusion (RFI)
- local file inclusion (LFI)

### Wednesday
- bitcoin

### Thursday
- tricking password managers
- race conditions

### Homework
required
	- adnvanced vulnerability challenges 
		- LFI challenges
		- race condition challenge
		- tricking a password manager


## Week 10 - Advanced (June 1 to 5)
### Tuesday
- mass assignment attacks
- deserialization attacks

### Wednesday
- online challenges

### Thursday
- review

### Homework
- final


## Final - no final during finals week, enjoy your summer!