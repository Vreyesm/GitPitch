## Lenguajes y Paradigmas de Programación
### Programación Orientada a Objetos

<br>

Daniel Pavez - Victor Reyes

---
## Conceptos principales
---
### Clases y Objetos

@ul
- **Clase**: Plantilla de un tipo de datos, en la cual se define sus atributos y las operaciones que se pueden realizar sobre un *objeto* de dicha clase.
- **Objeto**: Instancia de una *clase*, cuyos atributos y comportamiento está definido por la *clase* a la cual pertenece.

@ulend

@fa[arrow-down]

+++

### Ejemplo de Clases y Objetos

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
### Herencia

@ul

- Proceso por el cual una clase (*subclase*) adquiere las propiedades (atributos y/o métodos) de otra (*superclase*).
- Con el uso de herencia la información se puede manejar en orden jerárquico.

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
### Encapsulamiento

@fa[arrow-down]

+++

### Ejemplo de Encapsulamiento


---
### Polimorfismo

@fa[arrow-down]

+++

### Ejemplo

---
