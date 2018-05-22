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

#### Clases y Objetos - Ejemplo

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
#### Encapsulamiento - Niveles de Acceso

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
    <td style="text-align:center">Y</td>
    <td style="text-align:center">Y</td>
    <td style="text-align:center">Y</td>
    <td style="text-align:center">Y</td>
  </tr>
  <tr class="fragment">
    <td><b>protected</b></td>
    <td style="text-align:center">Y</td>
    <td style="text-align:center">Y</td>
    <td style="text-align:center">Y</td>
    <td style="text-align:center">N</td>
  </tr>
  <tr class="fragment">
    <td><i>no modifier</i></td>
    <td style="text-align:center">Y</td>
    <td style="text-align:center">Y</td>
    <td style="text-align:center">N</td>
    <td style="text-align:center">N</td>
  </tr>
  <tr class="fragment">
    <td><b>private</b></td>
    <td style="text-align:center">Y</td>
    <td style="text-align:center">N</td>
    <td style="text-align:center">N</td>
    <td style="text-align:center">N</td>
  </tr>
</table>

+++
#### Encapsulamiento - Ejemplo

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
@[20,22] (Uso del método `getColor()` para leer la variable privada `color`.)
@[21] (Uso del método `setColor()` para escribir en la variable privada `color`.)

---
### Herencia

@ul

- Proceso por el cual una clase (*subclase*) adquiere las propiedades (atributos y/o métodos) de otra (*superclase*).
- Con el uso de herencia, la información se puede manejar en orden jerárquico.

@ulend

@fa[arrow-down]

+++

#### Herencia - Ejemplo

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

@ul

- Ocultar los detalles de implementación.
- Lo que es importante conocer es "qué" realiza el objeto, no el "cómo" (caja negra).
- Uso de clases abstractas e interfaces en Java, las cuales no se pueden instanciar.
- Concepto de *clase abstracta* y *clase concreta*.

@ulend

@fa[arrow-down]

+++

#### Abstracción - Ejemplo 1

```Java
abstract class Persona {
  public String nombre;
  public int edad;

  public Persona(String nombre, int edad) {
    this.nombre = nombre;
    this.edad = edad;
  }

  public abstract void hablar();
}

class Estudiante extends Persona {
  public String matricula;

  public Estudiante(String nombre, int edad, String matricula) {
    super(nombre, edad);
    this.matricula = matricula;
  }

  public void hablar() {
    //super.hablar();
    System.out.println("Hola, me llamo " + this.nombre + ", tengo " + this.edad + " años.");
    System.out.println("Además, soy un Estudiante y mi número de matrícula es: " + this.matricula);
  }
}

public class Main {
  public static void main(String[] args) {
    Persona estudiante = new Estudiante("Daniel", 23, "2014407002");
    estudiante.hablar();
    //Persona persona = new Persona("Juan", 20);
  }
}
```

@[1-11] (Definición de la clase `Persona`.)
@[1] (Ahora `Persona` es una clase abstracta.)
@[10] (El método `hablar()` también es abstracto.)
@[13-26] (Definición de la clase `Estudiante`.)
@[17] (Aún podemos utilizar el constructor de la clase padre.)
@[21-25] (Implementación del método abstracto `hablar()`.)
@[28-34] (Programa principal.)
@[30] (Creación del objeto `estudiante`.)
@[31] (Llamada a la implementación del método `hablar()`.)
@[32] (Dado que `Persona` es una clase abstracta, no se puede instanciar.)

---
#### Abstracción - Ejemplo 2

```Java
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
    System.out.println("Además, soy un Estudiante y mi número de matrícula es: " + this.matricula);
  }
}

public class Main {
  public static void main(String[] args) {
    Persona estudiante = new Estudiante(23, "2014407002");
    estudiante.hablar();
    //Persona persona = new Persona("Juan", 20);
  }
}
```

@[1-5] (Definición de la *interfaz* `Persona`.)
@[2] (Se pueden definir constantes (final) pero no variables.)
@[4] (Método que debe implementar una *clase hija*.)
@[7-22] (Definición de la clase `Estudiante`.)
@[7] (Uso de `implements` en vez de `extends`.)
@[8,9] (Variables de `Estudiente`.)
@[12] (La clase padre ya no tiene un constructor.)
@[17-21] (Implementación del método `hablar()`.)
@[24-30] (Programa principal.)
@[26] (Creación del objeto `estudiante`.)
@[27] (Llamada a la implementación del método `hablar()`.)
@[28] (Dado que `Persona` es una *interfaz*, no se puede instanciar.)

---
### Polimorfismo

@fa[arrow-down]

+++

#### Polimorfismo - Ejemplo

---
