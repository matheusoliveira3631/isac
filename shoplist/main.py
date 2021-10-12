import os
import threading

import plotly.graph_objects as go
from tinydb import TinyDB, Query

from .display import image_viewer
#======================><==============================#
if __name__ != "__main__":
    path=os.getcwd()
    np=path+'/src'
    os.chdir(np)
#======================><==============================#
class shopping_list:
    
    def __init__(self, name:str):
        global db, shopping
        db=name+'.json'
        shopping=TinyDB(db)
        return 
    
    def clear(self):
        shopping.truncate()
        return True

    def delete(self):
        os.remove(db)

    def add(self, item, qty):
        shopping.insert({'item':item, 'quantity':qty})
        return True

    def write_img(self):
        items=[]
        values=[]
        if 'table.png' in os.listdir():
            os.remove('table.png')
        for key in shopping.all():
            items.append(key['item'])
            values.append(key['quantity'])
        fig = go.Figure(data=[go.Table(
            header=dict(values=['Produtos', 'Quantidade'],
                        line_color='darkslategray',
                        fill_color='lightskyblue',
                        align='center'),
            cells=dict(values=[items, # 1st column
                                values], # 2nd column
                    line_color='darkslategray',
                    fill_color='lightcyan',
                    align='left'))
        ])
        fig.write_image("table.png", engine="kaleido")
        viewer=image_viewer('table.png')
        viewer.show()

    def show(self):
        x=threading.Thread(target=self.write_img)
        x.run()


