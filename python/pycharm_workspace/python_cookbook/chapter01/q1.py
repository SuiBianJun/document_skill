
def get_avg_score(data):
    """
    使用*获取N个序列解压值
    :param data: all score
    :return: remove first and last, then cacl avg score
    """
    first, *scores, last = data
    return sum(scores) / len(scores)

avg_score = get_avg_score([1, 2, 3, 4])
print("avg score = " + str(avg_score)) # 2.5