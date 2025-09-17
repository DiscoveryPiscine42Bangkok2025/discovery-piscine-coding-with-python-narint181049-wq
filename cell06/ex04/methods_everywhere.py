import sys

def shrink(s): return s[:8]
def enlarge(s): return s + "z" * (8 - len(s))

if len(sys.argv) < 2:
    print("none")
else:
    for w in sys.argv[1:]:
        print(shrink(w) if len(w) > 8 else enlarge(w) if len(w) < 8 else w)  