#temporal

DROP_TABLES=('DROP TABLE if exists temporal;')

TEMPORAL_CREATION=('CREATE TABLE temporal('
    'artist VARCHAR(50),'
    'song VARCHAR(500),'
    'duration_ms int,'
    'explicit VARCHAR(50),'
    'year int,'
    'popularity decimal(10,4),'
    'danceability decimal(10,4),'
    'energy decimal(10,4),'
    'llave int,' 
    'loudness decimal(10,4),'
    'mode decimal(10,4),'
    'speechiness decimal(10,4),'
    'acousticness decimal(10,4),'
    'instrumentalness decimal(10,7),'
    'liveness decimal(10,4),'
    'valence decimal(10,4),'
    'tempo decimal(10,4),'
    'genre varchar(50) );')

LLENADO_TEMPORAL = ('INSERT INTO temporal ('
						'artist,'
						'song,'
						'duration_ms,'
						'explicit,'
						'year,'
						'popularity,'
						'danceability,'
						'energy,'
						'llave,' 
						'loudness,'
						'mode,'
						'speechiness,'
						'acousticness,'
						'instrumentalness,'
						'liveness,'
						'valence,'
						'tempo,'
						'genre )'
						'VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);'
						)

#Artista

DROP_ARTISTA=('DROP TABLE if exists artista CASCADE;')

CREAR_ARTISTA=('CREATE TABLE artista('
    'artistaId int NOT NULL AUTO_INCREMENT,'
    'nombre varchar(50),'
    'PRIMARY KEY (artistaId)'
    ');')

LLENAR_ARTISTA=('INSERT INTO artista(nombre)'
'SELECT DISTINCT artist '
'FROM temporal'
';')

#Género

DROP_GENERO=('DROP TABLE if exists genero CASCADE;')

CREAR_GENERO=('CREATE TABLE genero('
    'generoId int NOT NULL AUTO_INCREMENT,'
    'nombre varchar(50),'
    'PRIMARY KEY (generoId)'
    ');')

LLENAR_GENERO=('INSERT INTO genero(nombre)'
'SELECT DISTINCT genre '
'FROM temporal'
';')

#Canción

DROP_CANCION=('DROP TABLE if exists cancion CASCADE;')

CREAR_CANCION=('CREATE TABLE cancion('
    'cancionId int NOT NULL AUTO_INCREMENT,'
    'song VARCHAR(500),'
    'duration_ms int,'
    'explicit VARCHAR(50),'
    'year int,'
    'popularity decimal(10,4),'
    'danceability decimal(10,4),'
    'energy decimal(10,4),'
    'llave int,' 
    'loudness decimal(10,4),'
    'mode decimal(10,4),'
    'speechiness decimal(10,4),'
    'acousticness decimal(10,4),'
    'instrumentalness decimal(10,7),'
    'liveness decimal(10,4),'
    'valence decimal(10,4),'
    'tempo decimal(10,4),'
    'PRIMARY KEY (cancionId)'
    ');')

LLENAR_CANCION=('INSERT INTO cancion ('
						'song,'
						'duration_ms,'
						'explicit,'
						'year,'
						'popularity,'
						'danceability,'
						'energy,'
						'llave,' 
						'loudness,'
						'mode,'
						'speechiness,'
						'acousticness,'
						'instrumentalness,'
						'liveness,'
						'valence,'
						'tempo )'
						'SELECT '
                        'song,'
						'duration_ms,'
						'explicit,'
						'year,'
						'popularity,'
						'danceability,'
						'energy,'
						'llave,' 
						'loudness,'
						'mode,'
						'speechiness,'
						'acousticness,'
						'instrumentalness,'
						'liveness,'
						'valence,'
						'tempo '
                        'FROM temporal '
                        'GROUP BY artist, song'
                    ';')

#Reproducción

DROP_REPRODUCCION=('DROP TABLE if exists reproduccion CASCADE;')

CREAR_REPRODUCCION=('CREATE TABLE reproduccion('
    'reproduccionId int NOT NULL AUTO_INCREMENT,'
    'artistaId int,'
    'generoId int,'
    'cancionId int,'
    'PRIMARY KEY (reproduccionId),'
    'FOREIGN KEY (artistaId) REFERENCES artista(artistaId),'
    'FOREIGN KEY (generoId) REFERENCES genero(generoId),'
    'FOREIGN KEY (cancionId) REFERENCES cancion(cancionId)'
    ');')

LLENAR_REPRODUCCION=('INSERT INTO reproduccion(artistaId, generoId, cancionId)'
'SELECT'
'(SELECT artistaId FROM artista WHERE artista.nombre = temporal.artist LIMIT 1),'
'(SELECT generoId FROM genero WHERE genero.nombre = temporal.genre LIMIT 1),'
'(SELECT cancionId FROM cancion WHERE cancion.song = temporal.song and cancion.duration_ms = temporal.duration_ms LIMIT 1) '
'FROM temporal'
';')