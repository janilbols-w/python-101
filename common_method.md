# Common python usage

## syscall to use scp
```python
import os
os.system('scp "%s" "%s:%s"' % (localfile, remotehost, remotefile) )
```
