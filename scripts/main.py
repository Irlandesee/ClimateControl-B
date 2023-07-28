import hashlib
import random
import string
import time
filenameAreaInteresse = "/Users/mattiamac/Documents/Github/ClimateControl-B/data/areeInteresse.dati"
filenameCentroMonitoraggio = "/Users/mattiamac/Documents/Github/ClimateControl-B/data/centroMonitoraggio.dati"
filenameOperatore = "/Users/mattiamac/Documents/Github/ClimateControl-B/data/operatoriRegistrati.dati"
filenameQueries = "/Users/mattiamac/Documents/Github/ClimateControl-B/data/queries.dati"
filenameParamClimatici = "/Users/mattiamac/Documents/Github/ClimateControl-B/data/parametriClimatici.dati"
filenameNoteId = "/Users/mattiamac/Documents/Github/ClimateControl-B/data/noteids.dati"
filenameNoteQueries = "/Users/mattiamac/Documents/Github/ClimateControl-B/data/noteQueries.dati"

centriMonitoraggio = "/Users/mattiamac/Documents/Github/ClimateControl-B/data/centroMonitoraggio.csv"
areeInteresse = "/Users/mattiamac/Documents/Github/ClimateControl-B/data/areeInteresse.csv"

queryAreaInteresse = "insert into areainteresse(areaid, denominazione, stato, latitudine, longitudine) values("
queryCentroMonitoraggio = "insert into centromonitoraggio(centroid, nomecentro, comune, country, aree_interesse_ids) values({}, {}, {}, {}, ARRAY{});"
queryOperatori = "insert into operatore(nome, cognome, codice_fiscale, email, userid, password, centroid) values({}, {}, {}, {}, {}, {}, {});"
queryParamClimatici = "insert into parametro_climatico(parameterid, idcentro, areaid, pubdate, notaid, valore_vento, valore_umidita, valore_pressione, valore_temperatura, valore_precipitazioni, valore_alt_ghiacciai, valore_massa_ghiacciai) values('{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}');"
queryNotaId = "insert into nota_parametro_climatico(notaid, nota_vento, nota_umidita, nota_pressione, nota_temperatura, nota_precipitazioni, nota_alt_ghiacciai, nota_massa_ghiacciai) values('{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}');"
queries = []


def write_queries(queries=[]):
    with open(filenameQueries, "w") as f:
        for query in queries:
            f.write(query)
            f.write("\n")
    f.close()

def write_noteids_to_file(note=[]):
    with open(filenameNoteId, "w") as f:
        for nota in note:
            f.write(nota)
            f.write("\n")
    f.close()

def write_note_queries_to_file(queries=[]):
    with open(filenameNoteQueries, "w") as f:
        for query in queries:
            f.write(query)
            f.write("\n")
    f.close()

def read_centri_ids() ->[]:
    ids = []
    with open(centriMonitoraggio, "r") as f:
        f.readline() #read headers
        for line in f:
            id = line.split(",")[0]
            ids.append(id[1:(len(id)-1)])
    f.close()
    return ids

def read_aree_ids() -> []:
    ids = []
    with open(areeInteresse, "r") as f:
        f.readline()
        for line in f:
            id = line.split(",")[0]
            ids.append(id[1:(len(id)-1)])
    f.close()
    return ids


def generate_area_interesse():
    with open(filenameAreaInteresse, "r") as f:
        f.readline()  # read first line containing the header of the file
        for line in f:
            split_line = line.split(";")
            areaID = "'" + split_line[0] + "'"
            denominazione = "'" + split_line[1] + "'"
            stato = "'" + split_line[2] + "'"
            temp = split_line[3].split(",")
            latitude = "'" + temp[0] + "'"
            longitude = "'" + temp[1].strip() + "'"
            values = areaID + "," + denominazione + "," + stato + "," + latitude + "," + longitude + ");"
            complete_query = queryAreaInteresse + values
            queries.append(complete_query)
    f.close()
    write_queries(queries)


def generate_centri_monitoraggio():
    complete_queries = []
    with open(filenameCentroMonitoraggio, "r") as f:
        f.readline() # read headers
        for line in f:
            temp = line.split(";")
            centroID = "'" + temp[0] + "'"
            nomeCentro = "'" + temp[1] + "'"
            comune = "'" + temp[2] + "'"
            country = "'" + temp[3] + "'"

            aree_interesse_temp = temp[4].strip().split(",")
            aree_interesse_da_aggiungere = []
            for area in aree_interesse_temp:
                if area != "":
                    aree_interesse_da_aggiungere.append(area.strip())
            query = queryCentroMonitoraggio.format(centroID, nomeCentro, comune, country, aree_interesse_da_aggiungere)
            complete_queries.append(query)

    f.close()
    write_queries(complete_queries)

