-- Instalación de demostración preparada para la guía «Añadir OpenStreetMap como mapa de fondo»:
-- quita de todas las aplicaciones el mapa de fondo «OpenStreetMap» que trae la demostración,
-- para que el que crea la guía sea el único con ese nombre. Se puede aplicar más de una vez.
DELETE FROM stm_app_bckg
WHERE abc_backid IN (SELECT bac_id FROM stm_backgrd WHERE bac_name = 'OpenStreetMap');
