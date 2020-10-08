import re
from graphviz import Graph
from math import log
import os
import sys

os.environ["PATH"] += os.pathsep + 'path_to_graphviz_bin_folder'

class BookGraph:

    def __init__(self,sentences): 
        super(BookGraph, self).__init__()
        self.text = sentences
        self.names = {} 
        self.output = open("temp_output.txt","w")
        self.candidates = set()


    def write_output(self):
        for i in self.candidates:
            self.output.write(i+"\n")
        self.output.close()


    def read_dictionary(self, dictionary):
        self.dictionary = dictionary
        for name in open(self.dictionary,encoding="utf-8"):
            self.names[name.strip()] = 1 

        return self.names 


    def read_text(self):
        with open(self.text,encoding="utf-8") as text:
            for line in text:
                line = line.strip()
                sentences = re.split(r'(?<!\w\.\w.)(?<![A-Z][a-z]\.)(?<=\.|\?)\s', line)
                for sentence in sentences:
                    sentence = sentence.split()
            
                    yield sentence


    def coocurence_counts(self, iterator):
        Mentions = {}
        Coocurrences = {}

        for n,line in enumerate(iterator):
            names = []
            for token in line:
                if token in self.names:
                    names.append(token)
                    Mentions[n] = names

        for i in self.names:
            Coocurrences[i] = []
            for k,v in Mentions.items():
                if len(v) > 1:
                    if i in v:
                        v = set(v)
                        v.remove(i)
                        v = list(v)
                        if not len(v) == 0:
                            Coocurrences[i].append(v)

        for k,v in Coocurrences.items():
            total = {}
            for each in v:
                for character in each:
                    if not character in total:
                        total[character] = 1
                    else:
                        total[character] += 1
            yield k,total


    def finalize_network(self, iterator):
        temp = []
        for i in iterator:
            for e,c in i[1].items():
                temp.append((i[0],e,str(c)))
        sorting = []
        for t in temp:
            sorting.append(sorted(t))
        network = set(tuple(i) for i in sorting)
        network = [list(elem) for elem in network]
        network = sorted(network,key=lambda x: int(x[0]))
        cooc_mapping = {network[i][1]:[(round(log(int(network[j][0])),4),network[j][2]) \
            for j in range(len(network)) if network[j][1] == network[i][1]] \
            for i in range(len(network))} 

        return cooc_mapping


    def visualize(self, mapping):
        # number of letters should correspond to the number of names in the dict.
        labels = ['A','B','C','D','E','F','G'] 
        to_viz = []
        for tag,name in zip(labels,self.names):
            to_viz.append([tag,name]) # e.g. ['A','Olga']

        Nodes = dict()
        nodes = []

        for i in to_viz:
            Nodes[i[1]] = i[0]
            nodes.append((i[0],i[1]))

        edges = [] # edges for visualization, e.g. [AB,AC,...]
        weights = [] #log transformed counts for each edge
        for k,v in mapping.items():
            for each in v:
                edge = "%s%s" %(Nodes[k],Nodes[each[1]])
                edges.append(edge)
                weights.append(each[0])

        dot = Graph() #graphviz class
        for node in nodes:
            dot.node(str(node[0]),str(node[1]))
        for edge,w in zip(edges,weights):
            dot.edge(edge[0],edge[1],label=str(w))

        dot.render("Interaction of characters in %s.gv" %book, view=True)


if __name__=='__main__':
    book = sys.argv[1]
    names = sys.argv[2]
    start = BookGraph(book)
    start.read_dictionary(names)
    text = start.read_text()
    counts = start.coocurence_counts(text)
    data = start.finalize_network(counts)
    start.visualize(data)
