interface Persona {
  public String nombre = "Daniel";

  public void hablar();
}

class Estudiante implements Persona {
  public int edad;
  public String matricula;

  public Estudiante(int edad, String matricula) {
    //super(nombre, edad);
    this.edad = edad;
    this.matricula = matricula;
  }

  public void hablar() {
    //super.hablar();
    System.out.println("Hola, me llamo " + this.nombre + ", tengo " + this.edad + " años.");
    System.out.println("Soy un Estudiante y mi número de matrícula es: " + this.matricula);
  }
}

public class Main {
  public static void main(String[] args) {
    Persona estudiante = new Estudiante(23, "2014407002");
    estudiante.hablar();
    //Persona persona = new Persona("Juan", 20);
  }
}