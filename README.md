# music-wikidata
This repository contains code and data for extracting the sub-KG about the music domain from Wikidata. 
### *create_bz4kgtk.py*
- It creates a *.bz2* file of json objects (stored into a *.pkl* file) to give as input to KGTK
- once the *.bz2* is created, it can be converted into a KGTK graph with with:
> kgtk import-wikidata -i wikidata_music_entities.bz2 --node nodefile.tsv --edge edgefile.tsv --qual qualfile.tsv --proc 64

### *create_new_pkl.py*
- It uses the Wikidata index to select specific WIkidata entities (specified in a *.txt* file)
- It store the resulting json object into a *.pkl* file that can be used as input for *create_bz4kgtk.py*

### *objects_nosubjects.sh*
- It creates 4 files, starting from the edgefile.tsv of KGTK:
  - objects.tsv storing all objects of the graph
  - subjects.tsv storing all subjects
  - objects_subjects.tsv storing all objects that appear also in subject position
  - objects_nosubjects.tsv storing all objects that do not appear in subject position
- objects_nosubjects.tsv is given as input for *filter_Q_notQ_wd_entities.py*

## Data
Please download the following files into the data folder
- [music entities](https://liveunibo.sharepoint.com/:u:/r/sites/polifonia/Shared%20Documents/WP4/Wikipedia%20corpus-KG/data/wikidata_music_entities.pkl?csf=1&web=1&e=Eqb5Du) (*.pkl*)
- [Wikidata index](https://liveunibo.sharepoint.com/:u:/r/sites/polifonia/Shared%20Documents/WP4/Wikipedia%20corpus-KG/data/wikidata_index.pkl?csf=1&web=1&e=ob6bUH) (*.pkl*)
- a Wikidata json dump from [Wikidata](https://dumps.wikimedia.org/wikidatawiki/entities/) (*.bz2*-*.json*)
