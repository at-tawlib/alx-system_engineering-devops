# 0x02-shell_redirections

**[0-hello_world](0-hello_world)** : prints `“Hello, World”`, followed by a new line to the standard output

**[1-confused_smiley](1-confused_smiley)** : displays a confused smiley `"(Ôo)'`

**[2-hellofile](2-hellofile)** : display the content of the `/etc/passwd` file

**[3-twofiles](3-twofiles)** : display the content of `/etc/passwd` and `/etc/hosts`

**[4-lastlines](4-lastlines)** : display the last 10 lines of `/etc/passwd`

**[5-firstlines](5-firstlines)** : display the first 10 lines of `/etc/passwd`

**[6-third_line](6-third_line)** : displays the third line of the file `iacta`

**[7-file](7-file)** : creates a file named ***`\*\\'"Best School"\'\\*$\?\*\*\*\*\*:)`*** containing the text Best School ending by a new line

**[8-cwd_state](8-cwd_state)** :  writes into the file `ls_cwd_content` the result of the command `ls -la`. If the file `ls_cwd_content` already exists, it should be overwritten. If the file `ls_cwd_content` does not exist, create it.

**[9-duplicate_last_line](9-duplicate_last_line)** : duplicates the last line of the file `iactaa`

**[10-no_more_js](10-no_more_js)** : deletes all the regular files (not the directories) with a `.js` extension that are present in the current directory and all its subfolders

**[11-directories](11-directories)** : counts the number of directories and sub-directories in the current directory
>The current and parent directories should not be taken into account
>Hidden directories should be counted

**[12-newest_files](12-newest_files)** : displays the 10 newest files in the current directory

**[13-unique](13-unique)** : takes a list of words as input and prints only words that appear exactly once

**[14-findthatword](14-findthatword)** : display lines containing the pattern “root” from the file `/etc/passwd`

**[15-countthatword](15-countthatword)** : display the number of lines that contain the pattern “bin” in the file `/etc/passwd`

**[16-whatsnext](16-whatsnext)** : display lines containing the pattern “root” and 3 lines after them in the file `/etc/passwd`

**[17-hidethisword](17-hidethisword)** : display all the lines in the file `/etc/passwd` that do not contain the pattern `“bin”`

**[18-letteronly](18-letteronly)** : display all lines of the file `/etc/ssh/sshd_config` starting with a letter.

>include capital letters as well

**[19-AZ](19-AZ)** : replace all characters `A` and `c` from input to `Z` and `e` respectively

**[20-hiago](20-hiago)** : create a script that removes all letters `c` and `C` from input

**[21-reverse](21-reverse)** : reverses its input

**[22-users_and_home](22-users_and_home)** : displays all users and their home directories, sorted by users of the `/ect/passwd` file

**[100-empty_casks](100-empty_casks)** :  finds all empty files and directories in the current directory and all sub-directories
-   Hidden files should be listed
-   One file name per line  
-   The listing should end with a new line
-   You are not allowed to use  `basename`,  `grep`,  `egrep`,  `fgrep`  or  `rgrep`

**[101-gifs](101-gifs)** : lists all the files with a  `.gif`  extension in the current directory and all its sub-directories.
-   Hidden files should be listed
-   Only regular files (not directories) should be listed
-   The names of the files should be displayed without their extensions
-   The files should be sorted by byte values, but case-insensitive (
-   One file name per line
-   The listing should end with a new line
-   You are not allowed to use  `basename`,  `grep`,  `egrep`,  `fgrep`  or  `rgrep`

**[102-acrostic](102-acrostic)** : decodes acrostics that use the first letter of each line (the arcrostics file is `AcrosticElizabeth`)


**[103-the_biggest_fan](103-the_biggest_fan)** : arses web servers logs in TSV format as input and displays the 11 hosts or IP addresses which did the most requests.
>-   Order by number of requests, most active host or IP at the top
>-   You are not allowed to use  `grep`,  `egrep`,  `fgrep`  or  `rgrep`
