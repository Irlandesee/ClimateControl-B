package it.uninsubria.queryhandler;
import it.uninsubria.areaInteresse.AreaInteresse;
import it.uninsubria.centroMonitoraggio.CentroMonitoraggio;
import it.uninsubria.city.City;
import it.uninsubria.operatore.Operatore;
import it.uninsubria.operatore.OperatoreAutorizzato;
import it.uninsubria.parametroClimatico.ClimateParameter;
import it.uninsubria.util.Item;

import java.sql.*;
import java.util.LinkedList;
import java.util.Properties;
import java.util.concurrent.ConcurrentHashMap;

public class QueryHandler extends Thread{

    //number of slaves currently active
    private static int slaveCounter = 0;
    private ConcurrentHashMap<String, Item> itemConcurrentMap;

    public enum tables{
        AREAINTERESSE,
        CENTROMONITORAGGIO,
        CITY,
        NOTA_PARAM_CLIMATICO,
        OPERATORE,
        OP_AUTORIZZATO,
        PARAM_CLIMATICO
    };

    private String dbUrl;
    private Properties props;


    public QueryHandler(String url, Properties props){
        this.dbUrl = url;
        this.props = props;
    }

    public void run(){}

    //non thread-safe methods
    private void initCache(){

    }
    //thread safe methods
    public synchronized void printMap(){
        this.itemConcurrentMap.forEach((key, value) -> {
            System.out.printf("{%s} -> {%d}\n", value.getID(), value.getVal());
        });
    }

    public void selectObjectWithCond(String oggetto, tables table, String fieldCond, String cond){
        switch(table){
            case CITY -> {
                Worker w = new Worker(dbUrl, props, "workerCity");
                try(ResultSet res = w.selectObjFromCityWithCond(oggetto, fieldCond, cond)){
                    //TODO
                }catch(SQLException sqle){sqle.printStackTrace();}
            }
            case CENTROMONITORAGGIO -> {
                Worker w = new Worker(dbUrl, props, "workerCM");
                try(ResultSet res = w.selectObjFromCMWithCond(oggetto, fieldCond, cond)){
                    //TODO
                }catch(SQLException sqle){sqle.printStackTrace();}
            }
            case OPERATORE -> {
                Worker w = new Worker(dbUrl, props, "workerOP");
                try(ResultSet res = w.selectObjFromOPWithCond(oggetto, fieldCond, cond)){
                    //TODO
                }catch(SQLException sqle){sqle.printStackTrace();}
            }
            case OP_AUTORIZZATO -> {
                Worker w = new Worker(dbUrl, props, "workerAuthOP");
                try(ResultSet res = w.selectObjFromAuthOPWithCond(oggetto, fieldCond, cond)){
                    //TODO
                }catch(SQLException sqle){sqle.printStackTrace();}
            }
            case AREAINTERESSE -> {
                Worker w = new Worker(dbUrl, props, "workerAI");
                try(ResultSet res = w.selectObjFromAIWithCond(oggetto, fieldCond, cond)){
                    //TODO
                }catch(SQLException sqle){sqle.printStackTrace();}
            }
            case NOTA_PARAM_CLIMATICO -> {
                Worker w = new Worker(dbUrl, props, "workerNota");
                try(ResultSet res = w.selectObjFromNotaWithCond(oggetto, fieldCond, cond)){
                    //TODO
                }catch(SQLException sqle){sqle.printStackTrace();}
            }
            case PARAM_CLIMATICO -> {
                Worker w = new Worker(dbUrl, props, "workerPM");
                try(ResultSet res = w.selectObjFromPMWithCond(oggetto, fieldCond, cond)){
                    //TODO
                }catch(SQLException sqle){sqle.printStackTrace();}
            }
        }

    }

    public void selectAllWithCond(tables table, String fieldCond, String cond){
        switch(table){
            case CITY -> {
                Worker w = new Worker(dbUrl, props, "workerCity");
                LinkedList<City> cities = w.selectAllFromCityWithCond(fieldCond, cond);
                cities.forEach(System.out::println);
            }
            case CENTROMONITORAGGIO -> {
                Worker w = new Worker(dbUrl, props, "workerCM");
                LinkedList<CentroMonitoraggio> cms = w.selectAllFromCMWithCond(fieldCond, cond);
                cms.forEach(System.out::println);
            }
            case OPERATORE -> {
                Worker w = new Worker(dbUrl, props, "workerOperatore");
                LinkedList<Operatore> operatori = w.selectAllFromOpWithCond(fieldCond, cond);
                operatori.forEach(System.out::println);
            }
            case OP_AUTORIZZATO -> {
                Worker w = new Worker(dbUrl, props, "workerAuthOP");
                LinkedList<OperatoreAutorizzato> operatoriAutorizzati = w.selectAllFromAuthOpWithCond(fieldCond, cond);
                operatoriAutorizzati.forEach(System.out::println);
            }
            case AREAINTERESSE -> {
                Worker w = new Worker(dbUrl, props, "workerAI");
                LinkedList<AreaInteresse> areeInteresse = w.selectAllFromAIWithCond(fieldCond, cond);
                areeInteresse.forEach(System.out::println);
            }
            case NOTA_PARAM_CLIMATICO -> {
                Worker w = new Worker(dbUrl, props, "workerNota");
                //TODO
            }
            case PARAM_CLIMATICO -> {
                Worker w = new Worker(dbUrl, props, "workerPM");
                LinkedList<ClimateParameter> cps = w.selectAllFromCPWithCond(fieldCond, cond);
                cps.forEach(System.out::println);
            }
        }


    }


}
