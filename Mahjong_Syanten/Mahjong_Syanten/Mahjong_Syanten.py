import syanten

#変換テーブル
TABLE=list([
    "一","二","三","四","五","六","七","八","九",
    "1","2","3","4","5","6","7","8","9",
    "１","２","３","４","５","６","７","８","９",
    "東","南","西","北","白","発","中"])

while True:
    #入力
    print("手札を入力してください")
    print("----------")
    print("(m)一二...九")
    print("(p)12...9")
    print("(s)１２...９")
    print("(j)東南西北白発中")
    print("----------")
    #文字列形式の手札
    hand_str=list(input())

    #数値形式の手札
    hand_id=[]
    #数値に変換
    for c in hand_str:
        hand_id.append(TABLE.index(c)*4)

    #シャンテン数表示
    print(syanten.Syanten(hand_id))