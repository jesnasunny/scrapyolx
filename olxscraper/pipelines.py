# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


class OlxscraperPipeline:
    def process_item(self, item, spider):

#         class OlxscraperPipeline:
#     def process_item(self, item, spider):

#         adapter=ItemAdaptertem(item)
#         field_names=adapter.field_names()
#         for field_name in field_names:
#             if field_name!="description":
#                 value=adapter.get(field_name)
#                 adapter[field_name]=value.strip()
        
        # property_idstring=adapter.get(property_id)
        # split_string=property_idstring.split('(')
        # if len(split_string)<2:
        #     adapter['property_id']=0
        # else:
        #     pro_array=split_string[1].split(' ')
        #     adapter


        # num=adapter.get('property_id')


        # adapter['property_id']=int(num)


        # return item

        return item
# import mysql.connector
# class SaveToMySqlPipeline:

#     def __init__(self):
#         self.conn=mysql.connector.connect(
#             host='localhost',
#             user='',
#             password='',
#             database='olxnew'
#         )
#         self.cur=self.conn.cursor("""
#         CREATE TABLE IF NOT EXISTS books(
#             id int NOT NULL auto_increment,
#             property_name VARCHAR(400),
#             property_id INTEGER,
#             breadcrumbs VARCHAR(100),
#             price INTEGER,
#             image_url VARCHAR(350),
#             location VARCHAR(300),
#             bathrooms INTEGER,
#             bedrooms INTEGER,
#             PRIMARY KEY (id)

#         )
#         """)
#         self.cur.execute("""insert into olxnew(
#             property_name ,
#             property_id ,
#             breadcrumbs,
#             price ,
#             image_url,
#             location ,
#             bathrooms ,
#             bedrooms ,
            


#         )values(
#             %s,
#             %s,
#             %s,
#             %s,
#             %s,
#             %s,
#             %s,
#             %s

#         )""",(
#             item["property_name"],
#             item["property_id"],
#             item["breadcrumbs"],
#             item["price"],
#             item["image_url"],
#             item["location"],
#             item["bathrooms"],
#             item["bedrooms"],






#         ))
#         self.conn.commit()
#         return item
#     def close_spider(self,spider):
#         self.cur.close()
#         self.conn.close()

