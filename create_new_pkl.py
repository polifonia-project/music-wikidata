import argparse
import csv
import pickle
import bz2
import tqdm
import json
import itertools


def main(wikidata_path, index_path, new_entities_path):
    KG = dict()
    with open(new_entities_path) as f:
        reader = csv.reader(f, delimiter='\t')
        qids = [row for row in reader]
    with open(index_path, 'rb') as f:
        index = pickle.load(f)
    for i, qid in enumerate(tqdm.tqdm(qids[1:])):
        with bz2.open(wikidata_path, 'rt') as bzinput:
            try:
                linen = index[qid[0]]
                #bzinput.seek(linen)
                #json = next(bzinput)
                json = next(itertools.islice(bzinput, linen, linen+1))
                KG[qid[0]] = json
                assert qid[0] == json['id']
            except:
                print(qid[0], ' error')
    with open('data/wikidata_music_new_entities.pkl', 'wb') as f:
        pickle.dump(KG, f)




if __name__ == '__main__':
    parser = argparse.ArgumentParser()

    # Parameters
    parser.add_argument('--index_path',
                        type=str,
                        default='data/wikidata_index.pkl')
                        #default='/home/rocco/Desktop/python/wiki_parse/data/wikidata_index.pkl')
    parser.add_argument('--wikidata_path',
                        type=str,
                        default='data/data/latest-all.json')
                        #default='/media/4TB/rocco/Wikidata/latest-all.json.bz2')
    parser.add_argument('--new_entities_path',
                        type=str,
                        default='data/objects_item_nosubjects.tsv')
    args = parser.parse_args()
    main(args.wikidata_path, args.index_path, args.new_entities_path)