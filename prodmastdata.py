import pymysql

class Products:
    #first field is prod_id
    valid_prods = range(1,26)#1->25
    valid_stores = range(1,5)#1->4
    product_data = {
        1:{
            "prod_id": 1
            ,"prod_type": "frozen"
            ,"prod_name":"beans"
            ,"qty":1
            ,"price": 1.50
            ,"price_eff_st_date":"20000101"
            ,"price_eff_ed_date":"30000101"
        },
        2:{
            "prod_id": 2
            ,"prod_type": "food"
            , "prod_name": "zuccini"
            , "qty": 1
            , "price": 1.00
            , "price_eff_st_date": "20000101"
            , "price_eff_ed_date": "30000101"
        },
        3:{
            "prod_id": 3
            ,"prod_type": "office"
            , "prod_name": "pencils"
            , "qty": 12
            , "price": 2.00
            , "price_eff_st_date": "20000101"
            , "price_eff_ed_date": "30000101"
        },
        4:{
            "prod_id": 4
            ,"prod_type": "food"
            , "prod_name": "cake"
            , "qty": 1
            , "price": 5.50
            , "price_eff_st_date": "20000101"
            , "price_eff_ed_date": "30000101"
        },
        5:{
            "prod_id": 5
            ,"prod_type": "cleaning supplies"
            , "prod_name": "method"
            , "qty": 1
            , "price": 3.50
            , "price_eff_st_date": "20000101"
            , "price_eff_ed_date": "30000101"
        },
        6:{
            "prod_id": 6
            ,"prod_type": "apparel"
            , "prod_name": "tie"
            , "qty": 1
            , "price": 10.00
            , "price_eff_st_date": "20000101"
            , "price_eff_ed_date": "30000101"
        },
        7:{
            "prod_id": 7
            ,"prod_type": "office"
            , "prod_name": "paper"
            , "qty": 100
            , "price": 6.00
            , "price_eff_st_date": "20000101"
            , "price_eff_ed_date": "30000101"
        },
        8:{
            "prod_id": 8
            ,"prod_type": "food"
            , "prod_name": "grapes"
            , "qty": 1
            , "price": 1.69
            , "price_eff_st_date": "20000101"
            , "price_eff_ed_date": "30000101"
        },
        9:{
            "prod_id": 9
            ,"prod_type": "cleaning supplies"
            , "prod_name": "tilex"
            , "qty": 1
            , "price": 5.29
            , "price_eff_st_date": "20000101"
            , "price_eff_ed_date": "30000101"
        },
        10:{
            "prod_id": 10
            ,"prod_type": "food"
            , "prod_name": "apples"
            , "qty": 6
            , "price": 2.00
            , "price_eff_st_date": "20000101"
            , "price_eff_ed_date": "30000101"
        },
        11:{
            "prod_id": 11
            ,"prod_type": "apparel"
            , "prod_name": "socks"
            , "qty": 2
            , "price": 3.00
            , "price_eff_st_date": "20000101"
            , "price_eff_ed_date": "30000101"
        },
        12:{
            "prod_id": 12
            ,"prod_type": "cleaning supplies"
            , "prod_name": "clorox"
            , "qty": 1
            , "price": 4.00
            , "price_eff_st_date": "20000101"
            , "price_eff_ed_date": "30000101"
        },
        13:{
            "prod_id": 13
            ,"prod_type": "frozen"
            , "prod_name": "bergers"
            , "qty": 4
            , "price": 2.69
            , "price_eff_st_date": "20000101"
            , "price_eff_ed_date": "30000101"
        },
        14:{
            "prod_id": 14
            ,"prod_type": "food"
            , "prod_name": "protein bars"
            , "qty": 24
            , "price": 7.00
            , "price_eff_st_date": "20000101"
            , "price_eff_ed_date": "30000101"
        },
        15:{
            "prod_id": 15
            ,"prod_type": "office"
            , "prod_name": "notebook"
            , "qty": 3
            , "price": 2.50
            , "price_eff_st_date": "20000101"
            , "price_eff_ed_date": "30000101"
        },
        16:{
            "prod_id": 16
            ,"prod_type": "frozen"
            , "prod_name": "ice cream"
            , "qty": 1
            , "price": 3.50
            , "price_eff_st_date": "20000101"
            , "price_eff_ed_date": "30000101"
        },
        17:{
            "prod_id": 17
            ,"prod_type": "food"
            , "prod_name": "tomatoes"
            , "qty": 4
            , "price": 2.69
            , "price_eff_st_date": "20000101"
            , "price_eff_ed_date": "30000101"
        },
        18:{
            "prod_id": 18
            ,"prod_type": "office"
            , "prod_name": "chair"
            , "qty": 1
            , "price": 30.00
            , "price_eff_st_date": "20000101"
            , "price_eff_ed_date": "30000101"
        },
        19:{
            "prod_id": 19
            ,"prod_type": "cleaning supplies"
            , "prod_name": "finish"
            , "qty": 1
            , "price": 2.99
            , "price_eff_st_date": "20000101"
            , "price_eff_ed_date": "30000101"
        },
        20:{
            "prod_id": 20
            ,"prod_type": "apparel"
            , "prod_name": "shirt"
            , "qty": 1
            , "price": 29.00
            , "price_eff_st_date": "20000101"
            , "price_eff_ed_date": "30000101"
        },
        21:{
            "prod_id": 21
            ,"prod_type": "food"
            , "prod_name": "chips"
            , "qty": 1
            , "price": 5.00
            , "price_eff_st_date": "20000101"
            , "price_eff_ed_date": "30000101"
        },
        22:{
            "prod_id": 22
            ,"prod_type": "frozen"
            , "prod_name": "peas"
            , "qty": 1
            , "price": 3.99
            , "price_eff_st_date": "20000101"
            , "price_eff_ed_date": "30000101"
        },
        23:{
            "prod_id": 23
            ,"prod_type": "office"
            , "prod_name": "binder"
            , "qty": 1
            , "price": 6.00
            , "price_eff_st_date": "20000101"
            , "price_eff_ed_date": "30000101"
        },
        24:{
            "prod_id": 24
            ,"prod_type": "cleaning supplies"
            , "prod_name": "palmolive"
            , "qty": 1
            , "price": 3.50
            , "price_eff_st_date": "20000101"
            , "price_eff_ed_date": "30000101"
        },
        25:{
            "prod_id": 25
            ,"prod_type": "apparel"
            , "prod_name": "jeans"
            , "qty": 1
            , "price": 40.00
            , "price_eff_st_date": "20000101"
            , "price_eff_ed_date": "30000101"
        }
    }

    def getproductdatafromdb(self):
        conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='', db='billingaug2021')
        cursor = conn.cursor()

        cursor.execute("select * from Products;")
        g_prod_lookup_list = [dict(line) for line in
                              [zip([column[0] for column in cursor.description], row) for row in cursor.fetchall()]]

        #create map of prod_id: {}, so it looks same as prod_data
        prod_map = {}
        for prod_lkp in g_prod_lookup_list:
            prod_map[prod_lkp['prod_id']] = prod_lkp

        return (prod_map)


if __name__ == "__main__":
    myproducts = Products()
    myprodmap = myproducts.getproductdatafromdb()
    print(myprodmap)