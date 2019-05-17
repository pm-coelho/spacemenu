from numbers import Number

class Options:
    def __init__(self, options):
        self._raw_options = options if options else {}
        self._parse()
        self._set_defaults()
        self._validate_limits()
        self._convert_types()


    def _parse(self):
        o = self._raw_options
        self.inner_margin = o['inner_margin'] if 'inner_margin' in o else None
        self.column_spacing = o['column_spacing'] if 'column_spacing' in o else None
        self.row_spacing = o['row_spacing'] if 'row_spacing' in o else None
        self.max_columns = o['max_columns'] if 'max_columns' in o else None
        self.row_height = o['row_height'] if 'row_height' in o else None
        self.font = o['font'] if 'font' in o else None
        self.margin_left = o['margin_left'] if 'margin_left' in o else None
        self.margin_right = o['margin_right'] if 'margin_right' in o else None
        self.margin_bottom = o['margin_bottom'] if 'margin_bottom' in o else None
        self.background_color = o['background_color'] if 'background_color' in o else None
        self.button_background_color = o['button_background_color'] if 'button_background_color' in o else None
        self.button_text_color = o['button_text_color'] if 'button_text_color' in o else None


    def _set_defaults(self):
        self.inner_margin = self.inner_margin or 10
        self.column_spacing = self.column_spacing or 1
        self.row_spacing = self.row_spacing or 1
        self.max_columns = self.max_columns or 5
        self.row_height = self.row_height or 35
        self.margin_left = self.margin_left or 0
        self.margin_right = self.margin_right or 0
        self.margin_bottom = self.margin_bottom or 0


    def _validate_limits(self):
        if (self.row_height < 35):
            raise ValueError('Options.row_height minimum value is 35')


    def _convert_types(self):
        self.inner_margin = int(self.inner_margin)
        self.column_spacing = int(self.column_spacing)
        self.row_spacing = int(self.row_spacing)
        self.max_columns = int(self.max_columns)
        self.row_height = int(self.row_height)
        self.margin_left = int(self.margin_left)
        self.margin_right = int(self.margin_right)
        self.margin_bottom = int(self.margin_bottom)

        if(self.background_color and self.background_color[0] == '#'):
            self.background_color = self.background_color[1:]

        if(self.button_background_color and self.button_background_color[0] == '#'):
            self.button_background_color = self.button_background_color[1:]

        if(self.button_text_color and self.button_text_color[0] == '#'):
            self.button_text_color = self.button_text_color[1:]


    def get_dictionary(self):
        return {
            'inner_margin': self.inner_margin,
            'column_spacing': self.column_spacing,
            'row_spacing': self.row_spacing,
            'max_columns': self.max_columns,
            'row_height': self.row_height,
            'background_color': self.background_color,
            'button_background_color': self.button_background_color,
            'button_text_color': self.button_text_color,
            'font': self.font,
            'margin_left': self.margin_left,
            'margin_right': self.margin_right,
            'margin_bottom': self.margin_bottom,
        }
