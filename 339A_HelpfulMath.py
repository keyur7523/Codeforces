'''
Xenia the beginner mathematician is a third year student at elementary school. She is now learning the addition operation.

The teacher has written down the sum of multiple numbers. Pupils should calculate the sum. To make the calculation easier, the sum only contains numbers 1, 2 and 3. Still, that isn't enough for Xenia. She is only beginning to count, so she can calculate a sum only if the summands follow in non-decreasing order. For example, she can't calculate sum 1+3+2+1 but she can calculate sums 1+1+2 and 3+3.

You've got the sum that was written on the board. Rearrange the summans and print the sum in such a way that Xenia can calculate the sum.

Input
The first line contains a non-empty string s — the sum Xenia needs to count. String s contains no spaces. It only contains digits and characters "+". Besides, string s is a correct sum of numbers 1, 2 and 3. String s is at most 100 characters long.

Output
Print the new sum that Xenia can count.

Examples
InputCopy
3+2+1
OutputCopy
1+2+3
InputCopy
1+1+3+1+3
OutputCopy
1+1+1+3+3
InputCopy
2
OutputCopy
2
'''


def helpfulMath(eqn: str) -> str:
    if len(eqn) == 1: return eqn
    eqnList = eqn.split('+')
    count1 = eqnList.count('1')
    count2 = eqnList.count('2')
    count3 = eqnList.count('3')
    finalEqn = ''
    if count1:
        for _ in range(count1): finalEqn += '1+'
    if count2:
        for _ in range(count2): finalEqn += '2+'
    if count3:
        for _ in range(count3): finalEqn += '3+'
    return finalEqn[:len(finalEqn)-1]

eqn = input()
print(helpfulMath(eqn))
