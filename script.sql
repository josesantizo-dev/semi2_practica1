
create database semi1;

use semi1;

select * from temporal;
select * from artista;
select * from genero;
select * from cancion ;
select * from reproduccion;

select count(*) from temporal;
select count(*) from artista;
select count(*) from genero;
select count(*) from cancion;
select count(*) from reproduccion;

#CONSULTA1
select artista.nombre, count(*)
from artista
INNER JOIN reproduccion ON reproduccion.artistaId = artista.artistaId
group by artista.nombre
order by count(*) desc
limit 10
;

#CONSULTA2
select cancion.song, count(*)
from cancion
INNER JOIN reproduccion ON reproduccion.cancionId = cancion.cancionId
group by cancion.song, cancion.duration_ms
order by count(*) desc
limit 10
;

#CONSULTA3
select genero.nombre, count(*)
from genero
INNER JOIN reproduccion ON reproduccion.generoId = genero.generoId
group by genero.nombre
order by count(*) desc
limit 10
;

#CONSULTA4
select artista.artistaId, genero.generoId, artista.nombre, genero.nombre, count(*)
from reproduccion
INNER JOIN artista ON artista.artistaId = reproduccion.artistaId
INNER JOIN genero ON genero.generoId = reproduccion.generoId
group by artista.nombre, genero.nombre
having count(*) = (
select count(*)
from reproduccion
INNER JOIN artista ar ON ar.artistaId = reproduccion.artistaId
INNER JOIN genero gen ON gen.generoId = reproduccion.generoId
where gen.generoId = genero.generoId
group by ar.nombre, gen.nombre
order by count(*) desc
limit 1
)
order by count(*) desc
;

#CONSULTA5
select cancion.cancionId, genero.generoId, cancion.song, genero.nombre, count(*)
from reproduccion
INNER JOIN cancion ON cancion.cancionId = reproduccion.cancionId
INNER JOIN genero ON genero.generoId = reproduccion.generoId
group by cancion.song, genero.nombre, cancion.duration_ms
having count(*) = (
select count(*)
from reproduccion
INNER JOIN cancion can ON can.cancionId = reproduccion.cancionId
INNER JOIN genero gen ON gen.generoId = reproduccion.generoId
where gen.generoId = genero.generoId
group by can.song, gen.nombre, can.duration_ms
order by count(*) desc
limit 1
)
order by count(*) desc
;


#CONSULTA6
select cancion.cancionId, cancion.song, cancion.year, count(*)
from reproduccion
INNER JOIN cancion ON cancion.cancionId = reproduccion.cancionId
group by cancion.song, cancion.duration_ms, cancion.year
having count(*) = (
select count(*)
from reproduccion
INNER JOIN cancion can ON can.cancionId = reproduccion.cancionId
where can.year = cancion.year
group by can.song, can.duration_ms, can.year
order by count(*) desc
limit 1
)
order by count(*) desc
;

#CONSULTA7
select t.nombre, t.popularity
from
(
select artista.nombre , cancion.popularity
from reproduccion
INNER JOIN cancion ON cancion.cancionId = reproduccion.cancionId
INNER JOIN artista ON artista.artistaId = reproduccion.artistaId
group by cancion.popularity, artista.nombre
order by cancion.popularity desc
) as t
group by t.nombre
limit 10
;

#CONSULTA8
select cancion.song, cancion.popularity from cancion
order by popularity desc
limit 10;

#CONSULTA9
select t.nombre, t.popularity
from
(
select genero.nombre , cancion.popularity
from reproduccion
INNER JOIN cancion ON cancion.cancionId = reproduccion.cancionId
INNER JOIN genero ON genero.generoId = reproduccion.generoId
group by cancion.popularity, genero.nombre
order by cancion.popularity desc
) as t
group by t.nombre
limit 5
;

#CONSULTA10
select cancion.cancionId, genero.generoId, cancion.song, genero.nombre, count(*)
from reproduccion
INNER JOIN cancion ON cancion.cancionId = reproduccion.cancionId
INNER JOIN genero ON genero.generoId = reproduccion.generoId
where cancion.explicit LIKE '%True%'
group by cancion.song, genero.nombre, cancion.duration_ms
having count(*) = (
select count(*)
from reproduccion
INNER JOIN cancion can ON can.cancionId = reproduccion.cancionId
INNER JOIN genero gen ON gen.generoId = reproduccion.generoId
where gen.generoId = genero.generoId
and can.explicit LIKE '%True%'
group by can.song, gen.nombre, can.duration_ms
order by count(*) desc
limit 1
)
order by count(*) desc
;