'''
Harry was contesting to be the most stylist person in his college. He had to collect maximum points from the judges to be able to win. However there was a problem. The judges were sitting in a line and each pair of adjacent judges had ego issues with each other. So if one judge gave X points to Harry then the next judge won’t give him any points. Harry had a friend in the organizing team and through him he had found out the exact points he would get from each judge if he chose their score to be considered. Help him find out the maximum points he can score.

INPUT
The first line of input contains the number of test cases, T.
0 < T < = 10
Each test case starts with a number N, the number of judges.
0 <= N < = 10^4.
The next line will have N numbers, number of points each judge gave Harry
0 < = X(i) < = 10^9.
The order of the judges does not change.

OUTPUT
For each test case print “Case T: A” without quotes in a single line.
T is the case number, starting with 1.
A is the maximum number of points Harry can collect.

SAMPLE INPUT 
2
5
1 2 3 4 5
1
10
SAMPLE OUTPUT 
Case 1: 9
Case 2: 10
Explanation
Case 1 : Harry chooses judges 1,3 and 5 with points 1 ,3 and 5 respectively to add up to 9 points in total. Case 2: There is only one judge so Harry chooses his points alone.

Time Limit: 3.0 sec(s) for each input file.
Memory Limit: 256 MB
Source Limit: 1024 KB
Marking Scheme: Score is assigned if any testcase passes.
Allowed Languages: Bash, C, C++, C++14, C++17, Clojure, C#, D, Erlang, F#, Go, Groovy, Haskell, Java, Java 8, Java 14, JavaScript(Rhino), JavaScript(Node.js), Julia, Kotlin, Lisp, Lisp (SBCL), Lua, Objective-C, OCaml, Octave, Pascal, Perl, PHP, Python, Python 3, Python 3.8, R(RScript), Racket, Ruby, Rust, Scala, Swift-4.1, Swift, TypeScript, Visual Basic
'''
#python3 code
t=int(input())
for _ in range(t):
    n=int(input())
    x=list(map(int,input().split()))
    ans=0
    for i in range(0,n,2):
        ans += x[i]
    ans2=0
    for i in range(1,n,2):
        ans2 += x[i]
    
    print("Case {}: {}".format(_+1,str(max(ans,ans2))))
