import subprocess,sys
if len(sys.argv)<2: print('Usage'); exit()
for f in sys.argv[1:]:
    print("Running",f); subprocess.call(['python3',f])
