# Character Interaction Plotting with Graphviz and Python

You the code in this repo to quickly create a PDF document with a graph showing which characters in a book interact with each other.

An example of such a graph is shown on the image below.

## Dependencies

To run the program, you need `graphviz` both as a Python library and as system library installed on your machine.

Install the Python library: `pip install graphviz`

Then, go to the official Graphviz page and download a binary for your OS: https://graphviz.org/download/.

> Add Graphviz folder to your PATH after installation.

## Running the program

The program takes as input:
* a book file in plain `txt` format
* a text file with character names. Each name should be on a separate line. Because the program does not implement reliable NER, it is better if you use names of a single token.
