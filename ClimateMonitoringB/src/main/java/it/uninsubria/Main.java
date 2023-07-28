package it.uninsubria;
import it.uninsubria.city.City;
import it.uninsubria.queryhandler.QueryHandler;
import it.uninsubria.util.FakeDataGenerator;
import it.uninsubria.util.Item;

import javax.management.Query;
import java.io.BufferedReader;
import java.io.File;
import java.io.FileReader;
import java.io.IOException;
import java.util.List;
import java.util.LinkedList;
import java.util.Properties;
import java.util.concurrent.ConcurrentHashMap;
import java.sql.*;

public class Main {
    public static void main(String[] args) {

        String url = "jdbc:postgresql://localhost/postgres";
        Properties props = new Properties();
        props.setProperty("user", "postgres");
        props.setProperty("password", "qwerty");
        //props.setProperty("ssl", "true");

        QueryHandler queryHandler = new QueryHandler(url, props);
        queryHandler.selectAllWithCond(QueryHandler.tables.CITY, "country", "United States");
        queryHandler.selectAllWithCond(QueryHandler.tables.CENTRO_MONITORAGGIO, "country", "United States");
        //TODO: operatore è da rifare perchè ci sono dei valori invertiti
        //queryHandler.selectAllWithCond(QueryHandler.tables.OPERATORE, "")
        queryHandler.selectAllWithCond(QueryHandler.tables.OP_AUTORIZZATO, "codice_fiscale", "LNRMTM97L29F205L");
        queryHandler.selectAllWithCond(QueryHandler.tables.AREA_INTERESSE, "stato", "United States");
        //TODO: parametro climatico ha bisogno di query specifiche in quanto
        //le stesse query sono leggermente più complicate, per esempio, hanno bisogno
        //di join o di parametri in più
        //queryHandler.selectAllWithCond(QueryHandler.tables.PARAM_CLIMATICO, "pubdate", )



    }
}