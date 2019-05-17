# SpaceMenu

## Description
SpaceMenu is a python module inspired by the [spacemacs](http://spacemacs.org) "space menu". 
Designed to be used as a laucher for i3wm

## Dependencies
gtk-3.0

## Installation
```bash
pip install spacemenu
```

## Usage

### Window
The class Window represents the menu window itself

```python
from spacemenu import Window
window = Window(root, options)
```

##### Parameters
root -> A dictionary with the desired display information in the following schema:
```
{
  "label": 'title of the window',
  "branches": [
    {
      "label": "label for the first branch",
      "branches": [],
      "leaves": []
    }
  ],
  "leaves": [
    { "label": "label for leaf 1", "command": "shell command to be executed""}
  ]
}
```
so, a branch can contain other branches or leaves, and each leaf executes a command.


options -> Options can either be a dictonary or an Options object
```
{
  "margin": 10,
  "column_spacing": 1,
  "row_spacing": 1,
  "max_columns": 5,
  "row_height": 35,
  "margin_left": 0,
  "margin_right": 0,
  "margin_bottom": 0,
  "background_color": "#ffffff"
  "button_background_color": "#ffffff"
  "button_text_color": "#ffffff"
  "font": "italic bold 12px Georgia, serif",
}
```
More options will be added

#### Methods
draw() -> draw the window

### Options
#### Outer Shape
  * margin_left: Sets outer left margin (in px)
  * margin_right: Sets outer right margin (in px)
  * margin_bottom: Sets outer bottom margin (in px)

#### Inner Shap
  * inner_margin: Inner margin for the window
  * column_spacing: Spacing between each column
  * row_spacing: Spacing between each row
  * max_columns: Maximum number of columns to display
  * row_height: The height of the buttons in each row
  * font: Font to be used by the labels
  
#### Colors
  * background_color: The color for the window background (#rrggbb)
  * button_background_color: The color for the button background (#rrggbb)
  * button_text_color: The color for the text of the buttons(#rrggbb)

## TODO

## License
GPL-3.0-or-later 
