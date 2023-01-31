import requests
import json
import os

# could be used to generate classes in a type safe language like C++, C# or Java
# currently not used
def generate_by_value_type(value):
  value_type = type(value)
  if value_type == str:
    return str(value)
  elif value_type == int:
    return int(value)
  elif value_type == float:
    return float(value)
  elif value_type == bool:
    return bool(value)
  elif value_type == list:
    return list(value)
  elif value_type == dict:
    return dict(value)
  else:
    return None

def main():
  # Get DDragon the latest version
  ddragon_version = requests.get('https://ddragon.leagueoflegends.com/api/versions.json').json()[0]

  # Get list of champions
  champions_list = requests.get(f'http://ddragon.leagueoflegends.com/cdn/{ddragon_version}/data/en_US/champion.json').json()['data']

  # for each champion, get the element key string to lowercase
  champions = []
  for champion in champions_list:
    champions.append(str(champion).lower())

  for champion in champions:
    data = requests.get(f'https://raw.communitydragon.org/latest/game/data/characters/{champion}/{champion}.bin.json').json()
    champ_spells = {}

    # get data key and value
    for key, value in data.items():
      if 'Spells/' not in key:
        continue

      if 'mScriptName' not in value:
        continue

      if 'mSpell' not in value:
        continue

      mScriptName = value['mScriptName']
      mSpell = value['mSpell']

      champ_spells[mScriptName] = {}
      for k, v in mSpell.items():
        value_type = type(v)
        champ_spells[mScriptName].update({k: v})
    
    # create data folder if not exists
    if not os.path.exists('./data'):
      os.makedirs('./data')
    
    with open(f'./data/{champion}.json', 'w') as f:
      json.dump(champ_spells, f, indent=2)

  print('Done!')

if __name__ == "__main__":
  main()
