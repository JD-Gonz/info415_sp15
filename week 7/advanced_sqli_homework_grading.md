## Advanced SQLi HW Grading
Each of you will have your own seperate environment tied to your UW NetID.

To go to your individual challenges go to https://sqli.csuw.net/[netid]

Example: My UW NetID is amckenna (my email is amckenna@uw.edu) so I would go to: https://sqli.csuw.net/amckenna/

## Phase 1 - Initial Discovery (24 points)
There are 4 SQL injection vulnerabilities in the website. You must find each one and gather proof that you have in fact found a SQL injection vulnerability. This proof can be in the form of a copy of the Burp response from the server, a screenshot, a description of the server behavior, whatever you think is sufficient. Once you have gathered this proof you can email myself (amckenna@uw.edu) and CC the TA (shiji@uw.edu) with your proof and an explanation for why you think it is adequate proof of SQL injection - pretend we are a customer who owns the application and we have paid you to assess it.

If we feel that the proof is sufficient we will supply you with a snippit of code for that vulnerable area. You can use that code in Phase 2.

Note: Make sure you hold onto the proof because you will need to turn it in as a deliverable.

## Phase 2 - Full Exploitation (16 points)
Once you have the code snippit for the vulnerable functionality you will build an exploit that shows how bad the vulnerability is. This exploit will need to either abuse the vulnerable functionality to change or read sensitive information depending on the vulnerability. DO NOT USE IT TO DROP TABLES OR DELETE THINGS.

Once you have "weaponized" the vulnerability and used it to steal sensitive data from the database or change sensitive information, record your payload and test steps so they can be graded.

## Deliverables
In order to get full credit for this assignment you must turn in a .txt file containing the following:

- 4 proofs of concepts that prove there is SQL injection in each of the 4 vulnerable areas
	- These proofs of concepts should include the steps you took in order to show that you have in fact found a vulnerability and why your test steps prove it
	- If you have additional files like images then include them and turn in a .zip file
- 4 exploits that show the bad things you can do with the SQL injection
	- These exploits should include the steps you took in order to exploit the vulnerability and payloads so I can replicate the tests
	- These exploits should allow you to access or change sensitive data 

Note: these exploits may need to be explained in a series of steps instead of just providing a single link, so take care in explaining it as well as you can.

## Due Date
Thursday May 21st 3:30pm (15:30)

## Notes & Hints
These issues will be hard to find. Take a look at new functionality on the site and think about what must be happening on the backend to make this new functionality work.

Take a look at 2nd order SQL Injection.

Don't make assumptions about the type of database(s) that are being used.

Use Burp to intercept the requests and responses from the server. What the server puts in the body of a response and what is actually displayed to a user can differ. Just because you can't see something on the page (like an error message) doesn't mean it's not happening.

Please include links to any pages, guides, tutorials, people, or anything you used to help you figure out these challenges. Please do not cheat or trade answers! If you gently/fairly help one another out make sure to credit the people that helped you in your report. Give credit where credit is due.

No automated tools!