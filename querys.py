CONSULTA1=('select artista.nombre, count(*) '
'from artista '
'INNER JOIN reproduccion ON reproduccion.artistaId = artista.artistaId '
'group by artista.nombre '
'order by count(*) desc '
'limit 10'
';')

CONSULTA2=('select genero.nombre, count(*) '
'from genero '
'INNER JOIN reproduccion ON reproduccion.generoId = genero.generoId '
'group by genero.nombre '
'order by count(*) desc '
'limit 10'
';')