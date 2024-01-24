from machine import Timer #引入 計時器 功能
tim = Timer(-1)
tim.init(period=1000, mode=Timer.PERIODIC, callback=lambda t:print('ok')) #每 1 秒、作一次