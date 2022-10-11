def fleiss_kappa(a: int, w: int, c: int, table):
    """
    a: number of annotators, must be > 1
    w: number of wav/file
    c: number of categories
    table: annotation for each wav/file and each annotator for each category
    :return: float
    """
    
    """
    REMINDER
    < 0            Poor agreement
    0.01 – 0.20    Slight agreement
    0.21 – 0.40    Fair agreement
    0.41 – 0.60    Moderate agreement
    0.61 – 0.80    Substantial agreement
    0.81 – 1.00    Almost perfect agreement 
    """
    agree, pe_list = list(), list()

    for i in range(len(table)):
        agree_value = 0
        for column in table[i]:
            agree_value += column.item() ** 2
        agree_value -= a
        agree.append(round(((1/(a*(a-1)))*agree_value), 2))

    for j in range(c):
        pe_value = 0
        for u in range(len(table)):
            pe_value += table[u][j].item()
        pe_value = pe_value / (w * a)
        pe_list.append(round(pe_value ** 2, 2))
    
    mean_agree = round((1/w) * sum(agree), 2)
    pe = round(sum(pe_list), 2)
    kappa = (mean_agree - pe)/(1 - pe)

    return round(kappa, 2)
