…

# Librería necesaria para utilizar Normalizar datos
from sklearn.preprocessing import MinMaxScaler

…

# Función normalizadora
scaler = MinMaxScaler()

# Normalizamos y convertimos a DataFrame las 2 primeras 
# características del dataset
g1 = scaler.fit_transform(X.iloc[:, :2])
g1d = pd.DataFrame(g1, columns = ['HISTORIA_COD','FECNAC'])

…