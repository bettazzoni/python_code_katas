# python_katas


## Classic code katas in python 
A simple directory where build & run my katas.

## Installation
Python 3.10+ and [pytest](https://pytest.org/)


## Code katas

* [Alarm clock](#Alarm-clock)
* [Bowling game score](#Bowling-game-score)
* [Factorize into primes](#factorize-into-primes) 
* [Fizz Buzz](#fizzbuzz)
* [Game of Life](#Game-of-life)
* [Harry Potter books](#Harry-Potter-books)
* [Leap year](#Leap-year)
* Mars Rover challanges [(description on code.google)](https://code.google.com/archive/p/marsrovertechchallenge/)
* [Mine Field]()
* [Password checker](#Password-checker)
* [Remote calculator](#Remote-calculator)
* [Reverse Roman number](#reverse-roman)
* [Roman numbers](#Roman-numbers)

Thanks to [cyber dojo](https://cyber-dojo.org/) for kata descriptions, and to be "_a place to practice programming_"


---
### Alarm clock
As a programmer I want to receive/build an Alarm object 
so I can check the timeout only when I need/want

Warning: pseudo Java syntax

Alarm class has a public constructor `Alarm(long n_sec)` where 
* `n_sec` is the number of seconds before the alarm “expires” 
* `public boolean isExpired()` method that returns
    * `false` from its creation to n_sec-1 from the object creation
    * `true` after n_sec from the object creation
      
Examples
* `Alarm(0).isExpired()` returns true
* `Alarm(100).isExpired()` has to return `false` after 99 sec. or less
* `Alarm(100).isExpired()` has to return `true` after 100 sec. or more
      
**Alarm has to be unit-testable**: remove the dependency from the time (hint: use dependency injection)

---

### Bowling game score
  [(link to the original kata from Uncle Bob)](http://www.butunclebob.com/ArticleS.UncleBob.TheBowlingGameKata)

Write a program to score a game of Ten-Pin Bowling.

* Input: string (described below) representing a bowling game 
* Ouput: integer score

The scoring rules:   
Each game, or "line" of bowling, includes ten turns, or "frames" for the bowler.   
In each frame, the bowler gets up to two tries to knock down all ten pins.   
If the first ball in a frame knocks down all ten pins, this is called a "strike". The frame is over. The score for the frame is ten plus the total of the pins knocked down in the next two balls.       
If the second ball in a frame knocks down all ten pins, this is called a "spare". The frame is over. The score for the frame is ten plus the number of pins knocked down in the next ball.    
If, after both balls, there is still at least one of the ten pins standing the score for that frame is simply the total number of pins knocked down in those two balls.     
If you get a spare in the last (10th) frame you get one more bonus ball. If you get a strike in the last (10th) frame you get two more bonus balls. These bonus throws are taken as part of the same turn.     
If a bonus ball knocks down all the pins, the process does not repeat. The bonus balls are only used to calculate the score of the final frame.     
The game score is the total of all frame scores.   

Examples:
* X indicates a strike
* / indicates a spare
* '-' indicates a miss
* | indicates a frame boundary
* The characters after the || indicate bonus balls  `X|X|X|X|X|X|X|X|X|X||XX`    

`X|X|X|X|X|X|X|X|X|X||XX`  
Ten strikes on the first ball of all ten frames. Two bonus balls, both strikes.
Score for each frame == 10 + score for next two balls == 10 + 10 + 10 == 30      
Total score == 10 frames x 30 == 300

`9-|9-|9-|9-|9-|9-|9-|9-|9-|9-||  `
Nine pins hit on the first ball of all ten frames. Second ball of each frame misses last remaining pin. No bonus balls.
Score for each frame == 9   
Total score == 10 frames x 9 == 90

`5/|5/|5/|5/|5/|5/|5/|5/|5/|5/||5 `
Five pins on the first ball of all ten frames. Second ball of each frame hits all five remaining pins, a spare.
One bonus ball, hits five pins.
Score for each frame == 10 + score for next one ball == 10 + 5 == 15   
Total score == 10 frames x 15 == 150


`X|7/|9-|X|-8|8/|-6|X|X|X||81` 
Total score == 167

---

### Factorize into primes
Factorize a positive integer number into its prime factors.

For example: 
* 2 -> [2] 
* 3 -> [3]
* 4 -> [2,2] 
* 6 -> [2,3] 
* 9 -> [3,3]
* 12 -> [2,2,3] 
* 15 -> [3,5]

Note on **[Factorize](https://en.wikipedia.org/wiki/Factorization)**.   
In mathematics, **factorization** or factoring is the decomposition of an object into a product of other objects, 
  or factors, which when multiplied together give the original.    
For example, the number 15 factors into primes as 3 * 5

Note on [prime number](https://en.wikipedia.org/wiki/Prime_number).   
1 is not a prime number.    
Prime numbers start from 2.    
So 1 has to be excluded from this kata

---
## FizzBuzz
Count from 1 to N but replace certain numbers with the words "Fizz" and/or "Buzz", adhering to certain rules.

1. prints out the numbers 1 through 100, separated by newlines. 
2. Instead of numbers divisible by 3, the method should output "Fizz". 
3. Instead of numbers divisible by 5, the method should output "Buzz". 
4. Instead of numbers divisible by 3 and 5, the method should output "FizzBuzz".

Sample Output
`1
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
`
---

## Game of life
(From the description in [coding dojo](https://codingdojo.org/kata/GameOfLife/) )

This Kata is about calculating the next generation of Conway’s game of life, given any starting position. See http://en.wikipedia.org/wiki/Conway%27s_Game_of_Life for background.

You start with a two dimensional grid of cells, where each cell is either alive or dead.     
In this version of the problem, the grid is finite, and no life can exist off the edges. 
Grid rules:
Given `g[N][M]` a grid of N*M elements.

The grid follows the rules 
 * `g[N][] == g[0]`
 * `g[][M] == g[][0]`
 * `g[-1][] == g[N-1][]`
 * `g[][-1] == g[][M-1]`

When calcuating the next generation of the grid, follow these rules:

   1. Any live cell with fewer than two live neighbours dies, as if caused by underpopulation.
   2. Any live cell with more than three live neighbours dies, as if by overcrowding.
   3. Any live cell with two or three live neighbours lives on to the next generation.
   4. Any dead cell with exactly three live neighbours becomes a live cell.

You should write a program that can accept an arbitrary grid of cells, and will output a similar grid showing the next generation.

First version with Python 


---

### Harry Potter books
As a bookshop owner   
I want to see all the possible combinations of discounts on HP books     
so I can propose it to my customers

To try and encourage more sales of the 5 different Harry Potter books they sell, a bookshop has decided to offer discounts of multiple-book purchases.   
One copy of any of the five books costs 8 €.   
If, however, you buy two different books, you get a 5% discount on those two books.     
If you buy 3 different books, you get a 10% discount.     
If you buy 4 different books, you get a 20% discount.      
If you go the whole hog, and buy all 5, you get a huge 25% discount.    

Note that if you buy, say, four books, of which 3 are different titles, you get a 10% discount on the 3 that form part of a set, but the fourth book still costs 8 €.     
Your mission is to write a piece of code to calculate the price of any conceivable shopping basket (containing only Harry Potter books), giving as big a discount as possible.


**Example**: how much does this basket of books cost? 
* 2 copies of the first book 
* 2 copies of the second book 
* 2 copies of the third book 
* 1 copy of the fourth book 
* 1 copy of the fifth book

One way of group these 8 books is:
* 1 group of 5 --> 25% discount (1st,2nd,3rd,4th,5th)
* 1 group of 3 --> 10% discount (1st,2nd,3rd)   
This would give a total of    
 5 books at a 25% discount + 3 books at a 10% discount    
Giving   
5 x (8 - 2.00) == 5 x 6.00 == 30.00 +3 x (8 - 0.80) == 3 x 7.20 == 21.60       
For a total of 51.60

However, a different way to group these 8 books is:
* 1 group of 4 books --> 20% discount (1st,2nd,3rd,4th)
* 1 group of 4 books --> 20% discount (1st,2nd,3rd,5th) 
This would give a total of    
  4 books at a 20% discount +4 books at a 20% discount     
Giving    
4 x (8-1.60) == 4 x 6.40 == 25.60 +4 x (8-1.60) == 4 x 6.40 == 25.60    
For a total of 51.20

And 51.20 is the price with the biggest discount.


---
### Leap year
 
As a history professor    
I want to know what were the leap years    
so I can calculate the time exactly
   
(aka:   
write a _function_ that returns true or false depending on whether its input integer is a leap year or not.   
Year <0 is b.c, year >0 is a.d.)

Leap year definitions
* Before Julian calendar was applied (8 AD) no leap years were defined
* Julian calendar (from 8 to 1582): a leap year is defined as one that is divisible by 4    
 (_historical note: Julian calendar was introduced in 45 BC, but it was "full operational" only in 8 AD_)
* Gregorian calendar (from 1582): a leap year is defined as one that is divisible by 4, but is not otherwise divisible by 100 unless it is also divisible by 400.

Examples:
* +8 was the first leap year in history
* 1100 was a leap year
* 1584 was the first leap year of the Gregorian calendar
* 1900 is an atypical common year
* 2000 is an atypical leap year


---
### Mine Field

A field of N x M squares is represented by N lines of exactly M characters each.

* The character '@' represents a mine. 
* The character '.' represents no-mine.

Example input (a 3 x 4 mine-field of 12 squares, 2 of which are mines)

3 4    
@...    
..@.    
....    

Your task is to write a program to accept this input and produce as output a hint-field of identical dimensions where each square is a * for a mine or the number of adjacent mine-squares if the square does not contain a mine.

Example output (for the above input)     
@211    
12@1    
0111     


---

### Password checker
As a generic user    
I want to be warned if my password is too weak  
so I'm more safe

Rules: In order to be an acceptable password, a string must:
* Have a length greater than 7 characters.
* Contain at least one alphabetic character.
* Contain at least one digit.

---
### Remote calculator
Given a json `{ "Cmd": "add", "val1": -12, “val2”: 42 }`
define a function (method) that performs the command
(in this case has to return 30 )

The possible commands are
* `{ "Cmd": "add", "val1": 3, “val2”: 2 }` expected result = 5
* `{ "Cmd": "sub", "val1": 3, “val2”: 2 }` expected result = 1
* `{ "Cmd": "mul", "val1": 3, “val2”: 2 }` expected result = 6
* `{ "Cmd": "div", "val1": 3, “val2”: 2 }` expected result = 1.5


---
## Reverse Roman

Given a Roman number as a string (eg "XX") determine its integer value (eg 20).

You cannot write numerals like IM for 999. Wikipedia states "Modern Roman numerals are written by expressing each digit separately starting with the leftmost digit and skipping any digit with a value of zero."

Examples:

| | | | | | | |    |
|-|-|-|-|-|-|-|----|
| 1 | I | 10 | X | 100 | C | 1000 | M  |
| 2 | II | 20 | XX | 200 | CC | 1000 | MM |
| 3 | III | 30 | XXX | 300 | CCC | 1000 | MMM |
| 4 | IV | 40 | XL | 400 | CD | 1000 | MMMM |
| 5 | V | 50 | L | 500 | D | |    |
| 6 | VI | 60 | LX | 600 | DC | |    |
| 7 | VII | 70 | LXX | 700 | DCC | |    |
| 8 | VIII | 80 | LXXX | 800 | DCCC |  |    |
| 9 | IX | 90 | XC | 900 | CM |  |    |


* "MCMXC" -> 1990 ("M" -> 1000 + "CM" -> 900 + "XC" -> 90)
* "MMVIII" -> 2008 ("MM" -> 2000 + "VIII" -> 8)
* "XCIX" -> 99 ("XC" -> 90 + "IX" -> 9)
* "XLVII" -> 47 ("XL" -> 40 + "VII" -> 7)
* "MMMCDLXXIX" _> 3479  (3000 -> "MMM" + 400 -> "CD" + 70 -> "LXX" + 9 -> "IX")

---
### Roman numbers

As a history professor    
I want to translate our "_Arabic decimal numbers”_ into its Roman numeral representation    
so I can write it in latin.

Given a positive integer number determine its Roman numeral representation as a String 
(eg. 42 -> "XLII").

| | | | | | | |     |
|-|-|-|-|-|-|-|-----|
| 1 | I | 10 | X | 100 | C | 1000 | M   |
| 2 | II | 20 | XX | 200 | CC | 1000 | MM  |
| 3 | III | 30 | XXX | 300 | CCC | 1000 | MMM |
| 4 | IV | 40 | XL | 400 | CD | 1000 | MMMM |
| 5 | V | 50 | L | 500 | D | |     |
| 6 | VI | 60 | LX | 600 | DC | |     |
| 7 | VII | 70 | LXX | 700 | DCC | |     |
| 8 | VIII | 80 | LXXX | 800 | DCCC |  |     |
| 9 | IX | 90 | XC | 900 | CM |  |     |


You can have only number between 1 and 4999 (Between “I” and “MMMMCMXCIX”)     
You cannot write numerals like "IC" for 99 or “IM” for 999.    
Wikipedia states :
"Modern Roman numerals are written by expressing each digit separately starting with the leftmost digit and skipping any digit with a value of zero."

Examples:
*  1990 -> "MCMXC"  (1000 -> "M"  + 900 -> "CM" + 90 -> "XC")
*  2008 -> "MMVIII" (2000 -> "MM" + 8 -> "VIII")
*  3479 -> "MMMCDLXXIX" (3000 -> "MMM" + 400 -> "CD" + 70 -> "LXX" + 9 -> "IX")
*    99 -> "XCIX"   (  90 -> "XC" + 9 -> "IX")
*    47 -> "XLVII"  (  40 -> "XL" + 7 -> "VII")


