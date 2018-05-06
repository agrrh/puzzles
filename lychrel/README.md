# Lychrel numbers

A Lychrel number is a natural number that cannot form a palindrome through the iterative process of repeatedly reversing its digits and adding the resulting numbers. This process is sometimes called the 196-algorithm, after the most famous number associated with the process.

Here's a simple program to seek for such numbers.

## Usage

```
$ python lychrel.py
Usage:
	lychrel.py [start end iters]

# Seeking Lychrel numbers in 1 .. 200 with 50 iterations
196 -> 925153265399993573340628

$ python lychrel.py 1 1000 50
# Seeking Lychrel numbers in 1 .. 1000 with 50 iterations
196 -> 925153265399993573340628
295 -> 925153265399993573340628
394 -> 925153265399993573340628
493 -> 925153265399993573340628
592 -> 925153265399993573340628
689 -> 1751196640799987135692157
691 -> 925153265399993573340628
788 -> 1751196640799987135692157
790 -> 925153265399993573340628
879 -> 9041998323271812248892498
887 -> 1751196640799987135692157
978 -> 9041998323271812248892498
986 -> 1751196640799987135692157

$ python lychrel.py 1186060307891929990 1186060307891929990 260
# Seeking Lychrel numbers in 1186060307891929990 .. 1186060307891929990 with 260 iterations
1186060307891929990 -> 14051142433643311610130722643331260044362162241245310451360230640451135312412622544301622333362170321062133354432511503

$ python lychrel.py 1186060307891929990 1186060307891929990 261
# Seeking Lychrel numbers in 1186060307891929990 .. 1186060307891929990 with 261 iterations
```

## Links

- [Numbers which require exactly 261 'Reverse and Add' steps to reach a palindrome](https://oeis.org/A281506)
- [Wiki: Lychrel number](https://en.wikipedia.org/wiki/Lychrel_number)
