-- Instalación de demostración preparada para la guía «Añadir OpenStreetMap como mapa de fondo».
-- La demostración ya trae un mapa de fondo, una capa y un servicio llamados «OpenStreetMap»:
-- se quitan de las aplicaciones y se renombran, para que los que crea la guía sean los únicos
-- con ese nombre. start-sitmun.sh lo aplica una sola vez.
DELETE FROM stm_app_bckg
WHERE abc_backid IN (SELECT bac_id FROM stm_backgrd WHERE bac_name = 'OpenStreetMap');
UPDATE stm_backgrd SET bac_name = 'OpenStreetMap (demostración)', bac_active = false
WHERE bac_name = 'OpenStreetMap';
UPDATE stm_geoinfo SET geo_name = 'OpenStreetMap (demostración)' WHERE geo_name = 'OpenStreetMap';
UPDATE stm_service SET ser_name = 'OpenStreetMap (demostración)' WHERE ser_name LIKE 'OpenStreetMap%';
