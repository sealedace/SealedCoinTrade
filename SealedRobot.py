# -*- coding: utf-8 -*-
"""
title: SealedService
author: sealedace
"""
#!/usr/local/bin/python3

import SealedService


class SealedRobot(object):
    """交易机器人"""

    __btcBalance = 0.0
    __ethBalance = 0.0
    __zecBalance = 0.0
    __usdtBalance = 0.0

    def __init__(self):

        self.__service = SealedService.SealedService()
        self.__fetchAllBalanceData()

    def __fetchAllBalanceData(self):
        usdt = self.__service.getBalance(SealedService.CoinType_USDT)
        if usdt is not None:
            self.__usdtBalance = float(usdt)
            print("usdt balance: " + usdt)

        eth = self.__service.getBalance(SealedService.CoinType_ETH)
        if eth is not None:
            self.__ethBalance = float(eth)
            print("eth balance: " + eth)
        
        btc = self.__service.getBalance(SealedService.CoinType_BTC)
        if btc is not None:
            self.__btcBalance = float(btc)
            print("btc balance: " + btc)

        zec = self.__service.getBalance(SealedService.CoinType_ZEC)
        if zec is not None:
            self.__zecBalance = float(zec)
            print("zec balance: " + zec)


