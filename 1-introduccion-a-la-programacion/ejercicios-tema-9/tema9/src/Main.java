public class Main {
    public static void main(String[] args) {
        System.out.println("Hello world!");
        cliente miCliente = new cliente (30, "Luis", 123456, true);
    }

    public class Persona{
        int edad;
        String nombre;
        int telefono;
    }

    public class Cliente extends Persona {

        public class cliente {
            int edad;
            String nombre;
            int telefono;
            boolean credito;
        }

    }

    public class Trabajador extends Persona {
        int salario;

    }

}
