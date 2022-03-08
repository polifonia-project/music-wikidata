import argparse
import csv
import pickle
import bz2
import tqdm
import itertools


def main(wikidata_path, index_path, new_entities_path):
    KG = dict()
    with open(new_entities_path) as f:
        reader = csv.reader(f, delimiter='\t')
        qids = [row for row in reader]
    with open(index_path, 'rb') as f:
        index = pickle.load(f)
    with bz2.open(wikidata_path, 'rt') as bzinput:
        for i, qid in enumerate(tqdm.tqdm(qids[1:])):
            try:
                linen = index[qid[0]]
                json = next(itertools.islice(bzinput, linen, None))
                KG[qid[0]] = json
                print(qid[0], json['id'])
            except:
                print(qid[0], ' not indexed')
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