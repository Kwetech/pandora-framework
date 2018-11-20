#!/usr/bin/env python
import os
import time
os.system("cd ..;rm -rf pandora-framework;git clone https://github.com/OxfordSecurity/pandora-framework.git")

print("Latest \33[92;1mPandora \33[00mcloned")
time.sleep(2)
print("\33[91;1mtype 'chmod +x *' then './install.py'\33[00m")

print("\33[1m :-) yei, \33[92;1mYou are using the latest Pandora-Framework\33[00m\n")
print("\33[91;1mNOTE:\33[00m\33[1;3myou can update Pandora week after update\33[00m")
print("run ./panconsole to start")