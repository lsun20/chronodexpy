# chronodexpy
 generate a chronodex of your day (and mood) in python


20191108.txt


python3 chronodex.py 20191108

# chronodexpy
 generate a chronodex of your day in python
 
## Usage
- Create two subdirectories `./data/` and  `./figures/`
- Create a 24hr time table of your day using the format 'hr, agenda code, mood' 
    The dictionary for agenda is the follows
    1 chore
    2 food
    3 fun
    4 meeting
    5 sleep
    6 surf
    7 text
    8 work
- Save the time table to ./data/ under *filename.txt*
- Execute 
```python
python3 chronodex.py *filename*

```
and the chronodex *filename.png*  is saved in `./figures/`
## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[MIT](https://choosealicense.com/licenses/mit/)