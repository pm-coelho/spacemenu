
from .window import Window
from .options import Options


def main():
    window = Window({
                'label': 'test window',
                'branches': [{
                    'label': 'test branch 1',
                    'branches': [
                        {
                            'label': 'a',
                            'branches':[],
                            'leaves': [
                                {'label': 'a', 'command': 'pass show -c cloud/nextcloud'},
                                {'label': 'a', 'command': 'echo A'},
                            ]
                        },
                    ],
                    'leaves':[
                        {'label': 'a', 'command': 'pass show -c cloud/nextcloud'},
                        {'label': 'a', 'command': 'echo A'},
                    ]
                },{
                    'label': 'test branch 2',
                    'branches': [],
                    'leaves':[
                        {'label': 'a', 'command': 'pass show -c cloud/nextcloud'},
                    ]
                },{
                    'label': 'test branch 3',
                    'branches': [],
                    'leaves':[]
                }],
                'leaves':[
                    {'label': 'a', 'command': 'echo a'},
                    {'label': 'b', 'command': 'echo b'},
                    {'label': 'c', 'command': 'pass show -c avnoconn/jenkins'},
                    {'label': 'd', 'command': 'echo d'},
                    # {'label': 'b'},
                    # {'label': 'b'},
                    # {'label': 'c'},
                    # {'label': 'c'},
                    # {'label': 'd'},
                    # {'label': 'd'},
                    # {'label': 'e'},
                    # {'label': 'e'},
                    # {'label': 'f'},
                    # {'label': 'f'},
                    # {'label': 'g'},
                    # {'label': 'g'},
                    # {'label': 'h'},
                    # {'label': 'h'},
                    # {'label': 'i'},
                    # {'label': 'i'},
                    # {'label': 'j'},
                    # {'label': 'j'},
                    # {'label': 'k'},
                    # {'label': 'k'},
                    # {'label': 'l'},
                    # {'label': 'l'},
                    # {'label': 'm'},
                    # {'label': 'm'},
                    # {'label': 'n'},
                    # {'label': 'n'},
                    # {'label': 'o'},
                    # {'label': 'o'},
                    # {'label': 'p'},
                    # {'label': 'p'},
                    # {'label': 'q'},
                    # {'label': 'q'},
                    # {'label': 'r'},
                    # {'label': 'r'},
                    # {'label': 's'},
                    # {'label': 's'},
                    # {'label': 't'},
                    # {'label': 't'},
                    # {'label': 'u'},
                    # {'label': 'u'},
                    # {'label': 'v'},
                    # {'label': 'v'},
                    # {'label': 'x'},
                    # {'label': 'x'},
                    # {'label': 'y'},
                    # {'label': 'y'},
                    # {'label': 'z'},
                    # {'label': 'z'},
                ]
            },Options({
                'row_height': 100
            }))

    window.draw()
