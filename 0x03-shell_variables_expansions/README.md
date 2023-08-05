# 0x03. Shell, init files, variables and expansions

**[0-alias](0-alias)**  -creates an alias

**[1-hello_you](1-hello_you)**  : prints hello  `user`, where user is the current Linux user

**[2-path](2-path)**  : Add /action to the PATH (should be at the end of the PATH)

**[3-paths](3-paths)**  : counts the number of directories in the PATH

**[4-global_variables](4-global_variables)**  : lists environment variables

**[5-local_variables](5-local_variables)**  : lists all local variables and environment variables, and functions.

**[6-create_local_variable](6-create_local_variable)**  : creates a new local variable

**[7-create_global_variable](7-create_global_variable)**  : creates a new global variable.

**[8-true_knowledge](8-true_knowledge)**  : prints the result of the addition of 128 with the value stored in the environment variable  `TRUEKNOWLEDGE`, followed by a new line

**[9-divide_and_rule](9-divide_and_rule)**  : Write a script that prints the result of  `POWER`  divided by  `DIVIDE`, followed by a new line (`POWER`  and  `DIVIDE`  are environment variables)

**[10-love_exponent_breath](10-love_exponent_breath)**  : displays the result of  `BREATH`  to the power  `LOVE`  (both  `BREATH`  and  `POWER`  are environment variables

**[11-binary_to_decimal](11-binary_to_decimal)**  : converts a number from base 2 to base 10

**[12-combinations](12-combinations)**  : prints all possible combinations of two letters, except  `oo`

**[13-print_float](13-print_float)**  : prints a number with two decimal places, followed by a new line

**[100-decimal_to_hexadecimal](100-decimal_to_hexadecimal)** : converts a number from base 10 to base 16.

**[101-rot13](101-rot13)**  : encodes and decodes text using the rot13 encryption. Assume ASCII
```
pc@pc:~/shell/fun_with_the_shell$ cat quote
"Everyone is a proponent of strong encryption."
- Dorothy E. Denning
pc@pc:~/shell/fun_with_the_shell$ ./101-rot13 < quote
"Rirelbar vf n cebcbarag bs fgebat rapelcgvba."
- Qbebgul R. Qraavat
pc@pc:~/shell/fun_with_the_shell$
```
**[102-odd](102-odd)**:  prints every other line from the input, starting with the first line

**[103-water_and_stir](103-water_and_stir)**: adds the two numbers stored in the environment variables `WATER` and  `STIR` and prints the result
`STIR`  and prints the result.

-   `WATER`  is in base  `water`
-   `STIR`  is in base  `stir.`
-   The result should be in base  `bestchol`
```
pc@pc:~$ export WATER="ewwatratewa"
pc@pc:~$ export STIR="ti.itirtrtr"
pc@pc:~$ ./103-water_and_stir
shtbeolhc
pc@pc:~$
```