def generate_operatori():
    complete_queries = []
    with open(filenameOperatore, "r") as f:
        f.readline()
        for line in f:
            temp = line.split(";")
            userid = "'" + temp[0] + "'"
            pwd = "'" + temp[1] + "'"
            nome = "'" + temp[2] + "'"
            cognome = "'" + temp[3] + "'"
            cod_fiscale = "'" + temp[4] + "'"
            mail = "'" + temp[5] + "'"
            centro_monitoraggio = "'" + temp[6].strip() + "'"
            query = queryOperatori.format(userid, pwd, nome, cognome, cod_fiscale, mail, centro_monitoraggio)
            complete_queries.append(query)
    f.close()
    write_queries(complete_queries)

def str_time_prop(start, end, time_format, prop):
    s_time = time.mktime(time.strptime(start, time_format))
    e_time = time.mktime(time.strptime(end, time_format))

    p_time = s_time + prop * (e_time - s_time)
    return time.strftime(time_format, time.localtime(p_time))

def generate_random_date(start, end, prop):
    return str_time_prop(start, end, '%m/%d/%Y', prop)


def generate_nota_id():
    return hashlib.sha1((''.join(random.choices(string.ascii_lowercase, k=12)).encode())).hexdigest()

def generate_nota_param(nota_id: str) -> str: 
    nota_vento = ''.join(random.choices(string.ascii_lowercase, k=4))
    nota_umidita = ''.join(random.choices(string.ascii_lowercase, k=4))
    nota_pressione = ''.join(random.choices(string.ascii_lowercase, k=4))
    nota_temperatura = ''.join(random.choices(string.ascii_lowercase, k=4))
    nota_precipitazioni = ''.join(random.choices(string.ascii_lowercase, k=4))
    nota_alt_ghiacciai = ''.join(random.choices(string.ascii_lowercase, k=4))
    nota_massa_ghiacciai = ''.join(random.choices(string.ascii_lowercase, k=4))
    complete_query = queryNotaId.format(nota_id.strip(), nota_vento, nota_umidita, nota_pressione, nota_temperatura, nota_precipitazioni, nota_alt_ghiacciai, nota_massa_ghiacciai)
    return complete_query

#Returns a tuple containing the climate parameter and eventual notes
def generate_param_climatici(centri_ids = [], area_interesse_ids = []):
    queryParamClimatici = "insert into parametro_climatico(parameterid, idcentro, areaid, pubdate, notaid, valore_vento, valore_umidita, valore_pressione, valore_temperatura, valore_precipitazioni, valore_alt_ghiacciai, valore_massa_ghiacciai) values('{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}');"
    parameter_id = hashlib.sha1((''.join(random.choices(string.ascii_lowercase, k=12))
                                 .encode())).hexdigest()
    centro_id = centri_ids.pop()
    area_id = area_interesse_ids.pop()
    nota_id = generate_nota_id()
    nota_pc = generate_nota_param(nota_id)
    data_pub = generate_random_date("1/1/2008", "1/1/2023", random.random())
    valore_vento = random.randint(1, 5)
    valore_umidita = random.randint(1, 5)
    valore_pressione = random.randint(1, 5)
    valore_temperatura = random.randint(1, 5)
    valore_precipitazioni = random.randint(1, 5)
    valore_alt_ghiacciai = random.randint(1, 5)
    valore_massa_ghiacciai = random.randint(1, 5)
    queryCompleta = queryParamClimatici.format(parameter_id, centro_id, area_id, data_pub, nota_id, valore_vento, valore_umidita, valore_pressione, valore_temperatura, valore_precipitazioni, valore_alt_ghiacciai, valore_massa_ghiacciai)
    return (queryCompleta, nota_pc)

def main():
    queries_pc = []
    queries_note = []
    centri_ids = read_centri_ids()
    aree_ids = read_aree_ids()
    
    print("lunghezza centri: "+str(len(centri_ids)))
    print("lunghezza aree: "+str(len(aree_ids)))
    for i in range(0, len(centri_ids)):
       query = generate_param_climatici(centri_ids, aree_ids)
       queries_pc.append(query[0])
       queries_note.append(query[1])
       #print(query)
    write_note_queries_to_file(queries_note)
    write_queries(queries_pc)
        

main()
