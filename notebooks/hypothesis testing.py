import datetime

import numpy as np
import pandas as pd
import scikit_posthocs
from matplotlib import pyplot as plt
from scipy.stats import shapiro, bartlett, f_oneway, kruskal

import scipy.stats as st


def hypothesis_client_region():
    alfa = 0.01
    normal = True
    print("Testing H0: Região do Cliente não afeta a capacidade de venda")
    # calcular a receita por cidade, cada região fica com cerca de 40 cidades
    somas = df.groupby(['c_city', 'c_region']).sum()
    somas.reset_index(inplace=True)
    samples = []
    for region in np.unique(somas['c_region']):
        sample = somas[somas['c_region'] == region]['revenue']
        samples.append(list(sample))
        st, p = shapiro(sample)
        print(region, st, p)
        if p < alfa:
            print("NOT normal")
            normal = False
        else:
            print("normal")

    if normal:
        bt, p = bartlett(*samples)
        print(bt, p)
        if p < alfa:
            print("Unequal variances")
            normal = False
        else:
            print("Equal variances")

    test = f_oneway if normal else kruskal
    print("Testing H0: Região do Cliente não afeta a capacidade de venda")
    print("Using %s" % (test.__name__,))
    t, p = test(*samples)
    print(t, p)
    if p < alfa:
        print("Reject H0")
    else:
        print("Accept H0")


def hypothesis_dayofweek():
    alfa = 0.01
    normal = True
    print("Testing H0: Existe diferença de vendas entre dias da semana")
    # calcular a receita por cidade, cada região fica com cerca de 40 cidades
    somas = df.groupby(['dayofweek', 'weeknuminyear', 'year']).sum()
    somas.reset_index(inplace=True)

    somas.boxplot(column='revenue', by='dayofweek')
    plt.show()

    samples = []
    for dayofweek in np.unique(somas['dayofweek']):
        sample = somas[somas['dayofweek'] == dayofweek]['revenue']
        samples.append(list(sample))
        st, p = shapiro(sample)
        print(dayofweek, st, p)
        print("sample size: %d" % len(sample))
        if p < alfa:
            print("NOT normal")
            normal = False
        else:
            print("normal")

    if normal:
        bt, p = bartlett(*samples)
        print(bt, p)
        if p < alfa:
            print("Unequal variances")
            normal = False
        else:
            print("Equal variances")

    test = f_oneway if normal else kruskal
    print("Testing H0: Região do Cliente não afeta a capacidade de venda")
    print("Using %s" % (test.__name__,))
    t, p = test(*samples)
    print(t, p)
    if p < alfa:
        print("Reject H0")
    else:
        print("Accept H0")


def hypothesis_shipping():
    alfa = 0.01
    normal = True
    print("Testing H0: Existe diferença de utilização para cada shipping mode")
    # calcular a receita por cidade, cada região fica com cerca de 40 cidades
    somas = df.groupby(['l_shipmode', 'weeknuminyear', 'year']).sum()
    somas.reset_index(inplace=True)

    somas.boxplot(column='revenue', by='l_shipmode')
    plt.show()

    samples = []
    names = []
    for shipmode in np.unique(somas['l_shipmode']):
        sample = somas[somas['l_shipmode'] == shipmode]['l_quantity']
        samples.append(list(sample))
        names.append(shipmode)
        st, p = shapiro(sample)
        print(shipmode, st, p)
        print("sample size: %d" % len(sample))
        if p < alfa:
            print("NOT normal")
            normal = False
        else:
            print("normal")

    if normal:
        bt, p = bartlett(*samples)
        print(bt, p)
        if p < alfa:
            print("Unequal variances")
            normal = False
        else:
            print("Equal variances")

    test = f_oneway if normal else kruskal
    print("Testing H0: Região do Cliente não afeta a capacidade de venda")
    print("Using %s" % (test.__name__,))
    t, p = test(*samples)
    print(t, p)
    if p < alfa:
        print("Reject H0")
        n, s = [], []
        for k, v in zip(names, samples):
            n += [k] * len(v)
            s += v
        samples = pd.DataFrame({'shipmode': n, 'values': s})
        ph = scikit_posthocs.posthoc_dunn(samples, p_adjust='bonferroni', group_col='shipmode', val_col='values')
        print(ph)
    else:
        print("Accept H0")


def confidence_interval_sales_per_month():
    somas = df.groupby(['c_city', 'month']).sum()
    somas.reset_index(inplace=True)
    sample = list(somas['revenue'])
    print(somas['revenue'].describe())
    for alfa in [0.9, 0.95, 0.99]:
        print('alfa = %f' % alfa)
        print('%.2e, %.2e' % st.t.interval(alpha=alfa, df=len(sample) - 1, loc=np.mean(sample), scale=st.sem(sample)))

    somas.boxplot(column='revenue', by='month')
    plt.xticks(rotation=70)
    plt.tight_layout()
    plt.show()


if __name__ == '__main__':
    pd.set_option('display.max_columns', None)
    pd.set_option('display.width', None)

    fields = ['p_name', 'p_brand', 'p_category', 'c_name', 'c_nation', 'c_region', 's_name', 's_nation', 's_region', 'dayofweek', 'month', 'sellingseason', 'lastdayinmonthfl', 'holidayfl', 'weekdayfl', 'l_orderpriority', 'l_shipmode']
    titles = ['Product Name', 'Product Brand', 'Product Category', 'Customer Name', 'Customer Nation', 'Customer Region', 'Supplier Name', 'Supplier Nation', 'Supplier Region', 'Day of Week', 'Month', 'Selling Season', 'IsLastDayInMonth', 'IsHoliday', 'IsWeekDay', 'Order Priority', 'Shipping Mode']
    mapping = {k: v for k, v in zip(fields, titles)}

    df = pd.concat([pd.read_csv('../data/ssbana1998_6.txt', sep='\t'), pd.read_csv('../data/ssbana1999_6.txt', sep='\t')])
    df.columns = [s.strip() for s in df.columns]
    df['revenue'] = df['l_ordertotalprice'] * (100 - df['l_discount']) * (100 - df['l_tax']) / 100 / 100

    dates = [datetime.datetime.strptime('%04d-%02d-%02d' % (y, m, d), '%Y-%m-%d') for y, m, d in zip(df['year'], df['monthnuminyear'], df['daynuminmonth'])]
    df['orderdate'] = dates

    # hypothesis_client_region()
    # hypothesis_dayofweek()
    hypothesis_shipping()
    # confidence_interval_sales_per_month()
