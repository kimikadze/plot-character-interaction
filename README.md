# Character Interaction Plotting with Graphviz and Python

Use the code in this repo to quickly create a PDF document with an undirected graph showing which characters in a book interact with each other.

An example of such a graph is shown on the image below.



## Dependencies

To run the program, you need `graphviz` both as a Python library and as system library installed on your machine.

Install the Python library: `pip install graphviz`

Then, go to the official Graphviz page and download a binary for your OS: https://graphviz.org/download/; unpack it.

> Add Graphviz folder to your PATH after installation.

Edit path to Graphviz bin folder in the code:

```python
os.environ["PATH"] += os.pathsep + <path_to_graphviz_bin>.
```

## Running the program

The program takes as input:
* a book file in plain `txt` format
* a text file with character names. Each name should be on a separate line. Because the program does not implement reliable NER, it is better if you use names of a single token.

Run it as:

```bash
python run.py book.txt names.txt
```
> Make sure that the `book.txt` and `names.txt` files are in the same directory as the `run.py` file.

The program will output a PDF file with an undirected graph that shows character interactions with a weight associated with each interaction.
