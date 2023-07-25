filenameAreaInteresse = "/Users/mattiamac/Documents/Github/ClimateControl-B/data/areeInteresse.dati"
filenameCentroMonitoraggio = "/Users/mattiamac/Documents/Github/ClimateControl-B/data/centroMonitoraggio.dati"
filenameQueries = "/Users/mattiamac/Documents/Github/ClimateControl-B/data/queries.dati"
queryAreaInteresse = "insert into areainteresse(areaid, denominazione, stato, latitudine, longitudine) values("
queryCentroMonitoraggio = "insert into centromonitoraggio(centroid, nomecentro, comune, country, aree_interesse_ids) values({}, {}, {}, {}, ARRAY{});"
queries = []


def write_queries(queries=[]):
    with open(filenameQueries, "w") as f:
        for query in queries:
            f.write(query)
            f.write("\n")
    f.close()


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



def main():
    generate_centri_monitoraggio()

main()
