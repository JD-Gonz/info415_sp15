## XSS Homework Grading
Homework challenges can be found at: http://xss-challenges.r7.io/

### Part 1 - Vulnerabilities - 16 points
Each vulnerability will be worth 1 point. To earn 100% on this section you must complete all 16 challenges. 

Each vulnerability must call "alert(0)" via a payload entered through the website in order to demonstrate script execution. It is preferable that the injected JavaScript execute automatically when the page loads but that may not be possible in all cases. Please try to make it automatic where you can. Each answer must be in the form of a URL (link) that you could send to a victim to click on if possible. If not then include the steps necessary. 

### Part 3 - The Report - 9 points
- Description (1 point)
	- 2 to 3 sentences describing the type of vulernability (in this case: Reflected Cross-Site Scripting), what it is, and why it's bad.
- Test Steps (6 points)
	- 3 sets of test steps for the highest challenges you solved. These must include how you found the vulnerability, and why it happened.
	- If you solved 1-7, 9, 10, and 11 then you would write test steps for 9, 10, and 11 (the three highest)
	- These should be detailed enough that someone in the class who didn't solve the challenges could walk through the steps, be able to reproduce the vulnerabilities, know how they worked, and why they happened.
	- If for instance you know that the filter strips script tags but you can still get script execution through the onerror event handler of the img tag, then explain that in the test steps.
- Mitigations (2 points)
	- Give mitigation recommendations for 3 different languages/frameworks
		- Ruby on Rails
		- PHP
	- This should include a few sentences about how to properly mitigate XSS (such as escaping user input) and a code example (should only be a line of code or two)
	- Include a link for futher reading/reference for the "developer"

### Due Date
3:30pm (15:30) Thursday April 16th 2014 

### Note
Please include links to any pages, guides, tutorials, people, or anything you used to help you figure out these challenges. Please do not cheat or trade answers! If you gently/fairly help one another out make sure to credit the people that helped you in your report. Give credit where credit is due.

No automated tools!