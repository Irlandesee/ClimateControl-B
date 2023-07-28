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
        //To generate new data
        /**
        FakeDataGenerator dataGen = new FakeDataGenerator(10000);
        ConcurrentHashMap<String, Item> map = dataGen.getNewTestMap();
        map.forEach((id, item) -> {
            System.out.println(id + "=> " +item);
        });
         **/

        //Query
        String query = "CREATE TABLE Item(" +
                "itemID VARCHAR(100) PRIMARY KEY," +
                "val NUMERIC NOT NULL);";
        String insertQuery = "INSERT INTO Item(itemid, val) VALUES(?, ?)";

        //popola il database
        String url = "jdbc:postgresql://localhost/postgres";
        Properties props = new Properties();
        props.setProperty("user", "postgres");
        props.setProperty("password", "qwerty");
        //props.setProperty("ssl", "true");

        QueryHandler queryHandler = new QueryHandler(url, props);
        //queryHandler.printMap();
        /**
        try {
            Connection conn = DriverManager.getConnection(url, props);
            Statement statement = conn.createStatement();
            map.forEach((id, item) -> {
                String tmp = "'" +id + "'" + "," + "'" + item.getVal() +"'"+");";
                String completeQuery = insertQuery + tmp;
                //System.out.println(completeQuery);
                try {
                    ResultSet res = statement.executeUpdate(completeQuery);
                    System.out.printf("Executing {%s} : [%s]\n", query, res.toString());
                }catch(SQLException sqle){sqle.printStackTrace();}
            });
        }catch(SQLException sqle){sqle.printStackTrace();}
         **/
        /**
        try{
            Connection conn = DriverManager.getConnection(url, props);
            PreparedStatement stat = conn.prepareStatement(insertQuery);
            map.forEach((key, val) -> {
                try{
                    stat.setString(1, val.getID());
                    stat.setInt(2, val.getVal());
                    stat.addBatch();
                    stat.executeBatch();
                }catch(SQLException sqleException){sqleException.printStackTrace();}
            });

        }catch(SQLException sqle){sqle.printStackTrace();}
         **/
        /**
        String selectQuery = "select i.itemid, i.val from Item i where i.val > 50000 AND i.val < 100000";
        try{
           Connection conn = DriverManager.getConnection(url, props);
           PreparedStatement stat = conn.prepareStatement(selectQuery);
           ResultSet res = stat.executeQuery();
           while(res.next()){
               System.out.printf("{%s} -> {%d}\n", res.getString("itemid"), res.getInt("val"));
           }

        }catch(SQLException sqle){sqle.printStackTrace();}
         **/
        //queryHandler.selectAll(QueryHandler.tables.CITY, "country_code", "IT")
    }
}