
from .window import Window


def main():
    window = Window({
                'name': 'test window',
                'branches': [{
                    'name': 'test branch 1',
                    'branches': [],
                    'leaves':[]
                },{
                    'name': 'test branch 2',
                    'branches': [],
                    'leaves':[]
                },{
                    'name': 'test branch 3',
                    'branches': [],
                    'leaves':[]
                }],
                'leaves':[
                    {'name': 'leaf 1'},
                    {'name': 'leaf a'},
                    {'name': 'leaf b'},
                    {'name': 'leaf c'},
                    {'name': 'leaf d'},
                    {'name': 'leaf e'},
                    {'name': 'leaf f'},
                    {'name': 'leaf g'},
                    {'name': 'leaf h'},
                    {'name': 'leaf i'},
                    {'name': 'leaf j'},
                    {'name': 'leaf k'},
                    {'name': 'leaf x'},
                ]
            }, {
                'margin': 10,
                'column_spacing': 1,
                'row_spacing': 1,
                'max_columns': 5,
                'row_height': 35
            })
    window.draw()
