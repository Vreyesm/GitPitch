## Lenguajes y Paradigmas de Programación
### Programación Orientada a Objetos

<br>

Daniel Pavez - Victor Reyes

---
### Clases y Objetos

@ul
- **Clase**: Plantilla de un tipo de datos, en la cual se define sus atributos y las operaciones que se pueden realizar sobre un *objeto* de dicha clase.
- **Objeto**: Instancia de una *clase*, cuyos atributos y comportamiento está definido por la *clase* a la cual pertenece.

@ulend

@fa[arrow-down]

+++

### Clases y Objetos - Ejemplo

```Java
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
```

@[1] (Creación de la clase `Cuadrado`.)
@[1-11] (Creación de la clase `Cuadrado`.)
@[13-18] (Programa principal.)
@[15] (Creación del objeto `cuadrado`, cuyo lado es 5.)
@[16] (Uso del método `area()`, definido en la clase `Cuadrado`.)

---
## Conceptos Fundamentales
---
### Encapsulamiento

@ul

- Controlar la lectura y escritura de las variables de un objeto.
- Uso de los modificadores `public`, `private` y `protected` en Java.

@ulend

@fa[arrow-down]

+++
### Encapsulamiento - Niveles de Acceso

<table>
  <tr>
    <th>Modifier</th>
    <th>Class</th>
    <th>Package</th>
    <th>Subclass</th>
    <th>World</th>
  </tr>
  <tr>
    <td><b>public</b></td>
    <td>Y</td>
    <td>Y</td>
    <td>Y</td>
    <td>Y</td>
  </tr>
  <tr class="fragment">
    <td><b>protected</b></td>
    <td>Y</td>
    <td>Y</td>
    <td>Y</td>
    <td>N</td>
  </tr>
  <tr class="fragment">
    <td><i>no modifier</i></td>
    <td>Y</td>
    <td>Y</td>
    <td>N</td>
    <td>N</td>
  </tr>
  <tr class="fragment">
    <td><b>private</b></td>
    <td>Y</td>
    <td>N</td>
    <td>N</td>
    <td>N</td>
  </tr>
</table>

### Encapsulamiento - Ejemplo

```Java
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
```

@[1-15] (Definición de la clase `Lapiz`.)
@[2] (Variable `color` con modificador `private`.)
@[8-14] (Métodos públicos que permiten la lectura y escritura desde el exterior de la clase.)
@[20,22] (Uso del método `getColor()` para leer el valor de la variable privada `color`.)
@[21] (Uso del método `setColor()` para escribir en la variable privada `color`.)

---
### Herencia

@ul

- Proceso por el cual una clase (*subclase*) adquiere las propiedades (atributos y/o métodos) de otra (*superclase*).
- Con el uso de herencia, la información se puede manejar en orden jerárquico.

@ulend

@fa[arrow-down]

+++

### Ejemplo de Herencia

```Java
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
    System.out.println("Además, soy un Estudiante y mi número de matrícula es: " + this.matricula);
  }
}

public class Main {
  public static void main(String[] args) {
    Persona estudiante = new Estudiante("Daniel", 23, "2014407002");
    estudiante.hablar();
    ((Persona)estudiante).hablar();
  }
}
```

@[1-13] (Definición de la *superclase* `Persona`.)
@[15-27] (Definición de la *subclase* `Estudiante`.)
@[15] (Especificación de la herencia con el uso de `extends`.)
@[18-21] (Constructor de la clase `Estudiante`.)
@[19] (Uso del constructor de la *superclase* `Persona`.)
@[23-26] (Sobreescritura del método `hablar()`.)
@[24] (Uso del método `hablar()` de la *superclase*.)
@[29-35] (Programa principal.)
@[31] (Creación del objeto `estudiante`.)
@[32] (Llamada al método `hablar()` de la clase `Estudiante`.)
@[33] (También llama al método `hablar()` de la clase `Estudiante`.)

---
### Abstracción



@fa[arrow-down]

+++

### Ejemplo de Abstracción

---
### Polimorfismo

@fa[arrow-down]

+++

### Ejemplo

---
