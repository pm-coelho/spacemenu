from numbers import Number

class Options:
    def __init__(self, options):
        self._raw_options = options if options else {}
        self._parse()
        self._set_defaults()
        self._validate_limits()
        self._validate_types()


    def _parse(self):
        o = self._raw_options
        self.margin = o['margin'] if 'margin' in o else None
        self.column_spacing = o['column_spacing'] if 'column_spacing' in o else None
        self.row_spacing = o['row_spacing'] if 'row_spacing' in o else None
        self.max_columns = o['max_columns'] if 'max_coluns' in o else None
        self.row_height = o['row_height'] if 'row_height' in o else None


    def _set_defaults(self):
        self.margin = self.margin or 10
        self.column_spacing = self.column_spacing or 1
        self.row_spacing = self.row_spacing or 1
        self.max_columns = self.max_columns or 5
        self.row_height = self.row_height or 35


    def _validate_limits(self):
        if (self.row_height < 35):
            raise ValueError('Options.row_height minimum value is 35')


    def _validate_types(self):
        if not isinstance(self.margin, Number):
            raise ValueError('Expected Options.margin to be a Number')
        if not isinstance(self.column_spacing, Number):
            raise ValueError('Expected Options.column_spacing to be a Number')
        if not isinstance(self.row_spacing, Number):
            raise ValueError('Expected Options.margin to be a Number')
        if not isinstance(self.max_columns, Number):
            raise ValueError('Expected Options.max_columns to be a Number')
        if not isinstance(self.row_height, Number):
            raise ValueError('Expected Options.row_height to be a Number')


    def get_dictionary(self):
        return {
            'margin': self.margin,
            'column_spacing': self.column_spacing,
            'row_spacing': self.row_spacing,
            'max_columns': self.max_columns,
            'row_height': self.row_height
        }
