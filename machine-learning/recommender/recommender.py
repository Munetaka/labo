# refs
# http://www.kamishima.net/archive/recsysdoc.pdf
# http://qiita.com/ynakayama/items/59beb40b7c3829cc0bf2

from mylib import pearson_correlation as pc

# sample data
dataset = {
    '山田': {
        '親子丼': 1.0,
        '牛丼': 3.0,
        'カツ丼': 3.0
        },
    '田中': {
        '牛丼': 1.0,
        '海鮮丼': 3.0
        },
    '佐藤': {
        '親子丼': 2.0,
        '牛丼': 1.0,
        '海鮮丼': 3.0,
        'カツ丼': 1.0
        },
    '鈴木': {
        '親子丼': 1.0,
        '牛丼': 3.0,
        '海鮮丼': 2.0,
        }
    }
def recommend(user):

    totals = {}
    simSums = {}

    for other in dataset:
        if other == user:
            continue

        sim = pc.pearson_correlation(dataset[other], dataset[user])
        if sim <= 0:
            continue

        for item in dataset[other]:
            if item not in dataset[user] or dataset[user][item] == 0:
                # smilality * score
                totals.setdefault(item, 0)
                totals[item] += dataset[other][item] * sim
                # sum of similality
                simSums.setdefault(item, 0)
                simSums[item] += sim

    rankings = [(total / simSums[item], item) for item, total in list(totals.items())]
    rankings.sort()
    rankings.reverse()
    recommendations_list = [(recommend_item, score) for score, recommend_item in rankings]
    return recommendations_list


print('田中さんにオススメのメニュー', recommend('田中'))
