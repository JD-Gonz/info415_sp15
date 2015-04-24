## Clickjacking HW Grading
Homework challenges can be found at http://clickjacking-challenges.r7.io/

## Part 1 - Vulnerabilities (8 points)
Level 1: 2 points

Level 2: 4 points

Style: 4 points

The webpages you will be creating clickjacking attacks for are http://clickjacking-challenges.r7.io/level/1 and /level/2. These pages take 2 URL parameters: name and location. The name parameter specifies your UW NetID and the location is the location the form is going to submit to. So go to http://r7.io/exfil_create to create a unique exfiltration page for use in this HW. Then tweak the parameters in the URL so they match your information (see example below). This URL is the one you will be embedding in your iFrame on the clickjacking page. The goal is to trick a victim admin (me) into browsing to your page and clicking on something that secretly submits the form of the page in the iFrame. When you test your clickjacking attack your name and the phrase "unavailable" will be sent to the exfiltration page, but when I click on it a special hash will be sent to your exfiltration page, this is how I will verify that your attack worked.

TL;DR - To earn full points on the challenges you must craft a webpage that convinces a victim (me) to click somewhere on the page and in doing so submit the form with your information.

Note: the default URL parameters have to be changed to your information.
	- Example: my UW NetID is amckenna and my exfiltration page is http://r7.io/e/yOW7yTEspI (go create your own)
	- So my URL would be: http://clickjacking-challenges.r7.io/level/1?name=amckenna&location=http://r7.io/e/yOW7yTEspI

## Part 3 - The Report (2 points)
- Description (1 point)
- Mitigations (1 point)
	- Give a mitigation recommendations for stopping clickjacking

This must be submitted as a txt file. Please no PDFs or Word docs!

## Deliverables
A .zip file containing:

1. An HTML page I can open in Firefox that entices me to click somewhere on the page and triggers a clickjacking attack against the level 1 form.
2. An HTML page I can open in FIrefox that entices me to click somewhere on the page and triggers a clickjacking attack against the level 2 form.

## Due Date
The whole HW (vulnerabilities and report) are due at 3:30pm (15:30) Thursday April 30th 2014

## Notes
Please include links to any pages, guides, tutorials, people, or anything you used to help you figure out these challenges. Please do not cheat or trade answers! If you gently/fairly help one another out make sure to credit the people that helped you in your report. Give credit where credit is due.

No automated tools!