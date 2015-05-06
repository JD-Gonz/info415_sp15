## SQLi HW Grading
Homework challenges can be found at http://sqli-challenges.r7.io/

To go to your individual challenges go to http://sqli-challenges.r7.io/[uw-netid]

Example: My UW NetID is amckenna (my email is amckenna@uw.edu) so I would go to: http://sqli-challenges.r7.io/amckenna/

## Part 1 - Vulnerabilities (28 points)
- challenges 1-5: 10 points
- challenges 5-12: 14 points
- optimizations: 2 points
- version number: 2 points


To earn full points on all challenges you must craft a payload that reliably exfiltrates the flag user's username and password. On several of the challenges it is fine if the payload only inconsistently exfiltrates the flag user's credentials, though two extra point will be awarded if you can craft a reliable payload that exfiltrates the flag user's name and password every time (optimization point). The payload should be in the form of a link that I can click on to see the results. An additional two points will be awarded if you can get the database version number and submit to me the payload used, as well as the correct version number.

This part must be submitted in the form of a .txt file!

## Part 3 - The Report (7 points)
- Description (1 point)
	- A description of what SQL Injection is and why it's bad
- Test steps (4 points)
	- 1 set of test steps that include how you found the vuln and how it works.
	- This must be for the highest challenge you solve. If you solve up through 10, then this would be for the 10th challenge.
	- These should be detailed enough that someone in the class who didn't solve the challenges could walk through the steps, be able to reproduce the vulnerabilities, know how they worked, and why they happened.
	- No screenshots are necessary.
- Mitigations (2 points)
	- Give mitigation recommendations for 2 languages/frameworks
		- ASP.NET
		- PHP
	- This should include a few sentences about how to properly mitigate SQLi and a code example for each framework/language
	- Include a link or two to further reading/reference for the "developer"

This must be submitted in the form of a .txt file!

## Due Date
Tuesday May 12th 3:30pm (15:30)

## Notes & Hints
Please include links to any pages, guides, tutorials, people, or anything you used to help you figure out these challenges. Please do not cheat or trade answers! If you gently/fairly help one another out make sure to credit the people that helped you in your report. Give credit where credit is due.

No automated tools!