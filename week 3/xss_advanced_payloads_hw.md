## XSS Advanced Payloads

### Phase 1
Location: https://snapcat.csuw.net/

For phase 1 you will want to do the following:
- Setup Burp as an intercept proxy for Firefox
	- Make sure Firefox is proxying both HTTP and SSL traffic
	- See slide deck on tools setup from week 1 for more information
- Create 2 accounts for testing
	- One will be the victim and one will be the attacker
- Familiarize yourself with the web app, submit posts, follow and unfollow other users
- Find the stored XSS
	- The XSS should trigger automatically, no onmouseover or onclick
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
- Tips
	- Test your JS in the Firefox Developer Console - copy the payload, paste it, and hit enter. It should perform the same way as if you browsed to the page with the stored XSS
	- DON'T SAVE YOUR PAYLOAD IN MICROSOFT WORD OR GOOGLE DOCS! It will mess with the quotes and neuter your payload
		- http://imgur.com/oyKV4lE - Here you can see both types of quotes displayed in Sublime Text 2. The bad quotes are from the payload after I wrote it in Word. The second payload I wrote in Sublime Text 2. Notice the bad quotes are slightly more curved.
		- http://imgur.com/kDuNd3t - Here I copied the payloads into Firefox's developer tools console and ran it. The payload with the curvy quotes (BAD) from Word fails. The payload written in Sublime Text 2 with the straight ASCII quotes (GOOD) works just fine.


Note: Everyone is sharing this testing environment so delete posts you're not actively using and cover your tracks so you don't leave a mess. Also leave eachother alone and don't hack eachother's accounts. Traffic will be logged!


### Phase 2
Location: TBD

Here's the situation:
- You can only view someone's wall if they are following you
- The user butterfly follows and views everyone's posts constantly
- The user admin only follows butterfly and views their posts occasionally

For phase 2 you will take two of the payloads generated in phase 1 and string them together in order to get the admin to follow you so you can read something on their wall. This can be done in a single XSS payload that will spread through the system, or can be done is separate steps, stealing the other user's sessions as you go. The browsing by the butterfly and admin will be automated so it is your choice on how you solve it, but points will be awarded for use of a single payload.


### Deliverables
A .txt file containing the following:
1. Cookie stealing XSS payload (4 points)
2. "Follow me" XSS payload (7 points)
3. Auto-post XSS payload (10 points)
4. A single payload combining the "auto-post" and "follow me" payloads (5 points)
5. The loot - the message on the admin's wall (4 points)

These payloads need to be in a form that I can straight copy and paste into the snapcat site to verify they work. The loot can just be written in the .txt file.


### Due Date
3:30pm (15:30) Tuesday April 28th 2014 

### Note
Please include links to any pages, guides, tutorials, people, or anything you used to help you figure out these challenges. Please do not cheat or trade answers! If you gently/fairly help one another out make sure to credit the people that helped you in your report. Give credit where credit is due.

No automated tools!
