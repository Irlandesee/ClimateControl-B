``create table parametroclimatico(
	parameterid varchar(100) primary key,
	idcentro varchar(100) not null,
	areaid varchar(100) not null,
	pubdate date not null,
	valore_vento smallint constraint vento_check (valore_vento > 0 and valore_vento < 6),
	valore_umidita smallint constraint umidita_check (valore_umidita > 0 and valore_umidita < 6),
	valore_pressione smallint constraint pressione_check (valore_pressione > 0 and valore_pressione < 6),
	valore_temperatura smallint constraint temperatura_check (valore_temperatura > 0 and valore_temperatura < 6),
	valore_precipitazioni smallint constraint precipitazioni_check (valore_precipitazioni > 0 and valore_precipitazioni < 6),
	valore_alt_ghiacciai smallint constraint alt_ghiacciai_check (valore_alt_ghiacciai > 0 and valore_alt_ghiacciai < 6),
	valore_massa_ghiacciai smallint constraint valore_massa_ghiacciai (valore_massa_ghiacciai > 0 and valore_massa_ghiacciai < 6)
);``

``
create table operatore_registrato(
	userid varchar(100) not null,
	password varchar(100) not null,
	centroid varchar(100) not null,
	foreign key(centroid) references centromonitoraggio(centroid)
);
`` 

``java
	public void uploadGeonames(){
        LinkedList<City> cities = new LinkedList<City>();
        try {
            BufferedReader bReader = new BufferedReader(new FileReader(new File("/Users/mattiamac/Documents/Github/ClimateControl-B/data/geonames-and-coordinates.csv")));
            String line = bReader.readLine();
            while((line = bReader.readLine()) != null){
                String[] tokens = line.split(";");
                String[] coords = tokens[tokens.length-1].split(",");
                City c = new City(tokens[0],
                        tokens[1],
                        tokens[2],
                        tokens[3],
                        Float.parseFloat(coords[0]),
                        Float.parseFloat(coords[1]));
                cities.add(c);
            }
            bReader.close();
        }catch(IOException ioe){ioe.printStackTrace();}
        String query = "insert into city(geoname_id, ascii_name, country, country_code, latitude, longitude) values(?,?,?,?,?,?)";
        try{
            Connection conn = DriverManager
                    .getConnection(this.dbUrl, props);
            PreparedStatement statement = conn.prepareStatement(query);
            int count = 0;
            for(City c : cities){
                statement.setString(1, c.getGeonameID());
                statement.setString(2, c.getAsciiName());
                statement.setString(3, c.getCountry());
                statement.setString(4, c.getCountryCode());
                statement.setFloat(5, c.getLatitude());
                statement.setFloat(6, c.getLongitude());
                statement.addBatch();
                count++;
                if(count % 100 == 0 || count == cities.size()) {
                    System.out.println("Executing batch");
                    statement.executeBatch();
                }
            }
        }catch(SQLException sqle){sqle.printStackTrace();}
    }

``
