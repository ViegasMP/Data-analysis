import datetime

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


def barplot_all_combinations():
    for x in fields:
        for hue in fields:
            if x == hue:
                continue
            ''''segmentar'''
            # df = df[df['c_region'] == 'ASIA']

            '''calcular'''
            somas = df.groupby([x, hue]).sum()
            somas.reset_index(inplace=True)

            encomendas = df.groupby([x, hue]).count()
            encomendas.reset_index(inplace=True)

            '''plot'''
            plt.figure(figsize=(12, 8))
            sns.barplot(x=x, y='l_quantity', data=somas, hue=hue)
            plt.title('Products sold by %s and %s' % (mapping[x], mapping[hue]))
            plt.ylabel('# products sold')
            plt.xticks(rotation=70)
            plt.show()

            '''plot'''
            plt.figure(figsize=(12, 8))
            sns.barplot(x=x, y='revenue', data=somas, hue=hue)
            plt.title('Revenue by %s and %s' % (mapping[x], mapping[hue]))
            plt.xticks(rotation=70)
            plt.show()

            '''plot'''
            plt.figure(figsize=(12, 8))
            sns.barplot(x=x, y='revenue', data=encomendas, hue=hue)
            plt.title('Number of orders by %s and %s' % (mapping[x], mapping[hue]))
            plt.ylabel('# orders')
            plt.xticks(rotation=70)
            plt.show()


def plot_weekday():
    x = 'dayofweek'
    hue = 'c_region'
    ''''segmentar'''
    # df = df[df['c_region'] == 'ASIA']

    '''calcular'''
    somas = df.groupby([x, hue]).sum()
    somas.reset_index(inplace=True)

    '''calcular'''
    medias = df.groupby([x, hue]).sum()
    medias.reset_index(inplace=True)

    encomendas = df.groupby([x, hue]).count()
    encomendas.reset_index(inplace=True)

    orderlist = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

    '''plot'''
    plt.figure(figsize=(12, 8))
    sns.barplot(x=x, y='l_quantity', data=somas, hue=hue, order=orderlist)
    plt.title('Products sold by %s and %s' % (mapping[x], mapping[hue]))
    plt.ylabel('# products sold')
    plt.xticks(rotation=70)
    plt.show()

    '''plot'''
    plt.figure(figsize=(12, 8))
    sns.barplot(x=x, y='revenue', data=somas, hue=hue, order=orderlist)
    plt.title('Revenue by %s and %s' % (mapping[x], mapping[hue]))
    plt.xticks(rotation=70)
    plt.show()

    '''plot'''
    plt.figure(figsize=(12, 8))
    sns.barplot(x=x, y='revenue', data=encomendas, hue=hue, order=orderlist)
    plt.title('Number of orders by %s and %s' % (mapping[x], mapping[hue]))
    plt.ylabel('# orders')
    plt.xticks(rotation=70)
    plt.show()


def plot_sellingseason():
    x = 'sellingseason'
    hue = 'c_region'
    ''''segmentar'''
    # df = df[df['c_region'] == 'ASIA']

    '''calcular'''
    somas = df.groupby([x, hue]).sum()
    somas.reset_index(inplace=True)

    '''calcular'''
    medias = df.groupby([x, hue]).sum()
    medias.reset_index(inplace=True)

    encomendas = df.groupby([x, hue]).count()
    encomendas.reset_index(inplace=True)

    '''plot'''
    plt.figure(figsize=(12, 8))
    sns.barplot(x=x, y='l_quantity', data=somas, hue=hue)
    plt.title('Products sold by %s and %s' % (mapping[x], mapping[hue]))
    plt.ylabel('# products sold')
    plt.xticks(rotation=70)
    plt.show()

    '''plot'''
    plt.figure(figsize=(12, 8))
    sns.barplot(x=x, y='revenue', data=somas, hue=hue)
    plt.title('Revenue by %s and %s' % (mapping[x], mapping[hue]))
    plt.xticks(rotation=70)
    plt.show()

    '''plot'''
    plt.figure(figsize=(12, 8))
    sns.barplot(x=x, y='revenue', data=encomendas, hue=hue)
    plt.title('Number of orders by %s and %s' % (mapping[x], mapping[hue]))
    plt.ylabel('# orders')
    plt.xticks(rotation=70)
    plt.show()


