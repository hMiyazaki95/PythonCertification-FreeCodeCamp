🧠 Python Slicing Cheat Sheet
General Pattern
sequence[start : stop : step]


start → index to begin (inclusive)

stop → index to stop (exclusive)

step → how many positions to move

🔹 Basic Slicing (Most Used)
Slice	Meaning	Example (s = "python")	Result
s[:]	copy whole string	s[:]	"python"
s[:n]	first n chars	s[:3]	"pyt"
s[n:]	from index n to end	s[2:]	"thon"
s[a:b]	from a to b-1	s[1:4]	"yth"
🔹 Step Parameter
Slice	Meaning	Example	Result
s[::1]	normal copy	"abcd"[::1]	"abcd"
s[::2]	every 2nd char	"abcdef"[::2]	"ace"
s[::3]	every 3rd char	"abcdef"[::3]	"ad"
🔹 Reverse Slicing (Very Important)
Slice	Meaning	Example	Result
s[::-1]	reverse string	"hello"[::-1]	"olleh"
s[::-2]	reverse, skip every other	"abcdef"[::-2]	"fdb"
🔹 Negative Index Slicing
Slice	Meaning	Example	Result
s[-1]	last character	"python"[-1]	"n"
s[-2:]	last 2 characters	"python"[-2:]	"on"
s[:-1]	all except last	"python"[:-1]	"pytho"
s[:-2]	remove last 2	"python"[:-2]	"pyth"
🔹 Mixed Slicing
Slice	Meaning	Example	Result
s[1:-1]	remove first & last	"hello"[1:-1]	"ell"
s[2:-2]	remove first 2 & last 2	"abcdef"[2:-2] "cd"
🔹 Backward Ranges (Advanced, Optional)
Slice	Meaning	Example	Result
s[5:1:-1]	reverse part	"abcdef"[5:1:-1]	"fedc"


s[:]
s[::]
s[::-1]

s[:]     # copy
s[:n]    # first n
s[n:]    # from n
s[::2]   # skip
s[::-1]  # reverse