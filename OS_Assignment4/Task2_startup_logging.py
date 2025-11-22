import multiprocessing,logging,time
logging.basicConfig(filename='system_log.txt',level=logging.INFO)
def w(n): logging.info(n+' start'); time.sleep(2); logging.info(n+' end')
if __name__=='__main__':
    p1=multiprocessing.Process(target=w,args=("P1",))
    p2=multiprocessing.Process(target=w,args=("P2",))
    p1.start(); p2.start(); p1.join(); p2.join()
