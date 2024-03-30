from modules.compress import *
from modules.decompress import *
from modules.lsfiles import *
data = lsfiles(r"./DrvCeo")
#print(data)
#print(compress(data))
print(decompress(r"D:\code\python\pylbgz\NewFile.pylbgz", '.'))