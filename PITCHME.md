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

### Ejemplo

```Java
public class Cuadrado {
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
@[16] (Uso del objeto `cuadrado`.)
---
### Abstracción



@fa[arrow-down]

+++

### Ejemplo

---
### Encapsulamiento

@fa[arrow-down]

+++

### Ejemplo

---
### Herencia

@fa[arrow-down]

+++

### Ejemplo

---
### Polimorfismo

@fa[arrow-down]

+++

### Ejemplo

---
