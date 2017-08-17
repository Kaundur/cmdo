# CMDO
A command line todo list tool using Python and SQLite

![Cmdo](https://user-images.githubusercontent.com/8157119/28658090-9a77f6e0-72a1-11e7-8b5a-1a7c28f9d039.PNG)

## Installation
Python 2 required

Running cmdo.py will create the SQLite database

## Commands
<dl>
  <dt>Default</dt>
  <dd>No parameters will display todo list, or display welcome if there are no items in the list</dd>

  <dt>-welcome</dt>
  <dd>Displays splash screen</dd>
  
  <dt>-add title</dt>
  <dd>add an item to the todo list with a title</dd>

  <dt>-due [id] date</dt>
  <dd>mark an item with a due date, id is optional if passed in with -add</dd>
  <dd>currently accepted date formats are</dd>
</dl>

* YYYY-MM-DD
* DD-MON-YYYY
* DD-MON. Will set the year to the current year, or next year if the date has passed
* Today
* Tomorrow
* Day name [monday to sunday] will set the date to the next date when this day occurs

<dl>  
  <dt>-description [id] description</dt>
  <dd>Add an item description to an item, this is used to store more information on the item and isnt displayed on the main todo list,
  but can instead be accessed by using the command -view id. id is optional if passed in with -add</dd>

  <dt>-done id</dt>
  <dd>Mark an item as done</dd>

  <dt>-undone id</dt>
  <dd>Mark an item as not done</dd>

  <dt>-remove id</dt>
  <dd>Removes an item from the todo list</dd>

  <dt>-view [id]</dt>
  <dd> Defaults to display the todo list, passing id will display extra information on that item</dd>

  <dt>-vacuum</dt>
  <dd> Reorders the table so that there are no numerical gaps between item ids</dd>
<dl>

Tags @ and # can be used to better emphasise a title or description by changing the font color

## Examples
Add "test item" to the todo list

```
>cmdo.py -add test item
1    [ ]       test item
```

Add "test item" with description "new test item" to the todo list

```
>cmdo.py -add test item -description new test item
2    [ ]       test item
```

Add "test item" with due date 20/05/2020

```
>cmdo.py -add test item -due 20-may-2020
3    [ ]       test item                     2020-05-20
```

Add "test item" with due date tomorrow

```
>cmdo.py -add test item -due tomorrow
4   [ ]       test item                     Tomorrow
```

Update due date on item with id 5 to next friday

```
>cmdo.py -due 5 friday
5   [ ]       test item                     Friday
```

Mark item 5 as done

```
>cmdo.py -done 5
5   [x]       test item                     Friday
```
