
from .window import Window


def main():
    window = Window({
                'name': 'test window',
                'branches': [{
                    'name': 'test branch 1',
                    'branches': [],
                    'leaves':[
                    {'name': 'a', 'command': 'pass show -c cloud/nextcloud'},
                    {'name': 'a', 'command': 'a'},
                    ]
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
                    {'name': 'a', 'command': lambda x: 'a'},
                    {'name': 'a', 'command': lambda x: 'a'},
                    # {'name': 'b'},
                    # {'name': 'b'},
                    # {'name': 'c'},
                    # {'name': 'c'},
                    # {'name': 'd'},
                    # {'name': 'd'},
                    # {'name': 'e'},
                    # {'name': 'e'},
                    # {'name': 'f'},
                    # {'name': 'f'},
                    # {'name': 'g'},
                    # {'name': 'g'},
                    # {'name': 'h'},
                    # {'name': 'h'},
                    # {'name': 'i'},
                    # {'name': 'i'},
                    # {'name': 'j'},
                    # {'name': 'j'},
                    # {'name': 'k'},
                    # {'name': 'k'},
                    # {'name': 'l'},
                    # {'name': 'l'},
                    # {'name': 'm'},
                    # {'name': 'm'},
                    # {'name': 'n'},
                    # {'name': 'n'},
                    # {'name': 'o'},
                    # {'name': 'o'},
                    # {'name': 'p'},
                    # {'name': 'p'},
                    # {'name': 'q'},
                    # {'name': 'q'},
                    # {'name': 'r'},
                    # {'name': 'r'},
                    # {'name': 's'},
                    # {'name': 's'},
                    # {'name': 't'},
                    # {'name': 't'},
                    # {'name': 'u'},
                    # {'name': 'u'},
                    # {'name': 'v'},
                    # {'name': 'v'},
                    # {'name': 'x'},
                    # {'name': 'x'},
                    # {'name': 'y'},
                    # {'name': 'y'},
                    # {'name': 'z'},
                    # {'name': 'z'},
                ]
            }, {
                'margin': 10,
                'column_spacing': 1,
                'row_spacing': 1,
                'max_columns': 5,
                'row_height': 35
            })
    window.draw()
