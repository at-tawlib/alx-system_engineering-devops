# 0x19. Postmortem
## Issue Summary:
On the 13th May, 2023 from 10:15 AM to 11:30 AM GMT, requests to webservers for content resulted in 500 error response messages. Users were not able to access web contents successfully.

## Timeline (all times GMT)
- 10:15 AM: problem detected when a user submitted a report of not able to access webpage this was picked up by the monitoring service
- 10:20 AM: an alert was sent to the engineer on call
- 10:22 AM: the engineer responded to the alert and begun investigation
- 10:40 AM: engineer detected that the problem was from the Apache server
- 10:50 AM: engineer begun reading through Apache configuration and log files
- 11:00 AM: engineer found the source of error in the wp-settings.php file
- 11:10 AM: engineer handle error
- 11:15 AM: engineer restarted the server
- 11:30 AM: the requests started producing the required responses.

## Root Cause
The root cause was a clerical error. There was a misplelling of 'php' in the /var/www/htm/wp-settings.php file. Instead of 'php' it was typed as 'phpp'. This was an error made by an intern who was tasked to copy the config files and save locally. The intern did not only copy the files, he also edited the file which produced the problem

## Resolution and Recovery
The file /var/www/html/wp-settings.php was edited i.e. the 'phpp' was changed to 'php' and saved. The changes was commited and pushed to the testing team. After successful testing, the file was sent for production and updated. The server was restarted.

## Corrective and Prevantative Measures
It was decided that interns will not be allowed to edit files without supervision of senior engineers. Also all tasks performed by interns should be confirmed by a senior engineer before commiting. Finally interns will be given restricted access to the servers.
