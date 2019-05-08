
from .window import Window


def main():
    window = Window({
                'label': 'SpaceMenu',
                'branches': [{
                    'label': 'branch 1',
                    'branches': [
                        {
                            'label': 'branch 1.1',
                            'branches':[],
                            'leaves': [
                                {'label': 'leaf 1.1.1', 'command': 'echo leaf 1.1.1'},
                                {'label': 'leaf 1.1.2', 'command': 'echo leaf 1.1.2'},
                            ]
                        },
                    ],
                    'leaves':[
                        {'label': 'leaf 1.1', 'command': 'echo leaf 1.1'},
                        {'label': 'leaf 1.2', 'command': 'echo leaf 1.2'},
                    ]
                },{
                    'label': 'branch 2',
                    'branches': [],
                    'leaves':[
                        {'label': 'leaf 2.1', 'command': 'echo leaf 2.1'},
                    ]
                },{
                    'label': 'branch 3',
                    'branches': [],
                    'leaves':[]
                }],
                'leaves':[
                    {'label': 'leaf 1', 'command': 'echo leaf 1'},
                    {'label': 'leaf 2', 'command': 'echo leaf 2'},
                    {'label': 'leaf 3', 'command': 'echo leaf 3'},
                    {'label': 'leaf 4', 'command': 'echo leaf 4'},
                    {'label': 'leaf 5', 'command': 'echo leaf 5'},
                    {'label': 'leaf 6', 'command': 'echo leaf 6'},
                    {'label': 'leaf 7', 'command': 'echo leaf 7'},
                    {'label': 'leaf 8', 'command': 'echo leaf 8'},
                    {'label': 'leaf 9', 'command': 'echo leaf 9'},
                    # {'label': 'leaf 10', 'command': 'echo leaf 10'},
                    # {'label': 'leaf 11', 'command': 'echo leaf 11'},
                    # {'label': 'leaf 12', 'command': 'echo leaf 12'},
                    # {'label': 'leaf 13', 'command': 'echo leaf 13'},
                    # {'label': 'leaf 14', 'command': 'echo leaf 14'},
                    # {'label': 'leaf 15', 'command': 'echo leaf 15'},
                    # {'label': 'leaf 16', 'command': 'echo leaf 16'},
                    # {'label': 'leaf 17', 'command': 'echo leaf 17'},
                    # {'label': 'leaf 18', 'command': 'echo leaf 18'},
                    # {'label': 'leaf 19', 'command': 'echo leaf 19'},
                    # {'label': 'leaf 20', 'command': 'echo leaf 20'},
                    # {'label': 'leaf 21', 'command': 'echo leaf 21'},
                    # {'label': 'leaf 22', 'command': 'echo leaf 22'},
                    # {'label': 'leaf 23', 'command': 'echo leaf 23'},
                    # {'label': 'leaf 24', 'command': 'echo leaf 24'},
                    # {'label': 'leaf 25', 'command': 'echo leaf 25'},
                    # {'label': 'leaf 26', 'command': 'echo leaf 26'},
                    # {'label': 'leaf 27', 'command': 'echo leaf 27'},
                    # {'label': 'leaf 28', 'command': 'echo leaf 28'},
                    # {'label': 'leaf 29', 'command': 'echo leaf 29'},
                    # {'label': 'leaf 30', 'command': 'echo leaf 30'},
                    # {'label': 'leaf 31', 'command': 'echo leaf 31'},
                    # {'label': 'leaf 32', 'command': 'echo leaf 32'},
                    # {'label': 'leaf 33', 'command': 'echo leaf 33'},
                    # {'label': 'leaf 34', 'command': 'echo leaf 34'},
                    # {'label': 'leaf 35', 'command': 'echo leaf 35'},
                    # {'label': 'leaf 35', 'command': 'echo leaf 36'},
                    # {'label': 'leaf 37', 'command': 'echo leaf 37'},
                    # {'label': 'leaf 38', 'command': 'echo leaf 38'},
                    # {'label': 'leaf 39', 'command': 'echo leaf 39'},
                    # {'label': 'leaf 40', 'command': 'echo leaf 40'},
                    # {'label': 'leaf 41', 'command': 'echo leaf 41'},
                    # {'label': 'leaf 42', 'command': 'echo leaf 42'},
                    # {'label': 'leaf 43', 'command': 'echo leaf 43'},
                    # {'label': 'leaf 44', 'command': 'echo leaf 44'},
                    # {'label': 'leaf 45', 'command': 'echo leaf 45'},
                    # {'label': 'leaf 46', 'command': 'echo leaf 46'},
                    # {'label': 'leaf 47', 'command': 'echo leaf 47'},
                    # {'label': 'leaf 48', 'command': 'echo leaf 48'},
                    # {'label': 'leaf 49', 'command': 'echo leaf 49'},
                    # {'label': 'leaf 50', 'command': 'echo leaf 50'},
                ]
            })

    window.draw()
