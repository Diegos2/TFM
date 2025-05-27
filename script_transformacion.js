//conn = new Mongo("mongodb://localhost:27017/");
//db = conn.getDB("TFM");

db.humedad_5a.updateMany(
     {},
     { $unset: { fechaobservacion: 1 } }
);

db.humedad_5a.updateMany(
     {},
     { $unset: { nombreestacion: 1 } }
);

db.humedad_5a.updateMany(
     {},
     { $unset: { codigosensor: 1 } }
);

print("Campos eliminados");

db.humedad_5a.updateMany(
     { departamento: 'ARCHIPIELAGO DE SAN ANDRES PROVIDENCIA Y SANTA CATALINA' },
     { $set: { departamento: 'ARCHIPIELAGO DE SAN ANDRES, PROVIDENCIA Y SANTA CATALINA'}}
);

db.humedad_5a.updateMany(
     { departamento: 'SAN ANDRES PROVIDENCIA' },
     { $set: { departamento: 'ARCHIPIELAGO DE SAN ANDRES, PROVIDENCIA Y SANTA CATALINA'}}
);

db.humedad_5a.updateMany(
     { departamento: 'BOGOTA' },
     { $set: { departamento: 'BOGOTA D.C.'}}
);

db.humedad_5a.updateMany(
     { municipio: 'BOGOTA, D.C' },
     { $set: { municipio: 'BOGOTA D.C.'}}
);

db.humedad_5a.updateMany(
     { departamento: 'CUNDINAMARCA',
       municipio: 'BOGOTA D.C.'
     },
     { $set: { departamento: 'BOGOTA D.C.'}}
);

db.humedad_5a.updateMany(
     { municipio: 'CARTAGENA' },
     { $set: { municipio: 'CARTAGENA DE INDIAS'}}
);

db.humedad_5a.updateMany(
     { municipio: 'PATIA (EL BORDO)' },
     { $set: { municipio: 'PATIA'}}
);

db.humedad_5a.updateMany(
     { municipio: 'PATIA (EL BORDO)' },
     { $set: { municipio: 'PATIA'}}
);

db.humedad_5a.updateMany(
     { municipio: 'PURACE (COCONUCO)' },
     { $set: { municipio: 'PURACE'}}
);

db.humedad_5a.updateMany(
     { municipio: 'ALTO BAUDO (PIE DE PATO)' },
     { $set: { municipio: 'ALTO BAUDO'}}
);

db.humedad_5a.updateMany(
     { municipio: 'BAHIA SOLANO (MUTIS)' },
     { $set: { municipio: 'BAHIA SOLANO'}}
);

db.humedad_5a.updateMany(
     { municipio: 'BOJAYA (BELLAVISTA)' },
     { $set: { municipio: 'BOJAYA'}}
);

db.humedad_5a.updateMany(
     { municipio: 'CARMEN DEL DARIEN  (CURBARADO)' },
     { $set: { municipio: 'CARMEN DEL DARIEN'}}
);

db.humedad_5a.updateMany(
     { municipio: 'MEDIO ATRATO (BETE)' },
     { $set: { municipio: 'MEDIO ATRATO'}}
);

db.humedad_5a.updateMany(
     { municipio: 'ARIGUANI (EL DIFICIL)' },
     { $set: { municipio: 'EL DIFICIL'}}
);

db.humedad_5a.updateMany(
     { municipio: 'ARIGUANI (EL DIFICIL)' },
     { $set: { municipio: 'EL DIFICIL'}}
);

print("Documentos actualizados.");

conn.close();