## Final Grading
The final can be found at: http://final.r7.io/[NetID]

### Part 1 - The Vulnerabilities
There are a number of vulnerabilities in the application including XSS, CSRF, SQLi, business logic, information disclosure, and others. Your job as the penetration tester is to find and document as many of these as you can. There may be more than I originally intended so I will just say that you should be able to find roughly 20-25 "issues" of varying levels of severity for full credit. 

Notes on how to count issues: 

- If you find multiple occurences of XSS each of those is a seperate "issue" to be documented
- If you find multiple occurnaces of CSRF then group those all into one issue report and simply list the forms you found CSRF for and a proof-of-concept for one of the forms
    - This should be in the form of a page that the "developer" can simply open and the will execute the CSRF attack automatically.

### Part 2 - The Report
The reporting will be done a little differently this time. For every issue you find you will need to fill out this Google Form: http://goo.gl/forms/YqN0U3xbxt

The information requested on the form is similar to what has been requested on previous homeworks and I expect the same level of depth in your answers.

I would recommend saving all of your issue writeups in a txt file or spreadsheet, then filling out the form to submit them last all at once. You are able to go back and edit previous form submissions but you have to save the link to that form when you submit it.

### Part 3 - Proofs of Concept
For some of the issues such as CSRF you will need to provide a "proof of concept" that demonstrates that the CSRF, or whatever, is possible. This should be in the form of a page that the "developer" can simply open and the will execute the CSRF attack automatically. This can be submitted via a canvas dropbox and should reference the ID of the issue you submitted via the Google Form.

### Part 4 - Show off
Extra points will be awarded for particularly clever or polished exploits. XSS worms that steal people's money, second order SQL injection, convincing CSRF pages, etc. will be awarded extra points. Additionally rumor has it that the bank has relations with the Leprechaun Mafia, see what you can find out about that and submit a couple sentences describing what you found and how you found it.

Submissions for the "show off" points can be submitted to the canvas dropbox in a .zip folder. This folder can contain .html pages, links to your payloads, and descriptions of what you were able to do. 

Impress me!

### Due Date
This will all be due Tuesday June 9th at 1pm (13:00) PST

NO LATE DAYS CAN BE USED FOR THE MIDTERM. IF YOU TURN IT IN LATE YOU WILL RECEIVE A 0%

### Note
No automated tools!!

Be careful not to corrupt your database, if you do I will have to wipe it back to the original state.

Don't mess with eachother's sites!

If you have questions please feel free to email me.