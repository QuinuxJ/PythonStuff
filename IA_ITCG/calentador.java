public class calentador{
    public void FSM(Estados edo){
        int t=generarTemperatura();
        boolean ban = false;
        do{
            switch(edo){
                case CONECTADO:
                    estoyEn(edo);
                    t=generarTemperatura();
                    if(t>5){
                        edo=Estados.ENCENDIDO;
                        
                    }
                    break;
                case DESCONECTADO:
                    System.out.println("Hasta Luego");
                    ban=true;
                    break;

                case ENCENDIDO:
                    estoyEn(edo);
                    t=generarTemperatura();
                    if(t>15){
                        edo=Estados.APAGADO;
                        cambieA(edo);
                    }
                    else if(t==0){
                        edo = Estados.DESCONECTADO;
                        cambieA(edo);
                    }
                    break;
                case APAGADO:
                    estoyEn(edo);
                    t=generarTemperatura();
                    if(t<5){
                        edo=Estados.ENCENDIDO;
                        cambieA(edo);
                    }
                    else if(t==0){
                        edo = Estados.DESCONECTADO;
                        cambieA(edo);
                    }
                    break;
            }//switch
            System.out.println("**");
        }while(!ban);
        }
    }
    public void estoyEn(Estados edo){
        System.out.println("Me encuentro en el estado: " + edo);
    }
    public void cambieA(Estados edo){
        System.out.println("He pasado al estado: " + edo);
    }
    public int generarTemperatura(){
        return (int)(Math.random()*20);
    }
    public static void main(String[] args){
        calentador c = new calentador();
        c.FSM(Estados.CONECTADO);
    }
}


