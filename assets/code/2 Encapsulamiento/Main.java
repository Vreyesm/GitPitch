class Lapiz {
  private String color;

  public Lapiz(String color) {
    this.color = color;
  }

  public void setColor(String color) {
    this.color = color;
  }

  public String getColor() {
    return this.color;
  }
}

public class Main {
 public static void main(String[] args) {
   Lapiz lapiz = new Lapiz("negro");
   System.out.println("El color del lápiz es: " + lapiz.getColor());
   lapiz.setColor("rojo");
   System.out.println("El color del lápiz es: " + lapiz.getColor());
 }
}