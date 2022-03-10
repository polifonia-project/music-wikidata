import argparse
import csv
import pickle
import bz2
import tqdm
import json

def main(wikidata_path, new_entities_path):
    KG = dict()
    with open(new_entities_path) as f:
        reader = csv.reader(f, delimiter='\t')
        qids = [row[0] for row in reader]
    written = 0
    with bz2.open(wikidata_path, 'rt') as bzinput:
        for i, entry in enumerate(tqdm.tqdm(bzinput, total=96000000)):
            try:
                data = json.loads(entry[:-2])
                if data['id'] in qids:
                    KG[data['id']] = data
                    written = 0
            except:
                continue
            if len(KG.keys()) % 1000 == 0 and len(KG.keys()) != 0 and written == 0:
                with open('data/wikidata_music_new_entities_lazy.pkl', 'wb') as f:
                    pickle.dump(KG, f)
                    written = 1
            if len(KG) == len(qids):
                break
    with open('data/wikidata_music_new_entities_lazy.pkl', 'wb') as f:
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
    main(args.wikidata_path, args.new_entities_path)



