# SQLGO
## Dependencies
 - `sqlite3`
 - `csv`
 - `from prettytable import from_db_cursor`

## Functions
 - `display_that(column_name, value)`
   - displays specific lines
 - `display_all()`
   - displays entire stylized table
 - `insert_csv(filename)`
   - insert a csv file for table
 - `insert_standard(values)` 
   - insert values
 - `modify(column_name, value, car_id)`
   - change values
 - `delete(car_id)`
   - delete values by id

### Note:
This module only works for the cars.db database as of right now.

