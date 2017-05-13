checkhash.py is run by using 2 arguments following.  Those 2 arguments should be the files you want to compare for their hash.  Result will spit out if it's the same hash or different.

C:\Users\alex\Desktop\SofwerxPython>checkhash.py 7z1604.exe 7z1604-x64.exe
da7db29e783780f3a581e6e0bf4c595d
04584f3aed5b27fd0ac2751b36273d94
False

C:\Users\alex\Desktop\SofwerxPython>checkhash.py 7z1604.exe 7z1604.exe
da7db29e783780f3a581e6e0bf4c595d
da7db29e783780f3a581e6e0bf4c595d
True