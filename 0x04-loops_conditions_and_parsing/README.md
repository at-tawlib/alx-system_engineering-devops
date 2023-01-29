# 0x04. Loops, conditions and parsing

## [RSA_public_key.pub](RSA_public_key.pub)
Contains RSA public key

## [1-for_best_school](1-for_best_school)
Bash script that displays  `Best School`  10 times. using  `for` loops
```
sylvain@ubuntu$ ./1-for_best_school 
Best School
Best School
Best School
Best School
Best School
Best School
Best School
Best School
Best School
Best School
sylvain@ubuntu$ 
```

## [2-while_best_school](2-while_best_school)
Bash script that displays  `Best School`  10 times using `while` loop
```
sylvain@ubuntu$ ./2-while_best_school
Best School
Best School
Best School
Best School
Best School
Best School
Best School
Best School
Best School
Best School
sylvain@ubuntu$ 
```

## [3-until_best_school](3-until_best_school)
Bash script that displays  `Best School`  10 times using until loop
```
sylvain@ubuntu$ ./3-until_best_school
Best School
Best School
Best School
Best School
Best School
Best School
Best School
Best School
Best School
Best School
sylvain@ubuntu$ 
```

## [4-if_9_say_hi](4-if_9_say_hi)
Bash script that displays  `Best School`  10 times, but for the 9th iteration, displays  `Best School`  _and then_  `Hi`  on a new line using  only `while` loop and `if` statement
```
sylvain@ubuntu$ ./4-if_9_say_hi
Best School
Best School
Best School
Best School
Best School
Best School
Best School
Best School
Best School
Hi
Best School
sylvain@ubuntu$ 
```

## [5-4_bad_luck_8_is_your_chance](5-4_bad_luck_8_is_your_chance)
Bash script that loops from 1 to 10 and:
-   displays  `bad luck`  for the 4th loop iteration
-   displays  `good luck`  for the 8th loop iteration
-   displays  `Best School`  for the other iterations
- Using the  `while`  loop and  the  `if`,  `elif`  and  `else`  statements
```
sylvain@ubuntu$ ./5-4_bad_luck_8_is_your_chance
Best School
Best School
Best School
bad luck
Best School
Best School
Best School
good luck
Best School
Best School
sylvain@ubuntu$ 
```
## [6-superstitious_numbers](6-superstitious_numbers)
Bash script that displays numbers from 1 to 20 and:
-   displays  `4`  _and then_  `bad luck from China`  for the 4th loop iteration
-   displays  `9`  _and then_  `bad luck from Japan`  for the 9th loop iteration
-   displays  `17`  _and then_  `bad luck from Italy`  for the 17th loop iteration
- use the `while` loop and the `case` statement
```
sylvain@ubuntu$ ./6-superstitious_numbers
1
2
3
4
bad luck from China
5
6
7
8
9
bad luck from Japan
10
11
12
13
14
15
16
17
bad luck from Italy
18
19
20
sylvain@ubuntu$ 
```
##  [7-clock](7-clock)
Bash script that displays the time for 12 hours and 59 minutes:
-   display hours from 0 to 12
-   display minutes from 1 to 59
- using the `while` loop 
```
sylvain@ubuntu$ ./7-clock | head -n 70
Hour: 0
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
29
30
31
32
33
34
35
36
37
38
39
40
41
42
43
44
45
46
47
48
49
50
51
52
53
54
55
56
57
58
59
Hour: 1
1
2
3
4
5
6
7
8
9
...
sylvain@ubuntu$ 
```
### [8-for_ls](8-for_ls)
Bash script that displays:
-   The content of the current directory in a list format where only the part of the name after the first dash is displayed using `for` loop and do not display hidden files
```
sylvain@ubuntu$ ls
100-read_and_cut              1-for_best_school         6-superstitious_numbers
101-tell_the_story_of_passwd  2-while_best_school       7-clock
102-lets_parse_apache_logs    3-until_best_school       8-for_ls
103-dig_the-data              4-if_9_say_hi                  9-to_file_or_not_to_file
10-fizzbuzz                   5-4_bad_luck_8_is_your_chance
sylvain@ubuntu$  ./8-for_ls
read_and_cut
tell_the_story_of_passwd
lets_parse_apache_logs
dig_the-data
fizzbuzz
for_best_school
while_best_school
until_best_school
if_9_say_hi
4_bad_luck_8_is_your_chance
superstitious_numbers
clock
for_ls
to_file_or_not_to_file
sylvain@ubuntu$ 
```
## [9-to_file_or_not_to_file](9-to_file_or_not_to_file)
Bash script that gives you information about the  `school`  file using `if` and `else` statements
```
sylvain@ubuntu$ file school
school: cannot open `school' (No such file or directory)
sylvain@ubuntu$ ./9-to_file_or_not_to_file 
school file does not exist
sylvain@ubuntu$ touch school
sylvain@ubuntu$ ./9-to_file_or_not_to_file 
school file exists
school file is empty
school is a regular file
sylvain@ubuntu$ echo 'betty' > school 
sylvain@ubuntu$ ./9-to_file_or_not_to_file 
school file exists
school file is not empty
school is a regular file
sylvain@ubuntu$ rm school 
sylvain@ubuntu$ mkdir school
sylvain@ubuntu$ ./9-to_file_or_not_to_file 
school file exists
school file is not empty
sylvain@ubuntu$ 
```

## [10-fizzbuzz](10-fizzbuzz)
Bash script that displays numbers from 1 to 100 using `FizzBuzz`
```
sylvain@ubuntu$ ./10-fizzbuzz | head -20
1
2
Fizz
4
Buzz
Fizz
7
8
Fizz
Buzz
11
Fizz
13
14
FizzBuzz
16
17
Fizz
19
Buzz
sylvain@ubuntu$ 
```

> Written with [StackEdit](https://stackedit.io/).
