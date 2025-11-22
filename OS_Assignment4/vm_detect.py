import os,platform
print(platform.system(),platform.release())
paths=['/sys/class/dmi/id/product_name','/sys/class/dmi/id/sys_vendor']
for p in paths:
 if os.path.exists(p):
  t=open(p).read().lower()
  print(p,'->',t)
