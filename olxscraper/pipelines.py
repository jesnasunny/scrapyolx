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
