# chronodexpy
 generate an annotated chronodex of your day (and mood) in Python

## Usage
- Install `NumPy` and `Matplotlib`.
- Create two subdirectories `./data/` and  `./figures/`.
- Construct a 24hr time table of your day using the format `hour, agenda, mood, notes`.  That is, each line of this file represents one hour of the chronodex, delimited by comma, with notes overlay (if provided).    You can define your own agenda set e.g. `{chore, food, fun, meeting, sleep, surf, work}`.  The length of this set is currently capped at eight, by the size of the color palette I constructed (will add more).
- Make sure the first hour is filled. But to repeat the previous hour's agenda (or mood), just leave the entry blank.
- Save the time table to `./data/filename.txt`.
- Execute  `python3 chronodex.py filename` and the chronodex  is saved in `./figures/filename.png`.

An example time table can be found in `./data/20191113.txt` with its corresponding chronodex in `./figures/20191113.png`
## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update the example as appropriate.

## Credits
Inspired by Scription's [chronodex](https://scription.typepad.com/) and Jón's [implementation in ruby](https://github.com/jontg/Chronodex).

## License
[MIT](https://choosealicense.com/licenses/mit/)