CONSULTA1=('select artista.nombre, count(*)
'from artista'
'INNER JOIN reproduccion ON reproduccion.artistaId = artista.artistaId'
'group by artista.nombre'
'order by count(*) desc'
'limit 10'
';')