public class Main {
    public static void main(String[] args) {
        System.out.println("Hello world!");
        checkNum(2023);
        checkWhile(0);
        checkDoWhile(0);
        checkFor();
        checkSwitch("Primavera");
    }
    public static void checkNum(int numeroIf){
        if (numeroIf >= 1) {
            System.out.println("El numero es positivo y es " + numeroIf);
        } else if (numeroIf <= -1){
            System.out.println("El numero es negativo y es " + numeroIf);
        } else if (numeroIf == 0){
            System.out.println("El numero es " + numeroIf);
        }
    }
    // WHILE
    public static void checkWhile(int numeroWhile){
        while (numeroWhile < 3){
            System.out.println(numeroWhile);
            numeroWhile++;
        };
    }
    // DO WHILE
    public static void checkDoWhile(int numeroDoWhile){
        do{
            System.out.println(numeroDoWhile);
            numeroDoWhile++;
        }
        while (numeroDoWhile < 3);
    }
    // FOR
    public static void checkFor(){
        for(int numeroFor = 0; numeroFor <= 3; numeroFor++){
            System.out.println(numeroFor);
        }
    }
    // SWITCH
    public static void checkSwitch(String estacion){
        switch (estacion){
            case "Primavera":
                System.out.println("Es " + estacion);
            break;
            case "Verano":
                System.out.println("Es " + estacion);
            break;
            case "Otoño":
                System.out.println("Es " + estacion);
            break;
            case "Invierno":
                System.out.println("Es " + estacion);
            break;
            default:
                System.out.println("Error: la variable no es una estación");
        }
    }
}