from sys import argv
from os import chdir, getcwd, popen

if len(argv) != 5:
    print("Not enough arguments were submitted")
    exit(1)

path, start, end, command = argv[1], argv[2], argv[3], argv[4]

curr_path = getcwd()
chdir(path)
stream = popen(f"git log {start} {end} --oneline")
commits = [log.split()[0] for log in stream.read().split('\n')[:-1]]

left, right = 0, len(commits) - 1

while left + 1 < right:
    pivot = (right + left) // 2
    popen(f"git checkout {commits[pivot]} -q")
    popen(command)
    code = int((popen("echo $?")).read())

    if code == 0:
        left = pivot
    else:
        right = pivot

chdir(curr_path)
print(f"First bad commit is: {commits[left]}")
