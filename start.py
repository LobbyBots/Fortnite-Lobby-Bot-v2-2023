import subprocess
p1 = subprocess.Popen(["python3", "main.py"])
p2 = subprocess.Popen(["python3", "website.py"])
p1.wait()
p2.wait()
