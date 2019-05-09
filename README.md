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
  "row_height": 35
}
```
More options will be added

#### Methods
draw() -> draw the window

### Options
The class Options represents the options allowed to customize the display of the menu
#### Properties
#### Methods

## TODO

## License
GPL-3.0-or-later 