def plot_orderpriority():
    x = 'l_orderpriority'
    hue = 'c_region'
    ''''segmentar'''
    # df = df[df['c_region'] == 'ASIA']

    '''calcular'''
    somas = df.groupby([x, hue]).sum()
    somas.reset_index(inplace=True)

    encomendas = df.groupby([x, hue]).count()
    encomendas.reset_index(inplace=True)

    '''plot'''
    plt.figure(figsize=(12, 8))
    sns.barplot(x=x, y='l_quantity', data=somas, hue=hue)
    plt.title('Products sold by %s and %s' % (mapping[x], mapping[hue]))
    plt.ylabel('# products sold')
    plt.xticks(rotation=70)
    plt.show()

    '''plot'''
    plt.figure(figsize=(12, 8))
    sns.barplot(x=x, y='revenue', data=somas, hue=hue)
    plt.title('Revenue by %s and %s' % (mapping[x], mapping[hue]))
    plt.xticks(rotation=70)
    plt.show()

    '''plot'''
    plt.figure(figsize=(12, 8))
    sns.barplot(x=x, y='revenue', data=encomendas, hue=hue)
    plt.title('Number of orders by %s and %s' % (mapping[x], mapping[hue]))
    plt.ylabel('# orders')
    plt.xticks(rotation=70)
    plt.show()


def plot_region_sales():
    for x in ['c_region', 's_region']:
        ''''segmentar'''
        # df = df[df['c_region'] == 'ASIA']

        '''calcular'''
        somas = df.groupby(x).sum()
        somas.reset_index(inplace=True)

        encomendas = df.groupby(x).count()
        encomendas.reset_index(inplace=True)

        '''plot'''
        plt.figure(figsize=(12, 8))
        # sns.barplot(x=x, y='l_quantity', data=somas)
        plt.pie(somas['l_quantity'], labels=somas[x], autopct='%1.1f%%')
        plt.title('Products sold by %s' % (mapping[x],))
        plt.ylabel('# products sold')
        plt.xticks(rotation=70)
        plt.show()

        '''plot'''
        plt.figure(figsize=(12, 8))
        plt.pie(somas['revenue'], labels=somas[x], autopct='%1.1f%%')
        plt.title('Revenue by %s' % (mapping[x],))
        plt.xticks(rotation=70)
        plt.show()

        '''plot'''
        plt.figure(figsize=(12, 8))
        plt.pie(encomendas['revenue'], labels=somas[x], autopct='%1.1f%%')
        plt.title('Number of orders by %s' % (mapping[x]))
        plt.ylabel('# orders')
        plt.xticks(rotation=70)
        plt.show()


def describe_sales():
    x = 'sellingseason'
    hue = 'c_region'
    somas = df.groupby([x, hue])['revenue']
    print(somas.describe())


def plot_sales_over_time():
    x = 'orderdate'
    hue = 'p_category'
    window = 15
    ''''segmentar'''
    # df = df[df['c_region'] == 'ASIA']

    '''calcular'''
    somas = df.groupby([x, hue]).sum()
    somas = somas.rolling(window=window).mean()
    somas.reset_index(inplace=True)

    encomendas = df.groupby([x, hue]).count()
    encomendas.reset_index(inplace=True)

    '''plot'''
    plt.figure(figsize=(12, 8))
    sns.lineplot(x=x, y='revenue', data=somas, hue=None)
    plt.title('Revenue moving average %d days by %s' % (window, mapping[hue],))
    plt.ylabel('Revenue')
    plt.show()


if __name__ == '__main__':
    fields = ['p_name', 'p_brand', 'p_category', 'c_name', 'c_nation', 'c_region', 's_name', 's_nation', 's_region', 'dayofweek', 'month', 'sellingseason', 'lastdayinmonthfl', 'holidayfl', 'weekdayfl', 'l_orderpriority', 'l_shipmode']
    titles = ['Product Name', 'Product Brand', 'Product Category', 'Customer Name','Customer Nation', 'Customer Region', 'Supplier Name','Supplier Nation', 'Supplier Region', 'Day of Week', 'Month', 'Selling Season', 'IsLastDayInMonth', 'IsHoliday', 'IsWeekDay', 'Order Priority', 'Shipping Mode']
    mapping = {k: v for k, v in zip(fields, titles)}

    df = pd.concat([pd.read_csv('../data/ssbana1998_6.txt', sep='\t'), pd.read_csv('../data/ssbana1999_6.txt', sep='\t')])
    df.columns = [s.strip() for s in df.columns]
    df['revenue'] = df['l_ordertotalprice'] * (100 - df['l_discount']) * (100 - df['l_tax']) / 100 / 100


    dates = [datetime.datetime.strptime('%04d-%02d-%02d' % (y, m, d), '%Y-%m-%d') for y, m, d in zip(df['year'], df['monthnuminyear'], df['daynuminmonth'])]
    df['orderdate'] = dates

    # barplot_all_combinations()
    plot_weekday()
    # plot_sellingseason()
    # plot_orderpriority()
    # plot_region_sales()
    # plot_sales_over_time()

    pd.set_option('display.max_columns', None)
    pd.set_option('display.width', None)
    # print(df.groupby('year')[['l_ordertotalprice', 'l_supplycost', 'revenue']].describe())

    # print(describe_sales())
