## CSRF Homework Grading (20 points total)
Homework challenges can be found at: http://csrf-challenges.r7.io/

## Part 1 - Vulnerabilities 12 points
- Level 1 will be worth 2 points
- Level 2 will be worth 4 points 
- Level 3 will be worth 6 points

To earn full points on each challenge you must craft a webpage (for levels 1 & 2) and a link with an XSS payload (for level 3) that when the Admin goes to that page/link, it stealthily makes a post to the corresponding admin post page. This post MUST contain your full UW email.

Example: You create a webpage for Level 1 that I (as the admin) will open. This webpage needs to automatically submit a request in order to make a post to the Level 1 post page on http://csrf-challenges.r7.io. This post is made on behalf of the Admin without them knowing. Make sure to put your full UW email in the contents of the post so I can easily verify you.

TL;DR - for 100% you must turn in 2 pages and a URL/link that when clicked on by the admin a post will be submitted to their respective post page (level 1 to level 1 post page, level 2 to level 2 post page, etc). Be sure to include your full UW email in the contents of the post.

## Part 2 - The Report 8 points
- Description (1 point)
- Test Steps (4 points)
	- 2 sets of test steps, for the top 2 you solved, that include how you found the vulnerability and how it works.
	- This should be detailed enough that someone in the class who didn't solve the challenges could walk through the steps, be able to reproduce the vulnerabilities, know how they worked, and why they happened.
- Mitigations (3 points)
	- Give mitigation recommendations for 2 languages/frameworks
		- ASP.NET
		- Django
	- This should include a few sentences about how to properly mitigate CSRF and a code example for each framework/language
	- Include a link or two to further reading/reference for the "developer"

## Deliverables
A .zip file containing the following:

1. An HTML file that opens in Firefox and triggers the CSRF attack against lvl 1 and make a post on the lvl 1 wall.
2. An HTML file that opens in Firefox and triggers the CSRF attack against lvl 2 and make a post on the lvl 2 wall.
3. A .txt file containing a URL that I can copy and paste into Firefox that will trigger an attack against lvl 3 and make a post on the lvl 3 wall.

## Due Date
You can submit your malicious pages and link to me on Monday April 27nd by 5:30pm (17:30) via email and I will run them. This will allow you to verify whether your CSRF attacks worked, and if they didn't work, give you a few days to tweak them.

The whole HW (vulnerabilities and report) are due at 3:30pm (15:30) Thursday April 30th 2014

## Notes & Hints
Submit forms, even if you are not authenticated, and intercept the requests with Burp. This can give you a look at what is being sent to the server, so you can re-create that request in your malicious page.

Please include links to any pages, guides, tutorials, people, or anything you used to help you figure out these challenges. Please do not cheat or trade answers! If you gently/fairly help one another out make sure to credit the people that helped you in your report. Give credit where credit is due.

No automated tools!

## Resources
http://www.troyhunt.com/2010/11/owasp-top-10-for-net-developers-part-5.html
https://www.owasp.org/index.php/Testing_for_CSRF_(OWASP-SM-005)