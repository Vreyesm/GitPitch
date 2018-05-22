class Persona {
  public String nombre;
  public int edad;

  public Persona(String nombre, int edad) {
    this.nombre = nombre;
    this.edad = edad;
  }

  public void hablar() {
    System.out.println("Hola, me llamo " + this.nombre + ", tengo " + this.edad + " años.");
  }
}

class Estudiante extends Persona {
  public String matricula;

  public Estudiante(String nombre, int edad, String matricula) {
    super(nombre, edad);
    this.matricula = matricula;
  }

  public void hablar() {
    super.hablar();
    System.out.println("Soy un Estudiante y mi número de matrícula es: " + this.matricula);
  }
}

class Trabajador extends Persona {
  public String empresa;

  public Trabajador(String nombre, int edad, String empresa) {
    super(nombre, edad);
    this.empresa = empresa;
  }

  public void hablar() {
    super.hablar();
    System.out.println("Soy un Trabajador de " + this.empresa);
  }
}

public class Main {
  public static void main(String[] args) {
    Persona estudiante = new Estudiante("Daniel", 23, "2014407002");
    Trabajador trabajador = new Trabajador("Víctor", 21, "Google");
    estudiante.hablar();
    ((Persona)estudiante).hablar();
    trabajador.hablar();
    ((Persona)trabajador).hablar();
  }
}