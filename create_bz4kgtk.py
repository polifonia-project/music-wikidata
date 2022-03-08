import json
import bz2
import pickle
import argparse

def main(pkl_path, bz2_path):
    with open(pkl_path, 'rb') as f:
        wikidata_jsons = pickle.load(f)
    print(len(wikidata_jsons))
    jsons = []
    for i, j in enumerate(wikidata_jsons.values()):
        jsons.append(j)

    wikidata_json_list = [json.dumps(j) for j in jsons]
    with bz2.open(bz2_path, 'wt') as f:
        f.write('\n'.join(wikidata_json_list))

if __name__ == '__main__':
    parser = argparse.ArgumentParser()

    # Parameters
    parser.add_argument('--pkl_path',
                        type=str,
                        default='data/wikidata_music_entities.pkl')
    parser.add_argument('--bz2_path',
                        type=str,
                        default='data/wikidata_music_entities.bz2')
    args = parser.parse_args()
    main(args.pkl_path, args.bz2_path)