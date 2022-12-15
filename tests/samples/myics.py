import os
import sys
import locale
locale.setlocale(locale.LC_ALL,"fr_FR.UTF-8")

sys.path.insert(0,os.path.abspath("./src"))

import ics

if __name__ == "__main__":
    fic="./tests/samples/TP24 Bruno.ics"
    cal=ics.Calendar(open(os.path.abspath(fic)).read())
    
    print(cal.events[0])
    from datetime import datetime
    cal.timeline.range=(datetime(2023,1,1),datetime(2023,12,31))
    L=list(cal.timeline)
    fic2="./tests/samples/TP24 Bruno2.ics"
    open(fic2,"w").writelines(cal)
    pass
    