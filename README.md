# chronodexpy
 generate a chronodex of your day (and mood) in python

## Usage
- Create two subdirectories `./data/` and  `./figures/`.
- Construct a 24hr time table of your day using the format `hour, agenda, mood`.  That is, each line of this file represents one hour of the chronodex, delimited by comma.    The dictionary for the agenda is:
    1 chore
    2 food
    3 fun
    4 meeting
    5 sleep
    6 surf
    7 text
    8 work
- Save the time table to `./data/filename.txt`.
- Execute  `python3 chronodex.py filename` and the chronodex  is saved in `./figures/filename.png`.

An example time table can be found in `./data/20191108.txt` with its corresponding chronodex in `./figures/20191108.png`
## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update the example as appropriate.

## Credits
Inspired by Scription's [chronodex](https://scription.typepad.com/) and Jón's [implementation in ruby](https://github.com/jontg/Chronodex).

## License
[MIT](https://choosealicense.com/licenses/mit/)