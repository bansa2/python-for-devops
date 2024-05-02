import sys

def ec2(region,mem):
    a = region + mem
    return a
def memory(region,mem):
    a = region + mem + "unix"
    return a

name = sys.argv[1]
region = sys.argv[2]
mem = sys.argv[3]

if name == "linux":
    op = ec2(region,mem)
    print(op)
else:
    op = memory(region,mem)
    print(op)
  