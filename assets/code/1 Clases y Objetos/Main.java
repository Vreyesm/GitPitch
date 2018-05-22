class Cuadrado {
  public int lado;

  public Cuadrado(int lado) {
    this.lado = lado;
  }

  public int area() {
    return lado*lado;
  }
}

public class Main {
  public static void main(String[] args) {
    Cuadrado cuadrado = new Cuadrado(5);
    System.out.println( cuadrado.area() );
  }
}