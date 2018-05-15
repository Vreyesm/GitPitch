## Lenguajes y Paradigmas de Programación
### Tipos de datos y Flujo de Control

<br>

Daniel Pavez - Victor Reyes

---
## Tipos de datos
---
### Tipado fuerte vs Tipado débil

@ul

- En el tipado fuerte es necesario asignar explícitamente el tipo de nuestras variables.
- En el caso del tipado débil comúnmente el tipo de datos de las variables es inferido según su "contenido".
- Varios lenguajes permiten una combinación de ambos.

@ulend

---
### Tipado estático vs Tipado dinámico

@ul

- Tipado estático es comprobado en tiempo de compilación y dinámico en tiempo de ejecución.
- Ambos pueden hacer uso de **inferencia** de tipos.
- Sobrecarga de métodos: Tipado estático.
- Polimorfismo: Tipado dinámico.

@ulend

---
### Equivalencia estrutural y de nombres




@fa[arrow-down]

+++

### Ejemplo

¿Qué sucede en el siguiente caso equivalencia estructural y con equivalencia de nombres?

```
type student = record
name, address : string
age : integer
type school = record
name, address : string
age : integer
x : student;
y : school;
. . .
x := y;
```

@fa[arrow-down]

+++

### Ejemplo

**Equivalencia estructural:** Dado que ambos tipos tienen campos con los mismos nombres, tipos y en el mismo orden, éstos son iguales.

```
type student = record
name, address : string
age : integer
type school = record
name, address : string
age : integer
x : student;
y : school;
. . .
x := y;
```

@fa[arrow-down]

+++

### Ejemplo

**Equivalencia de nombre:** Dado que ambos tipos tienen distintos nombres, son considerados como tipos totalmente diferentes y no son compatibles, por ello, la asignación dará un error.

```
type student = record
name, address : string
age : integer
type school = record
name, address : string
age : integer
x : student;
y : school;
. . .
x := y;
```

---

### Equivalencia de nombre estricta y relajada

@ul

- Para la equivalencia de nombre estricta, si dos tipos se llaman distinto, estos son tipos distintos.
- Para la equivalencia de nombres relajada no necesariamente (como veremos a continuación).

@ulend

@fa[arrow-down]

+++

### Ejemplo

¿Qué sucede en este caso?

```
type cell = . . . 
type alink = pointer to cell
type blink = alink    //Fijarse aquí
p, q : pointer to cell
r : alink
s :blink
t : pointer to cell
u :alink
```

@fa[arrow-down]

+++

### Ejemplo

**Equivalencia de nombre estricta:** `type blink = alink` es una definición, por ello `type blink` es un tipo nuevo y totalmente distintos a `type alink`.

```
type cell = . . . 
type alink = pointer to cell
type blink = alink    //Fijarse aquí
p, q : pointer to cell
r : alink
s :blink
t : pointer to cell
u :alink
```

@fa[arrow-down]

+++

### Ejemplo

**Equivalencia de nombre relajada:** `type blink = alink` es tan sólo una declaración, por ello `type blink` comparte la definición de `type alink` y son considerados como tipos equivalentes.

```
type cell = . . . 
type alink = pointer to cell
type blink = alink    //Fijarse aquí
p, q : pointer to cell
r : alink
s :blink
t : pointer to cell
u :alink
```

---
### Coerción

@ul

- Elección de como "actuar" al operar sobre variables de tipos diferentes.
- Determinar si es posible operar dichas variables (compatibilidad).
- Puede estar basada en los operadores utilizados o tomar en cuenta los tipos del contexto.
- El resultado de la operación puede ser de un tipo distinto al de alguno de los operandos (transformación implícita, a diferencia de la conversión de tipos que es explícita, comúnmente por medio de *casteo*).

@ulend

---
## Flujo de control
---
### Ejercicios notaciones matemáticas

Transformar las siguientes expresiones a su forma prefija y sufija.

@ol

- A+B
- -A+B  +B-A A-B+
- A+B*C
- C*(A+B)
- (A+B^C)
- D+E^5
- (A+B^C)*D+E^5

@olend

---
### Ejercicios corto circuito

Determine bajo que situaciones ocurre un corto circuito en las siguientes expresiones.

@ol

- X AND Y
- X OR Y
- (A AND B) AND C
- (A OR B) AND C
- (A OR B) OR C

@olend