class Product:
    __margin = 0
    __usdPrice = 0
    __eurPrice = 0

    def __init__(self, name, price):
        self.name = name
        self.price = price

    def setMargin(self, margin):
        if isinstance(margin, (float,int)):
            if margin < 0:
                raise ValueError
            self.__margin = margin
        else:
            raise TypeError

    def setUsdPrice(self, price):
        if isinstance(price, (float,int)):
            if price < 0:
                raise ValueError
            self.__usdPrice = price
        else:
            raise TypeError

    def setEurPrice(self, price):
        if isinstance(price, (float, int)):
            if price < 0:
                raise ValueError
            self.__eurPrice = price
        else:
            raise TypeError

    def get_Euro_Price(self):
        return self.__eurPrice

    def get_USD_Price(self):
        return self.__usdPrice

    def get_margin(self):
        return self.__margin

    def del_Euro_Price(self):
        del self.__eurPrice

    def del_USD_Price(self):
        del self.__usdPrice

    def del_margin(self):
        del self.__margin

    def print(self):
        print('Name: {0:20s} Price: {1:5s} Margin: {2:5s} USD: {3:5s} EUR: {4:5s}'
              .format(self.name, str(self.price), str(self.__margin), str(self.__usdPrice), str(self.__eurPrice)))


class Calculator:
    __margin = 0.3

    def __init__(self, usd, eur):
        self.setUsdPrice(usd)
        self.setEurPrice(eur)
        self._usd = usd
        self._eur = eur

    def calcMargin(self, price):
        if price < 0:
            raise ValueError
        return round(price * self.__margin, 2)

    def calcUsdPrice(self, price):
        if price < 0:
            raise ValueError
        return round(price * self._usd, 2)

    def calcUsdPriceMargin(self, price):
        if price < 0:
            raise ValueError
        return round((price * (1 + self.__margin)) * self._usd, 2)

    def calcEurPrice(self, price):
        if price < 0:
            raise ValueError
        return round(price * self._eur, 2)

    def calcEurPriceMargin(self, price):
        if price < 0:
            raise ValueError
        return round((price * (1 + self.__margin)) * self._eur, 2)

    def setMargin(self, margin):
        if isinstance(margin, (float, int)):
            if margin < 0:
                raise ValueError
            self.__margin = margin
        else:
            raise TypeError

    def setUsdPrice(self, price):
        if isinstance(price, (float, int)):
            if price < 0:
                raise ValueError
            self._usd = price
        else:
            raise TypeError

    def setEurPrice(self, price):
        if isinstance(price, (float, int)):
            if price < 0:
                raise ValueError
            self._eur = price
        else:
            raise TypeError

    def get_Euro_Price(self):
        return self._eur

    def get_USD_Price(self):
        return self._usd

    def get_margin(self):
        return self.__margin

    def del_Euro_Price(self):
        del self._eur

    def del_USD_Price(self):
        del self._usd

    def del_margin(self):
        del self.__margin



products = [
        Product('mięso z dzika', 3),
        Product('jajo', 5),
        Product('kawa sypana', 3),
        Product('malpeczka', 7),
        Product('pomidorowy sok', 10)]

calc = Calculator(4, 4.5)

for x in products:
    x.setMargin(calc.calcMargin(x.price))
    x.setUsdPrice(calc.calcUsdPriceMargin(x.price))
    x.setEurPrice(calc.calcEurPriceMargin(x.price))

for x in products:
    x.print()
