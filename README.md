# Advent 2018

## Installation and Requirements
The `requirements.txt` file is only relevant if you're using the download and run scripts in `grab-puzzle-input.py`.
So far, all of the solutions only use the python stdlib, so no installs necessary.

## Use of `grab-puzzle-input.py`
Not super necessary, but it's a slow day at work, so I wrote a little script that downloads the input for you.
All it needs is the value of your session cookie.
To get that (at least on firefox), go to adventofcode.com, open the Storage tab of the developer tools and copy the value field of the session cookie.
Save that to a `.cookie` file (or some other name, in which case you should specify it when using the grab-puzzle-input script).

Basic usage:

```sh
> pip install -r requirements.txt
> python grab-puzzle-input.py -d 1
# Saves the day 1 input to day1_2018.txt

> python grab-puzzle-input.py -d 7 -y 2017
# Saves the day 7 input from 2017 to day7_2017.txt

> python grab-puzzle-input.py -d 3 --cookie-file="some_other_cookie.txt" --output-file="different_day3.txt"
# Loads the cookie value from some_other_cookie.txt and saves the day 3 input to different_day3.txt.
```

Working on adding a `download_all` command that fetches all un-fetched inputs, and a `run day x` command that checks for input, and then calls the `fn1` and `fn2` commands for that day.


## Python Version
As far as I know, I'm only using a single 3.7 specific feature (reading iso formatted dates in day 4). So if you change that line, you can use whatever py3 version you want (I think--have not tested).
But, for the sake of repeatability, I am using 3.7.0.

