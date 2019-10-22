import urllib.request
import json


def getResponse(url):
    operUrl = urllib.request.urlopen(url)
    if(operUrl.getcode()==200):
        data = operUrl.read()
        jsonData = json.loads(data)
    else:
        print("Error receiving data", operUrl.getcode())
    return jsonData


# Python program to get average of a list
def averageVolumePrice(lst):
    return sum(lst) / len(lst)


def Nmaxelements(list1, N):
    final_list = []

    for i in range(0, N):
        max1 = 0

        for j in range(len(list1)):
            if list1[j] > max1:
                max1 = list1[j];

        list1.remove(max1);
        final_list.append(max1)

    return final_list


def main():

    urlData = "https://poloniex.com/public?command=returnTradeHistory&currencyPair=BTC_ETH"
    jsonData = getResponse(urlData)
    priceList = []
    # print the data
    for i in jsonData:
        #print(i["rate"])
        priceList.append(float(i["amount"]))



    avrg = averageVolumePrice(priceList)
    highrPrice = Nmaxelements(priceList,10)


    print("Average Volume Weighted Price : " + str(avrg))
    print("List of the 10 Highest Prices : " + str(highrPrice))


if __name__ == '__main__':
    main()