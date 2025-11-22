import os
r,w=os.pipe(); pid=os.fork()
if pid>0:
    os.close(r); os.write(w,b'Hello'); os.close(w); os.wait()
else:
    os.close(w); print(os.read(r,50).decode()); os.close(r)
