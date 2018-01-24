# -*- coding: utf-8 -*-
#!/usr/local/bin/python3

import HuobiUtil
import HuobiService

CoinType_BTC = 0
CoinType_ETH = 1
CoinType_ZEC = 2
CoinType_USDT = 3

CoinTypeString = [ "btc", "eth", "zec", "usdt" ]


class SealedService:
    def __init__(self):
        pass

    def __getBalanceList(self):
        result = HuobiService.get_balance(HuobiUtil.ACCOUNT_ID)
        if result is None or result["status"] != "ok":
            return None
        else:
            return result["data"]["list"]
    
    def getBalance(self, coinType):
        balanceList = self.__getBalanceList()
        if balanceList is None:
            return None
        else:
            coinString = CoinTypeString[coinType]
            balance = ""
            ifExist = False
            for dic in balanceList:
                if dic["currency"] == coinString and dic["type"] == "trade":
                    balance = dic["balance"]
                    ifExist = True
                    break
            
            if ifExist:
                return balance
            else:
                return None
        

   
    
