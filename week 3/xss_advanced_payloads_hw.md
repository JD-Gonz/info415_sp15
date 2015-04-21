## XSS Advanced Payloads

### Phase 1 (over the weekend)
Location: https://info415.csuw.net/snapchat/user.php?action=login

For phase 1 you will want to do the following:
- Create 2 accounts for testing
	- One will be the victim and one will be the attacker
- Familiarize yourself with the web app, submit posts, follow and unfollow other users
- Find the stored XSS
- Generate a payload that steals another user's cookies
	- Remember you can use http://r7.io/exfil_create to help steal the cookie
	- Check the week 3 slides and demos for help
	- Deploy the stored XSS with the payload and browse to it with your victim account, see if you can get the victims account's session cookie just by browsing around and tripping the payload
- Generate a payload that causes a victim to "follow" you
	- While logged in and with Burp intercepting, follow another user and watch the request
	- See if you can perform the same request with an XSS payload
	- Remember that a GET request can be generated in the background by loading an image or iFrame (see the cookie stealing code)
	- Deploy the stored XSS with the payload and browse to it with your victim account
		- See if you can cause the victim to automatically follow you just by browsing around and tripping the payload
- Generate a payload that causes a victim to make a post
	- While logged in, and with Burp intercepting, make a post and watch the request
	- See if you can perform the same request with an XSS payload
	- Remember that a POST request can be generated in the background by using AJAX
	- Deploy the stored XSS with the payload and browse to it with your victim account
		- See if you can cause the victim to automatically make a post just by browsing around and tripping the payload

Note: Everyone is sharing this testing environment so delete posts you're not actively using and cover your tracks so you don't leave a mess. Also leave eachother alone and don't hack eachother's accounts.


### Phase 2 (Tuesday - Thursday)
Location: TBD

Here's the situation:
- You can only view someone's wall if they are following you
- The user social_butterfly follows and views everyone's posts constantly
- The user admin only follows social_butterfly and views her posts occasionally
- The user Wilfred only follows admin and views his posts occasionally

For phase 2 you will take the payloads generated in phase 1 and string them together in order to get the admin to follow you so you can read something on their wall and so you can steal a cookie from another user, Wilfred. This can all be done in a single XSS payload that will spread through the system, or can be done is separate steps, stealing the other user's sessions as you go. The browsing by the social_butterfly, admin, and Wilfred will be automated so it is your choice on how you solve it, but points will be awarded for use of a single payload.


### Deliverables

The point breakdown is as follows:
- Cookie stealing XSS payload (4 points)
- "Follow me" XSS payload (7 points)
- Auto-post XSS payload (10 points)
- One super payload combining the above (5 points)
- The loot
	- The message on the admin's wall (2 points)
	- Wilfred's session cookie (2 points)


### Due Date
3:30pm (15:30) Thursday April 23th 2014 

### Note
Please include links to any pages, guides, tutorials, people, or anything you used to help you figure out these challenges. Please do not cheat or trade answers! If you gently/fairly help one another out make sure to credit the people that helped you in your report. Give credit where credit is due.

No automated tools!