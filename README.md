## Setup

* create and start virtualenv
* `pip install -r requirements_dev.txt` (if you want to run tests)
* `pip install -r requirements.txt` (if you only want to run  the app)

## Testing

* From root directory `pytest tests`

## List of commands

* Show female percentage in population
`python command_line_interface.py female_percentage`

* Show male percentage in population
`python command_line_interface.py male_percentage`

* Show female average age in population
`python command_line_interface.py female_age_average`

* Show male average age in population
`python command_line_interface.py male_age_average`

* Show people average age in population
`python command_line_interface.py people_age_average`

* Show 'N' most popular cities
`python command_line_interface.py most_popular_cities N`

* Show 'N' most common passwords
`python command_line_interface.py most_common_password N`

* Show people born before date A and after date B (dates in format XXXX-MM-DD)
`python command_line_interface.py show_people_born_before_and_after_date A B`

* Show people born beetwen dates A and B (dates in format XXXX-MM-DD)
`python command_line_interface.py show_people_born_between_dates A B`

* Show the most secure password/passwords (passwords with highest points value)
`python command_line_interface.py get_best_passwords`