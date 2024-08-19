# importando a biblioteca da web
from tqdm import tqdm 
import time

# exibe uma barra de carregamento
for i in tqdm(range(100)):
    time.sleep(0.05)
