
class Options:
    def __init__(self, options):
        self._raw_options = options if options else {}
        self._validate()

    def _validate(self):
        o = self._raw_options
        self.margin = o['margin'] if 'margin' in o else 10
        self.column_spacing = o['column_spacing'] if 'column_spacing' in o else 1
        self.row_spacing = o['row_spacing'] if 'row_spacing' in o else 1
        self.max_columns = o['max_columns'] if 'max_coluns' in o else 5
        self.row_height = o['row_height'] if 'row_height' in o and o['row_height'] >= 35 else 35
