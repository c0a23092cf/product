
# 日用品と店舗のデータベース
daily_goods_store = {
    "シャンプー": ["ドラッグストア", "スーパーアルプス", "イオンフードスタイル", "ライフ", "マツモトキヨシ"],
    "歯磨き粉": ["ドラッグストア", "スーパー三和", "ヨーカドー", "サミット", "マツモトキヨシ"],
    "トイレットペーパー": ["ドラッグストア", "イオンフードスタイル", "グルメシティ", "スーパーアルプス", "ライフ"],
    "洗剤": ["ドラッグストア", "スーパーアルプス", "マルエツ", "ヤオコー", "イオンフードスタイル"],
    "ティッシュ": ["ドラッグストア", "ライフ", "サミット", "ヤオコー", "スーパー三和"],
}


# 雑貨と店舗のデータベース
miscellaneous_store = {
    "カーテン": ["ニトリ", "IKEA", "無印良品", "島忠ホームズ", "大塚家具"],
    "ラグ・カーペット": ["IKEA", "ニトリ", "無印良品", "島忠ホームズ", "大塚家具"],
    "時計": ["無印良品", "IKEA", "ニトリ", "島忠ホームズ", "大塚家具"],
    "鏡": ["島忠ホームズ", "IKEA", "ニトリ", "無印良品", "大塚家具"],
    "ランプ": ["大塚家具", "無印良品", "IKEA", "ニトリ", "島忠ホームズ"],
}

# 商品と店舗のデータベース
product_store = {
    "玉ねぎ": ["スーパーアルプス", "イオンフードスタイル", "ライフ", "マルエツ", "ヤオコー"],
    "人参": ["スーパー三和", "ヨーカドー", "サミット", "グルメシティ", "業務スーパー"],
    "キャベツ": ["イオンフードスタイル", "グルメシティ", "業務スーパー", "スーパーアルプス", "ライフ"],
    "マヨネーズ": ["スーパーアルプス", "マルエツ", "ヤオコー", "イオンフードスタイル", "ヨーカドー"],
    "牛乳": ["ライフ", "サミット", "ヤオコー", "スーパー三和", "グルメシティ"],
    "卵": ["ヨーカドー", "ライフ", "スーパー三和", "サミット", "マルエツ"],
    "トマト": ["マルエツ", "ヤオコー", "スーパーアルプス", "イオンフードスタイル", "ライフ"],
    "じゃがいも": ["サミット", "グルメシティ", "スーパー三和", "ヨーカドー", "業務スーパー"],
    "マンゴー": ["業務スーパー", "スーパーアルプス", "イオンフードスタイル", "ライフ", "ヤオコー"],
    "ケチャップ": ["グルメシティ", "スーパー三和", "サミット", "マルエツ", "ヨーカドー"],
    "りんご": ["ヤオコー", "ライフ", "スーパー三和", "スーパーアルプス", "イオンフードスタイル"],
    "バナナ": ["スーパーアルプス", "イオンフードスタイル", "ライフ", "マルエツ", "ヤオコー"],
    "ヨーグルト": ["スーパー三和", "ヨーカドー", "サミット", "グルメシティ", "業務スーパー"],
    "チーズ": ["イオンフードスタイル", "グルメシティ", "業務スーパー", "スーパーアルプス", "ライフ"],
    "醤油": ["スーパーアルプス", "マルエツ", "ヤオコー", "イオンフードスタイル", "ヨーカドー"],
}


# 店舗名をキー、距離をバリューとする辞書を作成
distance = {
    "スーパーアルプス": 1.2,
    "スーパー三和": 2.5,
    "イオンフードスタイル": 0.8,
    "グルメシティ": 3.1,
    "ヨーカドー": 2.2,
    "ライフ": 1.8,
    "サミット": 2.9,
    "業務スーパー": 3.5,  
    "マルエツ": 1.9,
    "ヤオコー": 2.7,
    "ニトリ": 2.0,
    "IKEA": 5.0,
    "島忠ホームズ": 3.8,
    "無印良品": 1.5,
    "大塚家具": 4.2,
    "ドラッグストア": 1.0,
    "マツモトキヨシ": 2.3,
}

# 商品名を入力
product_name = input("商品名を入力してください: ")

# 商品が存在する店舗を取得
if product_name in product_store:
    stores_with_product = product_store[product_name]
elif product_name in miscellaneous_store:
    stores_with_product = miscellaneous_store[product_name]
elif product_name in daily_goods_store:
    stores_with_product = daily_goods_store[product_name]
else:
    stores_with_product = None

if stores_with_product:
    # 距離順に並べ替えて表示
    sorted_stores = sorted(stores_with_product, key=lambda store: distance[store])
    for store in sorted_stores:
        print(f"{product_name} {store}: {distance[store]} km")
else:
    print("その商品は見つかりませんでした。")