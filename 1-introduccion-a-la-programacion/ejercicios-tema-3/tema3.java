public class Main {
    public static void main(String[] args) {
        suma(10, 50, 5);
        Coche miCoche = new Coche("Ford", "Fiesta", 3);
        miCoche.sumarPuertas(1);
    }
    public static void suma(int a, int b, int c) {
        int resultado;
        resultado = a + b + c;
        System.out.println(resultado);
    }
    public static class Coche {
        String marca;
        String modelo;
        int puertas = 2;
        public Coche(String marca, String modelo, int puertas){
            this.marca = marca;
            this.modelo = modelo;
            this.puertas = puertas;
        }
        public void sumarPuertas(int cantidad){
            this.puertas += cantidad;
            System.out.println(this.puertas);
        }
    }
}