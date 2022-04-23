# Pot

The teacher has sent an e-mail to her students with the following task: “Write a program that will determine and output the value of X if given the statement:

$$X=number^{pow_1}_{1}+number^{pow_2}_{2}+…+number^{pow_N}_{N}$$

and it holds that $number_1$, $number_2$ to $number_N$ are integers, and $pow_1$, $pow_2$ to $pow_N$ are one-digit integers.” Unfortunately, when the teacher downloaded the task to her computer, the text formatting was lost so the task transformed into a sum of N integers:

$$X=P_1+P_2+…+P_N$$

For example, without text formatting, the original task in the form of $X=21^2+125^3$ became a task in the form of $X=212+1253$. Help the teacher by writing a program that will, for given N integers from $P_1$ to $P_N$ determine and output the value of X from the original task.

## Input

The first line of input contains the integer N (1≤N≤10), the number of the addends from the task. Each of the following N lines contains the integer $P_i (10≤P_i≤9999, i=1,…,N)$ from the task.

## Output

The first and only line of output must contain the value of X (X≤1000000000) from the original task.

## Info

- Problem ID: pot
- CPU Time limit: 1 second
- Memory limit: 1024 MB
- Difficulty: 1.2
- Author: Nikola Dmitrović
- Source: Croatian Open Competition in Informatics 2015/2016, contest #3
