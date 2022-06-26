import platform
import psutil
import os
from rich import print

def get_systeminfo():
    res = {}
    my_system = platform.uname()
 
    res["System"] = my_system.system 
    res["Node Name"] = my_system.node
    res['Release'] = my_system.release
    res['Version'] = my_system.version
    res['Machine'] = my_system.machine
    res['Processor'] = my_system.processor
    res['num_process'] = os.cpu_count()
    res['Ram'] = psutil.virtual_memory().total/1024/1024/1024
    for k, v in res.items():
        res[k] = [v]
    return res
print(get_systeminfo())
