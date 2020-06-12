"""
utils.py 

Useful functions for the NetPyNE-based implementation of HNN

Contributors: salvadordura@gmail.com
"""

# utils 
# Function to set cfg params from .param file
def setCfgFromFile (fn, cfg, exclude = []):
    d = {}
    with open(fn,'r') as fp:
        ln = fp.readlines()
        for l in ln:
            s = l.strip()
            if s.startswith('#'): continue
            sp = s.split(':')
            sp[1] = sp[1].strip()
            if len(sp[1]) > 0:
                if '.' in sp[1] or 'e' in sp[1]:
                    try:
                        value = float(sp[1])
                    except:
                        value = str(sp[1])
                else:
                    try:
                        value = int(sp[1])
                    except:
                        value = str(sp[1])
                d[sp[0].strip()] = value
    for k, v in d.items():
        if k not in exclude:
            setattr(cfg, k, v)
        if 'duration' not in exclude:
            cfg.duration = cfg.tstop
    return cfg
